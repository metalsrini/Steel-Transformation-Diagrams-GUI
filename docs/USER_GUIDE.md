# User Guide

## Getting Started

### Installation

#### Method 1: Using the Standalone Application (Recommended for macOS users)
1. Download the latest release from our [releases page](https://github.com/metalsrini/Steel-Transformation-Diagrams-GUI/releases)
2. Extract the downloaded file
3. Double-click `Steel_Transformation_Diagrams.app`

#### Method 2: From Source Code
1. Install Python 3.8 or higher
2. Clone the repository:
   ```bash
   git clone https://github.com/metalsrini/Steel-Transformation-Diagrams-GUI.git
   cd Steel-Transformation-Diagrams-GUI
   ```
3. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
5. Run the application:
   ```bash
   python main.py
   ```

## Using the Application

### Main Window Layout
- **Left Panel**: Input fields for composition and parameters
- **Right Panel**: Plotting area
- **Bottom**: Action buttons and status information

### Input Parameters

#### Chemical Composition
Enter the weight percentage (wt%) for each element:

| Element | Range | Typical Use |
|---------|-------|-------------|
| Carbon (C) | 0.1-2.0% | Primary hardening element |
| Silicon (Si) | 0-3.0% | Deoxidizer |
| Manganese (Mn) | 0-3.0% | Increases hardenability |
| Nickel (Ni) | 0-5.0% | Improves toughness |
| Molybdenum (Mo) | 0-2.0% | Enhances hardenability |
| Chromium (Cr) | 0-3.0% | Improves corrosion resistance |
| Vanadium (V) | 0-2.0% | Grain refinement |
| Cobalt (Co) | 0-5.0% | High-temperature strength |
| Copper (Cu) | 0-2.0% | Corrosion resistance |
| Aluminum (Al) | 0-2.0% | Deoxidizer |
| Tungsten (W) | 0-2.0% | High-temperature strength |

#### Process Parameters
- **ASTM Grain Size**: 1-14 (larger number = finer grain)
- **Initial Temperature**: 700-1200°C

### Generating Diagrams

#### TTT/CCT Diagrams
1. Enter chemical composition
2. Set grain size and initial temperature
3. Click "Plot TTT/CCT"
4. Observe:
   - Transformation curves
   - Critical temperatures
   - Phase regions

#### Phase Fractions
1. Configure inputs as above
2. Click "Plot Phase Fractions"
3. Analysis shows:
   - Phase percentages vs temperature
   - Transformation boundaries
   - Equilibrium phases

#### Hardness Analysis
1. Set composition and parameters
2. Click "Plot Hardness"
3. Results display:
   - Hardness vs cooling rate
   - Phase contributions
   - Property predictions

### Interpreting Results

#### Critical Temperatures
- **Ae3**: Austenite → Ferrite transformation
- **Ae1**: Eutectoid temperature
- **Bs**: Bainite start temperature
- **Ms**: Martensite start temperature

#### Reading TTT Diagrams
1. Time scale (logarithmic)
2. Temperature scale (linear)
3. Transformation curves
4. Phase regions

#### Understanding CCT Diagrams
1. Cooling curves
2. Transformation regions
3. Final microstructure
4. Property predictions

### Best Practices

#### Composition Input
- Use realistic combinations
- Consider element interactions
- Stay within solubility limits
- Match standard grades when possible

#### Process Parameters
- Use appropriate grain sizes
- Consider practical heating limits
- Account for section size
- Match industrial conditions

#### Results Analysis
- Compare with known data
- Consider practical limitations
- Account for processing variables
- Validate predictions

### Troubleshooting

#### Common Issues

1. **Application Won't Start**
   - Check Python installation
   - Verify dependencies
   - Confirm file permissions

2. **Plotting Errors**
   - Validate input ranges
   - Check for conflicting inputs
   - Restart application

3. **Unexpected Results**
   - Verify composition
   - Check temperature ranges
   - Compare with literature

#### Error Messages

| Message | Cause | Solution |
|---------|-------|----------|
| "Invalid Input" | Out of range value | Check input ranges |
| "Calculation Error" | Mathematical error | Verify composition |
| "Plot Error" | Visualization issue | Restart application |

### Tips and Tricks

1. **Efficient Usage**
   - Save common compositions
   - Use standard ranges
   - Compare multiple conditions

2. **Accuracy Improvement**
   - Validate with experiments
   - Use reliable data sources
   - Consider uncertainty ranges

3. **Time Saving**
   - Prepare input sets
   - Document conditions
   - Plan analysis sequence

## Advanced Features

### Batch Processing
- Multiple compositions
- Parameter variations
- Comparative analysis

### Data Export
- Save diagrams
- Export data
- Generate reports

### Custom Analysis
- Modified parameters
- Special conditions
- Specific applications

## Support

### Getting Help
1. Check documentation
2. Search issues
3. Contact support

### Reporting Problems
1. Describe the issue
2. Provide input data
3. Share error messages

### Requesting Features
1. Describe need
2. Provide use case
3. Suggest implementation

## Additional Resources

### References
1. ASM Handbook
2. Steel Heat Treatment Guide
3. Metallurgical Textbooks

### Online Resources
1. Technical forums
2. Research papers
3. Industry standards

### Community
1. User groups
2. Discussion boards
3. Professional networks
