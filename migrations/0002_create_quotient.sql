-- Create quotient table
-- depends: 0001_create_addition

CREATE TABLE quotient (
    id SERIAL PRIMARY KEY,
    a DOUBLE PRECISION NOT NULL,
    b DOUBLE PRECISION NOT NULL,
    created_at TIMESTAMP NOT NULL DEFAULT NOW()
);
