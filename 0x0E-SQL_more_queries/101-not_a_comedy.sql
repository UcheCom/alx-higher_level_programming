-- Lists all shows without the genre Comedy in the
-- database hbtn_0d_tvshows
SELECT s.title
FROM tv_shows AS s
	LEFT JOIN (
		SELECT s.id, s.title
		FROM tv_shows AS s
		JOIN tv_show_genres AS sg
		ON sg.show_id = s.id
		JOIN tv_genres AS g
		ON sg.genre_id = g.id
		WHERE g.name = 'Comedy'
	  ) 
	AS x_shows
     	ON x_shows.id = s.id
	WHERE x_shows.id IS NULL
ORDER BY s.title;
