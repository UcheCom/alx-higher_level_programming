-- Lists all Comedy shows in the database hbtn_0d_tvshows.
SELECT t.title
FROM tv_shows AS t
	JOIN tv_show_genres AS s
	ON s.show_id = t.id
	JOIN tv_genres AS g
	ON g.id = s.genre_id
WHERE g.name = 'Comedy'
ORDER BY t.title;
