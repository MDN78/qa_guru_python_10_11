from pydantic_settings import BaseSettings


class Config(BaseSettings):
    driver_name: str = 'chrome'
    base_url: str = 'https://demoqa.com'
    hold_driver_at_exit: bool = False
    window_width: int = 1920
    window_height: int = 1080
    timeout: float = 4.0


config = Config()
