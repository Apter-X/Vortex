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