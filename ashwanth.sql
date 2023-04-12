#create database insurance;
#use insurance;
#create table person(driver_id varchar(20) primary key,name varchar(20),address varchar(50));
#create table car(license varchar(20) primary key,model varchar(20),year varchar(10))
#create table accident(report_no varchar(20) primary key,date date,location varchar(20))
#create table owns(driver_id varchar(20) primary key,license varchar(20))
#alter table owns add constraint foreign key owns(driver_id) references person(driver_id),add constraint foreign key owns(license) references car(license)
#create table participated(report_no varchar(15) primary key,license varchar(20),driver_id varchar(20),damage_amount varchar(20))
#alter table participated add constraint foreign key(driver_id) references person(driver_id),add constraint foreign key(license) references car(license)
#alter table participated add constraint foreign key(report_no) references accident(report_no)
#alter table car rename to vehicle
#alter table accident change report_no report_number varchar(20)
#alter table person add gender varchar(20);
#alter table accident drop column location;
#alter table participated modify column damage_amount numeric(3,1);
#use insurance;
#insert into person values('d001','Aswin','Thrissur','male');
#insert into person values('d002','Aswanth','Vadakara','male');
#insert into vehicle values('l002','Lamborghini','1991')
#insert into accident values('r002','2001/11/12');
#insert into owns values('d002','l002');
#insert into participated values('r002','l002','d002',89.5);
#alter table participated modify column damage_amount numeric(6,2);
#delete from participated where report_no='r002';
#insert into participated values('r002','l002','d002',8955.6);
#insert into owns values('d001','l004');
#use insurance;
#select * from person where  name like 'A%';
#select * from participated where damage_amount > '10000';
#insert into accident values('r003','2022/11/12');
#select * from accident where date between '2021/01/01' and '2023/12/31'; 
select vehicle.license,model,year,driver_id from vehicle,owns where vehicle.license=owns.license;



