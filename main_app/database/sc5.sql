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

create table file
(
    id            bigint auto_increment
        primary key,
    duplicate_key varchar(1000) null,
    file_name     varchar(500)  not null,
    description   varchar(500)  null,
    status        varchar(26)   null,
    created_at    datetime      null,
    updated_at    datetime      null
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

create table permission
(
    id        bigint auto_increment
        primary key,
    label     varchar(300) not null,
    code      varchar(200) null,
    parent_id bigint       null
);

create table role
(
    id          int auto_increment
        primary key,
    code        varchar(100)   not null,
    description varchar(300)   null,
    permissions varchar(20000) null comment 'Danh sách URL prefix được phép truy cập, cách nhau bởi dấu phẩy',
    constraint code_UNIQUE
        unique (code)
)
    collate = utf8_unicode_ci;

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

create table user
(
    id               bigint auto_increment
        primary key,
    username         varchar(100)                 not null,
    password         varchar(64)                  null,
    full_name        varchar(300) charset utf8mb4 null,
    status           int                          null comment '1-active, 2-locked',
    created_at       datetime                     null,
    login_fail_count int default 0                null,
    last_fail_login  datetime                     null,
    roles            varchar(10000)               null comment 'Danh sách role code, cách nhau bởi dấu phẩy',
    mobile           varchar(12)                  not null,
    email            varchar(100)                 null,
    constraint username_UNIQUE
        unique (username)
);

create table user_log
(
    id         bigint auto_increment
        primary key,
    created_at datetime       null,
    user_id    bigint         null,
    username   varchar(100)   null,
    ip_address varchar(45)    null,
    action     varchar(100)   null comment 'login, logout, upload_id_card, change_password...',
    data       varchar(20000) null
)
    comment 'Lưu lại các thao tác/hành động của user' collate = utf8_unicode_ci;

INSERT INTO sc5.user (id, username, password, full_name, status, created_at, login_fail_count, last_fail_login, roles, mobile, email) VALUES (1, 'huyvq74', '$2a$10$2zsCZF3bYFViAn6YiqJ1C.Y7Xb4pPflbPZ/Z/SM9iGBDUG1uplZn2', 'Vũ Quang Huy', 1, '2022-08-05 11:53:28', 0, '2023-01-09 18:27:23', 'admin', '0866605601', null);

