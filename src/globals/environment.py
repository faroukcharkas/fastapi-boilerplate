# builtin

# external
from pydantic_settings import BaseSettings

# internal


class Environment(BaseSettings):
    MY_API_KEY: str  # Your .env should be on the same level as the app.py and should match this file 1:1
