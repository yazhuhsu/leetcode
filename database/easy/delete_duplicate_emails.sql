DELETE FROM person WHERE id IN (
	SELECT id FROM (
		SELECT id, email,
		ROW_NUMBER() OVER (
			PARTITION BY email
			ORDER BY id
		)
		FROM person
	) dt WHERE row_number > 1
)