#!/usr/bin/env python
# coding: utf-8
#Converting the chemical structure of polymers to 2D planes using UMAP
import pandas as pd
import umap

file="../Data02-different_descriptors/Similarity_Analysis/selected_morgan.pkl"
df=pd.read_pickle(file)
beg=0
end=len(df)

X_all=df.drop(df.columns[0:3], axis=1)

reducer = umap.UMAP(random_state=42)
embedding = reducer.fit_transform(X_all[beg:end])


data=pd.DataFrame(embedding,columns=["x1","x2"])
data1=pd.concat([df.iloc[:, :3],data],axis=1)
path="../Data02-different_descriptors/Similarity_Analysis/"
file2="embedding_selected.pkl"
data1.to_pickle(path+file2)
