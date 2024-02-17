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
4) Значение конфигурационных настроек можно вынести в отдельный файл `.env`  Возможно нужна библиотека `python-dotenv` 
но не факт
5) Далее в файле куда из `.env` должны подтягиваться переменные указываем вызов `dotenv.load_dotenv()`
6) Как подружить pydantic с .env: - вызываем перед тем как создаем конфиг

```commandline
dotenv.load_dotenv()
config = Config()
```
как другой вариант - передать путь явно в функцию

```commandline
config = Config(_env_file='.env')
```

но, может не сработать если запускать тесты с другого места. Для этого улучим реализацию пути и указания, где этот файл
можно использовать хелпер - создать файл в папке `utils` и там будет код этого хелпера

Это означает - от файла `__init__`  в папке, где лежит этот скрипт поднимаемся вверх раз, второй, и уже в основной директории ищем файл
```commandline
def relative_from_root(path: str):
    from pathlib import Path
    return Path(__file__).parent.parent.joinpath(path).absolute().__str__()


config = Config(_env_file=path.relative_from_root('.env'))
```

### Хранение нескольких файлов `.env`

Принято файлы `.env` в Гит не выкладывать, тк там могут быть конфиденциальные данные - пароли или логины и добавляют его в gitignore

в Гите делают его с доп наименованием `.env.example` и в них отражать то что актуально для определенного типа запуска и не секретно

После этого нужно указывать какой `.env` использовать

```commandline
add import
from typing import Literal

class Config(BaseSettings):
    context: Literal['example', 'test'] = 'test'
    ......
    
config = Config(_env_file=path.relative_from_root(f'.env.{Config().context}'))
    
```

### Запуск с выбором Literal

Команда для bash терминала - `pytest context=example`

Команда для power shell:

```
-> set context=example
-> pytest
```

Командой `echo "context"` можем посмотреть что у нас в переменной
