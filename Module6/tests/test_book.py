# Tiffany M. Mui
# Module 6 Assignment - Testing
# CSCI-3025: Python Programming
# Purpose: Tests for Mui_Book.py module
# Run with: pytest tests/test_book.py -v


from datetime import datetime
import sys
from pathlib import Path


#Adds parent directory to front of module search path
sys.path.insert(0, str(Path(__file__).parent.parent))
from Mui_Book import Book


