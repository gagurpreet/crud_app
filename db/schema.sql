CREATE DATABASE online_learning_db;
\c online_learning_db

CREATE TABLE courses(
  id SERIAL PRIMARY KEY,
  name TEXT,
  length_of_course TEXT,
  fee INTEGER
);

INSERT INTO courses(name, length_of_course, fee  )
VALUES('software Engg.', '3 months' , 2000) ,( 'python', '6 months', 3000
);

CREATE TABLE users(
  id SERIAL PRIMARY KEY,
  first_name TEXT,
  last_name TEXT,
  email TEXT,
  password_digest TEXT
);