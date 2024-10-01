-- Aggregate Functions

SELECT COUNT(DISTINCT author_id) as num_authors
FROM authors;

SELECT AVG(year_published) as avg_year_published
FROM books;