# FlaskPDF
Função para gerar um pdf a partir de um arquivo html
(O wkhtmltopdf está com problemas para carregar arquivos estaticos, seu css e js devem ser colocados dentro do html)

### 🎲 

```bash
# Clone este repositório
$ git clone <git@github.com:zeguil/FlaskPDF.git>

# Acesse a pasta do projeto no terminal/cmd
$ cd FlaskPDF

# Crie uma maquina virtual
$ virtualenv venv 

# Acesse a maquina virtual
$ venv/Scripts/activate

#  Instale as bibliotecas necessarias 
$ pip install -r requirements.txt

# Instale o wkhtmltopf e adicione ao PATH nas variaveis de ambiente
$ https://wkhtmltopdf.org/downloads.html

# Dentro do arquivo app.py, na variavel 'path_wkhtmltopdf', você deve colocar o caminho onde foi instalado o wkhtmltopdf

```