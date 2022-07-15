create table if not exists  author (
    id text primary key,
    name text not null,
    email text unique not null,
    created timestamp,
    updated timestamp
);

create table if not exists  entry (
    id text primary key,
    description text not null,
    incomme bool default false,
    value float not null,
    author_id text not null REFERENCES author (id),
    created timestamp,
    updated timestamp
);

