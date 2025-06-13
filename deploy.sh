#!/bin/bash
# Deployment script for TDS Virtual TA

echo "🚀 TDS Virtual TA Deployment Guide"
echo "=================================="

echo "📁 Current project structure:"
ls -la

echo ""
echo "🔧 Testing local setup..."
python3 -c "import flask; print('✅ Flask is available')" 2>/dev/null || echo "❌ Flask not installed. Run: pip install -r requirements.txt"

echo ""
echo "📊 Data files status:"
if [ -f "CourseContentData.jsonl" ]; then
    echo "✅ CourseContentData.jsonl found"
else
    echo "❌ CourseContentData.jsonl missing"
fi

if [ -f "DicourseData.jsonl" ]; then
    echo "✅ DicourseData.jsonl found"  
else
    echo "❌ DicourseData.jsonl missing"
fi

echo ""
echo "🌐 Deployment Options:"
echo "1. Vercel (Recommended):"
echo "   - Go to https://vercel.com"
echo "   - Connect your GitHub repository" 
echo "   - Auto-deploy on git push"
echo ""
echo "2. Railway:"
echo "   - Go to https://railway.app"
echo "   - Connect your GitHub repository"
echo "   - Auto-deploy with zero config"
echo ""
echo "3. Render:"
echo "   - Go to https://render.com"
echo "   - Connect your GitHub repository"
echo "   - Choose 'Web Service'"
echo ""

echo "💡 Next steps:"
echo "1. Initialize git: git init"
echo "2. Add files: git add ."
echo "3. Commit: git commit -m 'Initial TDS Virtual TA'"
echo "4. Create GitHub repo and push"
echo "5. Deploy using one of the platforms above"
