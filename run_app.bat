@echo off
SETLOCAL

:: Check if Python is installed
python --version >nul 2>&1
IF %ERRORLEVEL% NEQ 0 (
    echo Python is not installed. Please install Python 3.9+ and add to PATH.
    pause
    exit /b
)

:: Create Virtual Environment if not exists
IF NOT EXIST "venv" (
    echo Creating virtual environment...
    python -m venv venv
)

:: Activate Virtual Environment
call venv\Scripts\activate

:: Check dependencies
pip install -r requirements.txt

:: Download Spacy Model
python -m spacy download en_core_web_sm

:: Setup Database (if not exists)
python create_db.py

:: Run Application
echo Starting Application...
cd App
streamlit run App.py
pause
