#!/usr/bin/env bash

source /quantium-starter-repo-main/venv/Scripts/activate

pytest /quantium-starter-repo-main/data/test_app_callbacks.py

if [ $? -eq 0 ]; then
  exit 0

  else
    exit 1

fi