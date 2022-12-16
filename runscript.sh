#!/bin/bash
if command -v python3 &> /dev/null
  then 
  source venv/bin/activate
  python3 src/viper.py
  exit
fi
if command -v python &> /dev/null
  then
  source venv/bin/activate
  python src/viper.py
  exit
fi

