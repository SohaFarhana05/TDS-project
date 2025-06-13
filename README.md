# TDS Virtual Teaching Assistant

A virtual Teaching Assistant API that automatically answers student questions based on Tools in Data Science course content and Discourse forum discussions.

## Features

- 🤖 **Intelligent Q&A**: Answers student questions using course content and discourse posts
- 📚 **Rich Knowledge Base**: Integrates real TDS course content and forum discussions  
- 🔗 **Contextual Links**: Provides relevant links with meaningful descriptions
- ⚡ **Fast Response**: Returns answers within 30 seconds
- 🎯 **Accurate Answers**: Handles specific questions about assignments, tools, and course topics

## API Usage

### Endpoint
```
POST /api/
```

### Request Format
```json
{
  "question": "Should I use gpt-4o-mini which AI proxy supports, or gpt3.5 turbo?",
  "image": "base64_encoded_image_data (optional)"
}
```

### Response Format
```json
{
  "answer": "You must use `gpt-3.5-turbo-0125`, even if the AI Proxy only supports `gpt-4o-mini`. Use the OpenAI API directly for this question.",
  "links": [
    {
      "url": "https://discourse.onlinedegree.iitm.ac.in/t/ga5-question-8-clarification/155939/4",
      "text": "Use the model that's mentioned in the question."
    }
  ]
}
```

## Local Development

1. **Clone the repository**
```bash
git clone <your-repo-url>
cd tds-project
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Add data files**
Place `CourseContentData.jsonl` and `DicourseData.jsonl` in the project root.

4. **Run the application**
```bash
python app.py
```

The API will be available at `http://localhost:8080/api/`

## Testing

Test the API with curl:
```bash
curl -X POST http://localhost:8080/api/ \
  -H "Content-Type: application/json" \
  -d '{"question": "If a student scores 10/10 on GA4 as well as a bonus, how would it appear on the dashboard?"}'
```

## Deployment

### Vercel (Recommended)
1. Connect your GitHub repository to Vercel
2. Vercel will automatically deploy on pushes to main branch
3. Your API will be available at `https://your-app.vercel.app/api/`

### Railway
1. Connect your GitHub repository to Railway
2. Railway will automatically build and deploy
3. Your API will be available at the provided Railway URL

## Data Sources

- **Course Content**: TDS Jan 2025 course materials from https://tds.s-anand.net/#/2025-01/
- **Discourse Posts**: TDS forum discussions from Jan 1, 2025 - Apr 14, 2025

## Project Structure

```
tds-project/
├── app.py              # Main Flask application
├── requirements.txt    # Python dependencies
├── LICENSE            # MIT License
├── README.md          # This file
├── CourseContentData.jsonl  # Course content data
└── DicourseData.jsonl      # Discourse forum data
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
