create table class
(
    id          bigint auto_increment
        primary key,
    name        varchar(255)                             null,
    code        varchar(50) charset ascii                null,
    semester    varchar(10) charset ascii                null,
    subject_id  bigint                                   null,
    week        varchar(50)                              null,
    day_of_week varchar(50)                              null,
    time_of_day varchar(50)                              null,
    is_assigned tinyint(2)                               null,
    teacher_id  bigint                                   null,
    created_at  datetime(3) default current_timestamp(3) not null,
    updated_at  datetime(3) default current_timestamp(3) null on update current_timestamp(3)
);

create table group_teacher
(
    id          bigint auto_increment
        primary key,
    name        varchar(255)                             null,
    description varchar(1000)                            null,
    leader      bigint                                   null,
    created_at  datetime(3) default current_timestamp(3) not null,
    updated_at  datetime(3) default current_timestamp(3) not null on update current_timestamp(3)
);

create table group_teacher_mapping
(
    id         bigint auto_increment
        primary key,
    teacher_id bigint       null,
    group_id   bigint       not null,
    role       varchar(500) null
);

create table input_algorithm
(
    id bigint auto_increment
        primary key
);

create table language
(
    id         bigint auto_increment
        primary key,
    name       varchar(100)                             null,
    created_at datetime(3) default current_timestamp(3) not null,
    updated_at datetime(3) default current_timestamp(3) not null on update current_timestamp(3)
);

create table language_teacher_mapping
(
    id          bigint auto_increment
        primary key,
    teacher_id  bigint null,
    language_id bigint null
);

create table output_algorithm
(
    id bigint auto_increment
        primary key
);

create table student_project
(
    id                  bigint auto_increment
        primary key,
    name                varchar(100)                             null,
    student_code        varchar(50) charset ascii                null,
    class_id            bigint                                   null,
    is_assigned         tinyint(2)                               null,
    created_at          datetime(3) default current_timestamp(3) not null,
    updated_at          datetime(3) default current_timestamp(3) null on update current_timestamp(3),
    teacher_1_id        bigint                                   null,
    teacher_2_id        bigint                                   null,
    teacher_3_id        bigint                                   null,
    teacher_assigned_id bigint                                   null
);

create table subject
(
    id         bigint auto_increment
        primary key,
    name       varchar(255)                             null,
    code       varchar(50) charset ascii                null,
    group_id   bigint                                   null,
    created_at datetime(3) default current_timestamp(3) not null,
    updated_at datetime(3) default current_timestamp(3) not null on update current_timestamp(3)
);

create table teacher
(
    id              bigint auto_increment
        primary key,
    full_name       varchar(100)                             null,
    rank_and_degree varchar(50)                              null,
    start_time      date                                     null,
    birthday        date                                     null,
    created_at      datetime(3) default current_timestamp(3) not null,
    updated_at      datetime(3) default current_timestamp(3) null on update current_timestamp(3)
);

