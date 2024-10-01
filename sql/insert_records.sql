-- Insert records into tables

INSERT INTO authors (author_id, first, last) VALUES
('qwerty123-12-34-56', 'Bram', 'Stoker'),
('qwerty123-12-34-57', 'Albert', 'Camus'),
('qwerty123-12-34-58', 'Charles', 'Dickens'),
('qwerty123-12-34-59', 'John', 'Steinbeck'),
('qwerty123-12-34-60', 'Edith', 'Wharton'),
('qwerty123-12-34-61', 'Evan', 'Shikibu');

INSERT INTO books (book_id, title, year_published, author_id) VALUES
('qwerty123-12-34-62', 'Dracula', '1908', 'qwerty123-12-34-56'),
('qwerty123-12-34-63', 'The Plague', '1932', 'qwerty123-12-34-57'),
('qwerty123-12-34-64', 'Nicholas Nickleby', '1953', 'qwerty123-12-34-58'),
('qwerty123-12-34-65', 'The Pearl', '1915', 'qwerty123-12-34-59'),
('qwerty123-12-34-66', 'Ethan Frome', '1897', 'qwerty123-12-34-60'),
('qwerty123-12-34-67', 'The Tale of Genji', '1941', 'qwerty123-12-34-61');