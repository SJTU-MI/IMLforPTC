# MLforPTC
Physical feature engineering and machine learning for polymer thermal conductivity prediction
## Description
An interpretable machine learning framework for exploring high thermal conductivity polymer structures and extracted the chemical heuristic for high thermal conductivity polymers design through underlying mechanism analysis. The physical features engineering approach is applicable not only to organic thermal functional materials, but also for the discovery of high-performance polymers with other desired properties. Please refer to our work "Exploring High Thermal Conductivity Polymers via Interpretable Machine Learning with Physical Descriptors " for additional details.
![workflow](https://github.com/SJTU-MI/MLforPTC/blob/main/workflow.jpg)
## Installation
To download, clone this repository<br>
````
git clone https://github.com/SJTU-MI/MLforPTC.git
````
To run most code in this repository, the relevant anaconda environment can be installed from environment.yml. To build this environment, run
````
cd ./MLforPTC
conda env create -f environment.yml
conda activate mlforptc
````
However, a separate Mol2vec environment is required to represent the molecular structures. To build this environment, run
````
pip install git+https://github.com/samoturk/mol2vec
````
Try the desired parts of the project:

