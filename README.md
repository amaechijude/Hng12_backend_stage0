# HNG12 Stage 0 Backend Task - Public API

## Description
This is a simple public API developed for the HNG12 Stage 0 backend task. The API returns the following details in JSON format:
- My registered email address on the HNG12 Slack workspace.
- The current datetime in ISO 8601 format (UTC).
- The GitHub repository URL of this project.

## Technology Stack
- **Backend:** Django & Django REST Framework
- **Hosting:** [Your chosen hosting platform]
- **Version Control:** GitHub

## API Endpoint

### **Base URL**
https://your-deployed-api.com/


### **GET Request**
#### Endpoint: `/`

**Response Format (`200 OK`)**
```json
{
  "email": "your-email@example.com",
  "current_datetime": "2025-01-30T09:30:00Z",
  "github_url": "https://github.com/amaechijude/Hng12_backend_stage0"
}
```

## Running Locall

### Clone the Repositor
```bash
git clone https://github.com/amaechijude/Hng12_backend_stage0
cd Hng12_backend_stage0
```

- Ensure you have Python installed
- Activate a virtual environment with uv

```bash
uv venv venv
source venv/bin/activate
```

- Install the required dependencies using uv
```bash
uv pip sync requirements.txt
```
### Run developement Server
```bash
python manage.py runserver
```
## Visit the development Server
```url
http://127.0.0.1:8000/
```
## Hire experienced python developers that are verified by HNG [here](https://hng.tech/hire/python-developers) 
