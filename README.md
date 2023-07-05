# Inori Mirai CNC Scraper V.2 - By Lore<3

### A working Mirai CNC scraper written in python.

## ❓ How does it work?:
Scrapes Mirai CNC servers off URLHaus. Then checks each server for a running MYSQL server on port 3306. 
Once it finds a running server it attempts to login the MYSQL server using default credentials.
After a successful login, it dumps the all the databases, specifically the users table in each database found. (CNC Logins)

- Also kills Mana V4.1 based Mirai CNC sources.

## ⭐ Improvements compared to V.1:
```bash
• Removed config file (Now requires CLI args).
• Made a proper threading system (MORE CONFIGURABLE).
• Code base is improved.
• Removed redundant module files.
```

## 🖥️ Features:
```bash
• Dumps MYSQL databases (CNC login credentials).
• Kills Mana V4.1 based sources.
• Stores results into a json file (database.json).
```

## 🔌 How To Install:
```bash
1. git clone https://github.com/PyLore/Inori-Mirai-CNC-Scraper-V.2
2. cd <directory folder is in>
3. py main.py or python3 main.py -t <amount of threads> (optional -k)
```
