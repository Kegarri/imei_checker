import requests
from fastapi import HTTPException
import os
import json

IMEICHECK_API_TOKEN = "cAbgd8isTdX4MtMcSzlg1iiyvQlyVP0cTDthQLQfb4ac80c0"

def check_imei_imeicheck(imei: str) -> dict:
    """
    Функция для запроса информации об IMEI с imeicheck.net.
    """
    url = "https://api.imeicheck.net/v1/checks"
    headers = {
        'Authorization': 'Bearer ' + IMEICHECK_API_TOKEN,
        'Content-Type': 'application/json'
    }
    body = json.dumps({
        'Content-Type': 'application/json',
        "deviceId": imei,
        "serviceId": 12
    })
    print(f"Запрос JSON: {body}") # <-- добавляем отладку
    try:
        response = requests.post(url, headers=headers, data=body)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Ошибка при запросе к imeicheck.net: {e}")
        raise HTTPException(status_code=500, detail="Ошибка внешнего API.")
