# Doctor Management API Endpoints

## List Doctors

- **URL:** http://localhost:8000/api/doctor-management/doctors/
- **Method:** GET
- **Headers:** 
    - **Key:** Authorization
    - **Value:** Bearer <access_token> (Replace <access_token> with the actual JWT access token)
- **Description:** Retrieve a list of all doctors.

## Create Doctor

- **URL:** http://localhost:8000/api/doctor-management/doctors/
- **Method:** POST
- **Headers:** 
    - **Key:** Authorization
    - **Value:** Bearer <access_token> (Replace <access_token> with the actual JWT access token)
- **Body:** JSON

    ```json
    {
        "user": "user_id",
        "name": "Dr. John Doe",
        "gender": "M",
        "contact_number": "1234567890",
        "specialization": "Cardiology",
        "qualifications": "MD",
        "departments": ["department_id"]
    }
    ```

- **Description:** Add a new doctor record.

## Update Doctor

- **URL:** http://localhost:8000/api/doctor-management/doctors/<id>/
- **Method:** PUT/PATCH
- **Headers:** 
    - **Key:** Authorization
    - **Value:** Bearer <access_token> (Replace <access_token> with the actual JWT access token)
- **Body:** JSON

    ```json
    {
        "name": "Dr. John Doe Updated",
        "specialization": "Updated Specialization"
    }
    ```

- **Description:** Update an existing doctor record. Replace `<id>` with the actual ID of the doctor.

## Delete Doctor

- **URL:** http://localhost:8000/api/doctor-management/doctors/<id>/
- **Method:** DELETE
- **Headers:** 
    - **Key:** Authorization
    - **Value:** Bearer <access_token> (Replace <access_token> with the actual JWT access token)
- **Description:** Remove a doctor record. Replace `<id>` with the actual ID of the doctor.
