-- Create subtraction table
-- depends: 0002_create_quotient

CREATE TABLE subtraction (
    id SERIAL PRIMARY KEY,
    a DOUBLE PRECISION NOT NULL,
    b DOUBLE PRECISION NOT NULL,
    created_at TIMESTAMP NOT NULL DEFAULT NOW()
);
