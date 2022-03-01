Andrew Pratt, Silvia Mayo, Wilson McCloy
For the tables to work with the hw2_music_database.php,
first create a database named music-db via phpMyAdmin.

Once you have done that, set up three tables for users, ratings, artists:

```sql
CREATE TABLE users (
    username VARCHAR(255) PRIMARY KEY,
    password VARCHAR(255)
    );

INSERT INTO users (username, password)
    VALUES ("Amelia-Earhart","Youaom139&yu7");
INSERT INTO users (username, password)
    VALUES ("Otto","StarWars2*");


CREATE TABLE artists (
    song VARCHAR(255) PRIMARY KEY,
    artist VARCHAR(255)
    );

INSERT INTO artists (song, artist)
    VALUES ("Freeway", "Aimee Mann");
INSERT INTO artists (song, artist)
    VALUES ("Days of Wine and Roses", "Bill Evans");
INSERT INTO artists (song, artist)
    VALUES ("These Walls", "Kendrick Lamar");


CREATE TABLE ratings (
    id INT(1) PRIMARY KEY AUTO_INCREMENT,
    username VARCHAR(255),
    song VARCHAR(255),
    rating INT(1),
    FOREIGN KEY (username) REFERENCES users(username) ON DELETE CASCADE,
    FOREIGN KEY (song) REFERENCES artists(song) ON DELETE CASCADE
    );

INSERT INTO ratings (username, song, rating)
    VALUES ("Amelia-Earhart", "Freeway", 3);
INSERT INTO ratings (username, song, rating)
    VALUES ("Amelia-Earhart", "Days of Wine and Roses", 4);
INSERT INTO ratings (username, song, rating)
    VALUES ("Otto", "Days of Wine and Roses", 5);
INSERT INTO ratings (username, song, rating)
    VALUES ("Amelia-Earhart", "These Walls", 4);
```