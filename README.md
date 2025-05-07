# Full Stack Project - Django Backend with React Frontend

This is a full-stack web application with a **Django** backend and a **React** frontend. The backend is built using Django REST Framework, while the frontend is developed with React.

## Technologies Used

- **Backend**: Django, Django REST Framework
- **Frontend**: React
- **Database**: SQLite
- **Package Managers**: pip (for Python), npm (for JavaScript)
- **Version Control**: Git
- **Deployment**: Will be detailed later

## Setup Instructions

### 1. Clone the Repository

Clone this repository to your local machine using the following command:

```bash
git clone https://github.com/yourusername/eminle.git
```

### 2. Setting Up the Backend

1. Navigate to the `backend` directory:

    ```bash
    cd backend
    ```

2. Create a virtual environment for the backend:

    ```bash
    python3 -m venv .venv
    ```

3. Activate the virtual environment:

    - On macOS/Linux:

        ```bash
        source .venv/bin/activate
        ```

    - On Windows:

        ```bash
        .venv\Scripts\activate
        ```

4. Install the backend dependencies:

    ```bash
    pip install -r requirements.txt
    ```

5. Apply database migrations:

    ```bash
    python manage.py migrate
    ```

6. Run the development server:

    ```bash
    python manage.py runserver
    ```

    This will start the Django backend on `http://localhost:8000/`.

### 3. Setting Up the Frontend

1. Navigate to the `frontend` directory:

    ```bash
    cd frontend
    ```

2. Install the frontend dependencies using npm:

    ```bash
    npm install
    ```

3. Start the React development server:

    ```bash
    npm start
    ```

    This will start the React frontend on `http://localhost:3000/`.

### 4. Connecting Backend with Frontend

The frontend will make requests to the backend API, which is served on `http://localhost:8000/` by default. You can modify the `axios` or fetch requests in the React frontend to target this URL for making API calls.

If you're using **Django CORS Headers** to handle cross-origin requests, make sure the backend allows the frontend to connect. You can add this to your backend's settings if you haven't already:

```python
# settings.py
INSTALLED_APPS = [
    ...
    'corsheaders',
    ...
]

MIDDLEWARE = [
    ...
    'corsheaders.middleware.CorsMiddleware',
    ...
]

CORS_ORIGIN_WHITELIST = [
    'http://localhost:3000',  # Your React frontend URL
]
```

### 5. Build the React App for Production (Optional)

To prepare the frontend for production, run the following command:

```bash
npm run build
```

This will generate a `build/` directory containing a production-ready version of your React app. You can serve this through your Django backend or deploy it separately.

### 6. Deployment (Optional)

You can deploy the backend (Django) and frontend (React) to services like Heroku, AWS, or DigitalOcean. Here are some common steps:

- **Backend Deployment**: Set up the backend on Heroku, AWS, or another platform. Make sure to configure the `DATABASE_URL` environment variable for PostgreSQL (or use SQLite if you prefer).
- **Frontend Deployment**: Deploy the React frontend on services like Netlify, Vercel, or a similar platform.
- **Serving Together**: If you want to serve both backend and frontend from a single domain, you can configure your Django app to serve the static files from the `frontend/build/` directory.

## Development Workflow

1. Start the backend server (Django):
    ```bash
    python manage.py runserver
    ```

2. Start the frontend server (React):
    ```bash
    npm start
    ```

3. Make changes to the code, and both servers should automatically reload your changes.

## Troubleshooting

- **Backend Not Responding**: If your backend is not responding, make sure it's running on `http://localhost:8000/` and check for any errors in the terminal.
- **CORS Issues**: If the frontend can't communicate with the backend due to CORS issues, ensure `django-cors-headers` is properly configured in the backend.

## Requirements

### Backend Requirements

- Django
- Django REST Framework
- Other dependencies listed in the `requirements.txt` file

### Frontend Requirements

- React (and dependencies managed through `package.json`)

