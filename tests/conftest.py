import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os
os.environ["TESTING"] = "1"

from app.main import app, get_db
from app.database import Base

TEST_DATABASE_URL = "postgresql://postgres:postgres@localhost:5432/postgres"

engine = create_engine(TEST_DATABASE_URL)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


@pytest.fixture(scope="function")
def client():
    # crea tablas
    Base.metadata.create_all(bind=engine)

    app.dependency_overrides[get_db] = override_get_db

    with TestClient(app) as c:
        yield c

    # limpia DB
    Base.metadata.drop_all(bind=engine)
    app.dependency_overrides.clear()
