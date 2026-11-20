# Tiffany M. Mui
# Module 8 Assignment - Testing
# CSCI-3025: Python Programming
# Purpose: Tests for ancillary module
# Run with: pytest tests/test_ancillary.py -v


import sys
from pathlib import Path
from datetime import date
import pytest


#Adds parent directory to front of module search path
sys.path.insert(0, str(Path(__file__).parent.parent))


import Mui_Ancillary as aux