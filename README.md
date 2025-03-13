# LinkedIn Insights Microservice

This is a FastAPI-based microservice for scraping and storing LinkedIn Page details, including page metadata, followers, posts, and employee details. The data is stored in MongoDB and exposed through RESTful APIs.

## Features
- Scrape LinkedIn pages for company details
- Store scraped data in MongoDB
- Retrieve page details via API
- Filter pages by follower count, name, and industry
- Paginated retrieval of posts

## Tech Stack
- **Backend:** FastAPI (Python)
- **Database:** MongoDB (Motor - Async Driver)
- **Web Scraping:** BeautifulSoup, Requests
- **Containerization:** Docker

## Installation

### 1. Clone the Repository
```sh
git clone https://github.com/your-repo/linkedin-insights.git
cd linkedin-insights
```

### 2. Set Up a Virtual Environment
```sh
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies
```sh
pip install -r requirements.txt
```

### 4. Start MongoDB
Ensure MongoDB is running locally on `mongodb://localhost:27017`.

### 5. Run the FastAPI Server
```sh
uvicorn main:app --host 0.0.0.0 --port 8000
```

## API Endpoints

### 1. Get Page Details
**Request:**
```http
GET /page/{page_id}
```
**Response:**
```json
{
  "page_id": "deepsolv",
  "name": "Deepsolv | LinkedIn",
  "url": "https://www.linkedin.com/company/deepsolv/",
  "profile_picture": "",
  "description": "",
  "followers": 5000,
  "head_count": 100,
  "specialities": ["AI", "Machine Learning"],
  "posts": []
}
```

### 2. Get Paginated Posts
**Request:**
```http
GET /page/{page_id}/posts?limit=10&offset=0
```
**Response:**
```json
[ {
    "post_id": "12345",
    "content": "Our latest AI project",
    "likes": 200,
    "comments": ["Great work!", "Awesome!"]
  }
]
```

### 3. Filter Pages by Followers & Industry
**Request:**
```http
GET /pages?followers_min=1000&followers_max=50000&industry=Tech
```
**Response:**
```json
[
  {
    "page_id": "techstartup",
    "name": "Tech Startup Inc",
    "followers": 25000,
    "industry": "Tech"
  }
]
```

## Docker Usage
### 1. Build Docker Image
```sh
docker build -t linkedin-insights .
```
### 2. Run the Container
```sh
docker run -p 8000:8000 linkedin-insights
```

## Postman Collection
Import the Postman collection from `postman_collection.json` for testing API requests.

## Known Issues & Limitations
- LinkedIn has anti-scraping protections; scraping may require proxy rotation.
- Some fields (followers, posts) may not always be available.

## Future Enhancements
- Add caching with Redis
- Implement AI-based insights for LinkedIn data
- Integrate with official LinkedIn API (OAuth)

## Author
Karthik M
