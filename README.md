# backend

This project was generated via [manage-fastapi](https://ycd.github.io/manage-fastapi/)! :tada:

## License

This project is licensed under the terms of the MIT license.


- `Link 1`: https://www.azepug.az/posts/fastapi/ecommerce-fastapi-nuxtjs/ecommerce-setup-fastapi.html

- `Link 2` : https://python-gino.org/docs/en/master/tutorials/fastapi.html

- `Link 3` : https://python-gino.org/docs/en/master/tutorials/fastapi.html

- `Link 4` : https://www.jeffastor.com/blog/designing-a-robust-user-model-in-a-fastapi-app

- `Link 5` : https://www.jeffastor.com/blog/pairing-a-postgresql-db-with-your-dockerized-fastapi-app

- `Link 6` : https://www.jeffastor.com/blog/authenticating-users-in-fastapi-with-jwt-tokens

- `Link 7` : https://github.com/ShahriyarR/azepug

- `Link 8` : https://www.jeffastor.com/app/blog/

- `Link 9` : 



- `poetry shell`
- `poetry add <package-name>`
- 


### Running the python files

- https://stackoverflow.com/questions/43728431/relative-imports-modulenotfounderror-no-module-named-x
- export PYTHONPATH="${PYTHONPATH}:/path/to/your/project/"
- cd into the file_directory and run
- python3 -m "file_to_run" without the .py




### Alembic Migration files

- `poetry run alembic revision --autogenerate -m 'update users table'`

- `poetry run alembic upgrade head`

- 


- Generate a secret key by using this commnand ; `openssl rand -hex 32`






### Connect to Postgresql (psql)

- postgres=# create user ecommerce with encrypted password '12345';
- `CREATE ROLE`

- postgres=# create database ecommerce;
- `CREATE DATABASE`

- postgres=# grant all privileges on database ecommerce to ecommerce;
- `GRANT`

- connect to the database
- `\c ecommerce

- List tables and schemas in the database
- `\dt+`

- `\l` is the equivalent of show databases. and `\dt` ≃ show tables

### 2. Show tables

Now in Psql you could run commands such as:

- `\?` list all the commands
- `\l` list databases
- `\conninfo` display information about current connection
- `\c [DBNAME]` connect to new database, e.g., \c template1
- `\dt` list tables of the public schema
- `\dt <schema-name>.*` list tables of certain schema, e.g., \dt public.*
- `\dt *.*` list tables of all schemas
Then you can run SQL statements, e.g., SELECT * FROM my_table;(Note: a statement must be terminated with semicolon ;)
- `\q` quit psql


















## Out of Context

#### Over-Engineering
- `Overengineering`, is the act of designing a product or providing a solution to a problem in an elaborate or complicated manner, where a simpler solution can be demonstrated to exist with the same efficiency and effectiveness as that of the original design.

#### DRY (Do Repeat Yourself) Principle
- `"Don't repeat yourself" (DRY)` is a principle of software development aimed at reducing repetition of software patterns, replacing it with abstractions or using data normalization to avoid redundancy.

- The DRY principle is stated as "Every piece of knowledge must have a single, unambiguous, authoritative representation within a system". 

- When the DRY principle is applied successfully, a modification of any single element of a system does not require a change in other logically unrelated elements.

- Additionally, elements that are logically related all change predictably and uniformly, and are thus kept in sync. 

- Besides using `methods` and `subroutines` in their code, Thomas and Hunt rely on `code generators`, `automatic build systems`, and `scripting languages` to observe the DRY principle across layers.


#### AHA ("Avoid Hasty Abstractions") Principle
- Another approach to abstractions is the AHA principle. AHA stands for "Avoid Hasty Abstractions", described by Kent C. Dodds as optimizing for change first, and avoiding premature optimization. and was influenced by Sandi Metz's "prefer duplication over the wrong abstraction".

- `AHA` is rooted in the understanding that the deeper the investment we've made into abstracting a piece of software, the more we perceive that the cost of that investment can never be recovered (sunk cost fallacy). Thus, engineers tend to continue to iterate on the same abstraction each time the requirement changes. AHA programming assumes that both WET and DRY solutions inevitably create software that is rigid and difficult to maintain. Instead of starting with an abstraction, or abstracting at a specific number of duplications, software can be more flexible and robust if abstraction is done when it is needed, or, when the duplication itself has become the barrier and it is known how the abstraction needs to function.


### ORM (Object-Relational Mapping)

- `Object-Relational Mapping (ORM)` is a technique that lets you query and manipulate data from a database using an object-oriented paradigm. 
- link : https://stackoverflow.com/questions/1279613/what-is-an-orm-how-does-it-work-and-how-should-i-use-one


