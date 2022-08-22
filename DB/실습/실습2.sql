-- SQLite
CREATE TABLE classmates (
    name TEXT,
    age INT,
    address TEXT
);
alter table people rename to classmates;
alter table people add column type text;

INSERT INTO people (id, name, type) VALUES (3, '홍길동','fast');
SELECT * FROM people;
INSERT INTO people (id, name, type) VALUES ('홍길동', 23, '서울');
INSERT INTO people VALUES ('김철수', 40, '서울');