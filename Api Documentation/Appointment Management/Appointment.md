# Appointment API Endpoints

## List Appointments

- **URL:** http://localhost:8000/api/appointment-management/appointments/
- **Method:** GET
- **Headers:** 
    - **Key:** Authorization
    - **Value:** Bearer <access_token> (Replace <access_token> with the actual JWT access token)
- **Description:** Retrieve a list of all appointments.

## Create Appointment

- **URL:** http://localhost:8000/api/appointment-management/appointments/
- **Method:** POST
- **Headers:** 
    - **Key:** Authorization
    - **Value:** Bearer <access_token> (Replace <access_token> with the actual JWT access token)
- **Body:** JSON

    ```json
    {
        "patient": "<patient_id>",
        "doctor": "<doctor_id>",
        "date": "YYYY-MM-DD",
        "time": "HH:MM",
        "reason": "Reason for the appointment",
        "is_completed": false
    }
    ```

- **Description:** Add a new appointment record.

## Update Appointment

- **URL:** http://localhost:8000/api/appointment-management/appointments/<id>/
- **Method:** PUT/PATCH
- **Headers:** 
    - **Key:** Authorization
    - **Value:** Bearer <access_token> (Replace <access_token> with the actual JWT access token)
- **Body:** JSON

    ```json
    {
        "reason": "Updated reason for the appointment",
        "is_completed": true
    }
    ```

- **Description:** Update an existing appointment record. Replace `<id>` with the actual ID of the appointment.

## Delete Appointment

- **URL:** http://localhost:8000/api/appointment-management/appointments/<id>/
- **Method:** DELETE
- **Headers:** 
    - **Key:** Authorization
    - **Value:** Bearer <access_token> (Replace <access_token> with the actual JWT access token)
- **Description:** Remove an appointment record. Replace `<id>` with the actual ID of the appointment.
