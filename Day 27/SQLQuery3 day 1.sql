--create object objectName

create database OurDb
--create table <TableName>
--(ColumnName DataType <constraint>,
	----------
--)
use OurDb

create table Student
(SId int primary key,
SName nvarchar(50) not null,
SFee float not null)
------------------------------------------------
select * from Student
insert into Student values (1,'Sam',5000.50)
insert into Student values 
(2,'Rohit',4500.25),
(3,'Neha',5000.58),
(4,'Ani',6000.58),
(5,'Arisha',4000.28)

select * from Student where SId<=3
select SName from Student
-------------------------------------------------------------------------

