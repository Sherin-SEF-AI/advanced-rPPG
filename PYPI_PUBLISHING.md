# PyPI Publishing Guide

This guide will help you publish the Advanced rPPG package to PyPI.

## Prerequisites

1. **PyPI Account**: Create an account at [PyPI](https://pypi.org/account/register/)
2. **TestPyPI Account**: Create an account at [TestPyPI](https://test.pypi.org/account/register/)
3. **API Tokens**: Generate API tokens for both PyPI and TestPyPI
4. **Build Tools**: Install required build tools

## Setup

### 1. Install Build Dependencies
```bash
pip install build twine
```

### 2. Configure API Tokens
Create a `~/.pypirc` file:
```ini
[distutils]
index-servers =
    pypi
    testpypi

[pypi]
username = __token__
password = pypi-your-api-token-here

[testpypi]
repository = https://test.pypi.org/legacy/
username = __token__
password = pypi-your-testpypi-api-token-here
```

## Building the Package

### 1. Clean Previous Builds
```bash
rm -rf build/ dist/ *.egg-info/
```

### 2. Build the Package
```bash
python -m build
```

This creates:
- `dist/advanced_rppg-1.0.0.tar.gz` (source distribution)
- `dist/advanced_rppg-1.0.0-py3-none-any.whl` (wheel distribution)

### 3. Check the Package
```bash
python -m twine check dist/*
```

## Publishing Process

### Step 1: Test on TestPyPI
Always test on TestPyPI first:

```bash
python -m twine upload --repository testpypi dist/*
```

### Step 2: Test Installation from TestPyPI
```bash
pip install --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple/ advanced-rppg
```

### Step 3: Publish to PyPI
If everything works on TestPyPI:

```bash
python -m twine upload dist/*
```

## Using the Build Script

We've provided a convenient build script:

```bash
# Build package only
python build_package.py

# Build and upload to TestPyPI
python build_package.py --test

# Build and upload to PyPI
python build_package.py --upload

# Show help
python build_package.py --help
```

## Version Management

### Updating Version
1. Update version in `pyproject.toml`:
   ```toml
   version = "1.0.1"
   ```

2. Update version in `setup.py`:
   ```python
   version="1.0.1",
   ```

3. Update version in `advanced_rppg/__init__.py`:
   ```python
   __version__ = "1.0.1"
   ```

### Version Numbering
- **Major.Minor.Patch** (e.g., 1.0.0)
- **Major**: Breaking changes
- **Minor**: New features, backward compatible
- **Patch**: Bug fixes, backward compatible

## Package Verification

### 1. Check Package Contents
```bash
tar -tzf dist/advanced_rppg-1.0.0.tar.gz
```

### 2. Test Installation
```bash
pip install dist/advanced_rppg-1.0.0-py3-none-any.whl
```

### 3. Test Functionality
```bash
python -c "import advanced_rppg; print(advanced_rppg.__version__)"
rppg-app --help
```

## Troubleshooting

### Common Issues

1. **Authentication Error**
   - Check your API tokens
   - Ensure `~/.pypirc` is properly configured

2. **Package Already Exists**
   - Increment version number
   - Delete old distributions

3. **Missing Dependencies**
   - Check `pyproject.toml` dependencies
   - Ensure all imports are available

4. **Build Errors**
   - Check for syntax errors
   - Verify package structure
   - Ensure all `__init__.py` files exist

### Error Messages

```
HTTPError: 400 Bad Request from https://pypi.org/legacy/
```
- Check package metadata
- Verify classifiers and descriptions

```
HTTPError: 403 Forbidden from https://pypi.org/legacy/
```
- Check authentication
- Verify API token permissions

## Best Practices

1. **Always test on TestPyPI first**
2. **Use semantic versioning**
3. **Include comprehensive documentation**
4. **Test installation in clean environment**
5. **Keep dependencies minimal**
6. **Use proper classifiers**
7. **Include license file**

## Automated Publishing

### GitHub Actions (Optional)
Create `.github/workflows/publish.yml`:

```yaml
name: Publish to PyPI

on:
  release:
    types: [published]

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v2
    - name: Set up Python
      uses: actions/setup-python@v2
      with:
        python-version: '3.8'
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install build twine
    - name: Build and publish
      env:
        TWINE_USERNAME: __token__
        TWINE_PASSWORD: ${{ secrets.PYPI_API_TOKEN }}
      run: |
        python -m build
        python -m twine upload dist/*
```

## Package Maintenance

### Regular Tasks
1. **Monitor Issues**: Check PyPI and GitHub for issues
2. **Update Dependencies**: Keep dependencies up to date
3. **Security Updates**: Address security vulnerabilities
4. **Documentation**: Keep documentation current

### Deprecation
If you need to deprecate the package:
1. Mark as deprecated in README
2. Add deprecation warning in code
3. Consider transferring ownership

## Support

For PyPI-specific issues:
- [PyPI Help](https://pypi.org/help/)
- [TestPyPI Help](https://test.pypi.org/help/)
- [Python Packaging User Guide](https://packaging.python.org/)

For package-specific issues:
- Email: sherin.joseph2217@gmail.com
- GitHub Issues: [Repository Issues](https://github.com/sherinjoseph/advanced-rppg/issues) 