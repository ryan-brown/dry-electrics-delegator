drop table if exists updates;
    create table updates (
        id integer primary key autoincrement,
        username text not null,
        percentage integer not null,
        charging integer not null,
        updated_at text not null
);