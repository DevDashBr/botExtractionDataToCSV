import sys

print(f'Versão do python: {sys.version_info.major}')

# Verificar se as bibliotecas utilizadas pelo projeto estão instaladas
try:
    # Exemplo
    import selenium
    print("A biblioteca selenium está instalada!")
except Exception as e:
    print("A biblioteca selenium não está instalada. Favor verificar!")
    raise Exception(f"Descrição do erro: {e}.")
