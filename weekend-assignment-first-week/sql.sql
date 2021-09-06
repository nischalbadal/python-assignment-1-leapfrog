-- creating tables and schemas as specified in assignment
CREATE SCHEMA IF NOT EXISTS general;

CREATE TABLE IF NOT EXISTS general.users(
     id SERIAL PRIMARY KEY,
     name VARCHAR(100) NOT NULL,
     dob DATE,
     profession VARCHAR(100)
 );

 CREATE TABLE IF NOT EXISTS general.address(
     id SERIAL PRIMARY KEY,
     user_id INT NOT NULL,
     permanent_address VARCHAR(10),
     temporary_address VARCHAR(10),
     CONSTRAINT fk_user_id
     FOREIGN KEY(user_id) 
     REFERENCES general.users(id)
 ); 

-- inserting dummy data
INSERT INTO general.users("name","dob","profession")
VALUES('Jane Henderson','1989-09-19', 'Actor'),
      ('Alice Sprigg','1991-11-12','Mechanic'),
      ('Dave Carr','1995-03-28','Banker'),
      ('Morris Beckman','2010-07-07','Receptionist' );

INSERT INTO general.address("user_id","permanent_address","temporary_address")
VALUES  ('1','Jhapa','Koteshwor'),
        ('2','Syanga','Lalitpur'),
        ('4','Kathmandu','Illam'),
        ('3','Dhading','Gongabuu');

-- selecting records from joined tables on given user_id i.e. 1
select * from general.address a
inner join general.users u on a.user_id = u.id
where user_id = 1;

-- selecting records from joined tables on given profession i.e. Actor
select * from general.address a
inner join general.users u on a.user_id = u.id
where profession = 'Actor';

-- selecting records from joined tables on given permanent_address i.e. 'Kathmandu'
select * from general.address a
inner join general.users u on a.user_id = u.id
where permanent_address = 'Kathmandu';

--alter table to add gender column
alter table general.users
add column gender varchar(10);

--calculating age from dob and deleting records whose age is less than 18
delete from general.users where id not in (
	select id as "age" from general.users where date_part('year', age(dob))>18
);