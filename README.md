# Kaggle Competiton - GoDaddy MicroBusiness Density Forecasting

Welcome to the GitHub repository for the GoDaddy MicroBusiness Density Forecasting competition on Kaggle. This repository contains the code and analysis used in our solution for the competition.

The GoDaddy MicroBusiness Density Forecasting competition is a time-series prediction task in which participants are asked to forecast the number of microbusinesses in a given region. The dataset provided contains historical data on microbusiness density in various regions, as well as demographic and economic data for each region. The goal of the competition is to create a model that can accurately predict future microbusiness density based on the provided data.

## Contents

* [**`code/`**](/code)
    * [`constants.py`](/code/constants.py): contains all constant values used across project
* [**`notebooks/`**](/notebooks/)
    * [`0_eda.ipynb`](/notebooks/0_eda.ipynb): contains the code for exploring and visualizing the dataset, as well as cleaning and preprocessing the data.
    * [`1_feature_selection.ipynb`](/notebooks/0_eda.ipynb): contains the code for selecting the most relevant features for the prediction model.
    * [`2_pca_analysis.ipynb`](/notebooks/0_eda.ipynb): contains the code for performing PCA analysis on the dataset.
    * [`3_final_model.ipynb`](/notebooks/3_final_model.ipynb): contains the code for training and evaluating the final prediction model.
* [**`data/`**](/data)
    * [`census_starter.csv`](/data/census_starter.csv): stores relevant census data for different counties
    * [`md-counties.csv`](/data/md-counties.csv): microbusiness density values for all counties from 2019-2022
    * [`test.csv`](/data/test.csv): test data sourced from kaggle
    * [`train.csv`](/data/train.csv): train data sourced from kaggle

## Installation & Usage

Data sets used for this projects were sourced from the Kaggle competiton and the GoDaddy data store. All data sets are publicly available and free to download.
1. [**Kaggle datasets**](https://www.kaggle.com/competitions/godaddy-microbusiness-density-forecasting/data): for census, train and test data
2. [**GoDaddy datasets**](https://www.godaddy.com/ventureforward/microbusiness-datahub/): for yearly microdensity data by counties

Download the `KaggleMar2023` package or clone this repository.

## Requirements

All requirements are captured in the [`requirements.txt`](/requirements.txt) file in the root directory.

## Acknowledgements

We would like to acknowledge GoDaddy for providing the data and hosting the competition, as well as the Kaggle community for their support and contributions.