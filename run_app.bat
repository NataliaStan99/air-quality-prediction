@echo off
setlocal ENABLEDELAYEDEXPANSION

REM --- Katalog aplikacji (folder, w którym leży ten BAT) ---
set "APP_DIR=%~dp0"
cd /d "%APP_DIR%"

REM --- Tworzymy prywatne środowisko w katalogu projektu (nie ruszamy systemu wykładowcy) ---
set "VENV_DIR=%APP_DIR%.runenv"

REM --- Sprawdź czy Python jest osiągalny jako 'py' (Windows launcher) ---
where py >nul 2>nul
if %ERRORLEVEL% neq 0 (
  echo [ERROR] Nie znaleziono interpretera 'py'. Zainstaluj Python 3.10+ i uruchom ponownie.
  pause
  exit /b 1
)

REM --- Utwórz venv, jeśli nie istnieje ---
if not exist "%VENV_DIR%\Scripts\python.exe" (
  echo Tworzenie srodowiska .runenv ...
  py -3 -m venv "%VENV_DIR%"
  if %ERRORLEVEL% neq 0 (
    echo [ERROR] Nie udalo sie utworzyc srodowiska wirtualnego.
    pause
    exit /b 1
  )
  echo Aktualizacja pip...
  "%VENV_DIR%\Scripts\python.exe" -m pip install --upgrade pip
  echo Instalacja zaleznosci...
  "%VENV_DIR%\Scripts\python.exe" -m pip install -r requirements.txt
)

REM --- Doinstaluj brakujace zaleznosci w razie czego (np. gdyby pip przerwal) ---
"%VENV_DIR%\Scripts\python.exe" -c "import streamlit,requests,pandas,streamlit_autorefresh" 1>nul 2>nul
if %ERRORLEVEL% neq 0 (
  echo Upewniam sie, ze wszystkie paczki sa zainstalowane...
  "%VENV_DIR%\Scripts\python.exe" -m pip install -r requirements.txt
)

REM --- Uruchom aplikacje Streamlit (port wybieramy automatycznie, zeby nie bylo kolizji) ---
echo Start aplikacji...
"%VENV_DIR%\Scripts\python.exe" -m streamlit run app.py --server.port 8501 --server.headless false

echo.
echo [INFO] Jesli przegladarka nie otworzyla sie automatycznie, skopiuj adres z okna powyzej (http://localhost:85xx)
pause
endlocal
