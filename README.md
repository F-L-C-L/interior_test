## Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/F-L-C-L/Interior_test
```
```
cd Interior_test
```

Установить и активировать виртуальное окружение:

```
python -m venv venv
```
Для Windows:
```
source venv/Scripts/activate
```
Для Mac/Linux:
```
source venv/bin/activate
```

Установка зависимостей:

```
pip install -r requirements.txt
```

```
playwright install
```

Запустить тест:

```
pytest test_2rdTask.py -v
```
