import os # Importar o módulo os para manipulação de arquivos e diretórios
import json # Importar o módulo json para manipulação de arquivos JSON
import shutil # Importar o módulo shutil para operações de alto nível em arquivos, como mover arquivos
import time # Importar o módulo time para manipulação de tempo, como pausar a execução do script por um determinado período

def load_config(): # Função para carregar a configuração do arquivo config.json
    with open('config.json', 'r', encoding='utf-8') as arquivo: # Abrir o arquivo config.json em modo de leitura com codificação UTF-8  
        return json.load(arquivo) # Carregar o conteúdo do arquivo config.json usando a função json.load() e retornar o resultado

def mover_arquivos(origem, destino): # Função para mover os arquivos do diretório de origem para o diretório de destino

    for arquivo in os.listdir(origem): # Listar todos os arquivos no diretório de origem
        if arquivo.lower().endswith('.xml'): # Verificar se o arquivo tem a extensão .xml (ignorando maiúsculas/minúsculas)
            caminho_origem = os.path.join(origem, arquivo) # Gerar o caminho completo do arquivo de origem
            caminho_destino = os.path.join(destino, arquivo) # Gerar o caminho completo do arquivo de destino

            try: # Tentar mover o arquivo para o destino, verificando se ele já existe no destino para evitar sobrescrita
                if not os.path.exists(caminho_destino): # Verificar se o arquivo já existe no destino
                    shutil.move(caminho_origem, caminho_destino) # Mover o arquivo para o destino
                print(f"Arquivo {arquivo} movido com sucesso!") 
            except Exception as e: # Tratar erros durante a movimentação do arquivo
                print(f"Erro ao mover o arquivo {arquivo}: {e}")

if __name__ == '__main__': # Verificar se o script está sendo executado diretamente (e não importado como módulo)
    while True: # Loop infinito para executar o script a cada 10 minutos
        print("Iniciando Script...\n")

        try: # Carregar a configuração do arquivo config.json
            config = load_config() # Chamar a função para carregar a configuração do arquivo config.json e armazenar o resultado na variável config

            origem = config['diretorio']['drive_compartilhado'] # Obter o diretório de origem do arquivo config.json
            destino = config['diretorio']['drive_local'] # Obter o diretório de destino do arquivo config.json

            mover_arquivos(origem, destino) # Chamar a função para mover os arquivos do diretório de origem para o diretório de destino

        except Exception as e: # Tratar erros durante a execução do script, como problemas de leitura do arquivo config.json ou erros de movimentação dos arquivos
            print(f"Erro: {e}") # Exibir a mensagem de erro no console

        print("\nScript finalizado! Aguardando 10 minutos...")
        time.sleep(600) # Aguardar 600 segundos (10 minutos) antes de executar o script novamente