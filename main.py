from fastapi import FastAPI
from app.router.account_router import router as account_router
from app.router.agent_router import router as agent_router

app = FastAPI()

app.include_router(account_router)
app.include_router(agent_router, prefix="/agent")