create table if not exists  author (
    id text primary key,
    name text not null,
    email text unique not null,
    created timestamp,
    updated timestamp
);
