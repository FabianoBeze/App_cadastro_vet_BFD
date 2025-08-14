Aplicativo simples para cadastrar, listar, editar e remover **animais** com interface **Tkinter** e persistência em **JSON**.

O arquivo `animais.json` será criado automaticamente na mesma pasta (com backup automático se o JSON estiver corrompido).

## Funcionalidades
- **Cadastrar**: novo animal
- **Listar**   : em tabela 
- **Editar**   : selecione uma linha, altere os campos e clique **Salvar edição (selecionado)**
- **Remover**  : selecione uma linha e clique **Remover (selecionado)**
- **Recarregar do JSON**: lê novamente o arquivo do disco
- Validação de idade e campos obrigatórios
- Tratamento para **JSON vazio/corrompido** (cria backup `.bak`)

## Estrutura dos dados (JSON)
Cada animal é um objeto com:json

  "id": 1
  "nome" Rex
  "especie": Cachorro
  "idade": 4
  "contato": 31999990000
  "procedimento": Vacina V10


## Dicas
- Dê duplo clique numa linha para carregar os dados nos campos (facilita edição).
- O ID é gerado automaticamente e nunca é reutilizado.
- Se você já tiver um animais.json, ele será lido e os registros vão aparecer na tabela.