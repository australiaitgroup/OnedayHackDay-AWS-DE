create schema development;

use development;

create table customer
(
	id int,
    first_name varchar(100),
    last_name varchar(100),
    data_of_birth date,
    address varchar(200),
    gender boolean
);

insert into customer
values
(1, 'aaa', 'AAA', '1995-01-01', 'king street', 1),
(2, 'bbb', 'BBB', '1996-01-01', 'george street', 0),
(3, 'ccc', 'CCC', '1997-01-01', 'kelly cres', 0),
(4, 'ddd', 'DDD', '1998-01-01', 'windsor road', 1),
(5, 'eee', 'EEE', '1999-01-01', 'victoria ave', 0);

select * from customer;