-- Select books published on or before 1950
SELECT * FROM books
WHERE year_published <= 1950;

-- Select books written by a certain author
SELECT authors.first, authors.last, books.title
FROM books
JOIN authors ON books.author_id = authors.author_id
WHERE authors.first = 'Harper' AND authors.last = 'Lee';