#!/bin/bash
set -e

psql -v ON_ERROR_STOP=1 --username "$(cat /run/secrets/db_user)" --dbname "$(cat /run/secrets/db_name)" << EOSQL
\c postgres
CREATE TABLE questions (
    id SERIAL PRIMARY KEY,
    question VARCHAR(126),
    description VARCHAR(512),
    key VARCHAR(50),
    created_on TIMESTAMP
);
EOSQL
