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

## Testing

Test the API with curl:
```bash
curl -X POST http://localhost:8080/api/ \
  -H "Content-Type: application/json" \
  -d '{"question": "If a student scores 10/10 on GA4 as well as a bonus, how would it appear on the dashboard?"}'
```

## Deployment

### Vercel - https://tds-project-git-main-soha-farhanas-projects.vercel.app


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
# TDS-project

