"""
-----------------------------------------------------
Copyright © Arthur Guiot 2018. All rights reserved
-----------------------------------------------------

test.py will train a "fake" model to check that
everything works as it should. You can use it as a
demo file.

"""
import neuron_ml as n
import os

# TensorFlow
data = n.load(os.path.abspath("./dataset/"))
model = n.train(data)
n.export(model, [
	os.path.abspath("./Model.pb"),
	os.path.abspath("./Labels.txt")
])

# TFLite

# n.export(model, os.path.abspath("./Model.tflite"), "tflite")

# CoreML

n.export(model, os.path.abspath("./Model.mlmodel"), "coreml")

# CreateML
data = n.load(os.path.abspath("./dataset/"), "createml")
model = n.train(data)
n.export(model, os.path.abspath("./CreateML.mlmodel"))
