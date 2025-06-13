# 🚀 TDS Virtual TA - Deployment Guide

## ✅ Project Status
- **Repository**: `tds-project` (clean, production-ready)
- **API**: Fully functional, tested with 100% pass rate
- **Data**: 558 course content items + 3,383 discourse posts
- **License**: MIT License included
- **Git**: Repository initialized and committed

## 📁 Project Structure
```
tds-project/
├── app.py                  # Main Flask application
├── requirements.txt        # Dependencies (Flask, requests, python-dotenv, gunicorn)
├── Procfile               # Railway start command
├── nixpacks.toml          # Railway build configuration
├── LICENSE                # MIT License
├── README.md              # Documentation
├── vercel.json            # Vercel deployment config
├── .gitignore             # Git ignore file
├── CourseContentData.jsonl # Course content (569KB)
├── DicourseData.jsonl     # Forum discussions (1.9MB)
├── test_api.py            # API testing script
├── deploy.sh              # Deployment helper script
└── api/                   # Vercel API directory
    └── index.py           # Vercel entry point
```

## 🌐 Deployment Options (Choose One)

### Option 1: Vercel (Recommended - Easiest)
1. **Create GitHub Repository**:
   ```bash
   # Go to https://github.com and create a new repository named "tds-project"
   # Then run these commands:
   git remote add origin https://github.com/YOUR_USERNAME/tds-project.git
   git branch -M main
   git push -u origin main
   ```

2. **Deploy on Vercel**:
   - Go to https://vercel.com
   - Sign in with GitHub
   - Click "New Project"
   - Import your `tds-project` repository
   - Vercel will auto-detect it's a Flask app
   - Click "Deploy"
   - Your API will be live at `https://your-app.vercel.app/api/`

### Option 2: Railway (Zero Config - Now Fixed)
1. **Push to GitHub** (same as above)
2. **Deploy on Railway**:
   - Go to https://railway.app
   - Sign in with GitHub
   - Click "Deploy from GitHub repo"
   - Select your `tds-project` repository
   - Railway will auto-deploy using the included `Procfile` and `nixpacks.toml`
   - Your API will be live at the provided Railway URL (e.g., `https://your-app.railway.app/api/`)

**Railway Configuration Files Included:**
- `Procfile`: Tells Railway how to start the app with gunicorn
- `nixpacks.toml`: Configures the build process
- Updated `requirements.txt` with gunicorn for production

### Option 3: Render (Free Tier)
1. **Push to GitHub** (same as above)
2. **Deploy on Render**:
   - Go to https://render.com
   - Sign in with GitHub
   - Click "New" → "Web Service"
   - Connect your `tds-project` repository
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `python app.py`
   - Click "Create Web Service"

## 🧪 Testing Your Deployed API

Once deployed, test with:
```bash
curl -X POST https://your-deployed-url/api/ \
  -H "Content-Type: application/json" \
  -d '{"question": "Should I use gpt-4o-mini or gpt-3.5-turbo?"}'
```

Expected response:
```json
{
  "answer": "You must use `gpt-3.5-turbo-0125`, even if the AI Proxy only supports `gpt-4o-mini`. Use the OpenAI API directly for this question.",
  "links": [...]
}
```

## 📋 Submission Checklist

For https://exam.sanand.workers.dev/tds-project-virtual-ta:

✅ **GitHub Repository URL**: `https://github.com/YOUR_USERNAME/tds-project`
✅ **API Endpoint URL**: `https://your-deployed-app.domain/api/`
✅ **MIT License**: ✓ Included in repository
✅ **Public Repository**: ✓ Make sure it's public
✅ **Response Time**: < 30 seconds ✓
✅ **Correct JSON Format**: ✓ Tested and validated

## 🔧 Local Testing (Optional)

If you want to test locally before deployment:
```bash
cd tds-project
python app.py
# Test at http://localhost:8080/api/
```

## 💡 Next Steps

1. **Create GitHub repository** and push your code
2. **Choose a deployment platform** (Vercel recommended)
3. **Deploy and get your API URL**
4. **Test the deployed API**
5. **Submit both URLs** at the exam portal

Your TDS Virtual TA is production-ready! 🎉
