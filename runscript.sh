#!/bin/bash
if command -v python3 &> /dev/null
  then python3 src/viper.py
fi
if command -v python &> /dev/null
  then python src/viper.py
fi

