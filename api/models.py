from pydantic import BaseModel, validator

class IMEIRequest(BaseModel):
    imei: str

    @validator("imei")
    def validate_imei(cls, imei):
        if not imei.isdigit() or len(imei) not in (15, 17):
            raise ValueError("IMEI должен состоять из 15 или 17 цифр.")
        return imei
