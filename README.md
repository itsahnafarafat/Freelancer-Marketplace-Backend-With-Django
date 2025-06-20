# 🧑‍💻 Freelancer Marketplace Backend API

A fully functional **Freelancer Marketplace backend** built with **Django** and **Django REST Framework (DRF)**. This project powers the backend for a freelance platform — enabling clients to post jobs, freelancers to apply, and providing secure, role-based access to a scalable API.

---

## 🚀 Live Deployment

> ✅ **Deployment Status**: `Deployed (Final Testing In Progress)`
>  
> 🌐 Hosted on **Railway**  
> 🔧 Final bug fixes are in progress to ensure 100% live stability.

---

## 📌 Project Summary

This is a real-world backend system for a **freelancing platform** like **Fiverr** or **Upwork**. It includes:

- 🔐 JWT-based authentication
- 👤 Role selection (Client/Freelancer)
- 📄 Job posting by clients
- 📬 Applications by freelancers
- 🧾 Dashboard views based on user role
- 🧪 API testing with Postman
- ☁️ Production-ready deployment

---

## 💡 Key Features

- ✅ Custom User Model with Role Selection
- ✅ JWT Token Authentication
- ✅ Client & Freelancer Profiles
- ✅ Role-Based Dashboards
- ✅ Job Posting System
- ✅ Freelancer Applications
- ✅ Secure, DRF TokenAuth Protected APIs
- ✅ Deployed on Railway
- 🔧 Testing & Bug Fixing (ongoing)
- 🔜 Unit Testing (up next)

---

## 🛠️ Technologies Used

| Tech        | Description                          |
|-------------|--------------------------------------|
| Python 3.12 | Backend Language                     |
| Django 5.2  | Core Backend Framework               |
| DRF         | Django REST Framework for APIs       |
| SQLite      | Dev Database                         |
| Railway     | Cloud Deployment Platform            |
| GitHub      | Version Control + CI/CD              |

---

## 📂 Project Structure

```

freelancer-backend/
├── core/
│   ├── models.py           # Custom User, Job, Profile, Application
│   ├── serializers.py      # DRF Serializers
│   ├── views.py            # Role-based View Logic
│   ├── urls.py             # API Routes
├── freelance\_backend/
│   ├── settings.py         # Django Settings
│   ├── urls.py             # Project Routes
├── manage.py
├── requirements.txt
└── README.md

````

---

## 📲 API Overview (Postman Ready)

### 🔑 Auth
- `POST /api/register/` – User registers as `Client` or `Freelancer`
- `POST /api/login/` – Login and receive auth token
- `GET /api/dashboard/` – Role-specific dashboard

### 📄 Jobs
- `POST /api/jobs/` – Client posts a job
- `GET /api/jobs/` – Freelancer views available jobs
- `POST /api/jobs/<job_id>/apply/` – Apply to a job

---

## 👨‍💻 Current Status

| Phase                | Status     |
|----------------------|------------|
| Core Features        | ✅ Complete |
| Role-based API       | ✅ Complete |
| Postman Testing      | ⏳ In Progress |
| Deployment (Railway) | ✅ Done |
| Bug Fixes            | 🔧 Ongoing |
| Unit Tests           | 🔜 Planned |

---

## 🔒 Security Best Practices

- ✅ Secret keys secured (not exposed in version control)
- ✅ Token-based authentication using DRF
- ✅ `DEBUG = False` in production
- ✅ Model validations & permission checks

---

## 🎯 Use Case

This project is ideal for:

- 🧑‍💻 Showcasing backend skills in job applications  
- 🛠️ API base for freelance platforms  
- 💼 Portfolio-ready deployment for recruiters  
- 🔄 Integration-ready backend for frontend teams

---

## ✅ Local Development Setup

```bash
# Clone the repo
git clone https://github.com/itsahnafarafat/freelancer-backend.git
cd freelancer-backend

# Create virtual environment
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Start the server
python manage.py runserver
````

---

## 👤 Author

**Ahnaf Arafat**
Backend Developer | Django & Flask & Python
🔗 [LinkedIn →](https://www.linkedin.com/in/ahnaf-arafat-30189a357)
🔗 [GitHub →](https://github.com/itsahnafarafat)

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---


