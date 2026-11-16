# Tiffany M. Mui
# Module 8 Assignment - NASA NeoWs API Handling Module
# CSCI-3025: Python Programming
# Purpose: Functions to handle interacting with the NeoWs API
# Dependencies: 
#   Standard: sys, os, pathlib, copy, datetime
#   External: dotenv, requests 
#   Custom: TBD


import sys
import os
from pathlib import Path
from dotenv import load_dotenv


def load_env(): # Copied from Module 7
    """Loads API configuration from environment variables file
    
    Args:
        None
    
    Returns:
        api_key: The API key stored as environment variable
    """
    load_dotenv(dotenv_path=Path(__file__).resolve().parent / ".env")
    api_key = os.getenv("API_KEY")
    return api_key
