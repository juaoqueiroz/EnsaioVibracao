import os
import csv

def substituir_tabs_virgulas_e_virgulas_pontos(pasta_origem, pasta_destino, headers=None):
    # Verifica se os caminhos são pastas válidas
    if not os.path.isdir(pasta_origem):
        print(f"O caminho '{pasta_origem}' não é uma pasta válida para a origem.")
        return
    if not os.path.isdir(pasta_destino):
        print(f"O caminho '{pasta_destino}' não é uma pasta válida para o destino.")
        return
    
    # Loop através dos arquivos na pasta de origem
    for nome_arquivo in os.listdir(pasta_origem):
        caminho_arquivo_origem = os.path.join(pasta_origem, nome_arquivo)
        
        # Verifica se é um arquivo de texto
        if os.path.isfile(caminho_arquivo_origem) and nome_arquivo.endswith('.csv'):
            with open(caminho_arquivo_origem, 'r') as arquivo:
                conteudo = arquivo.read()
            
            # Substitui os caracteres
            conteudo_modificado = conteudo.replace(',', '.').replace('\t', ',')
            
            # Cria o nome do arquivo de destino com extensão .csv
            nome_arquivo_destino = os.path.splitext(nome_arquivo)[0] + '.csv'
            caminho_arquivo_destino = os.path.join(pasta_destino, nome_arquivo_destino)
            
            # Escreve o conteúdo modificado no arquivo de destino
            with open(caminho_arquivo_destino, 'w') as arquivo_destino:
                arquivo_destino.write(conteudo_modificado)
                
            print(f"Arquivo '{nome_arquivo}' modificado e salvo como '{nome_arquivo_destino}'.")
            
            # Adiciona headers se fornecidos
            if headers:
                with open(caminho_arquivo_destino, 'r+') as arquivo_destino:
                    conteudo_com_headers = ','.join(headers) + '\n' + conteudo_modificado
                    arquivo_destino.seek(0)
                    arquivo_destino.write(conteudo_com_headers)
                
                print(f"Headers adicionados ao arquivo '{nome_arquivo_destino}'.")
                
        else:
            print(f"O arquivo '{nome_arquivo}' não é um arquivo CSV (.csv).")

# Exemplo de uso
pasta_origem = r'C:\Users\LIAE\Desktop\PRH\Projetos\AquisicaoVibracao\Data\BruteData\Ensaio_2023-12-19_1\SW20P'
pasta_destino = r'C:\Users\LIAE\Desktop\PRH\Projetos\AquisicaoVibracao\Data\DatasetEnsaios\Ensaio_2023-12-19_1\SW20P'
headers = ['tempo', 'vibracao', 'tensao']  # Adicione seus headers aqui

substituir_tabs_virgulas_e_virgulas_pontos(pasta_origem, pasta_destino, headers)
