# builtin
from contextlib import asynccontextmanager

# external
from fastapi import FastAPI

# internal
from src.globals.environment import Environment
from src.modules.example.module import ExampleModule


def setup_environment(app: FastAPI):
    environment: Environment = Environment()
    app.state.environment = environment


def setup_modules(app: FastAPI):
    example_module: ExampleModule = ExampleModule(app.state.environment)
    app.state.example_module = example_module


@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Starting up")
    await setup_environment(app)
    await setup_modules(app)
    yield
    print("Shutting down")


app: FastAPI = FastAPI(lifespan=lifespan)


@app.get("/")
async def root():
    return {"message": "Hello World"}
