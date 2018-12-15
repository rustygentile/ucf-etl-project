# NCAA ETL Project

# Authors:
* [Rusty Gentile](https://github.com/rustygentile)
* [Minal Jajoo](https://github.com/minaljajoo)
* [Scott Nubar](https://github.com/Rasbeartin)
* [Axander Wilson](https://github.com/AxanderW)

# Introduction

The purpose of this project was to model and demonstrate a successful ETL process. To achieve this, data from the 2017 and 2018 men’s basketball tournaments was extracted from the NCAA.com website.

# Website

To view the website, clone repository, navigate to ```./website``` and run:
```
python app.py
```

# Database

To create database navigate to Database/Create_database folder and first run 'create_ncaa2018_elite_eight_db.sql' file in mySQL. Next load labeled 'load'. 

###  Note: Order of loading matters. Load in the order below:
* load_regionTable.csv 
* load_positonsTable.csv
* load_tournament_roundTable.csv
* load_teamTable.csv
* load_playersTable.csv
* load_gameTable.csv
* load_team_statsTable.csv
* load_player_statsTable.csv

# Report

See: [Technical Report](./doc/Technical_Report_FINAL.docx)

