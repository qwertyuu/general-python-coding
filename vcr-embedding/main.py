from gpt4all import Embed4All
import numpy as np
import json
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
import umap
import plotly.express as px
import pandas as pd

# open json file
with open("D:\VCR\code\cassettes-gallery.json", encoding="utf-8") as f:
    data = json.load(f)


embedder = Embed4All()
# extract only "DescriptionContenu" from json file
new_data = []
embeddings = []
IDs = []
for i in range(len(data)):
    new_data.extend([x[3:].strip() for x in data[i]["DescriptionContenu"].split("\n") if len(x) > 3])
    IDs.extend([data[i]["ID"] for x in data[i]["DescriptionContenu"].split("\n") if len(x) > 3])
for i in range(len(new_data)):
    print(new_data[i])
    embeddings.append(embedder.embed(new_data[i]))
    #print(embeddings[i])

#exit()
#print(np.array(embeddings))

# plot the embeddings in 2D, including the ID of the cassettes (contained in the json file as "ID")

fit = umap.UMAP(n_components=3)
X = fit.fit_transform(np.array(embeddings))
#pca = PCA(n_components=2)
#pca.fit(embeddings)
#X = pca.transform(embeddings)
# generate some newlines in description to make it more readable
for i in range(len(new_data)):
    new_data[i] = new_data[i].replace(".", ".\n")

x_data = pd.DataFrame(X, columns=["x", "y", "z"])
x_data["IDs"] = IDs
x_data["Description"] = new_data


# Créer le nuage de points interactif en 3D
fig = px.scatter_3d(x_data, x="x", y="y", z="z", text="IDs", title="Cassettes VCR", hover_data=['Description'], template='plotly_dark')
fig.update_layout(
    hoverlabel=dict(
        bgcolor="white",
        font_size=13,
        font_family="Rockwell"
    )
)
fig.write_html("vcr-embedding/scatter.html")
fig.show()
