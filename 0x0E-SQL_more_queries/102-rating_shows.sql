-- Lists all shows from hbtn_0d_tvshows_rate by their rating.
-- Records are ordered by descending rating.
SELECT s.title, SUM(rate) AS rating
FROM tv_shows AS s
	INNER JOIN tv_show_ratings AS sr
	ON sr.show_id = s.id
GROUP BY s.title
ORDER BY rating DESC;
