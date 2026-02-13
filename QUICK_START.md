
# 🚀 AI Resume Analyzer - Setup & Run Guide

**Welcome!** This project has been simplified for easy setup.

## ⚡ Quick Start (Windows)
1.  **Install Python:** Download and install [Python 3.11+](https://www.python.org/downloads/) (Check "Add Python to PATH" during installation).
2.  **Install MySQL:** Download and install [MySQL Server](https://dev.mysql.com/downloads/installer/).
    *   Set Root Password: `Vivek@807` (or edit `App/App.py` and `App/Database_Scripts/create_db.py` if different).
3.  **Run the Project:**
    *   Find the file `run_app.bat` in this folder.
    *   **Double-click** it.
    *   Wait for automatic installation. The app will open in your browser!

## 🐧 Quick Start (Linux / Mac)
1.  Open Terminal.
2.  Run:
    ```bash
    bash run_app.sh
    ```

## 🛠 Troubleshooting
*   **Database Error:** Ensure MySQL is running. The script tries to create the `cv` database automatically.
*   **Python Version:** If you see build errors, ensure you are using a modern Python version (3.12+ recommended).
*   **Missing Logo:** If the app says `FileNotFoundError`, ensure you run it from the root directory using the script.

## 📂 Project Structure
*   `App/`: Main application code.
*   `pyresparser/`: Resume parsing logic (patched for modern Python).
*   `run_app.bat`: One-click runner for Windows.
*   `requirements.txt`: Python dependencies.
