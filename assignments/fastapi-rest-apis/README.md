# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a complete RESTful API using the FastAPI framework. Learn how to create endpoints, handle different HTTP methods, work with request/response models, and implement data validation and error handling.

## 📝 Tasks

### 🛠️	Create Basic API Endpoints

#### Description
Set up a FastAPI application with basic CRUD (Create, Read, Update, Delete) endpoints for managing a simple resource like books, users, or tasks. Implement proper HTTP methods and status codes.

#### Requirements
Completed program should:

- Install and configure FastAPI with all necessary dependencies
- Create a main application file with FastAPI instance
- Implement GET endpoint to retrieve all items
- Implement GET endpoint to retrieve a single item by ID
- Implement POST endpoint to create new items
- Implement PUT endpoint to update existing items
- Implement DELETE endpoint to remove items
- Return appropriate HTTP status codes for each operation


### 🛠️	Add Data Validation and Error Handling

#### Description
Enhance your API with Pydantic models for request/response validation and implement proper error handling to make your API robust and user-friendly.

#### Requirements
Completed program should:

- Create Pydantic models for request and response data
- Validate incoming data automatically using type hints
- Handle and return meaningful error messages for invalid requests
- Implement custom exception handlers for common errors
- Return structured error responses with proper HTTP status codes
- Add API documentation using FastAPI's automatic documentation features
- Test all endpoints using the built-in interactive documentation