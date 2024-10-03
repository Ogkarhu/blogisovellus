DROP TABLE if exists posts;

CREATE TABLE posts (
    id SERIAL PRIMARY KEY,
    breadtext TEXT NOT NULL,
    youtube_url VARCHAR,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

