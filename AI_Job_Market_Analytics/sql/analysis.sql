USE ai_job_market;
SELECT DATABASE();
SHOW TABLES;
CREATE TABLE job_postings (
    job_id VARCHAR(100),
    job_title VARCHAR(255),
    salary_usd DECIMAL(12,2),
    salary_currency VARCHAR(20),
    experience_level VARCHAR(50),
    employment_type VARCHAR(50),
    company_location VARCHAR(100),
    company_size VARCHAR(50),
    employee_residence VARCHAR(100),
    remote_ratio INT,
    required_skills TEXT,
    education_required VARCHAR(100),
    years_experience DECIMAL(5,2),
    industry VARCHAR(100),
    posting_date DATE,
    application_deadline DATE,
    job_description_length INT,
    benefits_score DECIMAL(5,2),
    company_name VARCHAR(255),
    experience_category VARCHAR(50),
    work_mode VARCHAR(50),
    posting_year INT,
    posting_month INT,
    posting_month_name VARCHAR(20),
    posting_quarter INT,
    application_window_days INT
);
DESCRIBE job_postings;
USE ai_job_market;
SELECT COUNT(*) AS total_jobs
FROM job_postings;
SELECT *
FROM job_postings
LIMIT 10;
SELECT COUNT(DISTINCT company_name) AS unique_companies
FROM job_postings;
SELECT COUNT(DISTINCT job_title) AS unique_roles
FROM job_postings;
SELECT
    ROUND(AVG(salary_usd), 2) AS average_salary
FROM job_postings;
SELECT
    MIN(salary_usd) AS minimum_salary,
    MAX(salary_usd) AS maximum_salary
FROM job_postings;
SELECT
    experience_level,
    COUNT(*) AS job_count,
    ROUND(AVG(salary_usd), 2) AS average_salary
FROM job_postings
GROUP BY experience_level
ORDER BY average_salary DESC;

SELECT
    experience_level,
    COUNT(*) AS job_count
FROM job_postings
GROUP BY experience_level
ORDER BY job_count DESC;
SELECT
    employment_type,
    COUNT(*) AS job_count
FROM job_postings
GROUP BY employment_type
ORDER BY job_count DESC;
SELECT
    company_size,
    COUNT(*) AS job_count
FROM job_postings
GROUP BY company_size
ORDER BY job_count DESC;
SELECT
    work_mode,
    COUNT(*) AS job_count
FROM job_postings
GROUP BY work_mode
ORDER BY job_count DESC;
SELECT
    work_mode,
    COUNT(*) AS job_count,
    ROUND(
        COUNT(*) * 100.0 /
        (SELECT COUNT(*) FROM job_postings),
        2
    ) AS percentage
FROM job_postings
GROUP BY work_mode
ORDER BY percentage DESC;
SELECT
    company_location,
    COUNT(*) AS job_count
FROM job_postings
GROUP BY company_location
ORDER BY job_count DESC
LIMIT 20;
SELECT
    company_location,
    COUNT(*) AS job_count,
    ROUND(AVG(salary_usd), 2) AS average_salary
FROM job_postings
GROUP BY company_location
HAVING COUNT(*) >= 10
ORDER BY average_salary DESC;
SELECT
    job_title,
    COUNT(*) AS job_count
FROM job_postings
GROUP BY job_title
ORDER BY job_count DESC
LIMIT 20;
SELECT
    job_title,
    COUNT(*) AS job_count,
    ROUND(AVG(salary_usd), 2) AS average_salary
FROM job_postings
GROUP BY job_title
HAVING COUNT(*) >= 10
ORDER BY average_salary DESC
LIMIT 20;
SELECT
    industry,
    COUNT(*) AS job_count
FROM job_postings
GROUP BY industry
ORDER BY job_count DESC;
SELECT
    industry,
    COUNT(*) AS job_count,
    ROUND(AVG(salary_usd), 2) AS average_salary
FROM job_postings
GROUP BY industry
HAVING COUNT(*) >= 10
ORDER BY average_salary DESC;
SELECT
    company_name,
    COUNT(*) AS job_count
FROM job_postings
GROUP BY company_name
ORDER BY job_count DESC
LIMIT 20;
SELECT
    company_name,
    COUNT(*) AS job_count,
    ROUND(AVG(salary_usd), 2) AS average_salary
FROM job_postings
GROUP BY company_name
HAVING COUNT(*) >= 10
ORDER BY average_salary DESC
LIMIT 20;
SELECT
    job_title,
    salary_usd,
    CASE
        WHEN salary_usd < 75000 THEN 'Low'
        WHEN salary_usd < 150000 THEN 'Medium'
        ELSE 'High'
    END AS salary_category
FROM job_postings
LIMIT 20;
SELECT
    job_title,
    company_name,
    salary_usd,
    work_mode
FROM job_postings
WHERE work_mode = 'Fully Remote'
LIMIT 20;
SELECT
    company_location,
    job_title,
    salary_usd,
    RANK() OVER (
        PARTITION BY company_location
        ORDER BY salary_usd DESC
    ) AS salary_rank
FROM job_postings;
