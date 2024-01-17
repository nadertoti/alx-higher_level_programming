-- list all shows in a table
SELECT b.title, a.genres
FROM tv_show_genres a
LEFT JOIN tv_shows b
ON a.show_id = b.id OR NULL
ORDER BY b.title, a.genre_id ASC;
