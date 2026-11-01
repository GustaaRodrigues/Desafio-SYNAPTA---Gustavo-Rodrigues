import os
import pandas as pd

def encontrar_arquivo():
    # Lista de nomes possíveis para o arquivo
    nomes_possiveis = ['data (1).xlsx', 'data.xlsx', 'data (1).csv', 'data.csv']
    
    # Locais prováveis onde o arquivo pode estar no Windows
    desktop = os.path.join(os.path.expanduser('~'), 'Desktop')
    downloads = os.path.join(os.path.expanduser('~'), 'Downloads')
    pastas_busca = ['.', desktop, downloads]
    
    for pasta in pastas_busca:
        for nome in nomes_possiveis:
            caminho_completo = os.path.join(pasta, nome)
            if os.path.exists(caminho_completo):
                print(f"✅ Arquivo encontrado em: {caminho_completo}")
                return caminho_completo
                
    raise FileNotFoundError("Nenhum arquivo 'data (1).xlsx' ou 'data.xlsx' foi encontrado na pasta atual, Área de Trabalho ou Downloads.")

# 1. Localizar o arquivo automaticamente
caminho_arquivo = encontrar_arquivo()

# 2. Ler o arquivo (suporta .xlsx e .csv)
if caminho_arquivo.endswith('.csv'):
    df_bruto = pd.read_csv(caminho_arquivo, header=None, on_bad_lines='skip')
else:
    df_bruto = pd.read_excel(caminho_arquivo, header=None)

# Função para corrigir caracteres com acentuação corrompida (mojibake)
def corrigir_acentos(texto):
    if isinstance(texto, str):
        try:
            return texto.encode('latin1').decode('utf-8')
        except (UnicodeEncodeError, UnicodeDecodeError):
            return texto
    return texto

linhas_tratadas = []

for idx, linha in df_bruto.iterrows():
    # Ignorar a linha de cabeçalho original se contiver o nome das colunas
    if idx == 0 and str(linha[0]).lower().startswith('address'):
        continue
    
    itens = [str(val).strip() for val in linha.dropna() if str(val).strip() != '']
    if not itens:
        continue

    try:
        total = float(itens[-1])
        rent = float(itens[-2])
        tipo = itens[-3]
        garage = int(float(itens[-4]))
        bedrooms = int(float(itens[-5]))
        area = float(itens[-6])
        
        sobra_esquerda = itens[:-6]
        if len(sobra_esquerda) == 1:
            address = sobra_esquerda[0]
            district = ""
        else:
            address = ", ".join(sobra_esquerda[:-1])
            district = sobra_esquerda[-1]
            
        linhas_tratadas.append({
            'address': address,
            'district': district,
            'area': area,
            'bedrooms': bedrooms,
            'garage': garage,
            'type': tipo,
            'rent': rent,
            'total': total
        })
    except Exception:
        continue

# 3. Criar DataFrame limpo e alinhado
df_limpo = pd.DataFrame(linhas_tratadas)

# 4. Corrigir acentuação
for col in ['address', 'district', 'type']:
    df_limpo[col] = df_limpo[col].apply(corrigir_acentos)

# 5. Salvar na pasta do projeto SYNAPTA
df_limpo.to_excel('data_organizado.xlsx', index=False)
df_limpo.to_csv('data_organizado_utf8.csv', index=False, encoding='utf-8-sig')

print("🎉 Processamento concluído! Os arquivos 'data_organizado.xlsx' e 'data_organizado_utf8.csv' foram criados na sua pasta SYNAPTA.")