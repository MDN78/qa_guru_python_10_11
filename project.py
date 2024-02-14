import dotenv
from pydantic_settings import BaseSettings
from typing import Literal
from utils import path


class Config(BaseSettings):
    context: Literal['example', 'test'] = 'test'
    driver_name: str = 'firefox'
    base_url: str = 'https://demoqa.com'
    hold_driver_at_exit: bool = False
    window_width: int = 1920
    window_height: int = 1080
    timeout: float = 4.0


# dotenv.load_dotenv()
# config = Config(_env_file='.env')
# config = Config(_env_file=path.relative_from_root('.env'))
config = Config(_env_file=path.relative_from_root(f'.env.{Config().context}'))

# как вариант использовать спец библиотеку dotenv для поиска пути
# dotenv.find_dotenv()
