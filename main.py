#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), 'transformation-diagrams'))

from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, 
                           QHBoxLayout, QPushButton, QLabel, QLineEdit, QGridLayout)
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
from transformation_models import Alloy, TransformationDiagrams

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Steel Transformation Diagrams')
        self.setGeometry(100, 100, 1400, 800)

        # Create main widget and layout
        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        layout = QHBoxLayout(main_widget)

        # Create left panel for inputs
        left_panel = QWidget()
        left_layout = QVBoxLayout(left_panel)

        # Create composition input section
        comp_widget = QWidget()
        comp_layout = QGridLayout(comp_widget)
        
        # Dictionary to store input fields
        self.inputs = {}
        
        # Add composition inputs
        row = 0
        comp_layout.addWidget(QLabel('ASTM grain size:'), row, 0)
        self.inputs['gs'] = QLineEdit('7')
        comp_layout.addWidget(self.inputs['gs'], row, 1)
        
        row += 1
        comp_layout.addWidget(QLabel('Initial temperature (°C):'), row, 0)
        self.inputs['Tini'] = QLineEdit('900')
        comp_layout.addWidget(self.inputs['Tini'], row, 1)
        
        # Add chemical composition inputs (exactly as in plot_diagrams.py)
        elements = [
            ('C', 'Carbon'),
            ('Si', 'Silicon'),
            ('Mn', 'Manganese'),
            ('Ni', 'Nickel'),
            ('Mo', 'Molybdenum'),
            ('Cr', 'Chromium'),
            ('V', 'Vanadium'),
            ('Co', 'Cobalt'),
            ('Cu', 'Copper'),
            ('Al', 'Aluminium'),
            ('W', 'Tungsten')
        ]
        
        for element, name in elements:
            row += 1
            comp_layout.addWidget(QLabel(f'{name} (wt%):'), row, 0)
            self.inputs[element] = QLineEdit('0')
            comp_layout.addWidget(self.inputs[element], row, 1)

        # Create buttons
        button_layout = QHBoxLayout()
        self.ttt_cct_button = QPushButton('Plot TTT/CCT')
        self.phase_button = QPushButton('Plot Phase Fractions')
        self.hardness_button = QPushButton('Plot Hardness')
        
        button_layout.addWidget(self.ttt_cct_button)
        button_layout.addWidget(self.phase_button)
        button_layout.addWidget(self.hardness_button)

        # Connect buttons
        self.ttt_cct_button.clicked.connect(self.plot_ttt_cct)
        self.phase_button.clicked.connect(self.plot_phase_fractions)
        self.hardness_button.clicked.connect(self.plot_hardness)

        # Add everything to left panel
        left_layout.addWidget(QLabel('Parameters:'))
        left_layout.addWidget(comp_widget)
        left_layout.addLayout(button_layout)
        left_layout.addStretch()

        # Add panels to main layout
        layout.addWidget(left_panel)

    def get_parameters(self):
        """Get all parameters from input fields"""
        params = {}
        for key, input_field in self.inputs.items():
            try:
                params[key] = float(input_field.text())
            except ValueError:
                print(f"Invalid value for {key}, using 0")
                params[key] = 0.0
        return params

    def plot_ttt_cct(self):
        """Plot TTT and CCT diagrams side by side"""
        print("\nPlotting TTT and CCT diagrams...")
        
        try:
            # Get parameters
            params = self.get_parameters()
            
            # Extract gs and Tini
            gs = params.pop('gs')
            Tini = params.pop('Tini')
            
            # Create Alloy object with composition
            alloy = Alloy(gs=gs, **params)
            
            # Print critical temperatures for verification
            print(f"\nCritical Temperatures:")
            print(f"Ae3: {alloy.Ae3:.1f}°C")
            print(f"Ae1: {alloy.Ae1:.1f}°C")
            print(f"Bs: {alloy.Bs:.1f}°C")
            print(f"Ms: {alloy.Ms:.1f}°C")
            
            # Create TransformationDiagrams object
            diagrams = TransformationDiagrams(alloy)
            
            # Create plot
            fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6), sharey=True)
            ax2.yaxis.set_tick_params(labelbottom=True)
            fig.subplots_adjust(wspace=.2)
            
            # Plot TTT
            diagrams.TTT(ax=ax1)
            
            t_min, t_max = ax1.get_xlim()
            
            # Plot CCT
            diagrams.CCT(Tini=Tini, ax=ax2, phi_min=Tini/t_max, phi_max=Tini/t_min)
            
            fig.suptitle(ax1.get_title())
            ax1.set_title('')
            ax2.set_title('')
            ax1.set_ylim(25, max(ax1.get_ylim()[1], Tini))
            
            plt.show()
            
        except Exception as e:
            print(f"Error plotting diagrams: {str(e)}")
            import traceback
            traceback.print_exc()

    def plot_phase_fractions(self):
        """Plot transformation diagram and phase fractions"""
        print("\nPlotting phase fractions...")
        
        try:
            # Get parameters
            params = self.get_parameters()
            
            # Extract gs and Tini
            gs = params.pop('gs')
            Tini = params.pop('Tini')
            
            # Create Alloy object with composition
            alloy = Alloy(gs=gs, **params)
            
            # Create TransformationDiagrams object
            diagrams = TransformationDiagrams(alloy)
            
            # Set parameters
            t = 45  # total time
            phi = 20  # cooling rate
            
            # Create plot
            fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))
            fig.subplots_adjust(wspace=.2)
            
            if phi == 0:
                # If isothermal, plot TTT
                diagrams.TTT(ax=ax1)
                xaxis = 't'
            else:
                diagrams.TTT(ax=ax1)
                t_min, t_max = ax1.get_xlim()
                ax1.clear()
                
                # Otherwise, plot CCT
                diagrams.CCT(Tini=Tini, ax=ax1, phi_min=Tini/t_max, phi_max=Tini/t_min)
                xaxis = 'T'
            
            t_, T_ = [0, t], [Tini, Tini - phi*t]
            diagrams.draw_thermal_cycle(ax1, t_, T_)
            diagrams.plot_phase_fraction(t_, T_, xaxis=xaxis, ax=ax2)
            
            fig.suptitle(ax1.get_title())
            ax1.set_title('')
            ax2.set_title('')
            
            plt.show()
            
        except Exception as e:
            print(f"Error plotting phase fractions: {str(e)}")
            import traceback
            traceback.print_exc()

    def plot_hardness(self):
        """Plot phase fractions and hardness vs cooling rate"""
        print("\nPlotting hardness vs cooling rate...")
        
        try:
            # Get parameters
            params = self.get_parameters()
            
            # Extract gs and Tini
            gs = params.pop('gs')
            Tini = params.pop('Tini')
            
            # Create Alloy object with composition
            alloy = Alloy(gs=gs, **params)
            
            # Create TransformationDiagrams object
            diagrams = TransformationDiagrams(alloy)
            
            # Define parameters
            Tfin = 25.  # final temperature
            cooling_rates = [1000, 300, 100, 30, 10, 3, 1, 3e-1,
                           1e-1, 3e-2, 1e-2, 3e-3, 1e-3]
            
            # Initialize lists for results
            f_ferr = []  # ferrite fractions
            f_pear = []  # pearlite fractions
            f_bain = []  # bainite fractions
            f_mart = []  # martensite fractions
            Hv = []      # hardness values
            
            # Calculate phase fractions and hardness for each cooling rate
            for phi in cooling_rates:
                print(f'Calculating phase fractions for phi={phi:.3g} °C/s...')
                
                total_time = (Tini - Tfin)/phi
                f = diagrams.get_transformed_fraction([0, total_time], [Tini, Tfin])
                
                f_fin = f.iloc[-1]
                
                f_ferr.append(f_fin['ferrite'])
                f_pear.append(f_fin['pearlite'])
                f_bain.append(f_fin['bainite'])
                f_mart.append(f_fin['martensite'])
                Hv.append(f_fin['Hv'])
            
            # Create plot
            fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))
            fig.subplots_adjust(wspace=.2)
            
            # Plot phase fractions
            ax1.plot(cooling_rates, f_ferr, label='Ferrite')
            ax1.plot(cooling_rates, f_pear, label='Pearlite')
            ax1.plot(cooling_rates, f_bain, label='Bainite')
            ax1.plot(cooling_rates, f_mart, label='Martensite')
            ax1.set_xlabel('Cooling rate (°C/s)')
            ax1.set_ylabel('Phase fraction')
            ax1.set_xscale('log')
            ax1.set_title(f'Phase fractions at {Tfin} °C')
            ax1.legend()
            
            # Plot hardness
            ax2.plot(cooling_rates, Hv)
            ax2.set_xlabel('Cooling rate (°C/s)')
            ax2.set_ylabel('Vickers Hardness')
            ax2.set_title(f'Hardness for phase fractions at {Tfin} °C')
            ax2.set_xscale('log')
            
            fig.suptitle(alloy.format_composition())
            
            plt.show()
            
        except Exception as e:
            print(f"Error plotting hardness: {str(e)}")
            import traceback
            traceback.print_exc()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
