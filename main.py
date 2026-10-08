from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from mcp_srv_ext import mcp as mcp_srv_ext
from mcp_server import mcp as mcp_server
import contextlib

# @contextlib.asynccontextmanager
# async def lifespan(app: FastAPI):
#     async with mcp_server.session_manager.run():
#         yield

@contextlib.asynccontextmanager
async def lifespan(app: FastAPI):
    async with contextlib.AsyncExitStack() as stack:
        await stack.enter_async_context(mcp_srv_ext.session_manager.run())
        await stack.enter_async_context(mcp_server.session_manager.run())
        yield

app = FastAPI(lifespan=lifespan)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.mount("/demo", mcp_server.streamable_http_app(), name="demo")
app.mount("/demoext", mcp_srv_ext.streamable_http_app(), name="demo_ext")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, log_level="debug")