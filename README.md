# Análise de Sentimentos com spaCy

## Integrantes
- Nome: Leonardo Zago G Ferreira
- RM: 558691

## Descrição
Este projeto realiza análise de sentimentos em frases em português utilizando o spaCy, com regras personalizadas usando PhraseMatcher e extensões no objeto Doc. O script detecta palavras positivas e negativas, classifica o sentimento da frase e imprime o resultado.

## Como funciona
1. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```
2. Baixe o modelo de português do spaCy:
   ```bash
   python -m spacy download pt_core_news_sm
   ```
3. Execute o script principal:
   ```bash
   python sentiment_analysis.py
   ```

O script irá analisar uma lista de frases e imprimir o sentimento de cada uma (Positivo, Negativo, Misto ou Neutro).

## Explicação do código
- Utiliza o spaCy e PhraseMatcher para identificar palavras positivas e negativas.
- Adiciona uma extensão personalizada ao objeto `Doc` chamada `sentimento`.
- Analisa frases e imprime o sentimento detectado para cada uma.
