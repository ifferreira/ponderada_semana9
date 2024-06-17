from flask import Flask, request, render_template
import cv2
import numpy as np
from tensorflow.keras.models import load_model
import os

modelo = load_model("pesos.h5")


app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/infer", methods=["POST"])
def infer():
    image_file = request.files["imagem"]
    path = os.path.join("./uploads", secure_filename(file.filename))
    image_file.save(path)
    #resultado = predict()

    image = cv2.imread(path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    image = cv2.resize(image, (28, 28))
    image = image / image.max()
    img = img.reshape(1, 28, 28, 1)
    inference = modelo.predict(image)
    result = np.argmax(inference)

    return render_template("resultado.html", result=result)



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)



