# Doctor Availability API Endpoints

## List Doctor Availabilities

- **URL:** http://localhost:8000/api/doctor-management/doctor-availabilities/
- **Method:** GET
- **Description:** Retrieve a list of all doctor availabilities.

## Create Doctor Availability

- **URL:** http://localhost:8000/api/doctor-management/doctor-availabilities/
- **Method:** POST
- **Headers:**
    - **Key:** Content-Type
    - **Value:** application/json
    - **Key:** Authorization
    - **Value:** Bearer <access_token>
- **Body:** JSON

    ```json
    {
        "doctor": "doctor_id",
        "days_of_week": [1, 2, 3],  // Represents Monday, Tuesday, Wednesday
        "start_time": "09:00",
        "end_time": "17:00"
    }
    ```

- **Description:** Add a new doctor availability record. Days are represented by numbers (1=Monday, 2=Tuesday, ..., 7=Sunday).

## Update Doctor Availability

- **URL:** http://localhost:8000/api/doctor-management/doctor-availabilities/<id>/
- **Method:** PUT/PATCH
- **Headers:**
    - **Key:** Content-Type
    - **Value:** application/json
    - **Key:** Authorization
    - **Value:** Bearer <access_token>
- **Body:** JSON

    ```json
    {
        "days_of_week": [4, 5],  // Update to the new set of days, e.g., Thursday and Friday
        "start_time": "10:00",
        "end_time": "18:00"
    }
    ```

- **Description:** Update an existing doctor availability record. Replace `<id>` with the actual ID. You can change the days (using numeric representations), start time, or end time as needed.

## Delete Doctor Availability

- **URL:** http://localhost:8000/api/doctor-management/doctor-availabilities/<id>/
- **Method:** DELETE
- **Headers:**
    - **Key:** Authorization
    - **Value:** Bearer <access_token>
- **Description:** Remove a doctor availability record. Replace `<id>` with the actual ID.
