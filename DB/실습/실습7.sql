SELECT *
FROM users INNER JOIN role
    ON users.role_id = role.id;

SELECT *
FROM articles INNER JOIN role
    ON articles.user_id = role.id;

SELECT 
    users.name, 
    role.title
FROM users INNER JOIN role
    ON users.role_id = role.id;

SELECT *
FROM users INNER JOIN role
    ON users.role_id = role.id
WHERE role.id = 2;

SELECT *
FROM users INNER JOIN role
    ON users.role_id = role.id
ORDER BY users.name DESC;


SELECT * 
FROM articles LEFT OUTER JOIN users
    ON articles.user_id = users.id;

-- id	title	content	user_id	id	name	role_id
-- 1	1번글	111	1	1	관리자	1
-- 2	2번글	222	2	2	김철수	2
-- 3	3번글	333	1	1	관리자	1
-- 4	4번글	444	NULL	NULL	NULL	NULL



SELECT * 
FROM  users LEFT OUTER JOIN articles
    ON users.id = articles.user_id;

-- id	name	role_id	id	title	content	user_id
-- 1	관리자	1	1	1번글	111	1
-- 1	관리자	1	3	3번글	333	1
-- 2	김철수	2	2	2번글	222	2
-- 3	이영희	2	NULL	NULL	NULL	NULL

SELECT * 
FROM articles JOIN users
    ON articles.user_id = users.id;

-- id	title	content	user_id	id	name	role_id
-- 1	1번글	111	1	1	관리자	1
-- 2	2번글	222	2	2	김철수	2
-- 3	3번글	333	1	1	관리자	1

SELECT * 
FROM articles LEFT OUTER JOIN users
    ON articles.user_id = users.id
WHERE articles.user_id IS NOT NULL;

-- id	title	content	user_id	id	name	role_id
-- 1	1번글	111	1	1	관리자	1
-- 2	2번글	222	2	2	김철수	2
-- 3	3번글	333	1	1	관리자	1

SELECT * 
FROM articles FULL OUTER JOIN users
    ON articles.user_id = users.id;

-- id	title	content	user_id	id	name	role_id
-- 1	1번글	111	1	1	관리자	1
-- 2	2번글	222	2	2	김철수	2
-- 3	3번글	333	1	1	관리자	1
-- 4	4번글	444	NULL	NULL	NULL	NULL
-- NULL	NULL	NULL	NULL	3	이영희	2

SELECT * 
FROM users CROSS JOIN role;
-- id	name	role_id	id	title
-- 1	관리자	1	1	admin
-- 1	관리자	1	2	staff
-- 1	관리자	1	3	student
-- 2	김철수	2	1	admin
-- 2	김철수	2	2	staff
-- 2	김철수	2	3	student
-- 3	이영희	2	1	admin
-- 3	이영희	2	2	staff
-- 3	이영희	2	3	student

SELECT * 
FROM users JOIN role;

SELECT * 
FROM articles
    JOIN users
        ON articles.user_id = users.id
    JOIN role
        ON users.role_id = role.id;
