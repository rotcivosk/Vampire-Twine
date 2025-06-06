label start:
    
    scene blackbg
    
    "Você está conversando com Jenny na casa dela."
    show jenny
    show j happy
    j "eae"

    scene jennyroom

    show jenny
    show j sad
    j "entendi"
    
    $ variB = "left"
    menu:
        "Ela te faz uma pergunta que te pega de surpresa"
        
        "Deixar beber sangue":
            jump escolha1_deixar_beber
        "Não deixar beber sangue":
            jump escolha1_nao_deixar

    label escolha1_deixar_beber:

        $ mordida = True
        $ renpy.notify("Você tem uma mordida na sua mão esquerda")

        "Jenny te morde e bebe um pouco do seu sangue."

    label escolha1_nao_deixar:
    
        $ mordida = False

        "Você recusa a oferta de Jenny."
        "No caminho de volta para casa, você sente que está sendo seguido por alguém."

    $ variB = None
    menu:
        "Eu deveria..."

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
    
    jump ferido

label correr:
    "Você começa a correr desesperadamente."
    "Ele corre atrás de você."
    "Você é atropelado, mas não se machuca muito."
    "Seu amigo te leva pra casa e o vampiro some."

    jump some