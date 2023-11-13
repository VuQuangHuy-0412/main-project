create table teacher
(
    id              bigint auto_increment,
    full_name       varchar(100) charset utf8mb4          not null,
    rank_and_degree varchar(50) charset utf8mb4           not null,
    start_time      date                                  null,
    birthday        date                                  null,
    created_at      datetime(3) default CURRENT_TIMESTAMP not null,
    updated_at      datetime(3) default CURRENT_TIMESTAMP not null on update CURRENT_TIMESTAMP,
    constraint teacher_pk
        primary key (id)
);

