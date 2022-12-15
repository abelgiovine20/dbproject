CREATE DATABASE project_db;
GRANT ALL PRIVILEGES ON project_db.* TO 'webapp'@'%';
FLUSH PRIVILEGES;


USE project_db;

-- Put your DDL 
CREATE TABLE main_user (
    userID INT AUTO_INCREMENT NOT NULL,
    username VARCHAR(20),
    password VARCHAR(20),
    name VARCHAR(20),
    city VARCHAR(50),
    state VARCHAR(50),
    age INT,
    gender VARCHAR(20),
    datingPref VARCHAR(20),
    phoneNumber VARCHAR(50),
    description VARCHAR(500),
    isActive INT NOT NULL DEFAULT 1,
    isFlagged INT NOT NULL DEFAULT 0,
    PRIMARY KEY (userID)
    ON UPDATE CASCADE

);

CREATE TABLE liked_profiles (
    main_userID INT,
    likedProfileID INT,
    PRIMARY KEY (main_userID, likedProfileID),
    FOREIGN KEY (main_userID) REFERENCES main_user(userID)

);

CREATE TABLE disliked_profiles (
    main_userID INT,
    dislikedProfileID INT,
    PRIMARY KEY (main_userID, dislikedProfileID),
    FOREIGN KEY (main_userID) REFERENCES main_user(userID)

);

CREATE TABLE matched_profiles (
    main_userID INT,
    matchedProfileID INT,
    PRIMARY KEY (main_userID, matchedProfileID),
    FOREIGN KEY (main_userID) REFERENCES main_user(userID)

);

CREATE TABLE content_mod (
    modID INT AUTO_INCREMENT NOT NULL,
    username VARCHAR(20),
    password VARCHAR(20),
    PRIMARY KEY (modID)

);

CREATE TABLE system_admin (
    adminID INT AUTO_INCREMENT NOT NULL,
    username VARCHAR(20),
    password VARCHAR(20),
    PRIMARY KEY (adminID)

);

-- Add sample data.
insert into main_user (userID, username, password, name, city, state, age, gender, phoneNumber, isActive, isFlagged, datingPref) values (1, 'afigurski0', 'CD7VQ3sO', 'Asher', 'Beaverton', 'OR', 35, 'Male', '503-301-6172', 1, 1, 'Male');
insert into main_user (userID, username, password, name, city, state, age, gender, phoneNumber, isActive, isFlagged, datingPref) values (2, 'rjorck1', 'E7vOLjjoT', 'Romonda', 'Merrifield', 'VA', 9, 'Female', '571-744-0269', 0, 1, 'Female');
insert into main_user (userID, username, password, name, city, state, age, gender, phoneNumber, isActive, isFlagged, datingPref) values (3, 'ndivisek2', 'SgxPrN5h', 'Nomi', 'Beaufort', 'SC', 17, 'Female', '843-431-5137', 1, 0, 'Male');
insert into main_user (userID, username, password, name, city, state, age, gender, phoneNumber, isActive, isFlagged, datingPref) values (4, 'grosenfelder3', 'HVer5eFt', 'Guy', 'Chesapeake', 'VA', 18, 'Male', '757-882-9500', 1, 1, 'Female');
insert into main_user (userID, username, password, name, city, state, age, gender, phoneNumber, isActive, isFlagged, datingPref) values (5, 'lsheber4', 'r3fhmydxDK', 'Liuka', 'Monticello', 'MN', 50, 'Female', '763-300-7367', 1, 0, 'Female');
insert into main_user (userID, username, password, name, city, state, age, gender, phoneNumber, isActive, isFlagged, datingPref) values (6, 'nbalderson5', 'ns3MRaE', 'Normie', 'Pompano Beach', 'FL', 10, 'Male', '954-615-0780', 1, 0, 'Female');
insert into main_user (userID, username, password, name, city, state, age, gender, phoneNumber, isActive, isFlagged, datingPref) values (7, 'ablyth6', 'HLVEp1enbs', 'Addi', 'Omaha', 'NE', 20, 'Female', '402-379-3711', 1, 1, 'Male');
insert into main_user (userID, username, password, name, city, state, age, gender, phoneNumber, isActive, isFlagged, datingPref) values (8, 'oknight7', '7HuvvDMt', 'Obie', 'Columbia', 'MO', 7, 'Male', '573-382-1453', 1, 0, 'Female');
insert into main_user (userID, username, password, name, city, state, age, gender, phoneNumber, isActive, isFlagged, datingPref) values (9, 'sfold8', 'H9WjoPzVf', 'Sherry', 'Elizabeth', 'NJ', 38, 'Female', '908-879-4004', 1, 1, 'Male');
insert into main_user (userID, username, password, name, city, state, age, gender, phoneNumber, isActive, isFlagged, datingPref) values (10, 'fstaples9', 'gsN2BVTT', 'Frazier', 'Columbia', 'SC', 46, 'Male', '803-873-5177', 0, 0, 'Male');

-- Giving some descriptions

UPDATE main_user
SET description = 'This is my description. I like outdoor stuff and reading boring books'
WHERE userID % 2 = 0;

UPDATE main_user
SET description = 'This is my description. I like to code sample data in my free time.'
WHERE userID % 2 = 1;


insert into liked_profiles (main_userID, likedProfileID) values (1, 10);
insert into liked_profiles (main_userID, likedProfileID) values (1, 9);
insert into liked_profiles (main_userID, likedProfileID) values (1, 3);
insert into liked_profiles (main_userID, likedProfileID) values (4, 10);
insert into liked_profiles (main_userID, likedProfileID) values (2, 7);
insert into liked_profiles (main_userID, likedProfileID) values (2, 1);
insert into liked_profiles (main_userID, likedProfileID) values (2, 3);
insert into liked_profiles (main_userID, likedProfileID) values (3, 4);
insert into liked_profiles (main_userID, likedProfileID) values (3, 1);
insert into liked_profiles (main_userID, likedProfileID) values (3, 5);

insert into disliked_profiles (main_userID, dislikedProfileID) values (1, 10);
insert into disliked_profiles (main_userID, dislikedProfileID) values (1, 9);
insert into disliked_profiles (main_userID, dislikedProfileID) values (1, 3);
insert into disliked_profiles (main_userID, dislikedProfileID) values (4, 10);
insert into disliked_profiles (main_userID, dislikedProfileID) values (2, 7);
insert into disliked_profiles (main_userID, dislikedProfileID) values (2, 1);
insert into disliked_profiles (main_userID, dislikedProfileID) values (2, 3);
insert into disliked_profiles (main_userID, dislikedProfileID) values (3, 4);
insert into disliked_profiles (main_userID, dislikedProfileID) values (3, 1);
insert into disliked_profiles (main_userID, dislikedProfileID) values (3, 5);

insert into matched_profiles (main_userID, matchedProfileID) values (1, 10);
insert into matched_profiles (main_userID, matchedProfileID) values (1, 9);
insert into matched_profiles (main_userID, matchedProfileID) values (1, 3);
insert into matched_profiles (main_userID, matchedProfileID) values (4, 1);
insert into matched_profiles (main_userID, matchedProfileID) values (2, 7);
insert into matched_profiles (main_userID, matchedProfileID) values (2, 1);
insert into matched_profiles (main_userID, matchedProfileID) values (2, 3);
insert into matched_profiles (main_userID, matchedProfileID) values (3, 4);
insert into matched_profiles (main_userID, matchedProfileID) values (3, 1);
insert into matched_profiles (main_userID, matchedProfileID) values (3, 5);

insert into content_mod (username, password) values ('ccastello0', 'EYzcJPB6bD');
insert into content_mod (username, password) values ('mhailwood1', 'Txr3dE');
insert into content_mod (username, password) values ('nbaugham2', 'HOYEfbL1hFOa');
insert into content_mod (username, password) values ('mbarnewall3', 'gh7S27xy');
insert into content_mod (username, password) values ('pdoudny4', '7pEwKpY');
insert into content_mod (username, password) values ('vsturley5', 'PrsXj7dmkp');
insert into content_mod (username, password) values ('tkeepe6', 'dCdcN3FIcuyb');
insert into content_mod (username, password) values ('bbartlosz7', 'tmZGtuNfif');
insert into content_mod (username, password) values ('djeste8', 'gKSoGuHJLRb');
insert into content_mod (username, password) values ('gdomanek9', 'MjuztVsM');

insert into system_admin (username, password) values ('jguthrum0', 'v33ZhzzgKd');
insert into system_admin (username, password) values ('jwhetland1', 'HZiLGhIcsdJ');
insert into system_admin (username, password) values ('dyoungs2', 'LIMUPz');
insert into system_admin (username, password) values ('zwharrier3', 'D1yHRwnz');
insert into system_admin (username, password) values ('qekins4', 'mFUYZ2HT');
insert into system_admin (username, password) values ('abonnick5', 'VYwKKdmn8');
insert into system_admin (username, password) values ('hrabbitt6', 'FswPHLwFNp');
insert into system_admin (username, password) values ('kcoldicott7', 'W4JUkGOwM');
insert into system_admin (username, password) values ('jabrehart8', 'HapRAPn2Ln9');
insert into system_admin (username, password) values ('rikringill9', '3Ss7i6Zb');
