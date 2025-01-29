from fastapi import FastAPI
from datetime import datetime, timezone

app = FastAPI()


@app.get("/")
def read_root():
    return {
            "email": "amaechijude178@gmail.com",
            "current_datetime": f"{datetime.now(timezone.utc).isoformat()}",
            "github_url": " https://github.com/amaechijude/Hng12_backend_stage0.git"
            }
