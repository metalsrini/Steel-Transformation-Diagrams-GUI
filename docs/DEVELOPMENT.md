# Development Guide

## Project Structure

```
Steel-Transformation-Diagrams-GUI/
├── main.py                 # Main application entry point
├── requirements.txt        # Python dependencies
├── transformation-diagrams/# Core calculation library
│   ├── plot_diagrams.py   # TTT/CCT plotting functions
│   ├── transformation_models.py # Transformation calculations
│   └── utils.py           # Utility functions
├── docs/                  # Documentation
│   ├── images/           # Screenshots and diagrams
│   ├── THEORY.md        # Theoretical background
│   └── DEVELOPMENT.md   # This file
└── README.md             # Project overview
```

## Development Setup

### Environment Setup
1. Create a Python virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. Install development dependencies:
   ```bash
   pip install -r requirements.txt
   pip install pytest pytest-cov black flake8
   ```

### Code Style
- Follow PEP 8 guidelines
- Use Black for code formatting:
  ```bash
  black .
  ```
- Use Flake8 for linting:
  ```bash
  flake8 .
  ```

## Architecture

### GUI Components (main.py)
- Built using PyQt5
- Main window class: `SteelTransformationGUI`
- Components:
  - Input fields for composition
  - Buttons for different plots
  - Matplotlib canvas for visualization

### Core Library (transformation-diagrams/)
1. **transformation_models.py**
   - `Alloy` class: Handles composition and calculations
   - `TransformationDiagrams` class: Generates diagrams

2. **plot_diagrams.py**
   - TTT diagram plotting
   - CCT diagram plotting
   - Phase fraction visualization
   - Hardness plotting

3. **utils.py**
   - Helper functions
   - Data validation
   - Unit conversions

## Implementation Details

### Data Flow
1. User inputs chemical composition
2. Values validated and normalized
3. Critical temperatures calculated
4. Transformation curves generated
5. Results plotted on canvas

### Key Calculations

#### Critical Temperatures
```python
def calculate_ae3(composition):
    """
    Calculate Ae3 temperature based on composition
    Args:
        composition (dict): Steel composition in wt%
    Returns:
        float: Ae3 temperature in °C
    """
    # Implementation details...
```

#### Phase Transformations
```python
def calculate_transformation_time(temp, composition):
    """
    Calculate transformation time at given temperature
    Args:
        temp (float): Temperature in °C
        composition (dict): Steel composition
    Returns:
        float: Transformation time in seconds
    """
    # Implementation details...
```

## Testing

### Unit Tests
- Located in `tests/` directory
- Run tests with pytest:
  ```bash
  pytest
  ```

### Test Coverage
- Generate coverage report:
  ```bash
  pytest --cov=.
  ```

## Building

### Development Build
```bash
python main.py
```

### Production Build
```bash
pyinstaller --clean --windowed --onefile \
    --add-data "transformation-diagrams:transformation-diagrams" \
    --hidden-import pandas \
    --hidden-import numpy \
    --hidden-import scipy \
    --hidden-import matplotlib \
    --name "Steel_Transformation_Diagrams" \
    main.py
```

## Contributing

### Workflow
1. Fork the repository
2. Create a feature branch
3. Make changes
4. Run tests
5. Submit pull request

### Guidelines
- Write clear commit messages
- Add tests for new features
- Update documentation
- Follow code style guidelines

## Debugging

### Common Issues
1. **Import Errors**
   - Check PYTHONPATH
   - Verify virtual environment
   - Check package installation

2. **Plotting Issues**
   - Backend compatibility
   - Memory management
   - Thread safety

3. **Performance**
   - Profile code with cProfile
   - Optimize calculations
   - Cache results when possible

### Logging
```python
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# Usage
logger.debug("Calculation details...")
logger.info("Operation completed")
logger.error("Error occurred", exc_info=True)
```

## Performance Optimization

### Strategies
1. **Calculation Optimization**
   - Use NumPy vectorization
   - Cache intermediate results
   - Parallel processing for heavy calculations

2. **Memory Management**
   - Clear plot data after use
   - Implement garbage collection
   - Monitor memory usage

3. **GUI Responsiveness**
   - Use background threads for calculations
   - Implement progress indicators
   - Batch updates to reduce redraws

## Future Development

### Planned Features
1. **Enhanced Visualization**
   - 3D phase diagrams
   - Interactive plots
   - Custom color schemes

2. **Additional Calculations**
   - Precipitation kinetics
   - Grain growth modeling
   - Mechanical properties prediction

3. **User Experience**
   - Save/load compositions
   - Export results
   - Batch processing

### Architecture Improvements
1. **Modularity**
   - Separate UI and business logic
   - Plugin system for extensions
   - API for external integration

2. **Testing**
   - Automated UI testing
   - Performance benchmarks
   - Integration tests

3. **Documentation**
   - API documentation
   - User guides
   - Video tutorials
