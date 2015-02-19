CREATE KEYSPACE IF NOT EXISTS kauai WITH REPLICATION = { 'class' : 'SimpleStrategy', 'replication_factor' : 1 };

USE kauai;

CREATE TABLE IF NOT EXISTS functions (
  uuid text,
  content text,
  PRIMARY KEY (uuid)
);
