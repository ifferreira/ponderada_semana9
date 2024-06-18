from flask import Flask, request, render_template
import cv2
import numpy as np
from tensorflow.keras.models import load_model
import os
from werkzeug.utils import secure_filename

modelo = load_model("pesos.h5")
modelo_linear = load_model("pesos2.h5")

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/linear")
def linear():
    return render_template("linear.html")

@app.route("/infer_cnn", methods=["POST"])
def infer_cnn():
    image_file = request.files["imagem"]
    path = os.path.join("./uploads", secure_filename(image_file.filename))
    image_file.save(path)
    image = cv2.imread(path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    image = cv2.resize(image, (28, 28))
    image = image / image.max()
    image = image.reshape(1, 28, 28, 1)
    inference = modelo.predict(image)
    result = np.argmax(inference)

    return render_template("resultado.html", result=result)

@app.route("/infer_linear", methods=["POST"])
def infer_linear():
    image_file = request.files["imagem"]
    path = os.path.join("./uploads", secure_filename(image_file.filename))
    image_file.save(path)
    image = cv2.imread(path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    image = image / image.max()
    image = image.reshape(1, 28, 28, 1)
    inference = modelo_linear.predict(image)
    result = np.argmax(ingerence)
    return render_template("resultado_linear.html", resutl=result)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)



