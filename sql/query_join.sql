-- Join command
SELECT authors.first, authors.last, books.title
FROM books
JOIN authors ON books.author_id = authors.author_id
WHERE authors.first = 'Ray' AND authors.last = 'Bradbury';