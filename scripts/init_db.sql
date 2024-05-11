--
-- PostgreSQL database dump
--

-- Dumped from database version 16.0
-- Dumped by pg_dump version 16.0

-- Started on 2024-05-12 01:29:47

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- TOC entry 215 (class 1259 OID 27388)
-- Name: alembic_version; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.alembic_version (
    version_num character varying(32) NOT NULL
);


--
-- TOC entry 231 (class 1259 OID 27479)
-- Name: bill; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.bill (
    order_id integer,
    dish_id integer,
    id integer NOT NULL
);


--
-- TOC entry 230 (class 1259 OID 27478)
-- Name: bill_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.bill_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- TOC entry 4906 (class 0 OID 0)
-- Dependencies: 230
-- Name: bill_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.bill_id_seq OWNED BY public.bill.id;


--
-- TOC entry 217 (class 1259 OID 27394)
-- Name: client; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.client (
    last_name character varying(30) NOT NULL,
    first_name character varying(30) NOT NULL,
    patronymic character varying(30) NOT NULL,
    phone_number character varying(20) NOT NULL,
    id integer NOT NULL
);


--
-- TOC entry 216 (class 1259 OID 27393)
-- Name: client_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.client_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- TOC entry 4907 (class 0 OID 0)
-- Dependencies: 216
-- Name: client_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.client_id_seq OWNED BY public.client.id;


--
-- TOC entry 233 (class 1259 OID 27497)
-- Name: composition_of_dish; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.composition_of_dish (
    product_id integer,
    dish_id integer,
    number_of_products double precision NOT NULL,
    unit_of_measurement_id integer,
    id integer NOT NULL
);


--
-- TOC entry 232 (class 1259 OID 27496)
-- Name: composition_of_dish_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.composition_of_dish_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- TOC entry 4908 (class 0 OID 0)
-- Dependencies: 232
-- Name: composition_of_dish_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.composition_of_dish_id_seq OWNED BY public.composition_of_dish.id;


--
-- TOC entry 225 (class 1259 OID 27433)
-- Name: dish; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.dish (
    name character varying(100) NOT NULL,
    cost double precision NOT NULL,
    weight double precision NOT NULL,
    calories double precision NOT NULL,
    cooking_time time without time zone NOT NULL,
    type_of_dish_id integer,
    id integer NOT NULL
);


--
-- TOC entry 224 (class 1259 OID 27432)
-- Name: dish_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.dish_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- TOC entry 4909 (class 0 OID 0)
-- Dependencies: 224
-- Name: dish_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.dish_id_seq OWNED BY public.dish.id;


--
-- TOC entry 227 (class 1259 OID 27451)
-- Name: order; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public."order" (
    client_id integer,
    date timestamp without time zone NOT NULL,
    id integer NOT NULL
);


--
-- TOC entry 226 (class 1259 OID 27450)
-- Name: order_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.order_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- TOC entry 4910 (class 0 OID 0)
-- Dependencies: 226
-- Name: order_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.order_id_seq OWNED BY public."order".id;


--
-- TOC entry 229 (class 1259 OID 27465)
-- Name: product; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.product (
    name character varying(30) NOT NULL,
    type_of_product_id integer,
    id integer NOT NULL
);


--
-- TOC entry 228 (class 1259 OID 27464)
-- Name: product_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.product_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- TOC entry 4911 (class 0 OID 0)
-- Dependencies: 228
-- Name: product_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.product_id_seq OWNED BY public.product.id;


--
-- TOC entry 219 (class 1259 OID 27406)
-- Name: type_of_dish; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.type_of_dish (
    name character varying(30) NOT NULL,
    id integer NOT NULL
);


--
-- TOC entry 218 (class 1259 OID 27405)
-- Name: type_of_dish_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.type_of_dish_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- TOC entry 4912 (class 0 OID 0)
-- Dependencies: 218
-- Name: type_of_dish_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.type_of_dish_id_seq OWNED BY public.type_of_dish.id;


--
-- TOC entry 221 (class 1259 OID 27415)
-- Name: type_of_product; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.type_of_product (
    name character varying(30) NOT NULL,
    id integer NOT NULL
);


--
-- TOC entry 220 (class 1259 OID 27414)
-- Name: type_of_product_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.type_of_product_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- TOC entry 4913 (class 0 OID 0)
-- Dependencies: 220
-- Name: type_of_product_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.type_of_product_id_seq OWNED BY public.type_of_product.id;


--
-- TOC entry 223 (class 1259 OID 27424)
-- Name: unit_of_measurement; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.unit_of_measurement (
    name character varying(100) NOT NULL,
    id integer NOT NULL
);


--
-- TOC entry 222 (class 1259 OID 27423)
-- Name: unit_of_measurement_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.unit_of_measurement_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- TOC entry 4914 (class 0 OID 0)
-- Dependencies: 222
-- Name: unit_of_measurement_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.unit_of_measurement_id_seq OWNED BY public.unit_of_measurement.id;


--
-- TOC entry 4685 (class 2604 OID 27482)
-- Name: bill id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.bill ALTER COLUMN id SET DEFAULT nextval('public.bill_id_seq'::regclass);


--
-- TOC entry 4678 (class 2604 OID 27397)
-- Name: client id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.client ALTER COLUMN id SET DEFAULT nextval('public.client_id_seq'::regclass);


--
-- TOC entry 4686 (class 2604 OID 27500)
-- Name: composition_of_dish id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.composition_of_dish ALTER COLUMN id SET DEFAULT nextval('public.composition_of_dish_id_seq'::regclass);


--
-- TOC entry 4682 (class 2604 OID 27436)
-- Name: dish id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.dish ALTER COLUMN id SET DEFAULT nextval('public.dish_id_seq'::regclass);


--
-- TOC entry 4683 (class 2604 OID 27454)
-- Name: order id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."order" ALTER COLUMN id SET DEFAULT nextval('public.order_id_seq'::regclass);


--
-- TOC entry 4684 (class 2604 OID 27468)
-- Name: product id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.product ALTER COLUMN id SET DEFAULT nextval('public.product_id_seq'::regclass);


--
-- TOC entry 4679 (class 2604 OID 27409)
-- Name: type_of_dish id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.type_of_dish ALTER COLUMN id SET DEFAULT nextval('public.type_of_dish_id_seq'::regclass);


--
-- TOC entry 4680 (class 2604 OID 27418)
-- Name: type_of_product id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.type_of_product ALTER COLUMN id SET DEFAULT nextval('public.type_of_product_id_seq'::regclass);


--
-- TOC entry 4681 (class 2604 OID 27427)
-- Name: unit_of_measurement id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.unit_of_measurement ALTER COLUMN id SET DEFAULT nextval('public.unit_of_measurement_id_seq'::regclass);


--
-- TOC entry 4882 (class 0 OID 27388)
-- Dependencies: 215
-- Data for Name: alembic_version; Type: TABLE DATA; Schema: public; Owner: -
--

INSERT INTO public.alembic_version VALUES ('3d46706d145b');


--
-- TOC entry 4898 (class 0 OID 27479)
-- Dependencies: 231
-- Data for Name: bill; Type: TABLE DATA; Schema: public; Owner: -
--

INSERT INTO public.bill VALUES (1, 3, 22);
INSERT INTO public.bill VALUES (1, 5, 23);
INSERT INTO public.bill VALUES (4, 1, 24);
INSERT INTO public.bill VALUES (3, 6, 25);
INSERT INTO public.bill VALUES (2, 2, 26);


--
-- TOC entry 4884 (class 0 OID 27394)
-- Dependencies: 217
-- Data for Name: client; Type: TABLE DATA; Schema: public; Owner: -
--

INSERT INTO public.client VALUES ('Булка', 'Емельян', 'Антонович', '+7 (987) 629-10-60', 1);
INSERT INTO public.client VALUES ('Ярмухаметов', 'Валентин', 'Макарович', '+7 (908) 630-78-19', 2);
INSERT INTO public.client VALUES ('Гришачёв', 'Игнатий', 'Себастьянович', '+7 (924) 315-85-71', 3);
INSERT INTO public.client VALUES ('Ярмоленко', 'Вера', 'Данииловна', '+7 (935) 271-44-15', 4);


--
-- TOC entry 4900 (class 0 OID 27497)
-- Dependencies: 233
-- Data for Name: composition_of_dish; Type: TABLE DATA; Schema: public; Owner: -
--

INSERT INTO public.composition_of_dish VALUES (1, 1, 100, 1, 8);
INSERT INTO public.composition_of_dish VALUES (2, 1, 70, 1, 9);
INSERT INTO public.composition_of_dish VALUES (3, 1, 1, 3, 10);
INSERT INTO public.composition_of_dish VALUES (4, 1, 50, 1, 11);
INSERT INTO public.composition_of_dish VALUES (5, 1, 80, 2, 12);
INSERT INTO public.composition_of_dish VALUES (6, 1, 20, 1, 13);
INSERT INTO public.composition_of_dish VALUES (12, 2, 300, 1, 14);
INSERT INTO public.composition_of_dish VALUES (13, 2, 150, 1, 15);
INSERT INTO public.composition_of_dish VALUES (4, 2, 500, 1, 16);
INSERT INTO public.composition_of_dish VALUES (15, 2, 150, 2, 17);
INSERT INTO public.composition_of_dish VALUES (14, 2, 120, 1, 18);
INSERT INTO public.composition_of_dish VALUES (16, 2, 2, 3, 19);
INSERT INTO public.composition_of_dish VALUES (17, 2, 20, 1, 20);
INSERT INTO public.composition_of_dish VALUES (8, 3, 750, 1, 21);
INSERT INTO public.composition_of_dish VALUES (18, 3, 300, 1, 22);
INSERT INTO public.composition_of_dish VALUES (9, 3, 300, 1, 23);
INSERT INTO public.composition_of_dish VALUES (1, 3, 150, 1, 24);
INSERT INTO public.composition_of_dish VALUES (19, 3, 150, 1, 25);
INSERT INTO public.composition_of_dish VALUES (20, 3, 40, 1, 26);
INSERT INTO public.composition_of_dish VALUES (3, 3, 100, 1, 27);
INSERT INTO public.composition_of_dish VALUES (21, 3, 10, 1, 28);
INSERT INTO public.composition_of_dish VALUES (9, 5, 70, 1, 29);
INSERT INTO public.composition_of_dish VALUES (1, 5, 50, 1, 30);
INSERT INTO public.composition_of_dish VALUES (4, 5, 25, 1, 31);
INSERT INTO public.composition_of_dish VALUES (7, 5, 100, 1, 32);
INSERT INTO public.composition_of_dish VALUES (26, 5, 30, 1, 33);
INSERT INTO public.composition_of_dish VALUES (11, 5, 20, 1, 34);
INSERT INTO public.composition_of_dish VALUES (8, 6, 150, 1, 35);
INSERT INTO public.composition_of_dish VALUES (2, 6, 50, 1, 36);
INSERT INTO public.composition_of_dish VALUES (4, 6, 22, 1, 37);
INSERT INTO public.composition_of_dish VALUES (1, 6, 70, 1, 38);
INSERT INTO public.composition_of_dish VALUES (22, 6, 15, 1, 39);
INSERT INTO public.composition_of_dish VALUES (24, 6, 2, 3, 40);
INSERT INTO public.composition_of_dish VALUES (25, 6, 50, 1, 41);
INSERT INTO public.composition_of_dish VALUES (26, 6, 50, 1, 42);


--
-- TOC entry 4892 (class 0 OID 27433)
-- Dependencies: 225
-- Data for Name: dish; Type: TABLE DATA; Schema: public; Owner: -
--

INSERT INTO public.dish VALUES ('Греческий салат', 260, 500, 421.5, '00:15:00', 3, 1);
INSERT INTO public.dish VALUES ('Чизкейк', 250, 100, 400, '00:20:00', 5, 2);
INSERT INTO public.dish VALUES ('Борщ', 200, 300, 173.1, '00:15:00', 1, 3);
INSERT INTO public.dish VALUES ('Капучино', 100, 240, 74, '00:10:00', 4, 4);
INSERT INTO public.dish VALUES ('Салат Цезарь', 320, 150, 300, '00:10:00', 3, 5);
INSERT INTO public.dish VALUES ('Бургер', 200, 150, 300, '00:20:00', 2, 6);


--
-- TOC entry 4894 (class 0 OID 27451)
-- Dependencies: 227
-- Data for Name: order; Type: TABLE DATA; Schema: public; Owner: -
--

INSERT INTO public."order" VALUES (3, '2023-05-03 14:14:00', 1);
INSERT INTO public."order" VALUES (2, '2023-05-03 11:57:00', 2);
INSERT INTO public."order" VALUES (1, '2023-05-03 08:40:00', 3);
INSERT INTO public."order" VALUES (4, '2023-05-03 20:32:00', 4);


--
-- TOC entry 4896 (class 0 OID 27465)
-- Dependencies: 229
-- Data for Name: product; Type: TABLE DATA; Schema: public; Owner: -
--

INSERT INTO public.product VALUES ('Помидор', 4, 1);
INSERT INTO public.product VALUES ('Огурец', 4, 2);
INSERT INTO public.product VALUES ('Лук', 4, 3);
INSERT INTO public.product VALUES ('Сыр', 5, 4);
INSERT INTO public.product VALUES ('Маслины', 3, 5);
INSERT INTO public.product VALUES ('Оливковое масло', 9, 6);
INSERT INTO public.product VALUES ('Курица', 1, 7);
INSERT INTO public.product VALUES ('Говядина', 1, 8);
INSERT INTO public.product VALUES ('Капуста', 4, 9);
INSERT INTO public.product VALUES ('Соус Цезарь', 10, 10);
INSERT INTO public.product VALUES ('Сухарики', 6, 11);
INSERT INTO public.product VALUES ('Печенья', 6, 12);
INSERT INTO public.product VALUES ('Сливочное масло', 9, 13);
INSERT INTO public.product VALUES ('Сахар', 6, 14);
INSERT INTO public.product VALUES ('Сливки', 6, 15);
INSERT INTO public.product VALUES ('Куриное яйцо', 11, 16);
INSERT INTO public.product VALUES ('Мука', 6, 17);
INSERT INTO public.product VALUES ('Картофель', 4, 18);
INSERT INTO public.product VALUES ('Свёкла', 4, 19);
INSERT INTO public.product VALUES ('Масло подсолнечное', 9, 20);
INSERT INTO public.product VALUES ('Чеснок', 4, 21);
INSERT INTO public.product VALUES ('Бекон', 1, 22);
INSERT INTO public.product VALUES ('Семга', 2, 23);
INSERT INTO public.product VALUES ('Булка', 6, 24);
INSERT INTO public.product VALUES ('Кетчуп', 10, 25);
INSERT INTO public.product VALUES ('Майонез', 10, 26);


--
-- TOC entry 4886 (class 0 OID 27406)
-- Dependencies: 219
-- Data for Name: type_of_dish; Type: TABLE DATA; Schema: public; Owner: -
--

INSERT INTO public.type_of_dish VALUES ('Супы', 1);
INSERT INTO public.type_of_dish VALUES ('Вторые блюда', 2);
INSERT INTO public.type_of_dish VALUES ('Салаты', 3);
INSERT INTO public.type_of_dish VALUES ('Коктейли, напитки', 4);
INSERT INTO public.type_of_dish VALUES ('Десерты', 5);


--
-- TOC entry 4888 (class 0 OID 27415)
-- Dependencies: 221
-- Data for Name: type_of_product; Type: TABLE DATA; Schema: public; Owner: -
--

INSERT INTO public.type_of_product VALUES ('Мясо', 1);
INSERT INTO public.type_of_product VALUES ('Морепродукты', 2);
INSERT INTO public.type_of_product VALUES ('Фрукты', 3);
INSERT INTO public.type_of_product VALUES ('Овощи', 4);
INSERT INTO public.type_of_product VALUES ('Молочные продукты', 5);
INSERT INTO public.type_of_product VALUES ('Мука, кондитерские изделия', 6);
INSERT INTO public.type_of_product VALUES ('Напитки', 7);
INSERT INTO public.type_of_product VALUES ('Рыба', 8);
INSERT INTO public.type_of_product VALUES ('Масло', 9);
INSERT INTO public.type_of_product VALUES ('Соусы', 10);
INSERT INTO public.type_of_product VALUES ('Яйца', 11);


--
-- TOC entry 4890 (class 0 OID 27424)
-- Dependencies: 223
-- Data for Name: unit_of_measurement; Type: TABLE DATA; Schema: public; Owner: -
--

INSERT INTO public.unit_of_measurement VALUES ('Граммы', 1);
INSERT INTO public.unit_of_measurement VALUES ('Миллилитры', 2);
INSERT INTO public.unit_of_measurement VALUES ('Штуки', 3);
INSERT INTO public.unit_of_measurement VALUES ('Килограммы', 4);
INSERT INTO public.unit_of_measurement VALUES ('Литры', 5);


--
-- TOC entry 4915 (class 0 OID 0)
-- Dependencies: 230
-- Name: bill_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.bill_id_seq', 26, true);


--
-- TOC entry 4916 (class 0 OID 0)
-- Dependencies: 216
-- Name: client_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.client_id_seq', 4, true);


--
-- TOC entry 4917 (class 0 OID 0)
-- Dependencies: 232
-- Name: composition_of_dish_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.composition_of_dish_id_seq', 42, true);


--
-- TOC entry 4918 (class 0 OID 0)
-- Dependencies: 224
-- Name: dish_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.dish_id_seq', 6, true);


--
-- TOC entry 4919 (class 0 OID 0)
-- Dependencies: 226
-- Name: order_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.order_id_seq', 4, true);


--
-- TOC entry 4920 (class 0 OID 0)
-- Dependencies: 228
-- Name: product_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.product_id_seq', 26, true);


--
-- TOC entry 4921 (class 0 OID 0)
-- Dependencies: 218
-- Name: type_of_dish_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.type_of_dish_id_seq', 5, true);


--
-- TOC entry 4922 (class 0 OID 0)
-- Dependencies: 220
-- Name: type_of_product_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.type_of_product_id_seq', 11, true);


--
-- TOC entry 4923 (class 0 OID 0)
-- Dependencies: 222
-- Name: unit_of_measurement_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.unit_of_measurement_id_seq', 11, true);


--
-- TOC entry 4688 (class 2606 OID 27392)
-- Name: alembic_version alembic_version_pkc; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.alembic_version
    ADD CONSTRAINT alembic_version_pkc PRIMARY KEY (version_num);


--
-- TOC entry 4725 (class 2606 OID 27484)
-- Name: bill bill_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.bill
    ADD CONSTRAINT bill_pkey PRIMARY KEY (id);


--
-- TOC entry 4690 (class 2606 OID 27399)
-- Name: client client_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.client
    ADD CONSTRAINT client_pkey PRIMARY KEY (id);


--
-- TOC entry 4728 (class 2606 OID 27502)
-- Name: composition_of_dish composition_of_dish_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.composition_of_dish
    ADD CONSTRAINT composition_of_dish_pkey PRIMARY KEY (id);


--
-- TOC entry 4709 (class 2606 OID 27438)
-- Name: dish dish_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.dish
    ADD CONSTRAINT dish_pkey PRIMARY KEY (id);


--
-- TOC entry 4719 (class 2606 OID 27456)
-- Name: order order_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."order"
    ADD CONSTRAINT order_pkey PRIMARY KEY (id);


--
-- TOC entry 4723 (class 2606 OID 27470)
-- Name: product product_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.product
    ADD CONSTRAINT product_pkey PRIMARY KEY (id);


--
-- TOC entry 4699 (class 2606 OID 27411)
-- Name: type_of_dish type_of_dish_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.type_of_dish
    ADD CONSTRAINT type_of_dish_pkey PRIMARY KEY (id);


--
-- TOC entry 4703 (class 2606 OID 27420)
-- Name: type_of_product type_of_product_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.type_of_product
    ADD CONSTRAINT type_of_product_pkey PRIMARY KEY (id);


--
-- TOC entry 4707 (class 2606 OID 27429)
-- Name: unit_of_measurement unit_of_measurement_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.unit_of_measurement
    ADD CONSTRAINT unit_of_measurement_pkey PRIMARY KEY (id);


--
-- TOC entry 4726 (class 1259 OID 27495)
-- Name: ix_bill_id; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX ix_bill_id ON public.bill USING btree (id);


--
-- TOC entry 4691 (class 1259 OID 27400)
-- Name: ix_client_first_name; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX ix_client_first_name ON public.client USING btree (first_name);


--
-- TOC entry 4692 (class 1259 OID 27401)
-- Name: ix_client_id; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX ix_client_id ON public.client USING btree (id);


--
-- TOC entry 4693 (class 1259 OID 27402)
-- Name: ix_client_last_name; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX ix_client_last_name ON public.client USING btree (last_name);


--
-- TOC entry 4694 (class 1259 OID 27403)
-- Name: ix_client_patronymic; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX ix_client_patronymic ON public.client USING btree (patronymic);


--
-- TOC entry 4695 (class 1259 OID 27404)
-- Name: ix_client_phone_number; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX ix_client_phone_number ON public.client USING btree (phone_number);


--
-- TOC entry 4729 (class 1259 OID 27518)
-- Name: ix_composition_of_dish_id; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX ix_composition_of_dish_id ON public.composition_of_dish USING btree (id);


--
-- TOC entry 4730 (class 1259 OID 27519)
-- Name: ix_composition_of_dish_number_of_products; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX ix_composition_of_dish_number_of_products ON public.composition_of_dish USING btree (number_of_products);


--
-- TOC entry 4710 (class 1259 OID 27444)
-- Name: ix_dish_calories; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX ix_dish_calories ON public.dish USING btree (calories);


--
-- TOC entry 4711 (class 1259 OID 27445)
-- Name: ix_dish_cooking_time; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX ix_dish_cooking_time ON public.dish USING btree (cooking_time);


--
-- TOC entry 4712 (class 1259 OID 27446)
-- Name: ix_dish_cost; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX ix_dish_cost ON public.dish USING btree (cost);


--
-- TOC entry 4713 (class 1259 OID 27447)
-- Name: ix_dish_id; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX ix_dish_id ON public.dish USING btree (id);


--
-- TOC entry 4714 (class 1259 OID 27448)
-- Name: ix_dish_name; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX ix_dish_name ON public.dish USING btree (name);


--
-- TOC entry 4715 (class 1259 OID 27449)
-- Name: ix_dish_weight; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX ix_dish_weight ON public.dish USING btree (weight);


--
-- TOC entry 4716 (class 1259 OID 27462)
-- Name: ix_order_date; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX ix_order_date ON public."order" USING btree (date);


--
-- TOC entry 4717 (class 1259 OID 27463)
-- Name: ix_order_id; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX ix_order_id ON public."order" USING btree (id);


--
-- TOC entry 4720 (class 1259 OID 27476)
-- Name: ix_product_id; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX ix_product_id ON public.product USING btree (id);


--
-- TOC entry 4721 (class 1259 OID 27477)
-- Name: ix_product_name; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX ix_product_name ON public.product USING btree (name);


--
-- TOC entry 4696 (class 1259 OID 27412)
-- Name: ix_type_of_dish_id; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX ix_type_of_dish_id ON public.type_of_dish USING btree (id);


--
-- TOC entry 4697 (class 1259 OID 27413)
-- Name: ix_type_of_dish_name; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX ix_type_of_dish_name ON public.type_of_dish USING btree (name);


--
-- TOC entry 4700 (class 1259 OID 27421)
-- Name: ix_type_of_product_id; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX ix_type_of_product_id ON public.type_of_product USING btree (id);


--
-- TOC entry 4701 (class 1259 OID 27422)
-- Name: ix_type_of_product_name; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX ix_type_of_product_name ON public.type_of_product USING btree (name);


--
-- TOC entry 4704 (class 1259 OID 27430)
-- Name: ix_unit_of_measurement_id; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX ix_unit_of_measurement_id ON public.unit_of_measurement USING btree (id);


--
-- TOC entry 4705 (class 1259 OID 27431)
-- Name: ix_unit_of_measurement_name; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX ix_unit_of_measurement_name ON public.unit_of_measurement USING btree (name);


--
-- TOC entry 4734 (class 2606 OID 27485)
-- Name: bill bill_dish_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.bill
    ADD CONSTRAINT bill_dish_id_fkey FOREIGN KEY (dish_id) REFERENCES public.dish(id);


--
-- TOC entry 4735 (class 2606 OID 27490)
-- Name: bill bill_order_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.bill
    ADD CONSTRAINT bill_order_id_fkey FOREIGN KEY (order_id) REFERENCES public."order"(id) ON DELETE CASCADE;


--
-- TOC entry 4736 (class 2606 OID 27503)
-- Name: composition_of_dish composition_of_dish_dish_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.composition_of_dish
    ADD CONSTRAINT composition_of_dish_dish_id_fkey FOREIGN KEY (dish_id) REFERENCES public.dish(id);


--
-- TOC entry 4737 (class 2606 OID 27508)
-- Name: composition_of_dish composition_of_dish_product_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.composition_of_dish
    ADD CONSTRAINT composition_of_dish_product_id_fkey FOREIGN KEY (product_id) REFERENCES public.product(id);


--
-- TOC entry 4738 (class 2606 OID 27513)
-- Name: composition_of_dish composition_of_dish_unit_of_measurement_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.composition_of_dish
    ADD CONSTRAINT composition_of_dish_unit_of_measurement_id_fkey FOREIGN KEY (unit_of_measurement_id) REFERENCES public.unit_of_measurement(id);


--
-- TOC entry 4731 (class 2606 OID 27439)
-- Name: dish dish_type_of_dish_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.dish
    ADD CONSTRAINT dish_type_of_dish_id_fkey FOREIGN KEY (type_of_dish_id) REFERENCES public.type_of_dish(id);


--
-- TOC entry 4732 (class 2606 OID 27457)
-- Name: order order_client_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."order"
    ADD CONSTRAINT order_client_id_fkey FOREIGN KEY (client_id) REFERENCES public.client(id);


--
-- TOC entry 4733 (class 2606 OID 27471)
-- Name: product product_type_of_product_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.product
    ADD CONSTRAINT product_type_of_product_id_fkey FOREIGN KEY (type_of_product_id) REFERENCES public.type_of_product(id);


-- Completed on 2024-05-12 01:29:48

--
-- PostgreSQL database dump complete
--

