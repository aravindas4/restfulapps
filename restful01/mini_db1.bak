--
-- PostgreSQL database dump
--

-- Dumped from database version 10.5 (Ubuntu 10.5-0ubuntu0.18.04)
-- Dumped by pg_dump version 10.5 (Ubuntu 10.5-0ubuntu0.18.04)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: plpgsql; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;


--
-- Name: EXTENSION plpgsql; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';


SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: auth_group; Type: TABLE; Schema: public; Owner: ara
--

CREATE TABLE public.auth_group (
    id integer NOT NULL,
    name character varying(80) NOT NULL
);


ALTER TABLE public.auth_group OWNER TO ara;

--
-- Name: auth_group_id_seq; Type: SEQUENCE; Schema: public; Owner: ara
--

CREATE SEQUENCE public.auth_group_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_group_id_seq OWNER TO ara;

--
-- Name: auth_group_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: ara
--

ALTER SEQUENCE public.auth_group_id_seq OWNED BY public.auth_group.id;


--
-- Name: auth_group_permissions; Type: TABLE; Schema: public; Owner: ara
--

CREATE TABLE public.auth_group_permissions (
    id integer NOT NULL,
    group_id integer NOT NULL,
    permission_id integer NOT NULL
);


ALTER TABLE public.auth_group_permissions OWNER TO ara;

--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE; Schema: public; Owner: ara
--

CREATE SEQUENCE public.auth_group_permissions_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_group_permissions_id_seq OWNER TO ara;

--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: ara
--

ALTER SEQUENCE public.auth_group_permissions_id_seq OWNED BY public.auth_group_permissions.id;


--
-- Name: auth_permission; Type: TABLE; Schema: public; Owner: ara
--

CREATE TABLE public.auth_permission (
    id integer NOT NULL,
    name character varying(255) NOT NULL,
    content_type_id integer NOT NULL,
    codename character varying(100) NOT NULL
);


ALTER TABLE public.auth_permission OWNER TO ara;

--
-- Name: auth_permission_id_seq; Type: SEQUENCE; Schema: public; Owner: ara
--

CREATE SEQUENCE public.auth_permission_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_permission_id_seq OWNER TO ara;

--
-- Name: auth_permission_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: ara
--

ALTER SEQUENCE public.auth_permission_id_seq OWNED BY public.auth_permission.id;


--
-- Name: auth_user; Type: TABLE; Schema: public; Owner: ara
--

CREATE TABLE public.auth_user (
    id integer NOT NULL,
    password character varying(128) NOT NULL,
    last_login timestamp with time zone,
    is_superuser boolean NOT NULL,
    username character varying(150) NOT NULL,
    first_name character varying(30) NOT NULL,
    last_name character varying(150) NOT NULL,
    email character varying(254) NOT NULL,
    is_staff boolean NOT NULL,
    is_active boolean NOT NULL,
    date_joined timestamp with time zone NOT NULL
);


ALTER TABLE public.auth_user OWNER TO ara;

--
-- Name: auth_user_groups; Type: TABLE; Schema: public; Owner: ara
--

CREATE TABLE public.auth_user_groups (
    id integer NOT NULL,
    user_id integer NOT NULL,
    group_id integer NOT NULL
);


ALTER TABLE public.auth_user_groups OWNER TO ara;

--
-- Name: auth_user_groups_id_seq; Type: SEQUENCE; Schema: public; Owner: ara
--

CREATE SEQUENCE public.auth_user_groups_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_user_groups_id_seq OWNER TO ara;

--
-- Name: auth_user_groups_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: ara
--

ALTER SEQUENCE public.auth_user_groups_id_seq OWNED BY public.auth_user_groups.id;


--
-- Name: auth_user_id_seq; Type: SEQUENCE; Schema: public; Owner: ara
--

CREATE SEQUENCE public.auth_user_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_user_id_seq OWNER TO ara;

--
-- Name: auth_user_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: ara
--

ALTER SEQUENCE public.auth_user_id_seq OWNED BY public.auth_user.id;


--
-- Name: auth_user_user_permissions; Type: TABLE; Schema: public; Owner: ara
--

CREATE TABLE public.auth_user_user_permissions (
    id integer NOT NULL,
    user_id integer NOT NULL,
    permission_id integer NOT NULL
);


ALTER TABLE public.auth_user_user_permissions OWNER TO ara;

--
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE; Schema: public; Owner: ara
--

CREATE SEQUENCE public.auth_user_user_permissions_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_user_user_permissions_id_seq OWNER TO ara;

--
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: ara
--

ALTER SEQUENCE public.auth_user_user_permissions_id_seq OWNED BY public.auth_user_user_permissions.id;


--
-- Name: authtoken_token; Type: TABLE; Schema: public; Owner: ara
--

CREATE TABLE public.authtoken_token (
    key character varying(40) NOT NULL,
    created timestamp with time zone NOT NULL,
    user_id integer NOT NULL
);


ALTER TABLE public.authtoken_token OWNER TO ara;

--
-- Name: competition; Type: TABLE; Schema: public; Owner: ara
--

CREATE TABLE public.competition (
    id integer NOT NULL,
    distance_in_feet integer NOT NULL,
    distance_achievement_date date NOT NULL,
    drone_id integer,
    pilot_id integer,
    CONSTRAINT competition_distance_in_feet_check CHECK ((distance_in_feet >= 0))
);


ALTER TABLE public.competition OWNER TO ara;

--
-- Name: competition_id_seq; Type: SEQUENCE; Schema: public; Owner: ara
--

CREATE SEQUENCE public.competition_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.competition_id_seq OWNER TO ara;

--
-- Name: competition_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: ara
--

ALTER SEQUENCE public.competition_id_seq OWNED BY public.competition.id;


--
-- Name: django_admin_log; Type: TABLE; Schema: public; Owner: ara
--

CREATE TABLE public.django_admin_log (
    id integer NOT NULL,
    action_time timestamp with time zone NOT NULL,
    object_id text,
    object_repr character varying(200) NOT NULL,
    action_flag smallint NOT NULL,
    change_message text NOT NULL,
    content_type_id integer,
    user_id integer NOT NULL,
    CONSTRAINT django_admin_log_action_flag_check CHECK ((action_flag >= 0))
);


ALTER TABLE public.django_admin_log OWNER TO ara;

--
-- Name: django_admin_log_id_seq; Type: SEQUENCE; Schema: public; Owner: ara
--

CREATE SEQUENCE public.django_admin_log_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_admin_log_id_seq OWNER TO ara;

--
-- Name: django_admin_log_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: ara
--

ALTER SEQUENCE public.django_admin_log_id_seq OWNED BY public.django_admin_log.id;


--
-- Name: django_content_type; Type: TABLE; Schema: public; Owner: ara
--

CREATE TABLE public.django_content_type (
    id integer NOT NULL,
    app_label character varying(100) NOT NULL,
    model character varying(100) NOT NULL
);


ALTER TABLE public.django_content_type OWNER TO ara;

--
-- Name: django_content_type_id_seq; Type: SEQUENCE; Schema: public; Owner: ara
--

CREATE SEQUENCE public.django_content_type_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_content_type_id_seq OWNER TO ara;

--
-- Name: django_content_type_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: ara
--

ALTER SEQUENCE public.django_content_type_id_seq OWNED BY public.django_content_type.id;


--
-- Name: django_migrations; Type: TABLE; Schema: public; Owner: ara
--

CREATE TABLE public.django_migrations (
    id integer NOT NULL,
    app character varying(255) NOT NULL,
    name character varying(255) NOT NULL,
    applied timestamp with time zone NOT NULL
);


ALTER TABLE public.django_migrations OWNER TO ara;

--
-- Name: django_migrations_id_seq; Type: SEQUENCE; Schema: public; Owner: ara
--

CREATE SEQUENCE public.django_migrations_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_migrations_id_seq OWNER TO ara;

--
-- Name: django_migrations_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: ara
--

ALTER SEQUENCE public.django_migrations_id_seq OWNED BY public.django_migrations.id;


--
-- Name: django_session; Type: TABLE; Schema: public; Owner: ara
--

CREATE TABLE public.django_session (
    session_key character varying(40) NOT NULL,
    session_data text NOT NULL,
    expire_date timestamp with time zone NOT NULL
);


ALTER TABLE public.django_session OWNER TO ara;

--
-- Name: drone; Type: TABLE; Schema: public; Owner: ara
--

CREATE TABLE public.drone (
    id integer NOT NULL,
    name character varying(250) NOT NULL,
    manufacturing_date timestamp with time zone NOT NULL,
    has_it_completed boolean NOT NULL,
    inserted_timestamp timestamp with time zone NOT NULL,
    drone_category_id integer NOT NULL,
    owner_id integer
);


ALTER TABLE public.drone OWNER TO ara;

--
-- Name: drone_category; Type: TABLE; Schema: public; Owner: ara
--

CREATE TABLE public.drone_category (
    id integer NOT NULL,
    name character varying(250) NOT NULL
);


ALTER TABLE public.drone_category OWNER TO ara;

--
-- Name: drone_category_id_seq; Type: SEQUENCE; Schema: public; Owner: ara
--

CREATE SEQUENCE public.drone_category_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.drone_category_id_seq OWNER TO ara;

--
-- Name: drone_category_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: ara
--

ALTER SEQUENCE public.drone_category_id_seq OWNED BY public.drone_category.id;


--
-- Name: drone_id_seq; Type: SEQUENCE; Schema: public; Owner: ara
--

CREATE SEQUENCE public.drone_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.drone_id_seq OWNER TO ara;

--
-- Name: drone_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: ara
--

ALTER SEQUENCE public.drone_id_seq OWNED BY public.drone.id;


--
-- Name: pilots; Type: TABLE; Schema: public; Owner: ara
--

CREATE TABLE public.pilots (
    id integer NOT NULL,
    name character varying(150) NOT NULL,
    gender character varying(2) NOT NULL,
    races_count integer NOT NULL,
    inserted_timestamp timestamp with time zone NOT NULL,
    CONSTRAINT pilots_races_count_check CHECK ((races_count >= 0))
);


ALTER TABLE public.pilots OWNER TO ara;

--
-- Name: pilots_id_seq; Type: SEQUENCE; Schema: public; Owner: ara
--

CREATE SEQUENCE public.pilots_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.pilots_id_seq OWNER TO ara;

--
-- Name: pilots_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: ara
--

ALTER SEQUENCE public.pilots_id_seq OWNED BY public.pilots.id;


--
-- Name: toys; Type: TABLE; Schema: public; Owner: ara
--

CREATE TABLE public.toys (
    id integer NOT NULL,
    created timestamp with time zone NOT NULL,
    name character varying(150) NOT NULL,
    description character varying(250) NOT NULL,
    toy_category character varying(200) NOT NULL,
    release_date timestamp with time zone NOT NULL,
    was_included_in_home boolean NOT NULL
);


ALTER TABLE public.toys OWNER TO ara;

--
-- Name: toys_id_seq; Type: SEQUENCE; Schema: public; Owner: ara
--

CREATE SEQUENCE public.toys_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.toys_id_seq OWNER TO ara;

--
-- Name: toys_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: ara
--

ALTER SEQUENCE public.toys_id_seq OWNED BY public.toys.id;


--
-- Name: auth_group id; Type: DEFAULT; Schema: public; Owner: ara
--

ALTER TABLE ONLY public.auth_group ALTER COLUMN id SET DEFAULT nextval('public.auth_group_id_seq'::regclass);


--
-- Name: auth_group_permissions id; Type: DEFAULT; Schema: public; Owner: ara
--

ALTER TABLE ONLY public.auth_group_permissions ALTER COLUMN id SET DEFAULT nextval('public.auth_group_permissions_id_seq'::regclass);


--
-- Name: auth_permission id; Type: DEFAULT; Schema: public; Owner: ara
--

ALTER TABLE ONLY public.auth_permission ALTER COLUMN id SET DEFAULT nextval('public.auth_permission_id_seq'::regclass);


--
-- Name: auth_user id; Type: DEFAULT; Schema: public; Owner: ara
--

ALTER TABLE ONLY public.auth_user ALTER COLUMN id SET DEFAULT nextval('public.auth_user_id_seq'::regclass);


--
-- Name: auth_user_groups id; Type: DEFAULT; Schema: public; Owner: ara
--

ALTER TABLE ONLY public.auth_user_groups ALTER COLUMN id SET DEFAULT nextval('public.auth_user_groups_id_seq'::regclass);


--
-- Name: auth_user_user_permissions id; Type: DEFAULT; Schema: public; Owner: ara
--

ALTER TABLE ONLY public.auth_user_user_permissions ALTER COLUMN id SET DEFAULT nextval('public.auth_user_user_permissions_id_seq'::regclass);


--
-- Name: competition id; Type: DEFAULT; Schema: public; Owner: ara
--

ALTER TABLE ONLY public.competition ALTER COLUMN id SET DEFAULT nextval('public.competition_id_seq'::regclass);


--
-- Name: django_admin_log id; Type: DEFAULT; Schema: public; Owner: ara
--

ALTER TABLE ONLY public.django_admin_log ALTER COLUMN id SET DEFAULT nextval('public.django_admin_log_id_seq'::regclass);


--
-- Name: django_content_type id; Type: DEFAULT; Schema: public; Owner: ara
--

ALTER TABLE ONLY public.django_content_type ALTER COLUMN id SET DEFAULT nextval('public.django_content_type_id_seq'::regclass);


--
-- Name: django_migrations id; Type: DEFAULT; Schema: public; Owner: ara
--

ALTER TABLE ONLY public.django_migrations ALTER COLUMN id SET DEFAULT nextval('public.django_migrations_id_seq'::regclass);


--
-- Name: drone id; Type: DEFAULT; Schema: public; Owner: ara
--

ALTER TABLE ONLY public.drone ALTER COLUMN id SET DEFAULT nextval('public.drone_id_seq'::regclass);


--
-- Name: drone_category id; Type: DEFAULT; Schema: public; Owner: ara
--

ALTER TABLE ONLY public.drone_category ALTER COLUMN id SET DEFAULT nextval('public.drone_category_id_seq'::regclass);


--
-- Name: pilots id; Type: DEFAULT; Schema: public; Owner: ara
--

ALTER TABLE ONLY public.pilots ALTER COLUMN id SET DEFAULT nextval('public.pilots_id_seq'::regclass);


--
-- Name: toys id; Type: DEFAULT; Schema: public; Owner: ara
--

ALTER TABLE ONLY public.toys ALTER COLUMN id SET DEFAULT nextval('public.toys_id_seq'::regclass);


--
-- Data for Name: auth_group; Type: TABLE DATA; Schema: public; Owner: ara
--

COPY public.auth_group (id, name) FROM stdin;
\.


--
-- Data for Name: auth_group_permissions; Type: TABLE DATA; Schema: public; Owner: ara
--

COPY public.auth_group_permissions (id, group_id, permission_id) FROM stdin;
\.


--
-- Data for Name: auth_permission; Type: TABLE DATA; Schema: public; Owner: ara
--

COPY public.auth_permission (id, name, content_type_id, codename) FROM stdin;
1	Can add log entry	1	add_logentry
2	Can change log entry	1	change_logentry
3	Can delete log entry	1	delete_logentry
4	Can view log entry	1	view_logentry
5	Can add permission	2	add_permission
6	Can change permission	2	change_permission
7	Can delete permission	2	delete_permission
8	Can view permission	2	view_permission
9	Can add group	3	add_group
10	Can change group	3	change_group
11	Can delete group	3	delete_group
12	Can view group	3	view_group
13	Can add user	4	add_user
14	Can change user	4	change_user
15	Can delete user	4	delete_user
16	Can view user	4	view_user
17	Can add content type	5	add_contenttype
18	Can change content type	5	change_contenttype
19	Can delete content type	5	delete_contenttype
20	Can view content type	5	view_contenttype
21	Can add session	6	add_session
22	Can change session	6	change_session
23	Can delete session	6	delete_session
24	Can view session	6	view_session
25	Can add toy	7	add_toy
26	Can change toy	7	change_toy
27	Can delete toy	7	delete_toy
28	Can view toy	7	view_toy
29	Can add competition	8	add_competition
30	Can change competition	8	change_competition
31	Can delete competition	8	delete_competition
32	Can view competition	8	view_competition
33	Can add drone	9	add_drone
34	Can change drone	9	change_drone
35	Can delete drone	9	delete_drone
36	Can view drone	9	view_drone
37	Can add drone category	10	add_dronecategory
38	Can change drone category	10	change_dronecategory
39	Can delete drone category	10	delete_dronecategory
40	Can view drone category	10	view_dronecategory
41	Can add pilot	11	add_pilot
42	Can change pilot	11	change_pilot
43	Can delete pilot	11	delete_pilot
44	Can view pilot	11	view_pilot
45	Can add Token	12	add_token
46	Can change Token	12	change_token
47	Can delete Token	12	delete_token
48	Can view Token	12	view_token
\.


--
-- Data for Name: auth_user; Type: TABLE DATA; Schema: public; Owner: ara
--

COPY public.auth_user (id, password, last_login, is_superuser, username, first_name, last_name, email, is_staff, is_active, date_joined) FROM stdin;
1	pbkdf2_sha256$120000$fGNh1u6KJnj2$Nf7uZzTWVsr9T/Nh7crsmH3BNGUwZXLSeW+bKqkQCaQ=	2018-11-06 17:46:05.9397+05:30	t	red			red@gmail.com	t	t	2018-11-06 16:25:12.889842+05:30
\.


--
-- Data for Name: auth_user_groups; Type: TABLE DATA; Schema: public; Owner: ara
--

COPY public.auth_user_groups (id, user_id, group_id) FROM stdin;
\.


--
-- Data for Name: auth_user_user_permissions; Type: TABLE DATA; Schema: public; Owner: ara
--

COPY public.auth_user_user_permissions (id, user_id, permission_id) FROM stdin;
\.


--
-- Data for Name: authtoken_token; Type: TABLE DATA; Schema: public; Owner: ara
--

COPY public.authtoken_token (key, created, user_id) FROM stdin;
ef96aa2e1d6a374496ded3f9a55a72bb81175ef4	2018-11-06 19:08:09.816324+05:30	1
\.


--
-- Data for Name: competition; Type: TABLE DATA; Schema: public; Owner: ara
--

COPY public.competition (id, distance_in_feet, distance_achievement_date, drone_id, pilot_id) FROM stdin;
\.


--
-- Data for Name: django_admin_log; Type: TABLE DATA; Schema: public; Owner: ara
--

COPY public.django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) FROM stdin;
\.


--
-- Data for Name: django_content_type; Type: TABLE DATA; Schema: public; Owner: ara
--

COPY public.django_content_type (id, app_label, model) FROM stdin;
1	admin	logentry
2	auth	permission
3	auth	group
4	auth	user
5	contenttypes	contenttype
6	sessions	session
7	toys	toy
8	drones	competition
9	drones	drone
10	drones	dronecategory
11	drones	pilot
12	authtoken	token
\.


--
-- Data for Name: django_migrations; Type: TABLE DATA; Schema: public; Owner: ara
--

COPY public.django_migrations (id, app, name, applied) FROM stdin;
1	contenttypes	0001_initial	2018-11-06 13:31:06.827044+05:30
2	auth	0001_initial	2018-11-06 13:31:07.841361+05:30
3	admin	0001_initial	2018-11-06 13:31:08.071578+05:30
4	admin	0002_logentry_remove_auto_add	2018-11-06 13:31:08.092893+05:30
5	admin	0003_logentry_add_action_flag_choices	2018-11-06 13:31:08.110906+05:30
6	contenttypes	0002_remove_content_type_name	2018-11-06 13:31:08.150975+05:30
7	auth	0002_alter_permission_name_max_length	2018-11-06 13:31:08.171099+05:30
8	auth	0003_alter_user_email_max_length	2018-11-06 13:31:08.201269+05:30
9	auth	0004_alter_user_username_opts	2018-11-06 13:31:08.223234+05:30
10	auth	0005_alter_user_last_login_null	2018-11-06 13:31:08.251291+05:30
11	auth	0006_require_contenttypes_0002	2018-11-06 13:31:08.261459+05:30
12	auth	0007_alter_validators_add_error_messages	2018-11-06 13:31:08.281652+05:30
13	auth	0008_alter_user_username_max_length	2018-11-06 13:31:08.362539+05:30
14	auth	0009_alter_user_last_name_max_length	2018-11-06 13:31:08.391354+05:30
15	sessions	0001_initial	2018-11-06 13:31:08.583002+05:30
16	toys	0001_added toy model	2018-11-06 13:31:08.69339+05:30
17	drones	0001_added drone app	2018-11-06 13:33:00.620458+05:30
18	authtoken	0001_initial	2018-11-06 17:30:21.042491+05:30
19	authtoken	0002_auto_20160226_1747	2018-11-06 17:30:21.111414+05:30
20	drones	0002_added autheticationsystem	2018-11-06 17:30:21.222889+05:30
\.


--
-- Data for Name: django_session; Type: TABLE DATA; Schema: public; Owner: ara
--

COPY public.django_session (session_key, session_data, expire_date) FROM stdin;
6p8pdscsvslfscpjgl8wb21uv3jfac69	NjRiZWIzNTUxMjgwNzcwOTU1ZTUyZDBjYzJlYmQ5ODI2YjNjMWEwYzp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJjZTkxMzdiODNiMDcyZjE1ODk4ZDg3MmY4MmNjZThiODIzYzFiMWI2In0=	2018-11-20 17:46:05.949682+05:30
\.


--
-- Data for Name: drone; Type: TABLE DATA; Schema: public; Owner: ara
--

COPY public.drone (id, name, manufacturing_date, has_it_completed, inserted_timestamp, drone_category_id, owner_id) FROM stdin;
5	Varuna	2018-01-01 16:31:00+05:30	f	2018-11-06 18:33:13.858148+05:30	3	1
\.


--
-- Data for Name: drone_category; Type: TABLE DATA; Schema: public; Owner: ara
--

COPY public.drone_category (id, name) FROM stdin;
1	Defence
2	Quadcopter
3	Health
\.


--
-- Data for Name: pilots; Type: TABLE DATA; Schema: public; Owner: ara
--

COPY public.pilots (id, name, gender, races_count, inserted_timestamp) FROM stdin;
1	Aravinda	M	23	2018-11-06 13:35:43.098355+05:30
2	Padma	F	2	2018-11-06 19:11:29.808007+05:30
\.


--
-- Data for Name: toys; Type: TABLE DATA; Schema: public; Owner: ara
--

COPY public.toys (id, created, name, description, toy_category, release_date, was_included_in_home) FROM stdin;
\.


--
-- Name: auth_group_id_seq; Type: SEQUENCE SET; Schema: public; Owner: ara
--

SELECT pg_catalog.setval('public.auth_group_id_seq', 1, false);


--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: ara
--

SELECT pg_catalog.setval('public.auth_group_permissions_id_seq', 1, false);


--
-- Name: auth_permission_id_seq; Type: SEQUENCE SET; Schema: public; Owner: ara
--

SELECT pg_catalog.setval('public.auth_permission_id_seq', 48, true);


--
-- Name: auth_user_groups_id_seq; Type: SEQUENCE SET; Schema: public; Owner: ara
--

SELECT pg_catalog.setval('public.auth_user_groups_id_seq', 1, false);


--
-- Name: auth_user_id_seq; Type: SEQUENCE SET; Schema: public; Owner: ara
--

SELECT pg_catalog.setval('public.auth_user_id_seq', 1, true);


--
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: ara
--

SELECT pg_catalog.setval('public.auth_user_user_permissions_id_seq', 1, false);


--
-- Name: competition_id_seq; Type: SEQUENCE SET; Schema: public; Owner: ara
--

SELECT pg_catalog.setval('public.competition_id_seq', 1, true);


--
-- Name: django_admin_log_id_seq; Type: SEQUENCE SET; Schema: public; Owner: ara
--

SELECT pg_catalog.setval('public.django_admin_log_id_seq', 1, false);


--
-- Name: django_content_type_id_seq; Type: SEQUENCE SET; Schema: public; Owner: ara
--

SELECT pg_catalog.setval('public.django_content_type_id_seq', 12, true);


--
-- Name: django_migrations_id_seq; Type: SEQUENCE SET; Schema: public; Owner: ara
--

SELECT pg_catalog.setval('public.django_migrations_id_seq', 20, true);


--
-- Name: drone_category_id_seq; Type: SEQUENCE SET; Schema: public; Owner: ara
--

SELECT pg_catalog.setval('public.drone_category_id_seq', 3, true);


--
-- Name: drone_id_seq; Type: SEQUENCE SET; Schema: public; Owner: ara
--

SELECT pg_catalog.setval('public.drone_id_seq', 5, true);


--
-- Name: pilots_id_seq; Type: SEQUENCE SET; Schema: public; Owner: ara
--

SELECT pg_catalog.setval('public.pilots_id_seq', 2, true);


--
-- Name: toys_id_seq; Type: SEQUENCE SET; Schema: public; Owner: ara
--

SELECT pg_catalog.setval('public.toys_id_seq', 1, false);


--
-- Name: auth_group auth_group_name_key; Type: CONSTRAINT; Schema: public; Owner: ara
--

ALTER TABLE ONLY public.auth_group
    ADD CONSTRAINT auth_group_name_key UNIQUE (name);


--
-- Name: auth_group_permissions auth_group_permissions_group_id_permission_id_0cd325b0_uniq; Type: CONSTRAINT; Schema: public; Owner: ara
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_permission_id_0cd325b0_uniq UNIQUE (group_id, permission_id);


--
-- Name: auth_group_permissions auth_group_permissions_pkey; Type: CONSTRAINT; Schema: public; Owner: ara
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_pkey PRIMARY KEY (id);


--
-- Name: auth_group auth_group_pkey; Type: CONSTRAINT; Schema: public; Owner: ara
--

ALTER TABLE ONLY public.auth_group
    ADD CONSTRAINT auth_group_pkey PRIMARY KEY (id);


--
-- Name: auth_permission auth_permission_content_type_id_codename_01ab375a_uniq; Type: CONSTRAINT; Schema: public; Owner: ara
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_codename_01ab375a_uniq UNIQUE (content_type_id, codename);


--
-- Name: auth_permission auth_permission_pkey; Type: CONSTRAINT; Schema: public; Owner: ara
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_pkey PRIMARY KEY (id);


--
-- Name: auth_user_groups auth_user_groups_pkey; Type: CONSTRAINT; Schema: public; Owner: ara
--

ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_pkey PRIMARY KEY (id);


--
-- Name: auth_user_groups auth_user_groups_user_id_group_id_94350c0c_uniq; Type: CONSTRAINT; Schema: public; Owner: ara
--

ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_user_id_group_id_94350c0c_uniq UNIQUE (user_id, group_id);


--
-- Name: auth_user auth_user_pkey; Type: CONSTRAINT; Schema: public; Owner: ara
--

ALTER TABLE ONLY public.auth_user
    ADD CONSTRAINT auth_user_pkey PRIMARY KEY (id);


--
-- Name: auth_user_user_permissions auth_user_user_permissions_pkey; Type: CONSTRAINT; Schema: public; Owner: ara
--

ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_pkey PRIMARY KEY (id);


--
-- Name: auth_user_user_permissions auth_user_user_permissions_user_id_permission_id_14a6b632_uniq; Type: CONSTRAINT; Schema: public; Owner: ara
--

ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_user_id_permission_id_14a6b632_uniq UNIQUE (user_id, permission_id);


--
-- Name: auth_user auth_user_username_key; Type: CONSTRAINT; Schema: public; Owner: ara
--

ALTER TABLE ONLY public.auth_user
    ADD CONSTRAINT auth_user_username_key UNIQUE (username);


--
-- Name: authtoken_token authtoken_token_pkey; Type: CONSTRAINT; Schema: public; Owner: ara
--

ALTER TABLE ONLY public.authtoken_token
    ADD CONSTRAINT authtoken_token_pkey PRIMARY KEY (key);


--
-- Name: authtoken_token authtoken_token_user_id_key; Type: CONSTRAINT; Schema: public; Owner: ara
--

ALTER TABLE ONLY public.authtoken_token
    ADD CONSTRAINT authtoken_token_user_id_key UNIQUE (user_id);


--
-- Name: competition competition_pkey; Type: CONSTRAINT; Schema: public; Owner: ara
--

ALTER TABLE ONLY public.competition
    ADD CONSTRAINT competition_pkey PRIMARY KEY (id);


--
-- Name: django_admin_log django_admin_log_pkey; Type: CONSTRAINT; Schema: public; Owner: ara
--

ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_pkey PRIMARY KEY (id);


--
-- Name: django_content_type django_content_type_app_label_model_76bd3d3b_uniq; Type: CONSTRAINT; Schema: public; Owner: ara
--

ALTER TABLE ONLY public.django_content_type
    ADD CONSTRAINT django_content_type_app_label_model_76bd3d3b_uniq UNIQUE (app_label, model);


--
-- Name: django_content_type django_content_type_pkey; Type: CONSTRAINT; Schema: public; Owner: ara
--

ALTER TABLE ONLY public.django_content_type
    ADD CONSTRAINT django_content_type_pkey PRIMARY KEY (id);


--
-- Name: django_migrations django_migrations_pkey; Type: CONSTRAINT; Schema: public; Owner: ara
--

ALTER TABLE ONLY public.django_migrations
    ADD CONSTRAINT django_migrations_pkey PRIMARY KEY (id);


--
-- Name: django_session django_session_pkey; Type: CONSTRAINT; Schema: public; Owner: ara
--

ALTER TABLE ONLY public.django_session
    ADD CONSTRAINT django_session_pkey PRIMARY KEY (session_key);


--
-- Name: drone_category drone_category_name_key; Type: CONSTRAINT; Schema: public; Owner: ara
--

ALTER TABLE ONLY public.drone_category
    ADD CONSTRAINT drone_category_name_key UNIQUE (name);


--
-- Name: drone_category drone_category_pkey; Type: CONSTRAINT; Schema: public; Owner: ara
--

ALTER TABLE ONLY public.drone_category
    ADD CONSTRAINT drone_category_pkey PRIMARY KEY (id);


--
-- Name: drone drone_pkey; Type: CONSTRAINT; Schema: public; Owner: ara
--

ALTER TABLE ONLY public.drone
    ADD CONSTRAINT drone_pkey PRIMARY KEY (id);


--
-- Name: pilots pilots_pkey; Type: CONSTRAINT; Schema: public; Owner: ara
--

ALTER TABLE ONLY public.pilots
    ADD CONSTRAINT pilots_pkey PRIMARY KEY (id);


--
-- Name: toys toys_pkey; Type: CONSTRAINT; Schema: public; Owner: ara
--

ALTER TABLE ONLY public.toys
    ADD CONSTRAINT toys_pkey PRIMARY KEY (id);


--
-- Name: auth_group_name_a6ea08ec_like; Type: INDEX; Schema: public; Owner: ara
--

CREATE INDEX auth_group_name_a6ea08ec_like ON public.auth_group USING btree (name varchar_pattern_ops);


--
-- Name: auth_group_permissions_group_id_b120cbf9; Type: INDEX; Schema: public; Owner: ara
--

CREATE INDEX auth_group_permissions_group_id_b120cbf9 ON public.auth_group_permissions USING btree (group_id);


--
-- Name: auth_group_permissions_permission_id_84c5c92e; Type: INDEX; Schema: public; Owner: ara
--

CREATE INDEX auth_group_permissions_permission_id_84c5c92e ON public.auth_group_permissions USING btree (permission_id);


--
-- Name: auth_permission_content_type_id_2f476e4b; Type: INDEX; Schema: public; Owner: ara
--

CREATE INDEX auth_permission_content_type_id_2f476e4b ON public.auth_permission USING btree (content_type_id);


--
-- Name: auth_user_groups_group_id_97559544; Type: INDEX; Schema: public; Owner: ara
--

CREATE INDEX auth_user_groups_group_id_97559544 ON public.auth_user_groups USING btree (group_id);


--
-- Name: auth_user_groups_user_id_6a12ed8b; Type: INDEX; Schema: public; Owner: ara
--

CREATE INDEX auth_user_groups_user_id_6a12ed8b ON public.auth_user_groups USING btree (user_id);


--
-- Name: auth_user_user_permissions_permission_id_1fbb5f2c; Type: INDEX; Schema: public; Owner: ara
--

CREATE INDEX auth_user_user_permissions_permission_id_1fbb5f2c ON public.auth_user_user_permissions USING btree (permission_id);


--
-- Name: auth_user_user_permissions_user_id_a95ead1b; Type: INDEX; Schema: public; Owner: ara
--

CREATE INDEX auth_user_user_permissions_user_id_a95ead1b ON public.auth_user_user_permissions USING btree (user_id);


--
-- Name: auth_user_username_6821ab7c_like; Type: INDEX; Schema: public; Owner: ara
--

CREATE INDEX auth_user_username_6821ab7c_like ON public.auth_user USING btree (username varchar_pattern_ops);


--
-- Name: authtoken_token_key_10f0b77e_like; Type: INDEX; Schema: public; Owner: ara
--

CREATE INDEX authtoken_token_key_10f0b77e_like ON public.authtoken_token USING btree (key varchar_pattern_ops);


--
-- Name: competition_drone_id_7a75e0f9; Type: INDEX; Schema: public; Owner: ara
--

CREATE INDEX competition_drone_id_7a75e0f9 ON public.competition USING btree (drone_id);


--
-- Name: competition_pilot_id_b0bf3075; Type: INDEX; Schema: public; Owner: ara
--

CREATE INDEX competition_pilot_id_b0bf3075 ON public.competition USING btree (pilot_id);


--
-- Name: django_admin_log_content_type_id_c4bce8eb; Type: INDEX; Schema: public; Owner: ara
--

CREATE INDEX django_admin_log_content_type_id_c4bce8eb ON public.django_admin_log USING btree (content_type_id);


--
-- Name: django_admin_log_user_id_c564eba6; Type: INDEX; Schema: public; Owner: ara
--

CREATE INDEX django_admin_log_user_id_c564eba6 ON public.django_admin_log USING btree (user_id);


--
-- Name: django_session_expire_date_a5c62663; Type: INDEX; Schema: public; Owner: ara
--

CREATE INDEX django_session_expire_date_a5c62663 ON public.django_session USING btree (expire_date);


--
-- Name: django_session_session_key_c0390e0f_like; Type: INDEX; Schema: public; Owner: ara
--

CREATE INDEX django_session_session_key_c0390e0f_like ON public.django_session USING btree (session_key varchar_pattern_ops);


--
-- Name: drone_category_name_c231e7ea_like; Type: INDEX; Schema: public; Owner: ara
--

CREATE INDEX drone_category_name_c231e7ea_like ON public.drone_category USING btree (name varchar_pattern_ops);


--
-- Name: drone_drone_category_id_3d5fc506; Type: INDEX; Schema: public; Owner: ara
--

CREATE INDEX drone_drone_category_id_3d5fc506 ON public.drone USING btree (drone_category_id);


--
-- Name: drone_owner_id_ae20e3c1; Type: INDEX; Schema: public; Owner: ara
--

CREATE INDEX drone_owner_id_ae20e3c1 ON public.drone USING btree (owner_id);


--
-- Name: auth_group_permissions auth_group_permissio_permission_id_84c5c92e_fk_auth_perm; Type: FK CONSTRAINT; Schema: public; Owner: ara
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissio_permission_id_84c5c92e_fk_auth_perm FOREIGN KEY (permission_id) REFERENCES public.auth_permission(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_group_permissions auth_group_permissions_group_id_b120cbf9_fk_auth_group_id; Type: FK CONSTRAINT; Schema: public; Owner: ara
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_b120cbf9_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES public.auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_permission auth_permission_content_type_id_2f476e4b_fk_django_co; Type: FK CONSTRAINT; Schema: public; Owner: ara
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_2f476e4b_fk_django_co FOREIGN KEY (content_type_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_groups auth_user_groups_group_id_97559544_fk_auth_group_id; Type: FK CONSTRAINT; Schema: public; Owner: ara
--

ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_group_id_97559544_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES public.auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_groups auth_user_groups_user_id_6a12ed8b_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: ara
--

ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_user_id_6a12ed8b_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_user_permissions auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm; Type: FK CONSTRAINT; Schema: public; Owner: ara
--

ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm FOREIGN KEY (permission_id) REFERENCES public.auth_permission(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_user_permissions auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: ara
--

ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: authtoken_token authtoken_token_user_id_35299eff_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: ara
--

ALTER TABLE ONLY public.authtoken_token
    ADD CONSTRAINT authtoken_token_user_id_35299eff_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: competition competition_drone_id_7a75e0f9_fk_drone_id; Type: FK CONSTRAINT; Schema: public; Owner: ara
--

ALTER TABLE ONLY public.competition
    ADD CONSTRAINT competition_drone_id_7a75e0f9_fk_drone_id FOREIGN KEY (drone_id) REFERENCES public.drone(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: competition competition_pilot_id_b0bf3075_fk_pilots_id; Type: FK CONSTRAINT; Schema: public; Owner: ara
--

ALTER TABLE ONLY public.competition
    ADD CONSTRAINT competition_pilot_id_b0bf3075_fk_pilots_id FOREIGN KEY (pilot_id) REFERENCES public.pilots(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: django_admin_log django_admin_log_content_type_id_c4bce8eb_fk_django_co; Type: FK CONSTRAINT; Schema: public; Owner: ara
--

ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_content_type_id_c4bce8eb_fk_django_co FOREIGN KEY (content_type_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: django_admin_log django_admin_log_user_id_c564eba6_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: ara
--

ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_user_id_c564eba6_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: drone drone_drone_category_id_3d5fc506_fk_drone_category_id; Type: FK CONSTRAINT; Schema: public; Owner: ara
--

ALTER TABLE ONLY public.drone
    ADD CONSTRAINT drone_drone_category_id_3d5fc506_fk_drone_category_id FOREIGN KEY (drone_category_id) REFERENCES public.drone_category(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: drone drone_owner_id_ae20e3c1_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: ara
--

ALTER TABLE ONLY public.drone
    ADD CONSTRAINT drone_owner_id_ae20e3c1_fk_auth_user_id FOREIGN KEY (owner_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- PostgreSQL database dump complete
--

