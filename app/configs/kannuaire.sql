-- *************** SqlDBM: PostgreSQL ****************;
-- ***************************************************;


-- ************************************** businesses

CREATE TABLE businesses
(
 business_id  uuid NOT NULL,
 name         varchar(50) NOT NULL,
 presentation text NOT NULL,
 about        text NOT NULL,
 CONSTRAINT PK_businesses PRIMARY KEY ( business_id )
);

-- ************************************** legal

CREATE TABLE legal
(
 legal_id    uuid NOT NULL,
 business_id uuid NOT NULL,
 legal_form  varchar(50) NOT NULL,
 year        date NOT NULL,
 capital     int NOT NULL,
 effective   varchar(50) NOT NULL,
 CONSTRAINT PK_legal PRIMARY KEY ( legal_id ),
 CONSTRAINT FK_41 FOREIGN KEY ( business_id ) REFERENCES businesses ( business_id )
);

CREATE INDEX fkIdx_42 ON legal
(
 business_id
);

-- ************************************** contacts

CREATE TABLE contacts
(
 contact_id  uuid NOT NULL,
 business_id uuid NOT NULL,
 name        varchar(50) NOT NULL,
 detail      varchar(255) NOT NULL,
 CONSTRAINT PK_contacts PRIMARY KEY ( contact_id ),
 CONSTRAINT FK_44 FOREIGN KEY ( business_id ) REFERENCES businesses ( business_id )
);

CREATE INDEX fkIdx_45 ON contacts
(
 business_id
);

-- ************************************** activities

CREATE TABLE activities
(
 activity_id uuid NOT NULL,
 name        varchar(50) NOT NULL,
 CONSTRAINT PK_activities PRIMARY KEY ( activity_id )
);

-- ************************************** services

CREATE TABLE services
(
 service_id uuid NOT NULL,
 name       varchar(50) NOT NULL,
 CONSTRAINT PK_services PRIMARY KEY ( service_id )
);

-- ************************************** cities

CREATE TABLE cities
(
 city_id uuid NOT NULL,
 name    varchar(50) NOT NULL,
 CONSTRAINT PK_cities PRIMARY KEY ( city_id )
);

-- ************************************** businesses_activities

CREATE TABLE businesses_activities
(
 activity_id uuid NOT NULL,
 business_id uuid NOT NULL,
 CONSTRAINT FK_35 FOREIGN KEY ( activity_id ) REFERENCES activities ( activity_id ),
 CONSTRAINT FK_38 FOREIGN KEY ( business_id ) REFERENCES businesses ( business_id )
);

CREATE INDEX fkIdx_36 ON businesses_activities
(
 activity_id
);

CREATE INDEX fkIdx_39 ON businesses_activities
(
 business_id
);

-- ************************************** businesses_services

CREATE TABLE businesses_services
(
 business_id uuid NOT NULL,
 service_id  uuid NOT NULL,
 CONSTRAINT FK_29 FOREIGN KEY ( business_id ) REFERENCES businesses ( business_id ),
 CONSTRAINT FK_32 FOREIGN KEY ( service_id ) REFERENCES services ( service_id )
);

CREATE INDEX fkIdx_30 ON businesses_services
(
 business_id
);

CREATE INDEX fkIdx_33 ON businesses_services
(
 service_id
);

-- ************************************** businesses_cities

CREATE TABLE businesses_cities
(
 city_id     uuid NOT NULL,
 business_id uuid NOT NULL,
 CONSTRAINT FK_11 FOREIGN KEY ( city_id ) REFERENCES Cities ( city_id ),
 CONSTRAINT FK_16 FOREIGN KEY ( business_id ) REFERENCES businesses ( business_id )
);

CREATE INDEX fkIdx_13 ON businesses_cities
(
 city_id
);

CREATE INDEX fkIdx_18 ON businesses_cities
(
 business_id
);
