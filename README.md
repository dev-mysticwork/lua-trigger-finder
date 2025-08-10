# Lua Trigger Finder

Um script em **Python** para escanear o arquivo `test_code.lua` e encontrar chamadas de `triggerEvent` e `triggerServerEvent`.  
Também é possível filtrar para exibir apenas as linhas que contenham `localPlayer`.

Você pode **escolher o nome do arquivo de saída** (por exemplo: `save.txt`) para salvar os resultados.

## 📌 Funcionalidades

- Busca por `triggerEvent` e `triggerServerEvent` no arquivo `test_code.lua`
- Filtro opcional para encontrar apenas linhas com `localPlayer`
- Permite escolher o nome do arquivo `.txt` onde os resultados serão salvos

## 🚀 Como usar

1. Clone este repositório:
   ```bash
   git clone https://github.com/seu-usuario/lua-trigger-finder.git
2. Entre na pasta do projeto:
   ```bash
   cd lua-trigger-finder
3. Coloque seu código Lua no arquivo test_code.lua (mesma pasta do script).

4. Execute o script:
   ```bash
   python trigger_finder.py
5. Informe no terminal:
 - O nome do arquivo .txt para salvar os resultados
