# Stage 0 - Backend Task (HNG)

## 🚀 Task Description
This project is a simple API endpoint that returns:
- My **name**
- My **email**
- My **programming language/framework**
- The **current timestamp** (in ISO 8601 format)
- A **random cat fact** fetched dynamically from [Cat Fact API](https://catfact.ninja/)

## 🧩 Endpoint
**URL:** [https://b33e8cf4-5faa-4bb6-84e1-40922fedeee3-00-2on6ataon6d6c.riker.replit.dev/me/](https://b33e8cf4-5faa-4bb6-84e1-40922fedeee3-00-2on6ataon6d6c.riker.replit.dev/me/)

### Example JSON Response
```json
{
  "status": "success",
  "user": {
    "email": "omotayoisrael24@gmail.com",
    "name": "Omotayo Israel",
    "stack": "Python/Django"
  },
  "timestamp": "2025-10-19T13:45:12Z",
  "fact": "Cats sleep 70% of their lives."
}
