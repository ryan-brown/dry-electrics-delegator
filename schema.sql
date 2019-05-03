drop table if exists users;
create table users (
    id integer primary key autoincrement,
    email text not null,
    username text not null,
    password text not null,
    zap_token text not null
);

drop table if exists updates;
create table updates (
    id integer primary key autoincrement,
    user_id integer not null,
    percentage integer not null,
    charging integer not null,
    updated_at text not null
);
