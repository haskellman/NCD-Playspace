# NCD PlaySpace

## Execução

Para Executar o jogo.


1. Abra um terminal ou prompt de comando.
2. Execute o seguinte comando:

```docker compose up -d```

* Esse comando criara um container docker e instalará todas as dependencias necessárias
e rodará o aplicativo.
* Vá para ```http://localhost:3333 ``` para visualizar o app, está versão rodará o programa
na versão web que tem alguns bugs visuais

## Para Rodar Localmente
1. Vá Até o diretório com o código fonte

```cd .\src\main\python\playspace\```

2. Instale as dependencias
```pip install -r requirements.txt```

3. Run!
```flet -r main.py```

## Desenvolvedores
- Israel dos Santos Candeias, Gabriel Paschoal

### Limitações Relevantes:
- Os jogos não estão na nuvem, eles dependem do python e pygame para rodarem

### Propostas de Melhoria:
- Usar um framework para autenticação mais confiavel
- Utilizar flask para banco de dados
- Colocar os jogos do pygame na nuvem

