import spacy
from spacy.matcher import PhraseMatcher
from spacy.tokens import Doc

# Listas de palavras positivas e negativas
palavras_positivas = ["feliz", "alegre", "ótimo", "excelente", "bom", "maravilhoso", "adoro"]
palavras_negativas = ["triste", "horrível", "péssimo", "ruim", "detesto", "chateado", "terrível"]

# Inicializa o nlp e o matcher fora do getter
nlp = spacy.load("pt_core_news_sm")
matcher = PhraseMatcher(nlp.vocab, attr="LOWER")
matcher.add("POSITIVO", [nlp.make_doc(texto) for texto in palavras_positivas])
matcher.add("NEGATIVO", [nlp.make_doc(texto) for texto in palavras_negativas])

# Função para classificar sentimento

def detectar_sentimento(doc):
    matches = matcher(doc)
    positivo = False
    negativo = False
    for match_id, start, end in matches:
        string_id = doc.vocab.strings[match_id]
        if string_id == "POSITIVO":
            positivo = True
        elif string_id == "NEGATIVO":
            negativo = True
    if positivo and not negativo:
        return "Positivo"
    elif negativo and not positivo:
        return "Negativo"
    elif positivo and negativo:
        return "Misto"
    else:
        return "Neutro"

# Adiciona a extensão personalizada ao Doc
Doc.set_extension("sentimento", getter=detectar_sentimento, force=True)

def main():
    frases = [
        "Estou muito feliz com o resultado!",
        "O dia está horrível e estou chateado.",
        "O almoço estava ótimo, mas o atendimento foi péssimo.",
        "Nada de especial aconteceu hoje.",
        "Adoro quando tudo dá certo!"
    ]

    for frase in frases:
        doc = nlp(frase)
        print(f"Frase: {frase}\nSentimento detectado: {doc._.sentimento}\n")

if __name__ == "__main__":
    main()
