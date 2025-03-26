# ECSE3038_lab2
Summary of Expected Behavior
POST /person
Description: This endpoint accepts a POST request to add a new person to the data list.
Request Body: It expects a JSON object with the following structure:
Validation: The request body must contain values for all three fields: name, occupation, and address. If any field is missing or empty, the server will return an error message with the status "invalid request".
Response: If the request is valid, the server responds with a success status and the person object that was added to the data list:


GET /person
Description: This endpoint retrieves the list of all people added through the POST /person endpoint.
Response: The server responds with a list of all people, each containing the name, occupation, and address:

Reason for Writing This Code
This code was written as part of an assignment for the ECSE3038 course at the University of the West Indies. The purpose is to practice building POST and GET request handlers with FastAPI, with a focus on handling data in JSON format and validating incoming requests. This assignment helps in understanding how to work with FastAPI to create simple API endpoints that perform CRUD operations.

