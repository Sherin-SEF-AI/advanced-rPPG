"""
Advanced rPPG Application
=========================

A comprehensive remote Photoplethysmography (rPPG) application for real-time
heart rate and Heart Rate Variability (HRV) estimation using computer vision.

Features:
- Live video processing with webcam support
- File-based video analysis
- Multiple rPPG algorithms (Chrominance, POS, Green Channel)
- Real-time heart rate and HRV estimation
- Signal quality assessment
- Cross-platform GUI with PyQt5
- Face detection using MediaPipe
- Data export and visualization

Author: Sherin Joseph Roy
Email: sherin.joseph2217@gmail.com
License: MIT
"""

__version__ = "1.0.0"
__author__ = "Sherin Joseph Roy"
__email__ = "sherin.joseph2217@gmail.com"
__license__ = "MIT"

from . import rppg_core
from . import gui
from . import utils

__all__ = ["rppg_core", "gui", "utils"] 