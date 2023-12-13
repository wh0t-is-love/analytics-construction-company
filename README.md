# Analytics of construction company

There is an artificially created case based on the analytics of a construction company.

## How to download?

Do:
```
git clone git@github.com:wh0t-is-love/analytics-construction-company.git
cd analytics-construction-company
poetry install
```
or
```
git clone https://github.com/wh0t-is-love/analytics-construction-company.git
cd analytics-construction-company
poetry install
```

## How to use?

To initialize project (for example^ by changing csv files in [csv](./csv/) directory) you need to run:

```
poetry run python db_creator.py
```

To run project you need to run:

```
poetry run main.py [OPTIONS]
```
Options list (equivalent to run `poetry run main.py -h`):
```
Options:
    -h or --help or h - manual
    object_profit - profit from objects
    number_of_tools (optional: object name) - necessary tools for construction
    richest_customer (optional: int or none) - customers who pay more than other (top n)
    technic_life - how much time to changing technic
    unsold_apartments - unsolved apartments info
    sold_apartments - sold apartments info
    construction_stage (optional: object name) - construction stage
    select (name of table) - select all info from this table
    
    if second flag is csv -> output will be saved in file output.csv
```

## How to save request in csv file?

There is two modes: printind and if option `csv` is on the second place, than request info will be saved in `output.csv` file.

For, example:

```
poetry run main.py csv object_profit
```