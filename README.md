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
python -m venv env
```

```
pip install pytest playwright
```

```
playwright install
```

Запустить тест:

```
pytest test_playwright_title.py -v
```
