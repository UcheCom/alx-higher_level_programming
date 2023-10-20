-- Lists all genres not linked to the show Dexter in the 
-- database hbtn_0d_tvshows.
SELECT g.name
FROM tv_genres AS g
	LEFT JOIN (
	     SELECT g.id, g.name
	     FROM tv_genres AS g
		    JOIN tv_show_genres AS sg
		    ON sg.genre_id = g.id
		    JOIN tv_shows AS s
		    ON sg.show_id = s.id
	     WHERE s.title = 'Dexter'
	     )
	AS x_genres
	ON g.id = x_genres.id
	WHERE x_genres.id IS NULL
ORDER BY g.name;
