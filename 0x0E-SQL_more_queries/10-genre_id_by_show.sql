-- Lists all shows with at least one genre linked.
-- tv_shows.title and tv_show_genres.genre_id ORDER
SELECT t.title, g.genre_id
FROM tv_shows AS t, tv_show_genres AS g
WHERE g.show_id = t.id
ORDER BY t.title, g.genre_id;
