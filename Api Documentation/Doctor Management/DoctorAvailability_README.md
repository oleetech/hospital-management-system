# Doctor Availability API Endpoints

## List Doctor Availabilities

- **URL:** http://localhost:8000/api/doctor-management/doctor-availabilities/
- **Method:** GET
- **Description:** Retrieve a list of all doctor availabilities.

## Create Doctor Availability

- **URL:** http://localhost:8000/api/doctor-management/doctor-availabilities/
- **Method:** POST
- **Body:** JSON

    ```json
    {
        "doctor": "doctor_id",
        "day_of_week": 1,
        "start_time": "09:00",
        "end_time": "17:00"
    }
    ```

- **Description:** Add a new doctor availability record.

## Update Doctor Availability

- **URL:** http://localhost:8000/api/doctor-management/doctor-availabilities/<id>/
- **Method:** PUT/PATCH
- **Body:** JSON

    ```json
    {
        "day_of_week": 2,
        "start_time": "10:00",
        "end_time": "18:00"
    }
    ```

- **Description:** Update an existing doctor availability record. Replace `<id>` with the actual ID.

## Delete Doctor Availability

- **URL:** http://localhost:8000/api/doctor-management/doctor-availabilities/<id>/
- **Method:** DELETE
- **Description:** Remove a doctor availability record. Replace `<id>` with the actual ID.
