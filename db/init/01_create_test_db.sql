SELECT 'CREATE DATABASE tasksdb_test'
WHERE NOT EXISTS (SELECT FROM pg_database WHERE datname = 'tasksdb_test')\gexec;
