# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn to build scalable REST APIs using the FastAPI framework. You'll create endpoints for CRUD operations, work with request validation using Pydantic models, and understand HTTP status codes and best practices for API design.

## 📝 Tasks

### 🛠️ Create a Basic API with FastAPI

#### Description

Set up a FastAPI application with a simple in-memory data store. You'll define a Pydantic model for items and create basic GET and POST endpoints to list and create items.

#### Requirements

Completed program should:

- Initialize a FastAPI application with proper imports
- Define a Pydantic model `Item` with fields: `id`, `name`, `description`, and `price`
- Create a GET `/items/` endpoint that returns all items
- Create a POST `/items/` endpoint that accepts an `Item` and stores it in a list
- Store items in a Python list (no database required)

### 🛠️ Implement CRUD Operations

#### Description

Extend your API with endpoints to retrieve, update, and delete individual items. Practice handling path parameters and proper HTTP status codes.

#### Requirements

Completed program should:

- Create a GET `/items/{item_id}` endpoint that returns a specific item by ID
- Handle the case where an item doesn't exist (return HTTP 404)
- Create a PUT `/items/{item_id}` endpoint to update an existing item
- Create a DELETE `/items/{item_id}` endpoint to delete an item
- Return appropriate HTTP status codes (200, 201, 404)

### 🛠️ Add Request Validation and Error Handling

#### Description

Improve your API by adding validation constraints to the Pydantic model and custom error messages for invalid requests.

#### Requirements

Completed program should:

- Add field validators to `Item` (e.g., `price` must be positive, `name` must not be empty)
- Return descriptive HTTP 422 error responses for validation failures
- Add a custom error handler with a helpful message when an item is not found
- Test your API with invalid data to ensure validation works

### 🛠️ Document and Test Your API (Bonus)

#### Description

Use FastAPI's built-in documentation features and add docstrings to your endpoints. Verify your API works correctly using provided test examples or Postman.

#### Requirements

Completed program should:

- Add docstrings to all endpoint functions
- Access the interactive API documentation at `/docs` (Swagger UI)
- Test all endpoints with valid and invalid data
- Document expected request/response formats in docstrings
