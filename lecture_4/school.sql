-- LAB 4: Student Grades Manager
-- File: school.sql

-- PART 1: CREATE TABLES

-- Drop tables if they exist
DROP TABLE IF EXISTS grades;
DROP TABLE IF EXISTS students;

-- Create students table
CREATE TABLE students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    full_name TEXT NOT NULL,
    birth_year INTEGER NOT NULL
);

-- Create grades table
CREATE TABLE grades (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id INTEGER NOT NULL,
    subject TEXT NOT NULL,
    grade INTEGER NOT NULL CHECK (grade BETWEEN 1 AND 100),
    FOREIGN KEY (student_id) REFERENCES students(id)
);


-- PART 2: CREATE INDEXES FOR OPTIMIZATION

-- Indexes for better query performance
CREATE INDEX idx_students_name ON students(full_name);
CREATE INDEX idx_students_birth ON students(birth_year);
CREATE INDEX idx_grades_student ON grades(student_id);
CREATE INDEX idx_grades_subject ON grades(subject);
CREATE INDEX idx_grades_grade ON grades(grade);


-- PART 3: INSERT DATA

-- Insert students
INSERT INTO students (full_name, birth_year) VALUES
('Alice Johnson', 2005),
('Brian Smith', 2004),
('Carla Reyes', 2006),
('Daniel Kim', 2005),
('Eva Thompson', 2003),
('Felix Nguyen', 2007),
('Grace Patel', 2005),
('Henry Lopez', 2004),
('Isabella Martinez', 2006);

-- Insert grades
INSERT INTO grades (student_id, subject, grade) VALUES
(1, 'Math', 88),
(1, 'English', 92),
(1, 'Science', 85),
(2, 'Math', 75),
(2, 'History', 83),
(2, 'English', 79),
(3, 'Science', 95),
(3, 'Math', 91),
(3, 'Art', 89),
(4, 'Math', 84),
(4, 'Science', 88),
(4, 'Physical Education', 93),
(5, 'English', 90),
(5, 'History', 85),
(5, 'Math', 88),
(6, 'Science', 72),
(6, 'Math', 78),
(6, 'English', 81),
(7, 'Art', 94),
(7, 'Science', 87),
(7, 'Math', 90),
(8, 'History', 77),
(8, 'Math', 83),
(8, 'Science', 80),
(9, 'English', 96),
(9, 'Math', 89),
(9, 'Art', 92);


-- PART 4: REQUIRED QUERIES

-- 3. Find all grades for a specific student (Alice Johnson)
SELECT 
    g.subject,
    g.grade
FROM students s
JOIN grades g ON s.id = g.student_id
WHERE s.full_name = 'Alice Johnson'
ORDER BY g.subject;

-- 4. Calculate the average grade per student
SELECT 
    s.full_name,
    ROUND(AVG(g.grade), 2) as average_grade,
    COUNT(g.id) as number_of_grades
FROM students s
LEFT JOIN grades g ON s.id = g.student_id
GROUP BY s.id, s.full_name
ORDER BY average_grade DESC;

-- 5. List all students born after 2004
SELECT 
    id,
    full_name,
    birth_year
FROM students
WHERE birth_year > 2004
ORDER BY birth_year;

-- 6. List all subjects and their average grades
SELECT 
    subject,
    ROUND(AVG(grade), 2) as average_grade,
    COUNT(*) as number_of_grades
FROM grades
GROUP BY subject
ORDER BY average_grade DESC;

-- 7. Find the top 3 students with the highest average grades
SELECT 
    s.full_name,
    ROUND(AVG(g.grade), 2) as average_grade
FROM students s
JOIN grades g ON s.id = g.student_id
GROUP BY s.id, s.full_name
ORDER BY average_grade DESC
LIMIT 3;


-- 8. Show all students who have scored below 80 in any subject
SELECT s.full_name
FROM students s
WHERE EXISTS (
    SELECT 1 
    FROM grades g 
    WHERE g.student_id = s.id 
    AND g.grade < 80
)
ORDER BY s.full_name;