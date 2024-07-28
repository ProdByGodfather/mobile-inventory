# Mobile Inventory Management System

This project is a mobile phone inventory management system implemented using Django.

## Features

- Register and manage phone brands
- Register and manage phone models
- Search and filter phones by brand, name, and other attributes
- Display a detailed list of phones

## Prerequisites

- Python 3.8+
- Django 5.0+
- pip (for installing dependencies)

## Installation and Setup

1. Clone the repository:
https://github.com/ProdByGodfather/mobile-inventory.git

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate # On Linux and macOS
venv\Scripts\activate # On Windows
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run migrations:
```bash
python manage.py migrate
```

5. Create an admin user:
```bash
python manage.py createsuperuser
```

6. Run the development server:
```bash
python manage.py runserver
```

7. View the project in your browser:
http://127.0.0.1:8000/

## How to Use

1. **Adding a Brand**: Use the "Add Brand" form to register new phone brands.

2. **Adding a Mobile Phone**: Use the "Add Mobile" form to register new phone models.

3. **Viewing the Phone List**: Navigate to the phone list page to see all registered phones.

4. **Filtering Phones**: 
- Use the search box to filter phones by brand name.
- Use the brand dropdown to filter phones by a specific brand.
- Use the checkbox to filter phones where the brand nationality matches the manufacturing country.

5. **Admin Panel**: Access the admin panel at `/admin` to manage the database directly.

## Project Structure

- `main/models.py`: Contains the database models for Brand and Mobile.
- `main/views.py`: Contains the view functions for rendering pages and handling requests.
- `main/forms.py`: Contains the forms for adding brands and mobiles.
- `templates/`: Contains the HTML templates for rendering pages.

## Contributing

Feel free to fork the project and submit pull requests for any enhancements.

## License

This project is open-source and available under the MIT License.