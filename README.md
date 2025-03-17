# 📚 BookHarvester - Scraping Books with Django & Scrapy


**BookHarvester** is a web application that scrapes book data from various sources using **Scrapy** and stores the information in a **Django** backend with a **PostgreSQL** database. The data is then made available through a REST API.  


---

## 🚀 Features  

✅ **Web Scraper** for extracting book details (title, description, price, and category)  
✅ **Django Backend** to manage and serve scraped data  
✅ **PostgreSQL Database** for persistent storage  
✅ **Django REST Framework (DRF)** for API endpoints  
✅ **Automated Data Import** using Django management commands  
✅ **Docker Support** for easy deployment  

---


## 🛠️ Installation  

### Prerequisites  
Make sure you have the following installed:  
- Python (>= 3.8)  
- PostgreSQL  
- Virtualenv (optional but recommended)  
- Docker (optional)  



### Setup  

1️⃣ **Clone the repository:**  
```sh
git clone https://github.com/yourusername/BookHarvester.git
cd BookHarvester
```

2️⃣ **Create and activate a virtual environment:**  
```sh
python -m venv .venv
source .venv/bin/activate  # On Windows, use `.venv\Scripts\activate`
```

3️⃣ **Install dependencies:**  
```sh
pip install -r requirements.txt
```

4️⃣ **Set up the database:**  
```sh
python manage.py migrate
```

5️⃣ **Run the Scrapy spider to fetch book data:**  
```sh
scrapy crawl books
```

6️⃣ **Run the Django development server:**  
```sh
python manage.py runserver
```

The app should now be running at **http://127.0.0.1:8000/** 🎉  

---

## 📡 API Endpoints  

- **`GET /api/books/`** – Retrieve all books  
- **`GET /api/books/<id>/`** – Retrieve a specific book  
- **`POST /api/books/`** – Add a new book (if manual entry is allowed)  
- **`PUT /api/books/<id>/`** – Update book details  
- **`DELETE /api/books/<id>/`** – Delete a book  

---


### Backend Tree 
---
<img src="./assets/Screenshot 2025-03-17 at 20.23.16.png" alt="backend tree" width="180"  height="300"/>
---
