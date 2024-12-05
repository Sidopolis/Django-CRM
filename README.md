<img width="959" alt="crm" src="https://github.com/user-attachments/assets/70f40694-82b9-4a26-8860-52c669d8da0d">

# Modern CRM

A minimal and powerful Customer Relationship Management system built with Django. This modern CRM helps businesses manage their customer relationships efficiently with a clean, dark-themed interface.

## Features

- 🔐 User Authentication
  - Register
  - Login
  - Logout
  - Session Management

- 👥 Customer Management
  - Add new customer records
  - View all customer records
  - Update existing records
  - Delete records

- 💫 Modern UI
  - Dark theme
  - Responsive design
  - Clean interface
  - Smooth transitions

## Technologies Used

- **Backend**
  - Django 4.x
  - Python 3.x
  - SQLite3 (Database)

- **Frontend**
  - HTML5
  - CSS3
  - JavaScript
  - Django Templates

## Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/modern-crm.git
   cd modern-crm

2. **Create a virtual environment**
   ```bash
   python -m venv venv

3. **Activate virtual environment**
   - Windows:
     ```bash
     env\Scripts\activate

   - Linux/Mac:
     ```bash
     source venv/bin/activate

5. **Install dependencies**
   ```bash
   pip install -r requirements.txt

6. **Run migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate

7. **Create superuser (Admin)**
   ```bash
   python manage.py createsuperuser

8. **Run the development server**
   ```bash
   python manage.py runserver

## Usage

1. Access the application at `http://localhost:8000`
2. Register a new account or login with existing credentials
3. Add, view, update, or delete customer records
4. Use the navigation bar to access different features
5. Logout when finished

## Project Structure

```
modern-crm/
├── website/
│ ├── templates/
│ │ ├── base.html
│ │ ├── home.html
│ │ ├── landing.html
│ │ ├── login.html
│ │ ├── register.html
│ │ ├── add_record.html
│ │ └── update_record.html
│ ├── models.py
│ ├── views.py
│ └── urls.py
├── static/
│ ├── css/
│ └── js/
├── manage.py
└── requirements.txt
```

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details

## Acknowledgments

* Django Documentation
* Modern UI/UX Design Principles
* Open Source Community
