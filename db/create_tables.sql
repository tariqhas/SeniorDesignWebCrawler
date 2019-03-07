CREATE DATABASE IF NOT EXISTS seniordesign;
USE seniordesign;

DROP TABLE IF EXISTS Urls;
create table Urls
(
	UrlId int auto_increment,
	Url varchar(255),
	UrlType varchar(255),
	UrlComment varchar(255),
	Primary Key(UrlId)
);


DROP TABLE IF EXISTS Attributes;
create table Attributes
(
	AttributeId int auto_increment,
	AttributeName varchar(255),
	AttributeType varchar(10),
	Pattern varchar(255),
	Primary Key(AttributeId)
);
/*select * from Urls where UrlId = 1;
Delete from Urls where UrlId = 1;


