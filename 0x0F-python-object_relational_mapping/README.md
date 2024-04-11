# Python - Object-relational mapping

This repo contains my tasks on the object-relational mapping project

## Object-relational Mappers (ORMs)
<p>An object-relational mapper (ORM) is a code library that automates the transfer of data stored in relational database tables into objects that are more commonly used in application code.</p>

![new](https://www.fullstackpython.com/img/visuals/orms-bridge.png)

<h2>Why are ORMs useful?</h2>
<p>
ORMs provide a high-level abstraction upon a relational database that allows a developer to write Python code instead of SQL to create, read, update and delete data and schemas in their database. Developers can use the programming language they are comfortable with to work with a database instead of writing SQL statements or stored procedures.
</p>

<p>
For example, without an ORM a developer would write the following SQL statement to retrieve every row in the USERS table where the zip_code column is 94107:
</p>
```
SELECT * FROM USERS WHERE zip_code=94107;
```
<p>
The equivalent Django ORM query would instead look like the following Python code:
</p>
```
# obtain everyone in the 94107 zip code and assign to users variable
users = Users.objects.filter(zip_code=94107)
```
