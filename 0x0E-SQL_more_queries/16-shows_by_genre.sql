-- Lists all shows, and all genres linked to that show,
-- from the database hbtn_0d_tvshows.
SELECT t.title, g.name
FROM tv_shows AS t
	LEFT JOIN tv_show_genres AS sg
	ON sg.show_id = t.id

	LEFT JOIN tv_genres AS g
	ON sg.genre_id = g.id
ORDER BY t.title, g.name;
