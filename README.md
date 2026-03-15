# SabaStyle – Women's Fashion Shopping Platform

**SabaStyle** is a premium women's and children's fashion e-commerce platform built with Django. It features trending collections, secure UPI payments, personalized branding, and a modern, secure shopping experience designed for the contemporary user.

## Key Features
* **User Registration and Login**: Visitors must authenticate to browse the platform.
* **Women Shopping Section**: Curated collections for women.
* **Child Shopping Section**: Trendy wear for children.
* **Product Discovery**: Detailed listings and individual product pages.
* **Category Browsing**: Filter by Jewellery, Makeup, Western, and Traditional attire.
* **Trending Products**: See what's popular in real-time.
* **Stylish UI**: Premium, responsive design with elegant typography.

## Technologies Used
* Python
* Django
* HTML / CSS / JavaScript
* Bootstrap 5
* SQLite Database

## Project Screenshots
![Home Page](file:///C:/Users/shabb/.gemini/antigravity/brain/656937d3-5660-4627-84d9-9929853a7e29/full_page_home_1773573933850.png)

## Demo Video
Watch the playback of the platform in action: [demo.mp4](./demo.mp4)

## Folder Structure
```
shopping_platform/
├── saba_kausar_platform/  # Project settings
├── shop/                   # Main application logic
├── accounts/               # User authentication
├── orders/                 # Cart and checkout
├── templates/              # HTML templates
├── media/                  # Product images
├── static/                 # CSS/JS and branding assets
├── db.sqlite3
└── requirements.txt
```

## Installation Guide
1. **Clone the repository**:
   ```bash
   git clone https://github.com/shabba-kausar/sabastyle-shopping-platform.git
   cd sabastyle-shopping-platform
   ```
2. **Setup Virtual Environment**:
   ```bash
   python -m venv venv
   .\venv\Scripts\activate
   ```
3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
4. **Run Migrations**:
   ```bash
   python manage.py migrate
   ```
5. **Start Server**:
   ```bash
   python manage.py runserver
   ```
   Visit `http://127.0.0.1:8000/` to explore.
