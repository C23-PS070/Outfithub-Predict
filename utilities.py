import numpy as np 
import pandas as pd
import pickle
import sklearn

df_top = pd.read_csv('models/topwear.csv')
df_bottom = pd.read_csv('models/bottomwear.csv')
model_top = pickle.load(open('models/topwear_model.sav', 'rb'))
model_bottom = pickle.load(open('models/bottomwear_model.sav', 'rb'))
similarities_top = np.load("models/topwear_data_similarities.npy")
similarities_bottom = np.load("models/bottomwear_data_similarities.npy")

def predict_pipeline(inputs):
    df_baju = df_top.copy()
    df_baju = df_baju[df_baju["gender"]==inputs["gender"]]
    df_baju = df_baju[df_baju["usage"]==inputs["usage"]]
    df_baju = df_baju[df_baju["baseColour"]==inputs["baseColour"]]
    
    df_celana = df_bottom.copy()
    df_celana = df_celana[df_celana["gender"]==inputs["gender"]]
    df_celana = df_celana[df_celana["usage"]==inputs["usage"]]
    df_celana = df_celana[df_celana["baseColour"]==inputs["baseColour"]]

    category = ["topWear","bottomWear"]
    
    row_index = [df_baju.index[df_baju['filename'] == df_baju["filename"].sample(n=1).tolist()[0]].tolist()[0],
                df_celana.index[df_celana['filename'] == df_celana["filename"].sample(n=1).tolist()[0]].tolist()[0]]
    hm = {}
    for count,i in enumerate(row_index):
        if count == 0:
            model = model_top
            similarities = similarities_top
            df = df_top.copy()
        elif count == 1:
            model = model_bottom
            similarities = similarities_bottom
            df = df_bottom.copy()
        dist, index = model.kneighbors(X=similarities[i,:].reshape(1,-1))
        hm2 = {}
        similar_item = []
        for j in range(7):
                similar_item.append({
                    "id": df.loc[index[0][j], "filename"].replace("images/", "").split(".")[0],
                    "link":"https://storage.googleapis.com/image_outfithub/transparent_"+df.loc[index[0][j], "filename"].replace("images/", "").split(".")[0]+".png"
                })
        hm[f"{category[count]}"] = similar_item
    return hm
