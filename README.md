# Steel Transformation Diagrams GUI

A graphical user interface application for generating Time-Temperature-Transformation (TTT) and Continuous-Cooling-Transformation (CCT) diagrams for steel compositions.

## Features

- Interactive input fields for chemical compositions (C, Si, Mn, Ni, Mo, Cr, V, Co, Cu, Al, W)
- Input fields for grain size and initial temperature
- Generate TTT/CCT diagrams
- Plot phase fractions
- Plot hardness vs cooling rate
- Display critical temperatures (Ae3, Ae1, Bs, Ms)

## Installation

1. Clone this repository:
```bash
git clone https://github.com/yourusername/transformation_diagrams_gui.git
cd transformation_diagrams_gui
```

2. Create a virtual environment and install dependencies:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## Running the Application

### From Source
```bash
python main.py
```

### Using the Standalone Application (macOS)
1. Navigate to the `dist` folder
2. Double-click `Steel_Transformation_Diagrams.app`

## Building the Standalone Application

To create a standalone application:
```bash
pyinstaller --clean --windowed --onefile --add-data "transformation-diagrams:transformation-diagrams" --hidden-import pandas --hidden-import numpy --hidden-import scipy --hidden-import matplotlib --name "Steel_Transformation_Diagrams" main.py
```

## Usage

1. Enter the chemical composition values in the input fields
2. Set the grain size and initial temperature
3. Click one of the buttons to generate the desired diagram:
   - "Plot TTT/CCT" for transformation diagrams
   - "Plot Phase Fractions" for phase distribution
   - "Plot Hardness" for hardness vs cooling rate

## License

This project is licensed under the MIT License - see the LICENSE file for details.
