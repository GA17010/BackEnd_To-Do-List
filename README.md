# To-Do List Backend

This is the backend for a To-Do List application built with Django and Python.

## Features

- Create, read, update, and delete tasks
- Due dates and reminders

## Requirements

- Python 3.11.2
- Django 5.1.5
- Django REST framework

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/GA17010/backend_to_do_list.git
    cd backend_to_do_list
    ```

2. Create and activate a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Apply migrations:
    ```bash
    python manage.py migrate
    ```

5. Create a superuser:
    ```bash
    python manage.py createsuperuser
    ```

6. Run the development server:
    ```bash
    python manage.py runserver
    ```

## API Endpoints

- `GET /api/tasks/` - List all tasks
- `POST /api/tasks/add/` - Create a new task
- `PUT /api/tasks/update/<id>/` - Update a task
- `DELETE /api/tasks/delete/<id>/` - Delete a task

## Contributing

1. Fork the repository
2. Create a new branch (`git checkout -b feature-branch`)
3. Commit your changes (`git commit -m 'Add some feature'`)
4. Push to the branch (`git push origin feature-branch`)
5. Open a pull request

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.