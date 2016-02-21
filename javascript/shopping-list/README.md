
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

## Cached FileServer

Also serves static assets of the `public` directory. Caches the gzipped results
so as not to read them from disk on every request. See the `streams` submodule
for the implementation and sample uses.