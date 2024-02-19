# Visit API Endpoints

## List Visits

- **URL:** http://localhost:8000/api/appointment-management/visits/
- **Method:** GET
- **Headers:** 
    - **Key:** Authorization
    - **Value:** Bearer <access_token> (Replace <access_token> with the actual JWT access token)
- **Description:** Retrieve a list of all visits.

## Create Visit

- **URL:** http://localhost:8000/api/appointment-management/visits/
- **Method:** POST
- **Headers:** 
    - **Key:** Authorization
    - **Value:** Bearer <access_token> (Replace <access_token> with the actual JWT access token)
- **Body:** JSON

    ```json
    {
        "patient": "<patient_id>",
        "admission_date": "YYYY-MM-DD",
        "admission_time": "HH:MM",
        "discharge_date": "YYYY-MM-DD",
        "discharge_time": "HH:MM",
        "ward": "Ward name or number"
    }
    ```

- **Description:** Add a new visit record.

## Update Visit

- **URL:** http://localhost:8000/api/appointment-management/visits/<id>/
- **Method:** PUT/PATCH
- **Headers:** 
    - **Key:** Authorization
    - **Value:** Bearer <access_token> (Replace <access_token> with the actual JWT access token)
- **Body:** JSON

    ```json
    {
        "discharge_date": "YYYY-MM-DD",
        "discharge_time": "HH:MM",
        "ward": "Updated ward name or number"
    }
    ```

- **Description:** Update an existing visit record. Replace `<id>` with the actual ID of the visit.

## Delete Visit

- **URL:** http://localhost:8000/api/appointment-management/visits/<id>/
- **Method:** DELETE
- **Headers:** 
    - **Key:** Authorization
    - **Value:** Bearer <access_token> (Replace <access_token> with the actual JWT access token)
- **Description:** Remove a visit record. Replace `<id>` with the actual ID of the visit.
