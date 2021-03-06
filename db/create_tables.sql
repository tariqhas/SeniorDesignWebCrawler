CREATE DATABASE IF NOT EXISTS seniordesign;
USE seniordesign;

SET FOREIGN_KEY_CHECKS = 0;

DROP TABLE IF EXISTS UrlIndex;
create table UrlIndex
(
	UrlId int auto_increment,
	FileName varchar(255),
	URLListName varchar(255),
	PRIMARY KEY(UrlId)
);
ALTER TABLE UrlIndex AUTO_INCREMENT = 1;


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
	PRIMARY KEY(AttributeId)
);
ALTER TABLE AttributeIndex AUTO_INCREMENT = 1;

DROP TABLE IF EXISTS Attributes;
create table Attributes
(
	AttributeId int,
	AttributeName varchar(255),
	AttributeType varchar(10),
	Pattern varchar(255),
	PRIMARY KEY(AttributeId, AttributeName),
	CONSTRAINT `fk_attribute_index`
		FOREIGN KEY (AttributeId) REFERENCES AttributeIndex (AttributeId)
		ON DELETE CASCADE
		ON UPDATE RESTRICT
);

DROP TABLE IF EXISTS CrawlDataIndex;
CREATE TABLE CrawlDataIndex
(
	CrawlDataId int auto_increment,
	CrawlDataTableName varchar(255),
	PRIMARY KEY(CrawlDataId)
);
# Not sure if we need the above, it serves as a list of crawl data that has been created

SET FOREIGN_KEY_CHECKS = 1;
/*select * from Urls where UrlId = 1;
Delete from Urls where UrlId = 1;*/

DELIMITER //

CREATE PROCEDURE getDocumentListById(IN docid INT)
 BEGIN
	 SELECT * FROM Urls WHERE UrlId = docid;
 end;
//

CREATE PROCEDURE addAttributeIndex(IN attfilename VARCHAR(255), IN attname VARCHAR(255))
	BEGIN
		INSERT INTO AttributeIndex (FileName, AttributeListName) VALUES (attfilename, attname);
		SELECT LAST_INSERT_ID();
	end; //

CREATE PROCEDURE addAttributeData(IN attid VARCHAR(255), IN attname VARCHAR(255), IN atttype VARCHAR(255), IN attpatt VARCHAR(255))
	BEGIN
		INSERT INTO Attributes (AttributeId, AttributeName, AttributeType, Pattern) VALUES (attid, attname, atttype, attpatt);
	end; //
															     
CREATE PROCEDURE addUrlIndex(IN urlfilenameIn VARCHAR(255), IN urllistnameIn VARCHAR(255))
	BEGIN
		INSERT INTO UrlIndex (FileName, URLListName) VALUES (urlfilenameInfilename, urllistnameIn);
		SELECT LAST_INSERT_ID();
	end; //

CREATE PROCEDURE addURLData(IN urlidIn VARCHAR(255), IN urlIn VARCHAR(255), IN urltypeIn VARCHAR(255), IN urlcommentIn VARCHAR(255))
	BEGIN
		INSERT INTO Urls (UrlId, Url, UrlType, UrlComment) VALUES (urlidIn, urlIn, urltypeIn, urlcommentIn);
	end; //

CREATE PROCEDURE getAttributeData(IN attributeIdIn INT)
 BEGIN
	 SELECT * FROM Attributes WHERE AttributeId = attributeIdIn;
 end;
//

CREATE PROCEDURE addCrawlTableData(IN tableNameIn VARCHAR(255))
IF NOT EXISTS (SELECT 1 FROM CrawlDataIndex WHERE CrawlDataTableName = tableNameIn)
	BEGIN
		INSERT INTO CrawlDataIndex (CrawlDataTableName) VALUES (tableNameIn);
		SELECT LAST_INSERT_ID();
	end; //
ELSE
	BEGIN
		UPDATE CrawlDataIndex SET CrawlDataTableName = tableNameIn WHERE CrawlDataTableName = tableNameIn
	end; //
DELIMITER ;
/* More stored procedures needed:
Tests for all existing procedures (Use insert_test_values.sql or python)
Add url data -> same as above, return urlid of new record [done]
get attribute data -> use the stored procedure above as example, but get attributes with a given attid [done]
Add crawltabledata -> given a table name, add a new record to crawldataindex and return crawldataid (If exists, replace) [done]
 */


