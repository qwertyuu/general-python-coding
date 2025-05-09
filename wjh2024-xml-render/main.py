import os
import networkx as nx
import xml.etree.ElementTree as ET

folder_path = __file__ + os.path.sep + ".."
folder_path = os.path.abspath(folder_path) + os.path.sep

images_path = folder_path + "images"
images_path = os.path.abspath(images_path) + os.path.sep

# Your XML data
with open(folder_path + "Design recettes.drawio.xml", 'r') as f:
    xml_data = f.read()

# Parse the XML data
root = ET.fromstring(xml_data)

# Create a directed graph
G = nx.DiGraph()
G.add_node('node', label='')

# Iterate through nodes in the XML and note their name
id_label_map = {}
for cell in root.iter('object'):
    if cell.get('label') is not None:
        id = cell.get('id')
        label = cell.get('label')
        id_label_map[id] = label
        image_attr = "\"" + images_path + label + ".png\""
        G.add_node(label, image=image_attr)
# Iterate through edges in the XML and add them to the graph
for cell in root.iter('mxCell'):
    if cell.get('edge') == '1':
        source = cell.get('source')
        target = cell.get('target')
        if source and target:
            G.add_edge(id_label_map[source], id_label_map[target])

# Generate DOT file
dotfile_path = folder_path + 'output.dot'
nx.drawing.nx_pydot.write_dot(G, dotfile_path)

print(f'DOT file generated: {dotfile_path}')

# Generate PNG file
pngfile_path = 'output'

# Use Graphviz to render the graph
from graphviz import Source
src = Source.from_file(dotfile_path)
src.render(folder_path + pngfile_path, format='png', cleanup=True)
