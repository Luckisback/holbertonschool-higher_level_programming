-- importing the database hbtn_0d_tvshows
-- source = /holbertonschool-higher_level_programming/
-- SQL_more_queries/hbtn_0d_tvshows.sql;

--  A script that lists all shows contained in hbtn_0d_tvshows
-- that have at least one genre linked

USE hbtn_0d_tvshows;

SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows JOIN tv_show_genres
ON tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id;
