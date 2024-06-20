# Projeto Flask - Sistema de Gestão de Alunos e Notas

Este é um projeto Flask simples para renderizar tabela de alunos e suas notas. 
Ele utiliza Flask como framework web e Pandas para manipulação de dados.


## Instalação

1. **Clone o repositório:**
    ``` bash
    git clone https://github.com/seu-usuario/projeto-flask.git
    ```

2. **Crie um ambiente virtual:**
    ```bash
    python -m venv_teste_python venv
    ```

3. **Ative o ambiente virtual:**
    ```bash
    source venv_teste_python/bin/activate
    ```

4. **Instale as dependências do projeto:**
    ```bash
    pip install --upgrade pip 
    pip install -r requirements.txt
    ```

5. **Rode a aplicação:**
    ```bash
    python app.py
    ```
    Acesse `http://localhost:5000` para ver a aplicação em execução.

6. **Rode o teste**
    ```bash
    pytest
    ```
    *Caso tenha algum erro de importação do modulo utils, utilize o comando abaixo, substituindo o caminho completo até o projeto(remova aspas):
    ```bash
    export PYTHONPATH="/caminho/completo/do/seu/projeto"/utils:$PYTHONPATH
    ```