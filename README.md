# 📚 EduPath — A Web-Based Learning Management System

EduPath is a full-stack web application built with Django that provides students with an organized and interactive learning experience. It features subject browsing, self-assessment quizzes, automatic progress tracking, and a personalized dashboard.

---

## 🌐 Live Demo
🔗 [sathyaaaa.pythonanywhere.com](https://sathyaaaa.pythonanywhere.com)

---

## ✨ Features

- 🔐 **User Authentication** — Register, login, logout with Django's built-in auth
- 📚 **Subject Browsing** — Subjects organized into 4 categories: Core, Theory, Allied, Emerging
- 🔍 **Keyword Search** — Search subjects by name instantly
- 📄 **Subject Detail Pages** — Thumbnail, description, YouTube lecture links, course material links
- 🧠 **Quiz Assessment** — Randomized multiple choice quizzes per subject
- ✅ **Answer Review** — Correct/wrong answer highlighting after submission
- 🎉 **Confetti Animation** — Triggers on passing a quiz
- 📊 **Progress Tracking** — Subjects auto-marked as completed on passing
- 📈 **Sidebar Dashboard** — Personalized progress bar, stats, and completed subjects list
- 🗃️ **Quiz Score History** — Every attempt saved with score and timestamp

---

## 🛠️ Tech Stack

| Technology | Usage |
|------------|-------|
| Python 3 | Core programming language |
| Django | Backend framework (MVT architecture) |
| SQLite3 | Database |
| HTML5 & CSS3 | Frontend (no external frameworks) |
| JavaScript | Quiz interactions and confetti |
| Google Fonts | DM Sans + DM Serif Display typography |
| Pillow | Subject thumbnail image handling |

---

## 📁 Project Structure

```
structured_learning_system/
├── core/                  # Project settings and URLs
│   ├── settings.py
│   └── urls.py
├── learning/              # Main app
│   ├── models.py          # Subject, Quiz, Progress, QuizScore
│   ├── views.py           # All view functions
│   └── templates/         # HTML templates
├── templates/             # Global templates
│   ├── home.html
│   ├── subject_detail.html
│   ├── quiz.html
│   ├── login.html
│   └── register.html
├── media/                 # Uploaded thumbnails
└── manage.py
```

---

## 🗄️ Database Models

- **Subject** — name, category, description, thumbnail, resource links
- **Quiz** — question, 4 options, correct answer (linked to Subject)
- **Progress** — tracks completion per user per subject
- **QuizScore** — stores score history with timestamps

---

## 🚀 Running Locally

```bash
# Clone the repo
git clone https://github.com/sathya16301/edupath.git
cd edupath

# Install dependencies
pip install django pillow

# Run migrations
python manage.py migrate

# Start server
python manage.py runserver
```

Then open `http://127.0.0.1:8000` in your browser!!

---

## 👩‍💻 Built By

**Sathya** — BCA Student  
🔗 [GitHub](https://github.com/sathya16301)
