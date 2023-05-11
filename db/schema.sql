CREATE DATABASE online_learning_db;
\c online_learning_db

CREATE TABLE languages(
  id SERIAL PRIMARY KEY,
  name TEXT,
  length_of_course TEXT,
  fee INTEGER
);

CREATE TABLE users(
  id SERIAL PRIMARY KEY,
  first_name TEXT,
  last_name TEXT,
  email TEXT,
  password_digest TEXT
);