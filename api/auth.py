from fastapi import HTTPException, Header
import os
API_TOKEN = os.getenv("API_TOKEN")

def api_token_auth(token: str = Header(..., alias="token")):
    if token != API_TOKEN:
        raise HTTPException(status_code=401, detail="Неверный токен авторизации.")
