-- Create addition table
-- depends:

CREATE TABLE addition (
    id SERIAL PRIMARY KEY,
    a DOUBLE PRECISION NOT NULL,
    b DOUBLE PRECISION NOT NULL,
    created_at TIMESTAMP NOT NULL DEFAULT NOW()
);
