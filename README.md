# Steel Transformation Diagrams GUI

A sophisticated graphical user interface application for generating and analyzing Time-Temperature-Transformation (TTT) and Continuous-Cooling-Transformation (CCT) diagrams for steel compositions. This tool helps metallurgists and materials engineers visualize and understand phase transformations in steel under various conditions.

## Application Screenshots

![Main Interface](docs/images/main_interface.png)
*Main application interface with input parameters*

[View more screenshots and detailed explanations](docs/SCREENSHOTS.md)

## Table of Contents
- [Features](#features)
- [Scientific Background](#scientific-background)
- [Installation](#installation)
- [Usage Guide](#usage-guide)
- [Technical Details](#technical-details)
- [Contributing](#contributing)
- [License](#license)

## Features

### Core Functionality
- Generate interactive TTT (Time-Temperature-Transformation) diagrams
- Create CCT (Continuous-Cooling-Transformation) diagrams
- Calculate and plot phase fractions
- Analyze hardness variations with cooling rate

### Input Parameters
- **Chemical Composition**
  - Carbon (C): 0.1-2.0 wt%
  - Silicon (Si): 0-3.0 wt%
  - Manganese (Mn): 0-3.0 wt%
  - Nickel (Ni): 0-5.0 wt%
  - Molybdenum (Mo): 0-2.0 wt%
  - Chromium (Cr): 0-3.0 wt%
  - Vanadium (V): 0-2.0 wt%
  - Cobalt (Co): 0-5.0 wt%
  - Copper (Cu): 0-2.0 wt%
  - Aluminum (Al): 0-2.0 wt%
  - Tungsten (W): 0-2.0 wt%
- **Process Parameters**
  - ASTM Grain Size: 1-14
  - Initial Temperature: 700-1200°C

### Output Information
- Critical Temperatures
  - Ae3 (Austenite to Ferrite transformation)
  - Ae1 (Eutectoid temperature)
  - Bs (Bainite start)
  - Ms (Martensite start)
- Phase Transformation Curves
- Hardness Predictions

## Scientific Background

### TTT Diagrams
Time-Temperature-Transformation diagrams, also known as isothermal transformation diagrams, show the kinetics of austenite transformation under constant temperature conditions. They are essential for:
- Heat treatment process design
- Understanding phase transformation mechanisms
- Predicting microstructure evolution

### CCT Diagrams
Continuous-Cooling-Transformation diagrams represent austenite transformation during continuous cooling. They are particularly useful for:
- Industrial heat treatment processes
- Welding applications
- Understanding real-world cooling scenarios

## Installation

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Method 1: From Source
```bash
# Clone the repository
git clone https://github.com/metalsrini/Steel-Transformation-Diagrams-GUI.git
cd Steel-Transformation-Diagrams-GUI

# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the application
python main.py
```

### Method 2: Standalone Application (macOS)
1. Download the latest release from the [releases page](https://github.com/metalsrini/Steel-Transformation-Diagrams-GUI/releases)
2. Extract the downloaded file
3. Double-click `Steel_Transformation_Diagrams.app`

## Usage Guide

### Basic Operation
1. Launch the application
2. Enter chemical composition values in the respective fields
3. Set the ASTM grain size and initial temperature
4. Click desired plotting button:
   - "Plot TTT/CCT" for transformation diagrams
   - "Plot Phase Fractions" for phase distribution
   - "Plot Hardness" for hardness analysis

### Tips for Best Results
- Ensure composition values are within typical ranges
- Consider the combined effects of alloying elements
- Use realistic cooling rates for CCT diagrams
- Compare results with experimental data when available

### Common Use Cases
1. **Heat Treatment Design**
   - Analyze transformation temperatures
   - Determine optimal cooling rates
   - Predict final microstructure

2. **Alloy Development**
   - Study composition effects
   - Optimize properties
   - Compare different steel grades

3. **Process Optimization**
   - Evaluate cooling strategies
   - Predict mechanical properties
   - Optimize treatment parameters

## Technical Details

### Software Architecture
- GUI: PyQt5
- Numerical Computations: NumPy, SciPy
- Data Management: Pandas
- Plotting: Matplotlib
- Modular design for easy maintenance and updates

### Calculation Methods
- Based on established metallurgical models
- Incorporates empirical relationships
- Validated against experimental data

### Performance Optimization
- Efficient algorithms for real-time calculations
- Optimized data structures
- Responsive user interface

## Contributing

We welcome contributions! Please follow these steps:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Based on established metallurgical research
- Inspired by industrial needs
- Thanks to all contributors and users

## Support

For support, please:
1. Check the [documentation](docs/)
2. Look through [existing issues](https://github.com/metalsrini/Steel-Transformation-Diagrams-GUI/issues)
3. Open a new issue if needed

---
Developed with ❤️ for the metallurgy community
