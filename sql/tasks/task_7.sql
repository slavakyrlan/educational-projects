SELECT *
FROM music_instrument 
WHERE id = 1;


SELECT id, name
FROM music_instrument 
WHERE id = 1;


SELECT 
	a.id, a.name,
	b.id as child_id, 
	b.name as child_name
FROM music_instrument as a
LEFT JOIN music_instrument as b 
	ON b.parent_id = a.id
WHERE a.id = 1;


SELECT 
	a.id, a.name,
	b.id as child_id, b.name as child_name,
	c.id as grandchild_id, c.name as grandchild_name,
	d.id as level_1_id, d.name as level_1_name,
	e.id as level_2_id, e.name as level_2_name
FROM music_instrument as a
LEFT JOIN music_instrument as b 
	ON b.parent_id = a.id
LEFT JOIN music_instrument as c 
	ON c.parent_id = b.id
LEFT JOIN music_instrument as d 
	ON d.parent_id = c.id
LEFT JOIN music_instrument as e 
	ON e.parent_id = d.id
WHERE a.id = 1
ORDER BY a.name, child_name, grandchild_name;