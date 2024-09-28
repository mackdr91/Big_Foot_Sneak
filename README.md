# Big Foot Sneak App

Big Foot Sneak is a Django-based web application for sneaker enthusiasts to manage their collections, track inventory, and share their passion for footwear.

## Features

- User authentication and profiles
- Sneaker management with detailed information
- Brand and category organization
- Collection creation and management
- QR code generation for each sneaker
- Image upload for sneakers
- Size and color tracking for each sneaker model

## Models

The app uses the following main models:

- User (Django's built-in user model)
- Brand
- Category
- Size
- Color
- SneakerImage
- Sneaker
- CollectionType
- Collection

## Setup

1. Clone the repository
2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Set up your database in `settings.py`
4. Run migrations:
   ```
   python manage.py makemigrations
   python manage.py migrate
   ```
5. Create a superuser:
   ```
   python manage.py createsuperuser
   ```
6. Run the development server:
   ```
   python manage.py runserver
   ```

## Usage

- Access the admin panel at `/admin` to manage data
- (Add more usage instructions as you develop the frontend)

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.


