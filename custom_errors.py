from fastapi import FastAPI, Request, status, HTTPException
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from pydantic import BaseModel, EmailStr

app = FastAPI()


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    errors = []

    for error in exc.errors():
        breakpoint()
        if error["type"] == "value_error" and error["loc"][1] == "email":
            errors.append("Sorry, you provided an invalid email.")
        elif error["type"] == "missing" and error["loc"][1] == "phoneNum":
            errors.append("Phone number is required if accepted phone call is true.")

    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, content={"errors": errors}
    )


class User(BaseModel):
    email: EmailStr
    phoneNum: str
    callAccepted: bool


@app.post("/user/")
async def create_user(user: User):
    return user


# input
# {
#   "email": "invalidemail.com",
#   "callAccepted": true
# }

# output
# {
#   "errors": [
#     "Sorry, you provided an invalid email.",
#     "Phone number is required if accepted phone call is true."
#   ]
# }
