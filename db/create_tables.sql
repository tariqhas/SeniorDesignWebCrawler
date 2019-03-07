CREATE DATABASE IF NOT EXISTS seniordesign;
USE seniordesign;

DROP TABLE IF EXISTS UrlIndex;
create table UrlIndex
(
	UrlId int auto_increment,
	FileName varchar(255),
	URLListName varchar(255),
	PRIMARY KEY(UrlId)
);

DROP TABLE IF EXISTS Urls;
create table Urls
(
	UrlId int,
	Url varchar(255),
	UrlType varchar(255),
	UrlComment varchar(255),
	PRIMARY KEY(UrlId, Url),
	CONSTRAINT `fk_url_index`
		FOREIGN KEY (UrlId) REFERENCES UrlIndex (UrlId)
		ON DELETE CASCADE
		ON UPDATE RESTRICT
);

DROP TABLE IF EXISTS AttributeIndex;
create table AttributeIndex
(
	AttributeId int auto_increment,
	FileName varchar(255),
	AttributeListName varchar(255),
	PRIMARY KEY(UrlId)
);

DROP TABLE IF EXISTS Attributes;
create table Attributes
(
	AttributeId int auto_increment,
	AttributeName varchar(255),
	AttributeType varchar(10),
	Pattern varchar(255),
	PRIMARY KEY(AttributeId, AttributeName),
	CONSTRAINT `fk_attribute_index`
		FOREIGN KEY (AttributeId) REFERENCES AttributeIndex (AttributeId)
		ON DELETE CASCADE
		ON UPDATE RESTRICT
);
/*select * from Urls where UrlId = 1;
Delete from Urls where UrlId = 1;


