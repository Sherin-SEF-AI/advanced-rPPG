#!/usr/bin/env python3
"""
Build script for Advanced rPPG PyPI package
"""

import os
import sys
import subprocess
import shutil
from pathlib import Path

def run_command(command, description):
    """Run a command and handle errors."""
    print(f"\n{description}...")
    print(f"Running: {command}")
    
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print("✓ Success!")
        if result.stdout:
            print(result.stdout)
        return True
    except subprocess.CalledProcessError as e:
        print(f"✗ Error: {e}")
        if e.stdout:
            print("STDOUT:", e.stdout)
        if e.stderr:
            print("STDERR:", e.stderr)
        return False

def clean_build():
    """Clean previous build artifacts."""
    print("\n🧹 Cleaning previous build artifacts...")
    
    dirs_to_clean = ["build", "dist", "*.egg-info"]
    for pattern in dirs_to_clean:
        for path in Path(".").glob(pattern):
            if path.is_dir():
                shutil.rmtree(path)
                print(f"Removed: {path}")
            elif path.is_file():
                path.unlink()
                print(f"Removed: {path}")

def build_package():
    """Build the package."""
    return run_command(
        "python -m build",
        "🔨 Building package"
    )

def check_package():
    """Check the built package."""
    return run_command(
        "python -m twine check dist/*",
        "✅ Checking package"
    )

def upload_to_testpypi():
    """Upload to TestPyPI."""
    print("\n📤 Uploading to TestPyPI...")
    print("You'll need to enter your TestPyPI credentials.")
    return run_command(
        "python -m twine upload --repository testpypi dist/*",
        "Uploading to TestPyPI"
    )

def upload_to_pypi():
    """Upload to PyPI."""
    print("\n📤 Uploading to PyPI...")
    print("You'll need to enter your PyPI credentials.")
    return run_command(
        "python -m twine upload dist/*",
        "Uploading to PyPI"
    )

def install_dev_dependencies():
    """Install development dependencies."""
    return run_command(
        "pip install build twine",
        "📦 Installing build dependencies"
    )

def main():
    """Main build process."""
    print("🚀 Advanced rPPG Package Builder")
    print("=" * 40)
    
    # Check if we're in the right directory
    if not os.path.exists("pyproject.toml"):
        print("❌ Error: pyproject.toml not found. Please run this script from the project root.")
        sys.exit(1)
    
    # Install dependencies
    if not install_dev_dependencies():
        print("❌ Failed to install build dependencies")
        sys.exit(1)
    
    # Clean previous builds
    clean_build()
    
    # Build package
    if not build_package():
        print("❌ Failed to build package")
        sys.exit(1)
    
    # Check package
    if not check_package():
        print("❌ Package check failed")
        sys.exit(1)
    
    print("\n🎉 Package built successfully!")
    print("\nNext steps:")
    print("1. Test the package: pip install --index-url https://test.pypi.org/simple/ advanced-rppg")
    print("2. Upload to TestPyPI: python build_package.py --test")
    print("3. Upload to PyPI: python build_package.py --upload")
    
    # Handle command line arguments
    if len(sys.argv) > 1:
        if sys.argv[1] == "--test":
            upload_to_testpypi()
        elif sys.argv[1] == "--upload":
            upload_to_pypi()
        elif sys.argv[1] == "--help":
            print("\nUsage:")
            print("  python build_package.py          # Build package only")
            print("  python build_package.py --test   # Build and upload to TestPyPI")
            print("  python build_package.py --upload # Build and upload to PyPI")
            print("  python build_package.py --help   # Show this help")

if __name__ == "__main__":
    main() 