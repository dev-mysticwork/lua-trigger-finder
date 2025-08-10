import os
import re

def search_triggers_in_file(filepath, output_filepath, filter_local_player=False):
    """
    Procura por linhas que começam com 'triggerEvent' ou 'triggerServerEvent'
    em um arquivo específico. Opcionalmente, filtra as linhas para incluir
    apenas aquelas que contêm 'localPlayer'.
    """
    found_lines = []
    trigger_pattern = re.compile(r"^(triggerEvent|triggerServerEvent)")

    if not os.path.isfile(filepath):
        print(f"Erro: O arquivo '{filepath}' não foi encontrado.")
        return

    try:
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as f_in:
            for line_num, line in enumerate(f_in, 1):
                stripped_line = line.strip()
                if trigger_pattern.match(stripped_line):
                    if filter_local_player:
                        if 'localPlayer' in stripped_line:
                            found_lines.append(stripped_line)
                    else:
                        found_lines.append(stripped_line)
    except Exception as e:
        print(f"Erro ao ler o arquivo {filepath}: {e}")

    try:
        with open(output_filepath, 'w', encoding='utf-8') as f_out:
            if found_lines:
                for line in found_lines:
                    f_out.write(line + '\n')
                print(f"Linhas encontradas salvas em '{output_filepath}'.")
            else:
                f_out.write("Nenhuma linha encontrada com os critérios especificados.\n")
                print("Nenhuma linha encontrada com os critérios especificados.")
    except Exception as e:
        print(f"Ocorreu um erro ao escrever no arquivo de saída: {e}")

if __name__ == '__main__':
    print("\n--- Ferramenta de Busca de Triggers --- ")
    print("Este script irá procurar por 'triggerEvent' ou 'triggerServerEvent' no arquivo 'test_code.lua'.")

    script_dir = os.path.dirname(os.path.abspath(__file__))
    input_file = os.path.join(script_dir, 'test_code.lua')

    if not os.path.exists(input_file):
        print(f"Erro: O arquivo 'test_code.lua' não foi encontrado na pasta do script ({script_dir}).")
        print("Por favor, certifique-se de que 'test_code.lua' está na mesma pasta que este script.")
    else:
        output_file_name = input("Digite o nome do arquivo de saída para salvar os resultados (ex: resultados_triggers.txt): ")
        output_filepath = os.path.join(os.getcwd(), output_file_name)

        while True:
            filter_option = input("Deseja filtrar apenas as linhas que contêm 'localPlayer'? (sim/não): ").lower()
            if filter_option in ['sim', 's']:
                filter_local_player = True
                break
            elif filter_option in ['não', 'nao', 'n']:
                filter_local_player = False
                break
            else:
                print("Opção inválida. Por favor, digite 'sim' ou 'não'.")

        search_triggers_in_file(input_file, output_filepath, filter_local_player)
        print("\nBusca concluída.")


