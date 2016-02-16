
A simple CRUD application for managing a shopping list.

## Supported endpoints

1. GET /items
2. POST /items
3. DELETE /items/:id
4. PUT /items/:id

## Making sample requests

Deleting an item:

```
curl -H "Content-Type: application/json" -X DELETE http://localhost:8080/items/2
```

Updating an item:

```
curl -H "Content-Type: application/json" -d '{"name": "chocolate", "id": 2}' -X PUT http://localhost:8080/items/2
```