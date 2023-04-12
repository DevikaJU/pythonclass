#create database company;
use company;
#create table jobs(job_id varchar(20) primary key,job_title varchar(20),min_salary varchar(50),max_salary varchar(50));
#create table regions(region_id varchar(20) primary key,region_name varchar(20));
#create table countries(country_id varchar(20) primary key,country_name varchar(20),region_id varchar(20));
#alter table countries add constraint foreign key countries(region_id) references regions(region_id);
#create table employees(employee_id varchar(20) primary key,first_name varchar(20),last_name varchar(20),email varchar(50),phone_number varchar(50),hire_date varchar(50),job_id varchar(20),salary varchar(20),manager_id varchar(20),department_id varchar(20));
#create table dependents(dependent_id varchar(20) primary key,first_name varchar(20),last_name varchar(20),relationship varchar(50),employee_id varchar(20));
#create table departments(department_id varchar(20) primary key,department_name varchar(20),location_id varchar(20));
#create table locations(location_id varchar(20) primary key,street_address varchar(20),postal_code varchar(20),city varchar(50),state_province varchar(20),country_id varchar(20));
#alter table locations add constraint foreign key locations(country_id) references countries(country_id);
#alter table departments add constraint foreign key departments(location_id) references locations(location_id);
#alter table dependents add constraint foreign key dependents(employee_id) references employees(employee_id);
#alter table employees add constraint foreign key employees(department_id) references departments(department_id);








