#!/bin/bash

# Check if Python is installed
if ! command -v python3 &> /dev/null
then
    echo "Python3 could not be found. Please install python3."
    exit
fi

# Create venv if not exists
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
fi

# Activate venv
source venv/bin/activate

# Install requirements
pip install -r requirements.txt

# Download Spacy model
python -m spacy download en_core_web_sm

# Setup Database
# Setup Database
python App/Database_Scripts/create_db.py

# Run App
echo "Starting Application..."
cd App
streamlit run App.py
