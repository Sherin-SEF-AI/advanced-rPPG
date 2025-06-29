# Advanced rPPG

[![PyPI version](https://badge.fury.io/py/advanced-rppg.svg)](https://badge.fury.io/py/advanced-rppg)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)

**Advanced Remote Photoplethysmography (rPPG) Application** - A comprehensive Python package for real-time heart rate and Heart Rate Variability (HRV) estimation using computer vision techniques.

## 🚀 Features

- **Real-time Processing**: Live video analysis with webcam support
- **Multiple Algorithms**: Chrominance, POS, and Green Channel rPPG methods
- **Face Detection**: Advanced face tracking using MediaPipe
- **Signal Quality**: Built-in quality assessment metrics
- **HRV Analysis**: Comprehensive Heart Rate Variability estimation
- **Cross-platform GUI**: Modern PyQt5-based interface
- **Data Export**: Save results in multiple formats
- **Visualization**: Real-time plotting with pyqtgraph

## 📦 Installation

### Quick Install
```bash
pip install advanced-rppg
```

### Install with Development Dependencies
```bash
pip install advanced-rppg[dev]
```

### System Dependencies (Ubuntu/Debian)
```bash
sudo apt-get update
sudo apt-get install -y \
    python3-dev \
    python3-pip \
    libgl1-mesa-glx \
    libglib2.0-0 \
    libsm6 \
    libxext6 \
    libxrender-dev \
    libgomp1 \
    libgthread-2.0-0 \
    libgtk-3-0 \
    libavcodec-dev \
    libavformat-dev \
    libswscale-dev \
    libv4l-dev \
    libxvidcore-dev \
    libx264-dev \
    libjpeg-dev \
    libpng-dev \
    libtiff-dev \
    libatlas-base-dev \
    gfortran \
    libhdf5-dev \
    libhdf5-serial-dev \
    libhdf5-103 \
    libqtgui4 \
    libqtwebkit4 \
    libqt4-test \
    python3-pyqt5
```

### System Dependencies (macOS)
```bash
brew install opencv qt5
```

### System Dependencies (Windows)
- Install Visual Studio Build Tools
- Install Qt5 from the official website

## 🎯 Quick Start

### Command Line Usage
```bash
# Run the application
rppg-app

# Or use Python module
python -m advanced_rppg.main
```

### Python API Usage
```python
from advanced_rppg.rppg_core.face_detector import FaceDetector
from advanced_rppg.rppg_core.signal_processor import SignalProcessor
from advanced_rppg.rppg_core.hrv_analyzer import HRVAnalyzer

# Initialize components
face_detector = FaceDetector()
signal_processor = SignalProcessor()
hrv_analyzer = HRVAnalyzer()

# Process video frames
# ... your processing code here
```

## 🔧 Configuration

The application supports various configuration options:

### Algorithm Selection
- **Chrominance Method**: Best for controlled lighting
- **POS Method**: Robust to motion artifacts
- **Green Channel**: Simple and fast

### Quality Metrics
- Signal-to-Noise Ratio (SNR)
- Peak-to-Peak Amplitude
- Motion Artifact Detection
- Face Detection Confidence

## 📊 Output Formats

- **CSV**: Time series data with timestamps
- **JSON**: Structured data with metadata
- **PNG**: Signal plots and visualizations
- **Video**: Annotated video with measurements

## 🏗️ Architecture

```
advanced_rppg/
├── rppg_core/          # Core rPPG algorithms
│   ├── face_detector.py
│   ├── signal_processor.py
│   ├── quality_metrics.py
│   └── hrv_analyzer.py
├── gui/                # User interface
│   ├── main_window.py
│   ├── video_widget.py
│   ├── plot_widget.py
│   └── control_panel.py
├── utils/              # Utility functions
│   ├── file_utils.py
│   └── validation.py
└── main.py            # Application entry point
```

## 🔬 Technical Details

### Supported Algorithms

1. **Chrominance Method**
   - Uses color channel differences
   - Robust to lighting variations
   - Best for controlled environments

2. **POS (Plane-Orthogonal-to-Skin)**
   - Motion-robust algorithm
   - Good for real-world scenarios
   - Handles head movements

3. **Green Channel**
   - Simple and fast
   - Good baseline performance
   - Minimal computational cost

### Signal Processing Pipeline

1. **Face Detection**: MediaPipe-based face tracking
2. **ROI Extraction**: Region of interest selection
3. **Signal Extraction**: Color channel processing
4. **Filtering**: Bandpass and detrending
5. **Peak Detection**: Heart rate estimation
6. **Quality Assessment**: Signal quality metrics
7. **HRV Analysis**: Time and frequency domain analysis

## 📈 Performance

- **Real-time Processing**: 30 FPS on modern hardware
- **Accuracy**: ±2 BPM compared to reference devices
- **Latency**: <100ms processing delay
- **Memory Usage**: <500MB typical usage

## 🤝 Contributing

We welcome contributions! Please see our [Contributing Guidelines](CONTRIBUTING.md) for details.

### Development Setup
```bash
git clone https://github.com/sherinjoseph/advanced-rppg.git
cd advanced-rppg
pip install -e .[dev]
```

### Running Tests
```bash
pytest tests/
```

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- MediaPipe for face detection
- OpenCV for computer vision
- PyQt5 for GUI framework
- SciPy for signal processing
- NumPy for numerical computations

## 📞 Support

- **Email**: sherin.joseph2217@gmail.com
- **Issues**: [GitHub Issues](https://github.com/sherinjoseph/advanced-rppg/issues)
- **Documentation**: [Read the Docs](https://advanced-rppg.readthedocs.io/)

## 🔄 Changelog

### Version 1.0.0
- Initial release
- Real-time rPPG processing
- Multiple algorithm support
- GUI interface
- HRV analysis
- Quality metrics

---

**Author**: Sherin Joseph Roy  
**Email**: sherin.joseph2217@gmail.com  
**License**: MIT 