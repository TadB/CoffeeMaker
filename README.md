# Coffee Maker simulation

## Description
This is a simple simulation of coffee maker. It simulates preparing perfect coffee e.g. americano, espresso, latte etc. 
User after push appropriate button may see usage of the necessary component of coffee (milk, water, etc.) Current amount of components is described for the user. 
There is also service button - change layout to service mode, when the user can fill up a selected tank. It can be full or partially refilled.

## Decisions:
- SQLite as a SQL Database Engine. At this moment I considered to not to use database engine at all. I thought about storing that few variables in dictionary and a list of classes, but it's almost the same work to do, to prepare models for database or locally stored variables. 
- database file is added to.gitignore. The database can be easily restored from .json file in python shell or using init_db.py script.
- coffee item in Coffee table is multiple espresso. Usage of coffee beans is calculated: 1 espresso use 9g of coffee beans. Usage of water per espresso is 30ml. 
- make_coffe() function takes 1 argument in the string. Do not validate data type, it always be a string sending by buttons. The user doesn't have any other method to interact with function.