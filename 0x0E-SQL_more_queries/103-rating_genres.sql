-- list genres in the database hbtn_0d_tvshows_rate by their rating
-- list rows in a database linked to a row in another table
SELECT tv_genres.name, sum(tv_show_ratings.rate) as rating FROM tv_genres
LEFT JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
LEFT JOIN tv_show_ratings ON tv_show_genres.show_id = tv_show_ratings.show_id
GROUP BY name
ORDER BY rating DESC;

