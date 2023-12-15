-- list shows that have a genre id
SELECT * FROM (SELECT tv_shows.title, tv_show_genres.genre_id FROM tv_shows LEFT JOIN tv_show_genres ON tv_show_genres.show_id = tv_shows.id) AS tv WHERE tv.genre_id IS NULL;
