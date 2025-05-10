# 🌟 Iconic Job Portal

Iconic Job Portal is a web-based application that connects job seekers and employers.  
Users can register as either **job seekers** or **employers**, post and apply for jobs, and manage applications.  
Built using Django and Bootstrap for a clean and responsive experience.

## 👨‍💼 User Roles

- **Job Seeker (Candidate):**
  - Register/login
  - Browse job listings
  - Apply for jobs
  - Bookmark jobs
  - Update profile and upload resume

- **Employer (Recruiter):**
  - Register/login
  - Post jobs with multiple tags
  - View and manage applicants
  - Update company profile

## 🔧 Tech Stack

- **Backend:** Python, Django, SQLite
- **Frontend:** HTML, CSS, Bootstrap
- **Auth:** Django's built-in authentication with a custom user model (AbstractUser)
- **Version Control:** Git & GitHub

## 🚀 Features

- Custom user registration with role selection (candidate or recruiter)
- Role-based login and dashboard
- Job posting with support for multiple tags (ManyToManyField)
- User profile management with profile picture support
- Application tracking for recruiters
- Responsive UI

## 📂 Project Structure

- `accounts/` – Custom user model, login, registration
- `jobs/` – Job posting and application logic
- `templates/` – HTML templates organized by role
- `static/` – CSS, JS, and images
- `media/` – Uploaded profile pictures and resumes
- `manage.py` – Django management script

## 💡 How to Run Locally

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/iconic-job-portal.git
   cd iconic-job-portal

## 📌 Purpose
This project was built to:
- Practice full-stack Django development
- Understand real-world user role management
- Build a functional job portal with end-to-end features
