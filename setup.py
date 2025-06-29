#!/usr/bin/env python3
"""
Setup script for Advanced rPPG Application
"""

from setuptools import setup, find_packages
import os

# Read README file
def read_readme():
    with open("README.md", "r", encoding="utf-8") as fh:
        return fh.read()

# Read requirements
def read_requirements():
    with open("requirements.txt", "r", encoding="utf-8") as fh:
        return [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="advanced-rppg",
    version="1.0.0",
    author="Sherin Joseph Roy",
    author_email="sherin.joseph2217@gmail.com",
    description="Advanced Remote Photoplethysmography Application with real-time heart rate and HRV estimation",
    long_description=read_readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/sherinjoseph/advanced-rppg",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Science/Research",
        "Intended Audience :: Healthcare Industry",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Scientific/Engineering :: Medical Science Apps.",
        "Topic :: Scientific/Engineering :: Image Processing",
        "Topic :: Multimedia :: Video",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
    python_requires=">=3.8",
    install_requires=read_requirements(),
    extras_require={
        "dev": [
            "pytest>=6.0",
            "pytest-cov>=2.0",
            "black>=21.0",
            "flake8>=3.8",
            "mypy>=0.800",
        ],
        "docs": [
            "sphinx>=4.0",
            "sphinx-rtd-theme>=1.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "rppg-app=advanced_rppg.main:main",
        ],
    },
    include_package_data=True,
    package_data={
        "advanced_rppg": ["data/*", "clips/*"],
    },
    keywords="rppg, photoplethysmography, heart-rate, computer-vision, medical, health, hrv, biometrics",
    project_urls={
        "Bug Reports": "https://github.com/sherinjoseph/advanced-rppg/issues",
        "Source": "https://github.com/sherinjoseph/advanced-rppg",
        "Documentation": "https://advanced-rppg.readthedocs.io/",
    },
) 