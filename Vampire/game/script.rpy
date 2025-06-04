label start:
    scene bg room

    "Você está conversando com Jenny na casa dela."

    menu:
        "Deixar beber sangue":
            jump deixar_beber
        "Não deixar beber sangue":
            jump nao_deixar

label deixar_beber:
    "Jenny te morde e bebe um pouco do seu sangue."
    # Tag "Mordida"
    "No caminho de volta para casa, você sente que está sendo seguido por alguém..."
    
    menu:
        "Confrontar":
            jump confrontar
        "Correr":
            jump correr

label nao_deixar:
    "Você recusa a oferta de Jenny."
    "No caminho de volta para casa, você sente que está sendo seguido por alguém..."

    menu:
        "Confrontar":
            jump confrontar
        "Correr":
            jump correr

label confrontar:
    "Você decide conversar com a figura sombria."
    "Você não sabe que ele é um vampiro ainda."
    "Ele não responde, apenas pergunta se você sente algo estranho."

    "De repente, ele te ataca ao sentir cheiro de 'ferrugem'."
    "Você o fere com um pedaço de madeira que achou no chão."
    "O vampiro desaparece na névoa."
    
    jump fim_ferido

label correr:
    "Você começa a correr desesperadamente."
    "Ele corre atrás de você."
    "Você é atropelado, mas não se machuca muito."
    "Seu amigo te leva pra casa e o vampiro some."

    jump fim_some

label fim_ferido:
    "Fim temporário: Vampiro é ferido."

    return

label fim_some:
    "Fim temporário: Vampiro some."

    return