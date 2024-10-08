DROP TABLE if exists comments;
DROP TABLE if exists posts;
DROP TABLE if exists users;


CREATE TABLE posts (
    id SERIAL PRIMARY KEY,
    breadtext TEXT NOT NULL,
    youtube_url VARCHAR,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    pw VARCHAR(255) NOT NULL,
    is_admin BOOL
);

CREATE TABLE comments (
    id SERIAL PRIMARY KEY,
    content TEXT,
    user_id INTEGER REFERENCES users,
    post_id INTEGER REFERENCES posts(id) ON DELETE CASCADE,
    sent_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);