# SGM Keep Alive

[![Keep Backend Alive](https://github.com/HackerKing5128/sgm-keep-alive/actions/workflows/keep-me-alive.yml/badge.svg)](https://github.com/HackerKing5128/sgm-keep-alive/actions)

---

This GitHub Actions workflow keeps the [Smart Grievance Management](https://github.com/HackerKing5128/smart-grievance-management)'s backend alive on [Render](https://render.com)'s free tier, which otherwise shuts down due to 15 minutes of inactivity.

### 🔧 How It Works

Every 5 minutes, a GitHub Actions workflow runs and pings the backend URL to simulate activity, preventing it from sleeping.


### ⚙️ Setup Steps

1. Clone this repository or copy the files into your own repo.
2. Edit `main.py` if your backend URL ever changes.
3. Push to GitHub.
4. Go to the **Actions** tab and manually run the workflow once.
5. GitHub will continue to ping your backend every 5 minutes using a cron job.

---
### ⚠️ Notes

- GitHub Actions may occasionally delay execution slightly (up to 5–10 minutes).
- This method is free and does not require any third-party uptime service.

---
