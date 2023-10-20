-- Script uses the hbtn_0d_tvshows database to lists all genres of the show Dexter
SELECT g.name
FROM tv_genres AS g
	JOIN tv_show_genres AS s
	ON g.id = s.genre_id
	JOIN tv_shows AS t
	ON s.show_id = t.id
WHERE t.title = 'Dexter'
ORDER BY g.name;
