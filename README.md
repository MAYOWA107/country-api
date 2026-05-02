# 🌍 Country API Wrapper (Django + DRF + Redis)

A production-style Django REST API that fetches country information from a public API and uses Redis caching to improve performance and reduce external API calls.

This project demonstrates clean backend architecture with service-layer separation, caching strategy, and API integration.

---

## 🚀 Features

- 🌍 Fetch real-time country data by name  
- ⚡ Redis caching to reduce external API calls  
- 🧠 Clean separation of concerns (View + Service layer)  
- 🔁 Cache-aside pattern implementation  
- 📦 Lightweight and fast API responses  

---

## 🧱 Tech Stack

- Django  
- Django REST Framework  
- Redis  
- External REST API (REST Countries)  

---

## 🌐 External API Used

This project uses the public country data API:

- https://restcountries.com/v3.1/name/{country}

No API key is required.

---

## 📂 Project Structure

```
weather_api/   (or your project root)
│
├── country_app/
│   ├── views.py        # Handles HTTP requests
│   ├── services.py     # External API logic
│
├── core/
│   ├── settings.py     # Django settings (Redis config)
│   ├── urls.py         # API routes
│
└── manage.py
```

---

## ⚙️ Setup & Installation

### 1. Clone the repository

```
git clone https://github.com/MAYOWA107/country-api.git
cd country-api
```

---

### 2. Create virtual environment

```
python -m venv .venv
source .venv/bin/activate   # Linux/Mac
.venv\Scripts\activate      # Windows
```

---

### 3. Install dependencies

```
pip install -r requirements.txt
```

---

### 4. Start Redis server

Make sure Redis is running locally:

```
redis-server
```

---

### 5. Run migrations

```
python manage.py migrate
```

---

### 6. Start development server

```
python manage.py runserver
```

---

## 🌐 API Usage

### Get Country Information

```
GET /api/country/{country}/
```

#### Example:

```
/api/country/nigeria/
```

---

## 🧪 Sample Response

```
{
  "name": "Nigeria",
  "capital": "Abuja",
  "region": "Africa",
  "population": 216000000,
  "currency": "Nigerian naira"
}
```

---

## ⚡ Caching Strategy

- Cache key format: `country:{country}`
- Cache duration: **12 hours**
- Uses Redis for fast in-memory storage
- Implements cache-aside pattern:
  - Check cache first
  - If miss → call external API
  - Store result in cache

---

## 🧠 Architecture Overview

```
Client Request
      ↓
   View Layer
      ↓
   Redis Cache
   ↓        ↓
 HIT      MISS
  ↓         ↓
Response   Service Layer → REST Countries API
                ↓
           Save to Cache
                ↓
             Response
```

---

## 📌 Key Concepts Demonstrated

- External API integration  
- Redis caching strategy  
- Service layer architecture  
- API response transformation  
- Cache-aside design pattern  

---

## ❗ Notes

- No API key required  
- Ensure Redis is running before starting the server  
- API responses are normalized for consistency  

---

## 📈 Future Improvements

- Swagger documentation  
- Rate limiting  
- Docker support  
- Unit tests  
- Async HTTP requests  

---

## 🤝 Contributing

Feel free to fork this project and improve it.

---

## 📄 License

This project is open-source and available under the MIT License.