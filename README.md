# EMINLE

Web-based game inspired by Yeezle. Users are challenged to guess a randomly selected Eminem song. The game provides hints based on track details, and players can make multiple attempts to find the correct answer.

## Full Stack Project - Django Backend with React Frontend

This is a full-stack web application with a **Django** backend and a **React** frontend. The backend is built using Django REST Framework, while the frontend is developed with React.


## Visual Highlights

<div style="display: flex; justify-content: space-between; gap: 20px;">
  <img src="https://github.com/user-attachments/assets/0508d280-93c4-4698-a20c-2850520bb45e" alt="Starting Page" width="48%" />
  <img src="https://github.com/user-attachments/assets/99fb2577-0839-4144-b733-f73fe7a140db" alt="Input" width="48%" />
</div>

<div style="display: flex; justify-content: space-between; gap: 20px; margin-top: 20px;">
  <img src="https://github.com/user-attachments/assets/2aa358f0-9e8e-4aae-b145-b7d5acbcd063" alt="You Won" width="48%" />
  <img src="https://github.com/user-attachments/assets/3ef28244-773b-420b-82d5-212257f00e6f" alt="You Lost" width="48%" />
</div>

## Technologies Used

- **Backend**: Django, Django REST Framework
- **Frontend**: React
- **Database**: SQLite
- **Package Managers**: pip (for Python), npm (for JavaScript)
- **Version Control**: Git

## Setup Instructions

### 1. Clone the Repository

Clone this repository to your local machine using the following command:

```bash
git clone https://github.com/w-makowski/eminle.git
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

