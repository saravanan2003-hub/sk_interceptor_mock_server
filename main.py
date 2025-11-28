import uvicorn
from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()


@app.post("/pre-signup")
async def pre_signup():
    return JSONResponse(
        status_code=200,
        content={
            "decision": "ALLOW",
            "error": {
                "code": 503,
                "message": "Signup not allowed"
            }
        }
    )


@app.post("/pre-session-creation")
async def pre_session_creation():
    return JSONResponse(
        status_code=200,
        content={
            "decision": "ALLOW",
            "error": {
                "code": 503,
                "message": "Session creation not allowed"
            }
        }
    )


@app.post("/pre-user-invitation")
async def pre_user_invitation():
    return JSONResponse(
        status_code=200,
        content={
            "decision": "ALLOW",
            "error": {
                "code": 503,
                "message": "User invitation not allowed"
            }
        }
    )


@app.post("/pre-m2m-token-creation")
async def pre_m2m_token_creation():
    return JSONResponse(
        status_code=200,
        content={
            "decision": "ALLOW",
            "error": {
                "code": 503,
                "message": "M2M token creation not allowed"
            }
        }
    )


# Required for Vercel serverless
handler = Mangum(app)