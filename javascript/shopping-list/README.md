
A simple CRUD application for managing a shopping list.

== Making sample requests ==

Deleting an item:

curl -H "Content-Type: application/json" -X DELETE http://localhost:8080/items/:id

Updating an item:

curl -H "Content-Type: application/json" -d '{"name": "chocolate", "id": 2}' -X PUT http://localhost:8080/items/:id