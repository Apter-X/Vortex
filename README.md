# Vortex
Vortex is a dynamic scraper using strategies.
## Instructions
- Go to `app/configs/database.py` ensure you put the right configurations.
- To add a new strategy go to `app/strategies/` 
  and create a new file `.py` with the name of what you target,
  than past the following schema:
  ```python
  NAME = ""
  URL = ""
  QUERY_PARAMS = None
  REQUEST_HEADERS = {
      "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 "
                    "Safari/537.36 "
  }
  SHARP = {
      "tag": "",
      "element": {}
  }
  STRATEGY = {
  }
  ```
  
- Don't forget to fill the required information of the strategy.

## How to use
1. Import a strategy
2. Instantiate the vortex class using the strategy
3. Start scraping
4. Extract data
5. Store data into database using `postgresql`

## Example
```python
from app.modules.vortex import Vortex
from strategies import my_strategy
from configs import database
from modules.database import Database


vortex = Vortex(my_strategy)
vortex.get_results(1, 5) # (from, to)
vortex.extract_data()
print(vortex.records)

db = Database(database.DATABASE)
db.store_multiple_dict(vortex.records, my_strategy.NAME)
fetch_all = db.fetch(""" SELECT * FROM companies """)
db.disconnect()
print(fetch_all)
```

Trigger postgesql for distributing data.
```sql
DECLARE
	new_tel_1 text;
	new_tel_2 text;
	new_id uuid;
	t_row varchar(255);
	activities text;
	services text;
	id_activity uuid;
	id_service uuid;

BEGIN
	new_tel_1 := jsonb(new.dict -> 'tel1');
	new_tel_2 := jsonb(new.dict -> 'tel2');

	INSERT INTO businesses
	(business_id, business_name, about, tel1, tel2, website, address)
	VALUES (	
		new.id,
		jsonb(new.dict -> 'name'),
		jsonb(new.dict -> 'about'),
		substring(new_tel_1 from '...............$'),
		substring(new_tel_2 from '...............$'),
		jsonb(new.dict -> 'website'),
		jsonb(new.dict -> 'address')
	);

	INSERT INTO legal
	(legal_id, business_id, legal_form, birthday, capital, effective, type)
	VALUES (
		uuid_generate_v4 (),
		new.id,
		jsonb(new.dict -> 'legal_form'),
		jsonb(new.dict -> 'year'),
		jsonb(new.dict -> 'capital'),
		jsonb(new.dict -> 'effective'),
		jsonb(new.dict -> 'type')
	);

	activities := jsonb(new.dict -> 'activities');
	FOR t_row IN SELECT regexp_split_to_table(substring(activities FROM 3), '-\s+')
	LOOP
		t_row := initcap(TRIM(BOTH ' "' FROM t_row));
		SELECT activity_id FROM activities INTO id_activity WHERE activity_name = t_row;
		IF not found THEN
			new_id := uuid_generate_v4 ();
			INSERT INTO activities (activity_id, activity_name) VALUES (new_id, t_row);
			INSERT INTO businesses_activities (activity_id, business_id) VALUES (new_id, new.id);
		ELSE
			INSERT INTO businesses_activities (activity_id, business_id) VALUES (id_activity, new.id);
		END IF;
	END LOOP;

	services := jsonb(new.dict -> 'services');
	FOR t_row IN SELECT * FROM regexp_split_to_table(substring(services FROM 3), '-\s+')
	LOOP
		t_row := initcap(TRIM(BOTH ' "' FROM t_row));
		SELECT service_id FROM services INTO id_service WHERE service_name = t_row;
		IF not found THEN
			new_id := uuid_generate_v4 ();
			INSERT INTO services (service_id, service_name) VALUES (new_id, initcap(TRIM(BOTH ' ' FROM t_row)));
			INSERT INTO businesses_services (service_id, business_id) VALUES (new_id, new.id);
		ELSE
			INSERT INTO businesses_services (service_id, business_id) VALUES (id_service, new.id);
		END IF;
	END LOOP;

RETURN NEW;
END;
```
