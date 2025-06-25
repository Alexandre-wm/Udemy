'''
 DOC: https://pypi.org/project/python-dotenv/
 
 Variáveis de ambiente com Python
 Para variáveis de ambiente
 Windows PS: $env:VARIAVEL='VALOR' | dir env:
 Linux e Mac: export NOME_VARIAVEL='VALOR' | echo $VARIAVEL
 
 Para obter o valor das variáveis de ambiente
 os.getenv ou os.environ['VARIAVEL']
 
 Para configurar variáveis de ambiente
 os.environ['VARIAVEL'] = 'VALOR'
 Ou usando python-dotenv e o arquivo .env
 
 pip install python-dotenv
 from dotenv import load_dotenv
 load_dotenv()
 
 OBS.: Sempre lembre-se de criar um .env.example
 
 NUNCA ENVIE O ARQUIVO .env PARA NENHUM LUGAR EXTERNO
'''
import os
from dotenv import load_dotenv  # type: ignore

load_dotenv()
# print(os.environ)
print(os.getenv('BD_PASSWORD'))