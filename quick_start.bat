@echo off
@chcp 65001 >nul
:: Проверка наличия файла requirements.txt
if not exist "requirements.txt" (
    echo Файл requirements.txt не найден.
    exit /b 1
)

:: Проверка наличия папки .venv
if not exist ".venv" (
    echo Виртуальная среда .venv не найдена.
    echo Создаю виртуальную среду...
    python -m venv .venv
    if errorlevel 1 (
        echo Не удалось создать виртуальную среду.
        exit /b 1
    )
)

:: Активация виртуальной среды
echo Активация виртуальной среды .venv...
call .venv\Scripts\activate.bat

:: Обновление pip
echo Обновление pip...
python -m pip install --upgrade pip
if errorlevel 1 (
    echo Не удалось обновить pip.
    exit /b 1
)

:: Установка зависимостей
echo Установка зависимостей из requirements.txt...
pip install -r requirements.txt
if errorlevel 1 (
    echo Не удалось установить зависимости.
    exit /b 1
)

:: Запуск uvicorn
echo Запуск uvicorn...
uvicorn app.main:app --host 0.0.0.0 --port 8080 --reload
if errorlevel 1 (
    echo Не удалось запустить приложение uvicorn.
    exit /b 1
)