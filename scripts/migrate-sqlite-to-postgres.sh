#!/bin/bash

# load db variables
source ../postgres.env

if ! type "sequel"; then
  echo "sequel command missing, try: sudo gem install sequel"
  exit
fi

if ! type "psql"; then
  echo "psql command missing, try: brew install postgres"
  exit
fi

# migrate from sqlite to postgres:
PGPASSWORD=$POSTGRES_PASSWORD sequel -C sqlite://../database.db postgres://$POSTGRES_USER@localhost/$POSTGRES_DB


# convert 'charging' column of `updates` table from bigint to boolean:
echo "ALTER TABLE updates ALTER COLUMN charging DROP DEFAULT; \
ALTER TABLE updates ALTER charging TYPE bool USING CASE WHEN charging =0 THEN FALSE ELSE TRUE END; \
ALTER TABLE updates ALTER COLUMN charging SET DEFAULT FALSE;" \
| PGPASSWORD=$POSTGRES_PASSWORD psql -h 127.0.0.1 -d $POSTGRES_DB -U $POSTGRES_USER