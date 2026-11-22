from flask import Flask,render_template,url_for,redirect,request

import os

app = Flask(__name__)

FICHEIRO_DADOS = "mensagens.txt"

# --- Funções de Manipulação do Ficheiro ---
def ler_mensagens():
   """Lê as mensagens guardadas no ficheiro de texto."""
   if os.path.exists(FICHEIRO_DADOS):
       with open(FICHEIRO_DADOS, 'r', encoding='utf-8') as f:
           # Remove espaços em branco e ignora linhas vazias
           return [linha.strip() for linha in f if linha.strip()]
   return []


def guardar_mensagem(nome, mensagem):
   """Adiciona uma nova linha ao final do ficheiro (Modo 'a' - Append)."""
   with open(FICHEIRO_DADOS, 'a', encoding='utf-8') as f:
       f.write(f"{nome}: {mensagem}\n")


def apagar_mensagens():
    with open(FICHEIRO_DADOS,"w"):
        pass

# --- Aqui estão as rotas da Aplicação ---
@app.route("/", methods=['GET', 'POST'])
def livro_mensagem():
   if request.method == 'POST':
       # Captura os dados do formulário de envio
       nome = request.form.get('nome')
       mensagem = request.form.get('mensagem')
      
       if nome and mensagem:
           guardar_mensagem(nome, mensagem)
          
       # Redireciona para o GET da própria página
       return redirect(url_for('livro_mensagem'))


   # No método GET, lemos os dados para exibir na página
   mensagens = ler_mensagens()
   return render_template("index.html", mensagens=mensagens)


@app.route("/confirmar_exclusão", methods=['POST'])
def confirmar_exclusao():
    return render_template("confirmar.html")

@app.route("/limpar", methods=['POST'])
def limpar_dados():
    apagar_mensagens()
    return redirect(url_for('livro_mensagem'))

    


if __name__ == "__main__":
   app.run(debug=True)

