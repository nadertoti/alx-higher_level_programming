-- list the table in hbnt_0d_usa database
SELECT b.title, c.genre_id
FROM tv_show_genres c
LEFT JOIN tv_shows b
ON c.show_id = b.id
ORDER BY b.title, c.genre_id ASC;
