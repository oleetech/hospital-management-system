# Nurse Management API Endpoints

## List Nurses

- **URL:** http://localhost:8000/api/doctor-management/nurses/
- **Method:** GET
- **Headers:** 
    - **Key:** Authorization
    - **Value:** Bearer <access_token> (Replace <access_token> with the actual JWT access token)
- **Description:** Retrieve a list of all nurses.

## Create Nurse

- **URL:** http://localhost:8000/api/doctor-management/nurses/
- **Method:** POST
- **Headers:** 
    - **Key:** Authorization
    - **Value:** Bearer <access_token> (Replace <access_token> with the actual JWT access token)
- **Body:** JSON

    ```json
    {
        "user": "user_id",
        "name": "Jane Doe",
        "gender": "F",
        "contact_number": "0987654321"
    }
    ```

- **Description:** Add a new nurse record.

## Update Nurse

- **URL:** http://localhost:8000/api/doctor-management/nurses/<id>/
- **Method:** PUT/PATCH
- **Headers:** 
    - **Key:** Authorization
    - **Value:** Bearer <access_token> (Replace <access_token> with the actual JWT access token)
- **Body:** JSON

    ```json
    {
        "name": "Jane Doe Updated",
        "contact_number": "1234567890"
    }
    ```

- **Description:** Update an existing nurse record. Replace `<id>` with the actual ID of the nurse.

## Delete Nurse

- **URL:** http://localhost:8000/api/doctor-management/nurses/<id>/
- **Method:** DELETE
- **Headers:** 
    - **Key:** Authorization
    - **Value:** Bearer <access_token> (Replace <access_token> with the actual JWT access token)
- **Description:** Remove a nurse record. Replace `<id>` with the actual ID of the nurse.
