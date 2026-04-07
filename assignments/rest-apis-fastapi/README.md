# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a functional REST API using the FastAPI framework in Python, learning how to define routes, handle HTTP methods, validate request data, and return structured JSON responses.

## 📝 Tasks

### 🛠️	Set Up a FastAPI Application

#### Description
Create a FastAPI application with a basic project structure. Define a root endpoint that returns a welcome message and run the server using Uvicorn.

#### Requirements
Completed program should:

- Import `FastAPI` and create an `app` instance
- Define a `GET /` route that returns a JSON welcome message (e.g., `{"message": "Welcome to the API"}`)
- Be runnable with `uvicorn` on a local port (e.g., port 8000)


### 🛠️	Create a CRUD Endpoint for a Resource

#### Description
Build a simple in-memory data store and implement full CRUD (Create, Read, Update, Delete) operations for an `Item` resource using FastAPI path and body parameters.

#### Requirements
Completed program should:

- Define a Pydantic model `Item` with at least `id` (int), `name` (str), and `description` (str) fields
- Implement `GET /items` to return all items
- Implement `GET /items/{item_id}` to return a single item by ID, returning a 404 error if not found
- Implement `POST /items` to create a new item from the request body
- Implement `PUT /items/{item_id}` to update an existing item, returning a 404 error if not found
- Implement `DELETE /items/{item_id}` to remove an item, returning a 404 error if not found

Example response for `GET /items/1`:
```json
{
  "id": 1,
  "name": "Pencil",
  "description": "A standard #2 pencil"
}
```


### 🛠️	Add Query Parameters and Input Validation

#### Description
Extend the `/items` endpoint to support filtering and pagination via query parameters, and add input validation constraints to the `Item` model using Pydantic.

#### Requirements
Completed program should:

- Add a `search` query parameter to `GET /items` that filters items by name (case-insensitive)
- Add `skip` (default 0) and `limit` (default 10) query parameters to `GET /items` for pagination
- Add Pydantic field constraints: `name` must be between 1 and 50 characters, `description` must be 200 characters or fewer
- Return a meaningful HTTP 422 validation error automatically when invalid data is submitted

Example request: `GET /items?search=pencil&skip=0&limit=5`
