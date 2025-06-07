label start:
    
    scene blackbg

    "Eu estou no banheiro escovando o meu dente para ir dormir"
    "Mas eu começo a sentir que eu esqueci de algo importante"
    "que dia era hoje mesmo?"
    "..."
    "....."
    "!"
    "Amanhã é o aniversário da minha nanmorada"

    show Jenny happy:
        zoom 1.3
        xalign 0.5
    with dissolve1

    "Eu comprei para ela um colar"
    "Eu salvei o dinheiro dos ultimos dois meses para isso"
    "Mas recentemente ela ficou doente, e eu não parei de pensar nisso a semana toda. Eu acabei esquecendo do colar"
    "normalmente eu não ficaria muito preucupado. Mas sempre que eu ligo para ela se recusa a explicar o que ela têm."
    "Ela sempre dá uma meia resposta, ou diz que não é nada demais."
    "Eu sinto que tem algo diferente no jeito que ela fala comigo"

    hide Jenny happy
    with dissolve1
    "Com a quela doença se espalhando por ai eu estou preucupada que ela tenho pego algo ruim"
    "Talzes eu devesse ligar para os pais dela para..."

    play sound "audio/oldphone_ringtone.ogg" volume 0.8 fadeout 0.5
    "..."
    "hmm?"
    "São quase 9 da noite"
    "Quem..."
    j "Eu preciso de contar uma coisa MUITO importante."
    j "Me desculpa não poder dizer nada agora, mas eu preciso conversar com você cara-a-cara..."

    scene park with dissolve1

    "Estou quase na casa dela. Não é muito longe da minha rua, então eu consigo ir a pé."
    "A única coisa que me incomoda é ter que vir à noite. A Jenny me disse para vir nesse horário porque ela diz que ela não se sente muito bem de manhã."
    "Ultimamente nenhuma parte da cidade tem sido muito segura."

    scene sidewalk with dissolve1

    "Eu vi no noticiário que ontem a noite um grupo de bandidos foi passando de casa em casa pelos subúrbios, invadindo casas."
    "Se eu não for assaltado é possível que eu seja abordado pela polícia."
    "Essa é a última coisa que eu preciso agora. Eu não deveria ter saído a esse horário e os meus pais vão me matar se eles me verem voltando para casa"
    "Eu finalmente chego na casa da Jenny"

    scene greens house with dissolve1

    "Faz algum tempo que eu não vou na casa dela"
    "..."
    "Eu consigo ver ela acenando para mim da janela do quarto."

    show jenny
    show j happy
    with dissolve1
    "Ela abre a porta da casa e eu a sigo no escuro até o quarto"

    scene jennyroom 
    with dissolve1

    show jenny
    show j happy
    with dissolve1

    "..."
    "A jenny me guia para uma"
    "Eu sento"
    hide j happy
    show j sad
    with dissolve1
    
    "A Jenny me fala sobre a situação dela. Que ele passou vários dias ficando cada vez mais fraco e sofrendo de alucinações."
    "Ela está convencida de que ela não beber sangue essa noite ela sente que algo muito ruim vai acontecer com ela"
    "Eu sei que muitas das pessoas afetadas mencionam para os médicos sintomas de delírio e fome."
    "Uma sede insaciável de sangue"
    "Esse é um dos sintomas finais da doença e que se continuar ela levará a morte"
    
    $ variB = None
    menu:
        "Eu não sei se isso vai ajudar ou não, mas não tenho nenhuma ideia melhor."
        
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

        "Você recusa o pedido da Jenny."
        "você a assegura que as coisas vão ficar melhor"
        a "Eu vou tentar pegar algo do açugue que tenha sangue para te dar."
        a "O amigo do meu pai é açogueiro então eu acho que eu consigo algo"
        "Ela não parece se sentir muito melhor mas não há nada que eu possa fazer no momento. Eu abraço a Jenny e prometo ver ela no dia seguinte"
        
    
    scene sidewalk with dissolve1

    "O caminho devolta para cas apesar de não ser muito longo me dá calafrios"
    "A vizinhança é um breu quase total fora das luzes dos postes. Se algo estivesse me seguindode lçonge eu não notaria"
    "Por extinto eu olha para tras, esperando algo."
    "..."
    "Para minha surpresa tem alguém."
    "parece um homen ele está longe demais para ver quem é. Eu sinto que ele está me seguindo. Não tem mais ninguém aqui."

    $ variB = None
    menu:
        "Eu deveria..."

        "Confronta-lo (Chamar a atenção dele)":
            jump confrontar
        "Correr":
            jump correr

label confrontar:

    scene sidewalk with dissolve1

    "Eu decide conversar com a figura sombria."
    a "Ei!."
    "..."
    "Ele não responde, ele apenas fica parado e depous de um tempo começa a se aproximar"

    show vampire
    show v neutral
    with dissolve
    "..."
    "Tem algo de errado com ele."
    "Ele se aproxima mais."
    "*continuar aqui."
    
    jump ferido

label correr:
    "Você começa a correr desesperadamente."
    "Ele corre atrás de você."
    "Você é atropelado, mas não se machuca muito."
    "Seu amigo te leva pra casa e o vampiro some."

    jump some