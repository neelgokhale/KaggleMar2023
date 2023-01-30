import os

# file paths
    
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NB_DIR = os.path.join(ROOT_DIR, 'notebooks')
DATA_DIR = os.path.join(ROOT_DIR, 'data')
TRAIN_PATH = os.path.join(DATA_DIR, 'train.csv')
TEST_PATH = os.path.join(DATA_DIR, 'test.csv')
CENSUS_PATH = os.path.join(DATA_DIR, 'census_starter.csv')
MD_PATH = os.path.join(DATA_DIR, 'md-counties.csv')
    