# Aplicação prática de redes convolucionais

# Como executar
Instale as dependências: `$ python3 -m pip install -r requirements.txt`

Entre no diretório src e inicie a aplicação main.py: `$ cd src && python3 main.py`

Abra o link http://localhost:3000/

# Rotas
## "/"
GET: renderiza a página index.html de dentro da pasta templates

## "/linear"
GET: renderiza a página linear.html de dentro da pasta templates

## "/infer_cnn"
POST: pega a imagem do formulário e faz inferência por meio do modelo convolucional. Depois, retorna a resposta do modelo com a renderização da página resultado.html.

## "/infer_linear"
POST: pega a imagem do formulário e faz inferência por meio do modelo linear. Depois, retorna a resposta do modelo com a renderização da página resultado_linear.html.



