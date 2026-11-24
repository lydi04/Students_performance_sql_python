CREATE DATABASE IF NOT EXISTS students_db;
USE students_db;

CREATE TABLE students_performance (
  gender VARCHAR(10),
  race_ethnicity VARCHAR(20),
  parental_education VARCHAR(40),
  lunch VARCHAR(30),
  test_prep VARCHAR(20),
  math_score INT,
  reading_score INT,
  writing_score INT
);

-- Q1: Gender wise average scores
SELECT gender, COUNT(*) AS students,
       ROUND(AVG(math_score),1) AS avg_math,
       ROUND(AVG(reading_score),1) AS avg_reading,
       ROUND(AVG(writing_score),1) AS avg_writing
FROM students_performance
GROUP BY gender;

-- Q2: Test prep course
SELECT test_prep, COUNT(*) AS students,
       ROUND(AVG(math_score),1) AS avg_math,
       ROUND(AVG(reading_score),1) AS avg_reading,
       ROUND(AVG(writing_score),1) AS avg_writing
FROM students_performance
GROUP BY test_prep;

-- Q3: Parents education wise average score
SELECT parental_education,
       ROUND(AVG((math_score + reading_score + writing_score)/3),1) AS avg_score
FROM students_performance
GROUP BY parental_education
ORDER BY avg_score DESC;

-- Q4: Top 10 students
SELECT *, (math_score + reading_score + writing_score) AS total
FROM students_performance
ORDER BY total DESC
LIMIT 10;

-- Q5: Math pass / fail (pass mark 40)
SELECT CASE WHEN math_score >= 40 THEN 'Pass' ELSE 'Fail' END AS result,
       COUNT(*) AS students
FROM students_performance
GROUP BY result;



