#parseFrenchGazPrices
====================

A simple python file to retrieve gazoline prices from the web and
writing it locally in a postgre database

##Usage

python3 launchParsing.py --conf_file /path/to/conf_file.yaml

--conf_file isn't mandatory, if you're not providing it, the script will try to use config.yaml located in the directory

##Dependencies

To use this script you'll need:
- python3
- psycopg2
- pyyaml
- BeautifulSoup4

##Requirements

You'll also need to install PostgreSQL, and create two tables:
- CREATE TABLE regional_id(id serial PRIMARY KEY, regional_name TEXT UNIQUE);
- CREATE TABLE gazprices(id serial PRIMARY KEY, gaz_name TEXT, gaz_price FLOAT, regional_id integer REFERENCES regional_id (id));
