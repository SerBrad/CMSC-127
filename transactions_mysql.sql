DROP DATABASE IF EXISTS transactions;

CREATE OR REPLACE USER 'appuser'@'localhost' IDENTIFIED BY 'useruser';
CREATE DATABASE transactions;
GRANT ALL ON transactions.* TO 'appuser'@'localhost';

use transactions;

-- DDL statements --

create table user(
userid int AUTO_INCREMENT,
username varchar(50) not null,
userbalance numeric(6,2),
primary key(userid)
);

create table usergroup(
groupid int AUTO_INCREMENT,
groupname varchar(50) not null,
groupbalance numeric(6,2),
primary key(groupid)
);

create table transaction(
transactionid numeric(10) not null,
transactionname varchar(50) not null,
transactiondate DATE not null,
owedmoney numeric(6,2) not null,
issettled boolean not null,
expensetype varchar(15) not null,
payorid numeric(7) not null,
groupid int,
primary key(transactionid),
foreign key(groupid) references usergroup(groupid)
);

create table befriends(
user1id numeric(7) not null,
user2id numeric(7) not null,
friendbalance numeric(6,2),
unique(user1id, user2id, friendbalance)
);

create table joins(
userid numeric(7) not null,
groupid numeric(7) not null,
unique(userid, groupid)
);

create table user_makes_transaction(
userid numeric(7) not null,
transactionid numeric(7) not null,
unique(userid, transactionid)
);

-- Dummy values --

insert into user(username, userbalance) values
("Betty", 0),
("James", 0),
("Inez", 0),
("August", 0);

insert into usergroup(groupname, groupbalance) values
("Genshin Players", 0),
("Swifties", 0),
("ML Players", 0);

insert into joins(userid, groupid) values
(1, 1),
(3, 1),
(4, 1);

-- FEATURES: Assumption is user 1 is using the application --

----- Add expense -----
-- Example: User 2 owes 200 pesos from User 1 to buy food (assumed both are friends)
-- if issettled = false, updates balance of currently signed in user and payor id
-- if user owes money, balance is positive. if user lends money, balance is negative.
insert into transaction(transactionid, transactionname, transactiondate, owedmoney, issettled, expensetype, payorid, groupid) values (1010, "Food", curdate(), 200, false, "Friend Expense", 2, null);
insert into user_makes_transaction values (1, 1010);
insert into user_makes_transaction values (2, 1010);
update user set userbalance = userbalance + 200 where userid = 1;
update user set userbalance = userbalance - 200 where userid = 2;
update befriends set friendbalance = friendbalance + 200 where user1id = 1 and user2id = 2;

-- Example: User 1 owes 5000 pesos from Genshin Players group 
insert into transaction(transactionid, transactionname, transactiondate, owedmoney, issettled, expensetype, payorid, groupid) values (2020, "Food Bundle", curdate(), 5000, false, "Group Expense", 1, 1);
insert into user_makes_transaction values (1, 2020);
insert into user_makes_transaction values (3, 2020);
insert into user_makes_transaction values (4, 2020);
update user set userbalance = userbalance + 200 where userid = 1;
update user set userbalance = userbalance - 200/2 where userid = 3; -- balance divided from remaining members of group
update user set userbalance = userbalance - 200/2 where userid = 4;
update usergroup set groupbalance = groupbalance + 200 where groupid = 1;


----- Delete expense -----
delete from transaction where transactionid = 1010;
delete from user_makes_transaction where transactionid = 1010;
update user set userbalance = userbalance - 200 where userid = 1;
update user set userbalance = userbalance + 200 where userid = 2;
update befriends set friendbalance = friendbalance - 200 where user1id = 1 and user2id = 2;
----- Search expense -----
select * from transaction natural join user_makes_transaction where userid = 1; -- provides all transactions made with signed in user
----- Update expense -----
update transaction set transactionid = 4040 where transactionid = 1010; -- updates necessary values set by logged in user (ex: transactionid)
update transaction set owedmoney = 400 where transactionid = 1010;
update user set userbalance = userbalance - (400-200) where userid = 1; -- if owed money is changed, updates balance accordingly (change = new - initial)
update user set userbalance = userbalance + (400-200) where userid = 2;


----- Add friend -----
insert into befriends values (1, 2, 0);
insert into befriends values (3, 1, 0);
----- Delete friend -----
delete from befriend where (user1id = 1 and user2id = 2) or (user1id = 2 and user2id = 1);
----- Search friend -----
select username from user join befriends on (user.userid = befriends.user1id or user.userid = befriends.user2id) and user.userid != 1;
----- Update friend -----
update user set username = "Taylor" where username = "Betty"; -- updates necessary values set by logged in user (ex: username)

----- Add group -----
insert into joins values(1,1);
----- Delete group -----
delete from joins where userid = 1 and groupid = 1;
----- Search group -----
select * from usergroup;
----- Update group -----
update usergroup set groupname = "Arianators" where groupname = "Swifties"; -- updates necessary values set by logged in user (ex: groupname)


-- REPORTS --

-- View all expenses made within a month
select * from transaction where month(transactiondate) = 5;
-- View all expenses made with a friend
select * from transaction natural join user_makes_transaction where userid = 1 and expenseType = "Friend Expense";
-- View all expenses made with a group
select * from transaction natural join user_makes_transaction where userid = 1 and expenseType = "Group Expense";
-- View current balance from all expenses
select userbalance from user where userid = 1;
-- View all friends with outstanding balance
select username from user join befriends on (user.userid = befriends.user1id or user.userid = befriends.user2id) and user.userid != 1 and friendbalance > 0;
-- View all groups; 
select * from usergroup;
-- View all groups with an outstanding balance
select * from usergroup where groupbalance > 0;