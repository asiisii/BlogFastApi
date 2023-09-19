from fastapi import FastAPI, Request, status
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from pydantic import BaseModel, EmailStr

app = FastAPI()


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    errors = []

    for error in exc.errors():
        if error["loc"] == ("body", "email"):
            errors.append("Sorry, you provided an invalid email.")

    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, content={"errors": errors}
    )


class User(BaseModel):
    email: EmailStr
    phoneNum: str = None
    callAccepted: bool


@app.post("/user/")
async def create_user(user: User):
    if user.callAccepted and user.phoneNum is None:
        return JSONResponse(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            content={
                "errors": "Phone number is required if accepted phone call is true."
            },
        )
    return user
