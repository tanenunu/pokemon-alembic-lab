# Intro

This is a project intended for absolute beginners to practice learning Alembic, a command-line database migration tool. It provides a self contained environment to practice migrations on a sqlite database using mocked pokemon-themed data.

The projects initial state represents a recently initialised Alembic Python app, with one migration/revision already performed to create the `trainers` table.

There are a number of [missions to complete](#practice-tasks), walking you through the basics. It is recommended that you refer to the excellent [Alembic tutorial documentation](https://alembic.sqlalchemy.org/en/latest/tutorial.html) while completing these missions, any question you have will likely be answered there.

## Safe Learning

The missions are merely a guide if you're lost, feel free to experiment!

- This project uses SQLite.

- The database file can safely be deleted.

Feel comfortable:

- Breaking migrations
- Rolling back migrations
- Recreating the database
- Editing migration files manually

## Getting started

This project uses `uv` for python package and environment management. After cloning this repo for the first time, follow these steps:

In terminal:

```Shell
uv sync
```

then:

```Shell
source .venv/Scripts/activate
```

## AI Assistant Guidance

This repository includes an `AGENTS.md` file intended for AI coding assistants and agents.

The guidance encourages a teaching-first approach and focuses on helping learners understand Alembic rather than simply providing commands.

Ai can be an excellent tutor and guide when prompted correctly. Always treat its outputs with skepticism and refer to the _Alembic documentation_ to verify answers (see [Resources](#resources) below).

## Important Files to consider

#### `models.py`

This is where you define the shape of the tables. This file could be anything, or split across multiple files, Alembic doesn't care about file names. What's important is defining the tables, which will be imported to...

#### `alembic/env.py`

This is where your table objects are imported into (in this case, they are imported from `models.py`). This is how you tell Alembic what to pay attention to.

#### `alembic/versions/`

This is where the directory where alembic's auto generated revision scripts will go. When you run `alembic revision --autogenerate -m "message"` a script will be generated here.

#### `alembic.ini`

- This is alembic's "config" file.
- Importantly, the line `sqlalchemy.url = sqlite:///pokemon.db`, is what connects alembic to the sqlite database used in this project.

#### `pokemon.db`

This is the sqlLite database for the project.

# Useful Commands

These will get you started:

```Shell
alembic revision --autogenerate -m "create trainers table"

alembic upgrade head

alembic downgrade -1
```

Full command list: [Commands — Alembic 1.20.0 documentation](https://alembic.sqlalchemy.org/en/latest/api/commands.html)

# Practice tasks

## Mission 1

Add:

```Python
age = Column(Integer)
```

Then:
_Generate migration._
_Review migration._
_Apply migration._

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

```Python
Column(
    "id",
    ForeignKey("other.id"),
    primary_key=True
)
```

Learn how Alembic handles constraints.

### Hint

If getting errors:
[Batch loading - Alembic 1.20.0 documentation](https://alembic.sqlalchemy.org/en/latest/batch.html)

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
