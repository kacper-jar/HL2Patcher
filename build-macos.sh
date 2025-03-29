#!/bin/bash

if [ -d "build" ]; then
    echo "Existing 'build' folder found. Deleting..."
    rm -rf build
    echo "'build' folder deleted."
fi

if [ ! -d ".venv" ]; then
    echo "Virtual environment not found. Creating one..."
    python3 -m venv .venv

    if [ ! -d ".venv" ]; then
        echo "Failed to create the virtual environment. Exiting."
        exit 1
    fi

    echo "Activating virtual environment and installing dependencies..."
    source .venv/bin/activate
    pip install -r requirements.txt

    if [ $? -ne 0 ]; then
        echo "Failed to install dependencies. Exiting."
        exit 1
    fi
fi

source .venv/bin/activate

flet build macos

echo "Build completed."
