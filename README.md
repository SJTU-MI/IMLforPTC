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
However, a separate Mol2vec environment is required to represent the molecular structures (optional). To build this environment, run
````
pip install git+https://github.com/samoturk/mol2vec
````
## Try the desired parts of the project:
### Folders
**main**: Some core code implementation <br>
**01descriptor_Statisticalselection**: Process files generated by different down-selection stages for physical descriptors <br>
**02optimized&graph_descriptors**: Optimized descriptors, graph descriptors of Morgan fingerprint, MACCS and Mol2vec, 2D vectors converted from polymer chemical structures by UMAP <br>
**03ML_models**: Trained machine learning models <br>
**04model_accuracy**: Accuracy statistics of machine learning models with different representations or physical descriptors at various down-selection stages  <br>
**05Polymer_data**: PolyInfo (datasteA) and PI1M (datasteB) polymer datasets <br>
### Code in the main folder
**01feature_engineering.ipynb**: Feature engineering for down-selection of physical descriptors <br>
**02_1graph_descriptor.ipynb**: Generation of morgan, morgan counts and MACCS fingerprints using RDkit <br>
**02_2Mol2vec.ipynb**: Generation of Mol2vec fingerprints <br>
**02_3Similarity_plot.ipynb**: Visualization of polymer data distribution in a 2D space by UMAP. The polymer structure is first transformed into a two-dimensional vector by *UMAP_for_polymer.py* <br>
**03_1ML_optimized_descriptor.ipynb**: Machine learning models training with *optimized descriptors* <br>
**03_2ML_Mol2vec.ipynb**: Machine learning models training with *Mol2vec descriptors*  <br>
**03_3ML_MACCS.ipynb**: Machine learning models training with *MACCS descriptors*  <br>
**03_4ML_Morgan.ipynb**: Machine learning models training with *Morgan descriptors*  <br>
**03_5ML_cMargan.ipynb**: Machine learning models training with *Morgan counts descriptors* <br>
**03_6ML_PCA.ipynb**: Machine learning models training with *PCA-based descriptors*  <br>
**04SHAP_RF.ipynb**: Feature importance analysis by SHAP with RF model <br>
**05TC_Prediction.ipynb**: Virtual screening of high thermal conductivity polymers in PolyInfo and PI1M datasets <br>
**06Model_accuracy.ipynb**: Plotting of model accuracy corresponding to different down-selection stages or different representations <br>
## Authors

| **AUTHORS** |Xiang Huang, Shengluo Ma,Shenghong Ju            |
|-------------|--------------------------------------------------|
| **VERSION** | 1.0 / January,2023                               |
| **EMAILS**  | shenghong.ju@sjtu.edu.cn, msl@sjtu.edu.cn, huangxiang@sjtu.edu.cn |

## Attribution
This work is under BSD-2-Clause License. Please, acknowledge use of this work with the appropiate citation to the repository and research article.
