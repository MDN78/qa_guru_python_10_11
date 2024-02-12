# Работа с библиотеками os.getenv, pytest options, Pydantic

1) Устанавливаем библиотеку `pydantic` Она позволяет задавать переменные параметров с которыми мы хотим запускать тесты.

[документация pydantic](https://docs.pydantic.dev/latest/concepts/pydantic_settings/)

2) Установить через консоль `pip install pydantic-settings`
3) Далее создаем отдельный класс где будут прописаны конфигурационные настройки и вынести в отдельный конфигурационный файл
например `project.py` прямо в корне проекта:

```commandline
from pydantic_settings import BaseSettings

class Config(BaseSettings):
    driver_name: str = 'chrome'
    base_url: str = 'https://demoqa.com'
    hold_driver_at_exit: bool = False
    window_width: int = 1920
    window_height: int = 1080
    timeout: float = 4.0

config = Config()
```
4) 


