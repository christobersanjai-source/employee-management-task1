from pydantic_settings import BaseSettings, SettingsConfigDict
class Settings(BaseSettings):
    app_name: str = "Employee Management API"
    database_url: str = "postgresql://postgres:postgres@db:5432/employee_db"
    secret_key: str = "local-development-only-change-me"
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")
settings = Settings()
