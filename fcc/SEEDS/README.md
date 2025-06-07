# Seoul Bike Sharing Demand ML Project

## Overview

This project uses **bike sharing demand data** to develop and evaluate machine learning models for predicting rental bike availability in Seoul's public bike sharing system. The dataset contains hourly bike rental counts with corresponding weather conditions and holiday information to help optimize bike distribution and ensure stable supply across the city.

## Dataset

The dataset is sourced from the **Seoul Bike Sharing System** with comprehensive temporal and environmental data:

- **Reference:** Sathishkumar V E, Jangwoo Park, Yongyun Cho, "Using data mining techniques for bike sharing demand prediction in Metropolitan city", Computer Communications, vol. 153, pp. 353-366, 2020.
- **Additional Reference:** Sathishkumar V E, Yongyun Cho, "A rule-based model for Seoul Bike sharing demand prediction using Weather data", European Journal of Remote Sensing, Vol. 52, no. 1, pp. 166-183, 2020.
- Contains **8,760 instances** with **13 features** covering hourly bike rental patterns and environmental factors.

## Features

The dataset contains several key **temporal and environmental parameters** used for demand prediction:

- **Date**: Year-month-day timestamp
- **Rented Bike Count**: Target variable - hourly bike rental count
- **Hour**: Hour of the day (0-23)
- **Temperature**: Temperature in Celsius
- **Humidity**: Relative humidity percentage
- **Wind Speed**: Wind speed in m/s
- **Visibility**: Visibility in 10m units
- **Dew Point Temperature**: Dew point in Celsius
- **Solar Radiation**: Solar radiation in MJ/m²
- **Rainfall**: Precipitation in mm
- **Snowfall**: Snow accumulation in cm
- **Seasons**: Categorical season information
- **Holiday**: Holiday/No holiday indicator
- **Functioning Day**: Functional/Non-functional hours indicator

## Goal

The objective is to train a **machine learning model** to:

- **Predict** hourly bike sharing demand using weather and temporal features.
- **Optimize** bike distribution strategies for stable supply across the city.
- **Evaluate** regression performance using accuracy metrics and temporal validation techniques.