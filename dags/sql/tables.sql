
CREATE TABLE dim_film
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

CREATE TABLE dim_customer
(
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(255) NOT NULL,
    last_name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    activebool BOOLEAN,
    create_date DATE,
    last_update TIMESTAMP,
    active INT
);

CREATE TABLE fact_sales
(
    id SERIAL PRIMARY KEY,
    film_id INT REFERENCES dim_film (id),
    customer_id INT REFERENCES dim_customer (id),
    rental_date TIMESTAMP NOT NULL,
    return_date TIMESTAMP NOT NULL,
    payment_date TIMESTAMP NOT NULL,
    amount DECIMAL NOT NULL
);
