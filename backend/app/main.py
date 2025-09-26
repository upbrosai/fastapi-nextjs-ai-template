import sentry_sdk
from fastapi import FastAPI
from fastapi.routing import APIRoute
from starlette.middleware.cors import CORSMiddleware

from app.api.main import api_router
from app.core.config import settings


def custom_generate_unique_id(route: APIRoute) -> str:
    return f"{route.tags[0]}-{route.name}"

# Setup Remote Debugging with PyCharm, when in development environment, especially for Docker.
# PyCharm Python Debugger Server: https://www.jetbrains.com/help/pycharm/remote-debugging-with-product.html
if settings.ENVIRONMENT == "local" and settings.PYCHARM_DEBUG_ENABLED:
    try:
        import pydevd_pycharm
        print(f"PyCharm debug server: {settings.PYCHARM_DEBUG_HOST}:{settings.PYCHARM_DEBUG_PORT}")
        pydevd_pycharm.settrace(
            settings.PYCHARM_DEBUG_HOST,
            port=settings.PYCHARM_DEBUG_PORT,
            stdout_to_server=True,
            stderr_to_server=True,
        )
    except ImportError:
        print("pydevd-pycharm not available, add the package by 'uv sync --dev'")
    except Exception as e:
        print(f"pydevd-pycharm setup failed: {e}")

if settings.SENTRY_DSN and settings.ENVIRONMENT != "local":
    sentry_sdk.init(dsn=str(settings.SENTRY_DSN), enable_tracing=True)

app = FastAPI(
    title=settings.PROJECT_NAME,
    openapi_url=f"{settings.API_V1_STR}/openapi.json",
    generate_unique_id_function=custom_generate_unique_id,
)

# Set all CORS enabled origins
if settings.all_cors_origins:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.all_cors_origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

app.include_router(api_router, prefix=settings.API_V1_STR)
