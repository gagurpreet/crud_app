CREATE DATABASE job_portal_db;
\c job_portal_db

CREATE TABLE jobs(
  id SERIAL PRIMARY KEY,
  company_name TEXT,
  job_link TEXT,
  job_level TEXT
);

INSERT INTO jobs(company_name, job_link, job_level  )
VALUES('Babcock Pty Ltd
', 'https://www.seek.com.au/job/67177411?type=standout#sol=4c3d9c7106c96e69af995cb0ba6fb087cd752994' , 'Experienced') ,( 'Paxus', 'https://www.seek.com.au/job/67328547?type=standard#sol=5e36d3e519a840d47fca544253f17207db812349', 'Experienced'
), ( 'GradConnection', 'https://www.seek.com.au/job/66856481?type=standard#sol=05aaf1548c10fdb09dc222e70aaafd8eca168206', 'graduate'
);

CREATE TABLE users(
  id SERIAL PRIMARY KEY,
  first_name TEXT,
  last_name TEXT,
  email TEXT,
  password_digest TEXT
);

CREATE TABLE likes(
  id SERIAL PRIMARY KEY,
  user_id INTEGER,
  job_id INTEGER
);

CREATE TABLE comments(
  id SERIAL PRIMARY KEY,
  user_id INTEGER,
  job_id INTEGER
);

ALTER TABLE comments ADD COLUMN content TEXT;

-- SELECT jobs.id, jobs.company_name, jobs.job_link, jobs.job_level, comments.content
-- FROM jobs
-- INNER JOIN comments ON jobs.id = comments.job_id;


