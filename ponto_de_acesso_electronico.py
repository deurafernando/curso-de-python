identidade=input("Qual é o número do seu B.I?")
resultado=identidade.strip()
base_de_dados={
    "004843261LA049":
    {
        "nome":"Joice Calunga",
        "curso":"Curso de python",
        "computador":"Mediateca"
        }
    }

aluna=base_de_dados.get("resultado")
if aluna:
    print("A aluna foi encontrada com sucesso")
    hora_de_entrada=input("Hora de entrada")
else:
    print("O B.I não corresponde a nenhuma aluna")
    
 
