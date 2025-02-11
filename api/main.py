from fastapi import FastAPI, Depends, HTTPException
from api.auth import api_token_auth
from api.models import IMEIRequest
from api.utils import check_imei_imeicheck

app = FastAPI(title="IMEI Checker API", description="API для проверки IMEI")

@app.post("/api/check-imei")
def check_imei_endpoint(req: IMEIRequest, token: str = Depends(api_token_auth)):
    """
    API endpoint для проверки IMEI.
    """
    try:
        imei_info = check_imei_imeicheck(req.imei)
        return imei_info
    except HTTPException as e:
        raise e

if __name__ == "__main__":
    import uvicorn
    from dotenv import load_dotenv
    load_dotenv()
    uvicorn.run(app, host="0.0.0.0", port=8000)
