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

NAME="HL2Patcher"
COPYRIGHT="Copyright (c) 2025 Kacper Jarosławski"
DESC="HL2Patcher makes Half-Life 2 playable on modern ARM Macs that only support 64-bit apps. Its goal is to simplify the process into an easy-to-use app, so anyone can enjoy the game again without hassle."
BUILD="1.0.1"

flet build --project "$NAME" --product "$NAME" --copyright "$COPYRIGHT" --description "$DESC" --build-version "$BUILD" macos

echo "Build completed."
