# Spellbook Ingredients

This repo contains a small application that fetches all tables used as a source in [Spellbook](https://github.com/duneanalytics/spellbook), and uploads it to Dune using the [Dune API](https://dune.com/docs/api/) so the data can be queried directly on [Dune](dune.com).

## Pre-requisites

- You should have a Dune API key. See how to get one [here](https://dune.com/docs/api/)
- You should have [Poetry](https://python-poetry.org/docs/master/) installed
- [Spellbook](https://github.com/duneanalytics/spellbook) repo cloned locally
- Initial dbt setup in local Spellbook repo according to instructions in [README](https://github.com/duneanalytics/spellbook/blob/main/README.md)

## Instructions

Example of usage, from the root of this repo:

```console
~/Dune/spellbook-ingredients 
➜ cd spellbook_ingredients 

Dune/spellbook-ingredients/spellbook_ingredients 
➜ poetry shell
Spawning shell within /Users/antoniomendes/Library/Caches/pypoetry/virtualenvs/spellbook-ingredients-a4ovDk4L-py3.11

Dune/spellbook-ingredients/spellbook_ingredients 
➜ emulate bash -c '. /Users/antoniomendes/Library/Caches/pypoetry/virtualenvs/spellbook-ingredients-a4ovDk4L-py3.11/bin/activate'

Dune/spellbook-ingredients/spellbook_ingredients via spellbook-ingredients-a4ovDk4L-py3.11 
➜ python3 main.py $MY_DUNE_API_KEY ~/Dune/spellbook/target/manifest.json                      
Success writing CSV to Dune.com!
```

#### Useful link:

- Dune write API guide by [0xBoxer](https://github.com/0xBoxer)
- Data generated by this repo on Dune -> https://dune.com/queries/2461525