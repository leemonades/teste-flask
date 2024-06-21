from flask import Flask, render_template
import pandas as pd
from utils.verifica_dados import verifica_qtd_dados # importando a função criada para validação de dados e tratamento

app = Flask(__name__)
'''
Mock dos dados
'''
alunos = ['Renato', 'Fernando', 'Rodrigo', 'Ana', 'Joana', 'Silvio', 'Carolina']
notas = [15.00, 39.58, 62.92, 41.46, 48.33, 63.13, 70.00]

''' 
Utiliza a função criada para garantir o tamanho de elementos nos dados fornecidos
para garantir que a aplicação não quebre por falta de elementos, mesmo que neste caso sejam arrays simples e íntegros.
'''
df = verifica_qtd_dados(Alunos=alunos, Notas=notas) # passa o nome da coluna e o array de dados correspondente


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/table')
def table():
    
    return render_template('table.html',
                           df=df ) # passando o DataFrame como contexto

'''
trecho para inicializar o servidor Flask localmente ao executar este arquivo utilizando o comando python app.py conforme item 1.4.1 do teste
'''
if __name__ == '__main__': 
    app.run(debug=True)