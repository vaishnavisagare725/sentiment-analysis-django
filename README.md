# 🧠 Sentiment Analysis Web Application

> A Django-based web application that analyzes user-entered text and classifies it as **Positive, Negative, or Neutral** using **TextBlob**.

---

## 📌 About The Project

This project is a **Sentiment Analysis Web Application** developed using **Python and Django**.

Users can enter any text, and the application analyzes it using the **TextBlob Natural Language Processing library**.

The application displays:

* 😊 Sentiment classification
* 📊 Polarity score
* 📝 Subjectivity score
* 📚 Analysis history
* 📈 Sentiment dashboard

The project also includes **user authentication, REST API integration, Postman testing, and Django Admin**.

---

## ✨ Features

| Feature                | Description                     |
| ---------------------- | ------------------------------- |
| 🔐 User Authentication | Register, Login and Logout      |
| 🧠 Sentiment Analysis  | Analyze user-entered text       |
| 😊 Positive            | Detect positive text            |
| 😐 Neutral             | Detect neutral text             |
| 😞 Negative            | Detect negative text            |
| 📊 Polarity            | Displays polarity score         |
| 📝 Subjectivity        | Displays subjectivity score     |
| 📚 History             | Stores user's previous analyses |
| 🔎 Search              | Search previous analyses        |
| 🏷️ Filter             | Filter by sentiment             |
| 🗑️ Delete             | Delete previous analysis        |
| 📈 Dashboard           | Displays sentiment statistics   |
| 📊 Chart               | Visual sentiment distribution   |
| 🔧 Admin Panel         | Manage application data         |
| 🌐 REST API            | Analyze text through API        |
| 🧪 Postman             | Test REST API                   |

---

## 🛠️ Technologies Used

### Backend

* 🐍 Python
* 🌐 Django
* 🧠 TextBlob
* 🔌 Django REST Framework

### Database

* 🗄️ SQLite

### Frontend

* HTML
* CSS
* Bootstrap
* JavaScript
* Chart.js

### Tools

* Git
* GitHub
* Postman
* Visual Studio Code

---

## 🧠 How Sentiment Analysis Works

The application uses **TextBlob** to calculate two important values.

### 📊 Polarity

Polarity represents how positive or negative the text is.

```text
Range: -1 to +1
```

| Value | Meaning       |
| ----- | ------------- |
| -1    | Very Negative |
| 0     | Neutral       |
| +1    | Very Positive |

### 📝 Subjectivity

Subjectivity represents how objective or subjective the text is.

```text
Range: 0 to 1
```

| Value | Meaning         |
| ----- | --------------- |
| 0     | More Objective  |
| 1     | More Subjective |

---

## 🎯 Sentiment Classification

The application classifies text into three categories:

```text
😊 Positive
😐 Neutral
😞 Negative
```

### Example 1 — Positive

**Input:**

```text
I really love this application!
```

**Output:**

```text
Sentiment: Positive
Polarity: Calculated by TextBlob
Subjectivity: Calculated by TextBlob
```

### Example 2 — Negative

**Input:**

```text
This product is very bad.
```

**Output:**

```text
Sentiment: Negative
Polarity: Calculated by TextBlob
Subjectivity: Calculated by TextBlob
```

### Example 3 — Neutral

**Input:**

```text
The product is available.
```

**Output:**

```text
Sentiment: Neutral
Polarity: Calculated by TextBlob
Subjectivity: Calculated by TextBlob
```

---

## 📂 Project Structure

```text
sentiment-analysis-django/
│
├── manage.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── sentiment_project/
│   ├── settings.py
│   ├── urls.py
│   └── ...
│
└── sentiment/
    │
    ├── migrations/
    │
    ├── templates/
    │   └── sentiment/
    │       ├── analyze.html
    │       ├── dashboard.html
    │       ├── history.html
    │       ├── login.html
    │       └── register.html
    │
    ├── admin.py
    ├── models.py
    ├── urls.py
    └── views.py
```

---

## 🚀 Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/vaishnavisagare725/sentiment-analysis-django.git
```

### 2️⃣ Navigate to the Project

```bash
cd sentiment-analysis-django
```

### 3️⃣ Create Virtual Environment

```bash
python -m venv venv
```

### 4️⃣ Activate Virtual Environment

**Windows:**

```bash
venv\Scripts\activate
```

### 5️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 6️⃣ Run Migrations

```bash
python manage.py migrate
```

### 7️⃣ Start the Server

```bash
python manage.py runserver
```

### 8️⃣ Open in Browser

```text
http://127.0.0.1:8000/
```

---

## 🌐 REST API

The project provides a REST API for sentiment analysis.

### API Endpoint

```text
POST /api/analyze/
```

### Request

```json
{
    "text": "I really love this application!"
}
```

### Response

```json
{
    "id": 1,
    "text": "I really love this application!",
    "sentiment": "Positive",
    "polarity": 0.625,
    "subjectivity": 0.6
}
```

> ℹ️ The polarity and subjectivity values depend on the input text.

---

## 🧪 API Testing

The REST API was tested using **Postman**.

### Test Request

```text
Method: POST
URL: http://127.0.0.1:8000/api/analyze/
```

### Body

```json
{
    "text": "This is an amazing application!"
}
```

---

## 🔐 Authentication

The application provides:

* User Registration
* User Login
* User Logout
* User-specific analysis history
* Protected dashboard
* Protected history
* Protected sentiment analysis

---

## 📈 Dashboard

The dashboard provides an overview of analyzed text:

```text
Total Analyses
Positive
Negative
Neutral
```

It also displays a visual chart showing sentiment distribution.

---

## 🔧 Django Admin

The project includes a Django Admin panel for managing sentiment analysis records.

Admin URL:

```text
http://127.0.0.1:8000/admin/
```

---

## 🧪 Testing

The application was tested for:

* ✅ Positive sentiment
* ✅ Negative sentiment
* ✅ Neutral sentiment
* ✅ User registration
* ✅ User login
* ✅ User logout
* ✅ Analysis history
* ✅ Search functionality
* ✅ Sentiment filtering
* ✅ Delete functionality
* ✅ Dashboard statistics
* ✅ Sentiment chart
* ✅ REST API
* ✅ Postman API testing
* ✅ Django Admin

---

## 🎓 Learning Outcomes

Through this project, I gained practical experience in:

* Python and Django development
* Natural Language Processing basics
* TextBlob sentiment analysis
* Django ORM
* SQLite database
* User authentication
* REST API development
* API testing with Postman
* Data visualization
* Git and GitHub
* Project documentation

---

## 🔮 Future Improvements

* 🤖 Machine Learning based sentiment analysis
* 🔐 API authentication
* 👤 User profile management
* 📊 Advanced dashboard
* ☁️ Cloud deployment
* 🐳 Docker support
* 🧠 Advanced NLP features

---

## 👩‍💻 Author

### Vaishnavi Sagare

**Python Full Stack Developer**

🔗 **GitHub:**
https://github.com/vaishnavisagare725

---

## ⭐ Project

If you find this project useful, consider giving it a ⭐ on GitHub.

---

### 📌 Project Summary

> **Sentiment Analysis Web Application** — Developed a Django-based web application using TextBlob to analyze user-entered text and classify it as Positive, Negative, or Neutral. Implemented polarity and subjectivity score calculation, user authentication, analysis history, search/filter functionality, dashboard visualization, Django Admin, and REST API integration.

