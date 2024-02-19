# Installation

To use Django Rest Framework along with Simple JWT and Djoser, follow these installation steps:

1. Install Django Rest Framework:

    ```bash
    pip install djangorestframework
    ```

2. Install Django Rest Framework Simple JWT:

    ```bash
    pip install djangorestframework-simplejwt
    ```

3. Install django-cors-headers package:

    ```bash
    pip install django-cors-headers
    ```

4. Install Djoser:

    ```bash
    pip install djoser
    ```

# Configuration

1. Configure your Django project settings by adding the following apps to the `INSTALLED_APPS` in your `settings.py` file:

    ```python
    INSTALLED_APPS = [
        # For API
        'corsheaders',
        'rest_framework',
        'djoser',
        'rest_framework_simplejwt'
    ]
    ```

2. Allow all origins for CORS:

    ```python
    CORS_ALLOW_ALL_ORIGINS = True
    ```

3. Configure JWT token expiration time in your `settings.py`:

    ```python
    # Import necessary module
    from datetime import timedelta

    # Configure JWT token expiration time
    SIMPLE_JWT = {
        'ACCESS_TOKEN_LIFETIME': timedelta(minutes=15),  # Expires in 15 minutes
        'REFRESH_TOKEN_LIFETIME': timedelta(days=1),      # Expires in 1 day
    }
    ```

4. Configure authentication classes and middleware in your `settings.py`:

    ```python
    # settings.py
    REST_FRAMEWORK = {
        'DEFAULT_AUTHENTICATION_CLASSES': [
            'rest_framework.authentication.TokenAuthentication',  # Token authentication
            'rest_framework_simplejwt.authentication.JWTAuthentication',  # JWT authentication
            'rest_framework.authentication.SessionAuthentication',  # Session authentication
            'rest_framework.authentication.BasicAuthentication',  # Basic authentication
        ],
    }

    MIDDLEWARE = [
        'corsheaders.middleware.CorsMiddleware',
        # Add other middleware classes if any
    ]
    ```

Now, your Django project is configured to use Django Rest Framework, Simple JWT, and Djoser.
