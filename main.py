import uvicorn
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi import Body

app = FastAPI()


@app.post("/pre-signup")
async def pre_signup(payload: dict = Body(default={})):
    return JSONResponse(
        status_code=200,
        content={
            "decision": "ALLOW",
            "error": {
                "code": "503",
                "message": "Signup not allowed"
            }
        }
    )


@app.post("/pre-session-creation")
async def pre_session_creation(payload: dict = Body(default={})):
    return JSONResponse(
        status_code=200,
        content={
            "decision": "ALLOW",
            "error": {
                "code": "503",
                "message": "Session creation not allowed"
            }
        }
    )


@app.post("/pre-user-invitation")
async def pre_user_invitation(payload: dict = Body(default={})):
    return JSONResponse(
        status_code=200,
        content={
            "decision": "ALLOW",
            "error": {
                "code": "503",
                "message": "User invitation not allowed"
            }
        }
    )


@app.post("/pre-m2m-token-creation")
async def pre_m2m_token_creation(payload: dict = Body(default={})):
    return JSONResponse(
        status_code=200,
        content={
            "decision": "ALLOW",
            "error": {
                "code": "503",
                "message": "M2M token creation not allowed"
            }
        }
    )

@app.post("/org-decision/pre-signup")
async def org_decision_pre_signup(payload: dict = Body(default={})):
    return JSONResponse(
        status_code=200,
        content={
            "decision": "ALLOW",
            "error": {
                "code": "200",
                "message": "Signup was allowed, and the user was added to the organization.”"
            },
            "response": {
                "create_organization_membership": {
                    "external_organization_id":"ext_0987654321",
                    "roles": [
                        "admin",
                        "member"
                    ]
                }
            }
        }
    )

@app.get("/.well-known/oauth/client-metadata.json")
async def mcp_cimd():
    return JSONResponse(
        status_code=200,
        content={
            "client_id": "https://skinterceptormockserver-production.up.railway.app/.well-known/oauth/client-metadata.json",
            "client_name": "Scalekit Automation CIMD",
            "client_uri": "https://skinterceptormockserver-production.up.railway.app",
            "redirect_uris": [
                "https://postman-echo.com/get",
                "http://127.0.0.1:6274/oauth/callback",
                "http://127.0.0.1:6274/callback",
                "http://127.0.0.1:6274/oauth/callback/debug",
                "https://oauth.pstmn.io/v1/callback"
            ],
            "grant_types": [
                "authorization_code",
                "refresh_token",
                "urn:ietf:params:oauth:grant-type:device_code"
            ],
            "response_types": [
                "code"
            ],
            "token_endpoint_auth_method": "none",
            "application_type": "native"
        }
    )

@app.get("/render/.well-known/oauth/client-metadata.json")
async def mcp_cimd_using_render():
    return JSONResponse(
        status_code=200,
        content={
            "client_id": "https://sk-interceptor-mock-server-7ntk.onrender.com/render/.well-known/oauth/client-metadata.json",
            "client_name": "Scalekit Automation CIMD",
            "client_uri": "https://sk-interceptor-mock-server-7ntk.onrender.com",
            "redirect_uris": [
                "https://postman-echo.com/get",
                "http://127.0.0.1:6274/oauth/callback",
                "http://127.0.0.1:6274/callback",
                "http://127.0.0.1:6274/oauth/callback/debug",
                "https://oauth.pstmn.io/v1/callback"
            ],
            "grant_types": [
                "authorization_code",
                "refresh_token",
                "urn:ietf:params:oauth:grant-type:device_code"
            ],
            "response_types": [
                "code"
            ],
            "token_endpoint_auth_method": "none",
            "application_type": "native"
        }
    )

@app.get("/health")
def health():
    return {"status": "ok"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
