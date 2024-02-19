# Patient Management API Endpoints

## List Patients

- **URL:** http://localhost:8000/api/patient-management/patients/
- **Method:** GET
- **Headers:** 
    - **Key:** Authorization
    - **Value:** Bearer <access_token> (Replace <access_token> with the actual JWT access token)
- **Description:** Retrieve a list of all patients.

## Create Patient

- **URL:** http://localhost:8000/api/patient-management/patients/
- **Method:** POST
- **Headers:** 
    - **Key:** Authorization
    - **Value:** Bearer <access_token> (Replace <access_token> with the actual JWT access token)
    - **Key:** Content-Type
    - **Value:** application/json
- **Body:** JSON with the patient details.

    ```json
    {
        "name": "Jane Doe",
        "date_of_birth": "1991-02-02",
        "gender": "F",
        "address": "124 Main St",
        "contact_number": "0987654321",
        "email": "jane.doe@example.com",
        "medical_history": "None",
        "allergies": "Peanuts"
    }
    ```
- **Description:** Add a new patient record.

## Update Patient

- **URL:** http://localhost:8000/api/patient-management/patients/<id>/
- **Method:** PUT
- **Headers:** 
    - **Key:** Authorization
    - **Value:** Bearer <access_token> (Replace <access_token> with the actual JWT access token)
    - **Key:** Content-Type
    - **Value:** application/json
- **Body:** JSON with the updated patient details.

    ```json
    {
        "name": "Jane Doe Updated",
        "date_of_birth": "1991-02-02",
        "gender": "F",
        "address": "124 Main St Updated",
        "contact_number": "0987654322",
        "email": "jane.updated@example.com",
        "medical_history": "Updated history",
        "allergies": "Updated allergies"
    }
    ```
- **Description:** Update an existing patient record. Replace `<id>` with the actual ID of the patient.

## Delete Patient

- **URL:** http://localhost:8000/api/patient-management/patients/<id>/
- **Method:** DELETE
- **Headers:** 
    - **Key:** Authorization
    - **Value:** Bearer <access_token> (Replace <access_token> with the actual JWT access token)
- **Description:** Remove a patient record. Replace `<id>` with the actual ID of the patient.

## JWT Token Refresh

- **URL:** http://localhost:8000/auth/jwt/refresh/
- **Method:** POST
- **Body:** JSON with the refresh token.

    ```json
    {
        "refresh": "<refresh_token>"
    }
    ```
- **Description:** Refresh the JWT access token by providing the refresh token obtained during login.

## JWT Token Verify

- **URL:** http://localhost:8000/auth/jwt/verify/
- **Method:** POST
- **Body:** JSON with the access token.

    ```json
    {
        "token": "<access_token>"
    }
    ```
- **Description:** Verify the validity of the JWT access token by providing it in the request body.
