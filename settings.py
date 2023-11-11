from pydantic_settings import SettingsConfigDict, BaseSettings


class Settings(BaseSettings):
    openai_api_key: str

    model_config = SettingsConfigDict(env_file=".env")
