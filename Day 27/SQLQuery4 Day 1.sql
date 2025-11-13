use OurDb
--constraint, not null, primary key
--primary key: not null and unique,

create table Emp
(Id int primary key,
FName nvarchar(50) not null,
LName nvarchar(50))

select * from Emp
insert into Emp values (1,'Sam','Dicosta')
insert into Emp (Id,FName) values (2,'Rameez')
select * from Emp

delete from Emp --delete the data but the table still exist
select * from Emp

drop table Emp --delete the table with the data
select * from Emp

--default
create table Emp
(Id int primary key,
FName nvarchar(50) not null,
LName nvarchar(50),
City nvarchar (50) default ('Kuala Lumpur')
)
insert into Emp values (1,'Sam','Dicosta','Brisbane')
insert into Emp values (2,'Rina','Kumari','Delhi')
select * from Emp
insert into Emp (Id,FName,LName) values (3,'Alina','Khan')
select * from Emp
-----------------------------------------------------------------------------------------------
--Check
drop table Emp --delete the table with the data
create table Emp
(Id int primary key,
FName nvarchar(50) not null,
LName nvarchar(50),
City nvarchar (50) default ('Kuala Lumpur'),
Salary float not null check(Salary>=10000 and Salary<=50000)
)
insert into Emp (Id,FName,LName,Salary) values (3,'Alina','Khan',12000)
insert into Emp (Id,FName,LName,Salary) values (2,'Rina','Kumari','Delhi',1000)
--the INSERT statement conflicted with the Chech Constraint

drop table Emp
create table Emp
(Id int primary key,
FName nvarchar(50) not null,
Mobile nvarchar(10) check (Mobile like '[0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]')
)
select * from Emp
insert into Emp values (1,'Maan','0174077567')
insert into Emp values (2,'Meen','074077567')
--cannot execute due to only 9digit in mobile number
insert into Emp values (2,'Muun','0074077567')
-----------------------------------------------------------------------------------------------
--Unique : not duplicate allows null but once
drop table Emp
create table Emp
(Id int primary key,
FName nvarchar(50) not null,
Mobile nvarchar(10) unique not null
check (Mobile like '[0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]'),
Email nvarchar(100) unique
)
insert into Emp values (1,'Sam','0174077567','sam@yahoo.com')
insert into Emp values (2,'Ravi','0174077567','ravi@yahoo.com')
-- violation of Unique key constraint
--------------------------------------------------------------------------------------------
--identity (seed,increment)
create table Students
(SId int identity,
SName nvarchar(50) not null,
SFee float)
insert into Students(SName,SFee) values ('Ravi',5000.50)
insert into Students(SName,SFee) values ('Ani',3000.50)
insert into Students(SName,SFee) values ('joy',4500.50)
select * from Students
insert into Students(SName,SFee) values ('Riya',7500.50)

drop table Students

create table Students
(SId int identity(100,5),
SName nvarchar(50) not null,
SFee float)
insert into Students(SName,SFee) values ('Ravi',5000.50)
insert into Students(SName,SFee) values ('Ani',3000.50)
insert into Students(SName,SFee) values ('joy',4500.50)
select * from Students
insert into Students(SName,SFee) values ('Riya',7500.50)
-------------------------------------------------------------------------------
create table Salary
(Grade varchar(1) primary key,
BasicSalary float,
HRA as BasicSalary*0.10 persisted,
TA as BasicSalary*0.15 persisted,
DA as BasicSalary*0.20 persisted)
select * from Salary

insert into Salary values ('A',10000)
insert into Salary values ('B',5000)

select Grade,BasicSalary,TA,HRA,DA,BasicSalary+TA+DA+HRA as 'Net Salary' from Salary
insert into Salary values ('C',2000)
insert into Salary values ('D',1000)

select max(BasicSalary) as 'Max Basic' from Salary
select avg(BasicSalary) as 'Average Basic' from Salary
select min(BasicSalary) as 'Min Basic' from Salary
------------------------------------------------------------------------------------------------------------------
--foreign key
create table Category
(CatId int primary key,
CategoryName nvarchar(50) not null unique
)
insert into Category values 
(1,'Electronics'),
(2,'Clothing'),
(3,'Home Decor'),
(4,'Mobile')
select * from Category order by CatId

create table Product
(PId int primary key identity,
PName nvarchar(50) not null,
PPrice float not null,
ProductCategory int foreign key references Category
)
insert into Product values ('Iphone 17',5000,4)
insert into Product values ('Nothing 3',2000,4)
insert into Product values ('Washing Machine',4000,1)
insert into Product values ('Shirt',200,2)
insert into Product values ('T-Shirt',199,2)
insert into Product values ('Jeans',399,2)
select * from Product
insert into Product values ('Remote',199,5)
--The INSERT statement conflicted with the FOREIGN KEY constraint "FK__Product__Product__5070F446"
--The conflict occurred in database "OurDb", table "dbo.Category", column 'CatId'.
select * from Category
select * from Product

--select column from table1 join table2 on Table1.CommonColumn=Table2.CommonColumn
select * from Product join Category 
on Product.ProductCategory=Category.CatId

select * from Product p join Category c 
on p.ProductCategory=c.CatId

select p.PId 'Product ID',p.PName 'Product Name',p.PPrice 'Product Price',p.ProductCategory 'Category ID' ,c.CategoryName 'Category Name'
from Product p join Category c 
on p.ProductCategory=c.CatId