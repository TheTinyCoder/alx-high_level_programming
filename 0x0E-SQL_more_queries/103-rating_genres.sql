-- lists all genres by the sum of their rating
SELECT name, SUM(tv_show_ratings.rate) AS rating FROM tv_genres JOIN tv_show_genres ON tv_show_genres.genre_id = tv_genres.id JOIN tv_shows ON tv_shows.id = tv_show_genres.show_id JOIN tv_show_ratings ON tv_shows.id = tv_show_ratings.show_id GROUP BY name ORDER BY rating DESC;
