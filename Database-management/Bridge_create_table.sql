-- Table: public.Bridges

-- DROP TABLE public."Bridges";

CREATE TABLE public."Bridges"
(
    "ID" integer NOT NULL,
    country text COLLATE pg_catalog."default",
    province text COLLATE pg_catalog."default",
    district text COLLATE pg_catalog."default",
    district_id integer,
    sector text COLLATE pg_catalog."default",
    sector_id integer,
    cell text COLLATE pg_catalog."default",
    cell_id integer,
    village text COLLATE pg_catalog."default",
    village_id integer,
    name text COLLATE pg_catalog."default",
    project_code integer,
    type text COLLATE pg_catalog."default",
    stage text COLLATE pg_catalog."default",
    sub_stage text COLLATE pg_catalog."default",
    individuals_directly_served integer,
    span integer,
    lat double precision,
    "long" double precision,
    community_served_1 text COLLATE pg_catalog."default",
    community_served_1_id integer,
    community_served_2 text COLLATE pg_catalog."default",
    community_served_2_id integer,
    community_served_3 text COLLATE pg_catalog."default",
    community_served_3_id integer,
    community_served_4 text COLLATE pg_catalog."default",
    community_served_4_id integer,
    community_served_5 text COLLATE pg_catalog."default",
    community_served_5_id integer,
    form text COLLATE pg_catalog."default",
    case_safe_id text COLLATE pg_catalog."default",
    opportunity_id text COLLATE pg_catalog."default",
    CONSTRAINT "Bridges_pkey" PRIMARY KEY ("ID")
)

TABLESPACE pg_default;

ALTER TABLE public."Bridges"
    OWNER to postgres;