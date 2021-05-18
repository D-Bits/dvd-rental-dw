
CREATE TABLE dw.fact_sales
(
    id SERIAL PRIMARY KEY,
    film_id INT REFERENCES dw.dim_film (id),
    customer_id INT REFERENCES dw.dim_customer (id),
    rental_date DATETIME NOT NULL,
    return_date DATETIME NOT NULL,
    payment_date DATETIME NOT NULL,
    amount DECIMAL NOT NULL
);

CREATE TABLE dw.dim_film
(
    id SERIAL PRIMARY KEY,
    title VARCHAR(255),
    "description" TEXT,
    release_year INT,
    rental_duration SMALLINT,
    rental_rate DECIMAL NOT NULL,
    "length" SMALLINT,
    replacement_cost DECIMAL NOT NULL,
    -- MPAA rating
    rating VARCHAR(6),
    last_update TIMESTAMP,
    special_features TEXT
);

CREATE TABLE dw.dim_customer
(
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(255) NOT NULL,
    last_name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    activebool BOOLEAN,
    create_date DATE,
    last_update TIMESTAMP,
    active INT
)