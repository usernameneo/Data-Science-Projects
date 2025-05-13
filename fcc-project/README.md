# MC-Generated Data ML Project

## Overview
This project uses **Monte Carlo-generated data** to develop and evaluate machine learning models for gamma-ray detection in a **Cherenkov gamma telescope**. The dataset simulates high-energy gamma particle registrations using imaging techniques and helps differentiate gamma-initiated showers from cosmic-ray-induced hadronic showers.

## Dataset
The dataset is generated using the **Corsika Monte Carlo simulation program**:
- **Reference:** D. Heck et al., CORSIKA: A Monte Carlo Code to Simulate Extensive Air Showers, Forschungszentrum Karlsruhe FZKA 6019 (1998).  
  [http://rexa.info/paper?id=ac6e674e9af20979b23d3ed4521f1570765e8d68](http://rexa.info/paper?id=ac6e674e9af20979b23d3ed4521f1570765e8d68)
- Simulated events include Cherenkov radiation signals from **gamma rays and cosmic ray background**.

## Features
The dataset contains several key **image parameters** used for classification:
- **fLength**: Major axis of the shower ellipse  
- **fWidth**: Minor axis of the ellipse  
- **fSize**: Logarithmic sum of pixel contents  
- **fConc & fConc1**: Ratios of highest pixel intensities  
- **fAsym**: Distance from the highest pixel to the center  
- **fM3Long & fM3Trans**: Higher-order moments for image shape characterization  
- **fAlpha & fDist**: Geometric alignment of the shower ellipse  
- **class**: Labels (gamma = signal, hadron = background)

## Goal
The objective is to train a **machine learning model** to:
- **Classify** gamma-ray showers from hadronic showers using feature engineering.
- **Optimize** model performance using statistical and deep learning techniques.
- **Evaluate** accuracy, precision, and recall across various models.

## Installation & Usage
1. Clone the repository:
   ```bash
   git clone https://github.com/YOUR_USERNAME/YOUR_REPO.git
   cd YOUR_REPO

