import os
import uvicorn
from apps.create_app import create_app

# Constant
port = os.environ.get("PORT", 7860)


app = create_app()


# Base route
@app.get("/")
def index():
    return {"message": "Hello, World"}


# Start the server
if __name__ == "__main__":
    print(f"✨ Listening on port {port}")
    uvicorn.run(app, port=port)
