# Getting started
This project uses `uv` for python package and environment management. After cloning this repo for the first time, follow these steps:
In terminal:
```Shell
uv sync
source .venv/Scripts/activate
```
## AI Assistant Guidance

This repository includes an `AGENTS.md` file intended for AI coding assistants and agents.

The guidance encourages a teaching-first approach and focuses on helping learners understand Alembic rather than simply providing commands.

## Basic setup
This is a practice app for learning alembic, a command-line database migration tool.

### Important Files to consider 
#### `models.py` 
This is where you define the shape of the tables. This file could be anything, or split across multiple files, Alembic doesn't care about file names. What's important is defining the tables, which will be imported to...
#### `alembic/env.py` 
This is where your table objects are imported into (in this case, they are imported from `models.py`). This is how you tell Alembic what to pay attention to.
#### `alembic/versions/`
This is where the directory where alembic's auto generated revision scripts will go. When you run `alembic revision --autogenerate -m "message"` a script will be generated here.
#### `alembic.ini`
- This is alembic's "config" file. 
- Importantly, the line `sqlalchemy.url = sqlite:///pokemon.db`, is what connects alembic to the sqlite database used in this project.

### Safe Learning Practices
- This project uses SQLite.

- The database file can safely be deleted.

Feel comfortable:
- Breaking migrations
- Rolling back migrations
- Recreating the database
- Editing migration files manually


# Useful Commands
```Shell
alembic revision --autogenerate -m "create trainers table"

alembic upgrade head

alembic downgrade -1
```

# Practice tasks
## Mission 1
Add:
```Python
age = Column(Integer)
```
Then:
*Generate migration.*
*Review migration.*
*Apply migration.*

## Mission 2
Rollback:
```Shell
alembic downgrade -1
```

Then:
```Shell
alembic upgrade head
```

## Mission 3
Create `Pokemon` table:
```Python
class Pokemon(Base):

    __tablename__ = "pokemon"

    id = Column(Integer, primary_key=True)

    name = Column(String(50))

    type = Column(String(50))
```
Generate and apply migration

## Mission 4
Add a relationship:
```
trainer_id
```
as a foreign key.
Learn how Alembic handles constraints.

## Mission 5
Insert samples data.
Create:
```
Ash
Pikachu
Charmander
```
Then create a migration that updates data.

## Mission 6
Rename a column.
Observe how Alembic behaves.
This teaches one of the most common migration pitfalls.

## Mission 7
Delete a column.
Watch what happens to the data.
This is where you'll start understanding why DBAs get nervous around migrations.

# Resources
[Tutorial — Alembic 1.20.0 documentation](https://alembic.sqlalchemy.org/en/latest/tutorial.html)