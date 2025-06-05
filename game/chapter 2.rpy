label ferido:

    "2 semanas se passaram desede de o incidente. Você voltou para casa em uma viatura da polícia."

    "Você está de castido a uma semana o resto do Ato 2"

    if mordida:
        "Você começa a ter os primeiros sinais de vampismo."

        "Cançaso, aversão a luz do dia e uma sede e fome insafiável e repentina. Sua irmã comenta na sua condição /(A escola dela foi cancelada pela semana por uma inspeção de quarentena no bloco/)."

    else:
        "Você tenta ligar para a Jenny para saber como ela está, mas ela não atende."

    "Já de noite alguém está do lado de fora de sua casa. Olhando da janela você reconhece o homen que te atacou."

    "Ele parece ter a camisa rasgada, com sangue escorrendo do seu torso."

    "O homen tenta entrar em sua casa, tentando forçar a porta."

    menu:
        "O que eu faço? Preciso pensar rápido."

        "Confrontar o estranho com um taco de baisebol":
            jump confrontar_visitante

        "Sair de casa pelo quintal":
            jump sair_de_casa

label some:

    "2 semanas se passaram desede de o incidente. Você voltou para casa sem os seus pais notarem que você fugiu de noite."
    "Você vai direto para a casa do seu amigo e fala do seu encontro com o “estranho”."
    "Seu amigo te fala das coisas estranha que vem acontecendo na cidade e como ele acha que as autoridades estão escondendo as coisas"

    if mordida:

        "Você começa a ter os primeiros sinais de vampirismo."

        "Cançaso, aversão a luz do dia e uma sede e fome insafiável e repentina. Enquanto você e seu amigo conversão você bebe todo o leite e suco da geladeira dele."

        "Ele comenta sobre o seu conportamento estranho. Você passa mal mais tarde e ele descide dirigir você de volta para a sua casa já no final da tarde."

    else:

        "Você tenta ligar para a Jenny para saber como ela está, mas ela não atende."
    
        "Você volta para casa e um policial está caido no meio da rua." 
        "O uniforme dele está ensaguentado, mas parece que ele ainda está respirando." 

    menu:
        "Talvez ainda seja possivel salva-lo."

        "Ajudar policial":
            jump ajudar_policial

        "Continuar dirigindo":
            jump continuar_dirigindo

