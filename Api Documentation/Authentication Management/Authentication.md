# API Endpoints

## User Registration

- **URL:** http://localhost:8000/auth/users/
- **Method:** POST
- **Body:** JSON

    ```json
    {
        "username": "example_user",
        "password": "example_password",
        "re_password": "example_password",
        "email": "example@example.com"
    }
    ```

- **Description:** Register a new user with the provided username, password, and email.

## User Login

- **URL:** http://localhost:8000/auth/token/login/
- **Method:** POST
- **Body:** JSON

    ```json
    {
        "username": "example",
        "password": "password"
    }
    ```

- **Description:** Obtain an authentication token by providing the username and password.

## User Logout

- **URL:** http://localhost:8000/auth/token/logout/
- **Method:** POST
- **Headers:** 
    - **Key:** Authorization
    - **Value:** Bearer <auth_token> (Replace <auth_token> with the actual authentication token obtained during login)

- **Description:** Log out the authenticated user by providing the authentication token.

## User Profile Details

- **URL:** http://localhost:8000/auth/users/me/
- **Method:** GET
- **Headers:** 
    - **Key:** Authorization
    - **Value:** Bearer <auth_token> (Replace <auth_token> with the actual authentication token)

- **Description:** Retrieve the profile details of the authenticated user.

## User Profile Update

- **URL:** http://localhost:8000/auth/users/me/
- **Method:** PUT
- **Headers:** 
    - **Key:** Authorization
    - **Value:** Bearer <auth_token> (Replace <auth_token> with the actual authentication token)

- **Body:** JSON with the data to update the user profile.

    ```json
    {
        "username": "new_username",
        "email": "new_email@example.com"
    }
    ```

- **Description:** Update the profile details of the authenticated user.

## Password Reset Request

- **URL:** http://localhost:8000/auth/users/reset_password/
- **Method:** POST
- **Body:** JSON

    ```json
    {
        "email": "example@example.com"
    }
    ```

- **Description:** Request a password reset by providing the email address associated with the account.

## Password Reset Confirmation

- **URL:** http://localhost:8000/auth/users/reset_password_confirm/
- **Method:** POST
- **Body:** JSON with the data to confirm the password reset.

    ```json
    {
        "uid": "uid",
        "token": "token",
        "new_password": "new_password"
    }
    ```

- **Description:** Confirm the password reset by providing the user ID (uid), token, and new password.

# API Endpoints for JWT Authentication

## User Login

- **URL:** http://localhost:8000/auth/jwt/create/
- **Method:** POST
- **Body:** JSON

    ```json
    {
        "username": "example",
        "password": "password"
    }
    ```

- **Description:** Obtain a JWT token by providing the username and password.

## JWT Token Refresh

- **URL:** http://localhost:8000/auth/jwt/refresh/
- **Method:** POST
- **Body:** JSON with the refresh token.

    ```json
    {
        "refresh": "refresh_token"
    }
    ```

- **Description:** Refresh the JWT token by providing the refresh token obtained during token creation.

## JWT Token Verify

- **URL:** http://localhost:8000/auth/jwt/verify/
- **Method:** POST
- **Body:** JSON with the token.

    ```json
    {
        "token": "access_token"
    }
    ```

- **Description:** Verify the validity of the JWT token by providing the access token.
