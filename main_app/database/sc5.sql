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

create table group_teacher
(
    id          bigint auto_increment,
    group_name  varchar(100) charset utf8mb4          not null,
    description varchar(500) charset utf8mb4          null,
    leader_id   bigint                                null,
    created_at  datetime(3) default CURRENT_TIMESTAMP not null,
    updated_at  datetime(3) default CURRENT_TIMESTAMP not null on update CURRENT_TIMESTAMP,
    constraint group_teacher_pk
        primary key (id)
)
    comment 'Nhóm chuyên môn';