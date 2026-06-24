import os 
def listar_arquivos(pasta):
    """
    Função que lista o nome dos arquivos e retorna eles separados
    individualmente por linhas.
    """
    arquivos = os.listdir(pasta)
    return arquivos

def transformar_nome(nome):
    """
    função que troca o nome dos arquivos
    """
    nome_alt = nome.strip().lower().replace(' ', '_')
    return nome_alt
    
def renomear(caminho):
    """
    Função que usa duas funções para buscar o caminho e renomear o
    nome do arquivo
    """
    arqv_list = []
    for item in listar_arquivos(caminho):
        ori = os.path.join(caminho,item)
        new = os.path.join(caminho , transformar_nome(item))
        arqv_list.append({'original':item,'novo':transformar_nome(item)})
        print(f'De original: {ori} para Novo: {new}')
        os.rename(ori,new)
    return arqv_list
    
resultado = renomear('/Users/guzazo/Downloads/teste')


def gerar_relatorio(lista):
    arq = {}
    print('Relatório')
    total = len(lista)
    for arq in lista:
        print(f"Original: {arq['original']} Novo: {arq['novo']}") 
    print(f'Quantidade de arquivos: {total}')

gerar_relatorio(resultado)



