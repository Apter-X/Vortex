-- Scrap brut table --
create table scrap_brut
(
    id            bigserial not null,
    dict          jsonb,
    target        varchar,
    targeted_link text,
    scrap_date    date      default now(),
    date_time     timestamp default now()
);

create unique index scrap_brute_id_uindex
    on scrap_brut (id);

-- Vue full brut data --
create view full_data
            (br, md, yr, fl, fp, ts, km, pr, ph, pt, doors, origin, first_owner, city, scrap_date, date_time, target) as
SELECT DISTINCT ON ((c.dict ->> 'br'::text), (c.dict ->> 'md'::text), (c.dict ->> 'pt'::text), (c.dict ->> 'yr'::text), (c.dict ->> 'pr'::text))
    c.dict ->> 'br'::text           AS br,
     c.dict ->> 'md'::text           AS md,
     c.dict ->> 'yr'::text           AS yr,
     c.dict ->> 'fl'::text           AS fl,
     c.dict ->> 'fp'::text           AS fp,
     c.dict ->> 'transmission'::text AS ts,
     c.dict ->> 'km'::text           AS km,
     c.dict ->> 'pr'::text           AS pr,
     c.dict ->> 'ph'::text           AS ph,
     c.dict ->> 'pt'::text           AS pt,
     c.dict ->> 'doors'::text        AS doors,
     c.dict ->> 'origin'::text       AS origin,
     c.dict ->> 'first_owner'::text  AS first_owner,
     c.dict ->> 'city'::text         AS city,
     c.scrap_date,
     c.date_time,
     c.target::text                  AS target
FROM (SELECT scrap_brut.dict,
             scrap_brut.target,
             scrap_brut.scrap_date,
             scrap_brut.date_time
      FROM scrap_brut
      WHERE (scrap_brut.dict ->> 'br'::text) IS NOT NULL
        AND (scrap_brut.dict ->> 'md'::text) IS NOT NULL
        AND (scrap_brut.dict ->> 'pt'::text) IS NOT NULL
      ORDER BY scrap_brut.scrap_date DESC) c;

-- Extract brut data routine in between date --
create function extract_data_brut_avito(start_date text, end_date text)
    returns TABLE(br text, md text, yr text, fl text, fp text, ts text, km text, pr text, ph text, pt text, doors text, origin text, first_owner text, city text, scrap_date date, date_time timestamp without time zone, target text)
    language plpgsql
as
$$
BEGIN
    RETURN QUERY SELECT *
                 FROM full_data
                 WHERE (full_data.date_time, full_data.date_time) OVERLAPS (start_date::DATE, end_date::DATE);
END
$$;
