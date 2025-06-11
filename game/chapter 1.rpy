﻿label start:
    play music "audio/Music/ghosts1.ogg" fadein 7 fadeout 4 volume 0.7 
    scene blackbg
    "Eu estou no banheiro escovando o meu dente para ir dormir."
    "Eu começo a sentir que eu esqueci de algo importante."
    "que dia era hoje mesmo?"
    "..."
    "!"
    "Amanhã é o aniversário da minha namorada."


    show Jenny happy:
        zoom 1.3
        xalign 0.5
    with dissolve1


    "Eu comprei para a Jenny um colar."
    "Eu salvei o dinheiro dos últimos dois meses trabalhando meio período numa loja de conveniências."
    "Mas recentemente ela ficou doente, e eu não parei de pensar nisso a semana toda. Eu acabei esquecendo do colar."
    "Normalmente eu não ficaria muito preocupado, mas sempre que eu ligo para ela se recusa a explicar o que ela têm."
    "Ela sempre dá uma meia resposta, ou diz que não é nada demais."
    "Ela não costuma falar assim comigo. A Jenny sempre me conta tudo e eu sempre conto tudo para ela."
    "É um hábito nosso. Eu nunca tinha sequer parado para pensar muito nisso até recentemente."
    "Talvez seja só paranoia. Mas ainda sim."


    hide Jenny happy
    with dissolve1
    "Eu não consegui comer ontem. Tudo que me vem à cabeça é a Jenny e o maldito noticiário matinal."
    "Algo sobre o centro da cidade ter sido interditado pela guarda nacional. Meu amigo Paul disse que tem algo haver com uma doença. Um tipo de quarentena."
    "Eu disse para ele que não fazia sentido nenhum aquilo, que se fosse uma doença séria a ponto de precisar parar parte da cidade nós já teríamos sido avisados, provavelmente pelo prefeito ou algo assim."
    "Mas agora eu não consigo parar de pensar na possibilidade."
    "É plausível que a Jenny tenha pego algo do pai voltando do trabalho."
    "Acho que é melhor simplesmente ligar para os pais dela e perguntar se..."
 
    play sound "audio/Sounds/oldphone_ringtone.ogg" volume 0.9 fadeout 0.5
    pause
    "hmm?"
    a "São quase 9 da noite"
    a "Quem..."
    "Eu vou para a sala em direção ao telefone"
    "...É a Jenny"
    j "Eu preciso de contar uma coisa MUITO importante."
    j "Me desculpa não poder dizer nada agora, mas eu preciso conversar com você cara-a-cara AGORA..."
    "Eu faço mais perguntas mas ela se recusa a responder. Sem opção, eu pego o meu casaco e vou em direção a casa da Jenny."


    scene park with dissolve1


    "Eu passo pelo parque perto da minha casa. Eu sempre faço o mesmo caminho para a casa da Jenny. O lugar já é bem familiar para mim, mas é bem mais intimidador no escuro da noite."
    "Ainda assim, minhas dúvidas tomam boa parte da minha atenção. Vários cenários passam na minha cabeça sobre o que poderia estar acontecendo."
    "A Jenny me implorou no telefone para não contar nada para ninguém e vir o mais rápido possível."


    scene sidewalk with dissolve1
    "Poderia ser alguma emergência médica? Não, improvável, O pai dela é médico, se ela estivesse doente ela com certeza teria contado algo para ele, não?"
    "Talvez ela esteja escondendo algo de ruim que ela acha que ela fez? mas o que eu poderia fazer por ela? Eu faria algo, com certeza, mas ainda assim..."
    "As possibilidades inundam os meus pensamentos conforme eu me aproximo da casa dela."
    scene greens house with dissolve1
    pause
    "Faz algum tempo que eu não visito a Jenny na casa dela."
    "Eu consigo ver ela acenando para mim na entrada da casa."
    "No momento eu quase me esqueço do porque eu estava lá."


    show jenny
    show j happy
    with dissolve1
    "Ela sorri para mim mas tem algo de errado. Faz um gesto para eu entrar e eu a sigo no escuro até o quarto."
    scene jennyroom
    with dissolve1


    show jenny
    show j happy
    with dissolve1
    pause


    "É o quarto dela. Eu nunca vi ele antes. Eu só cheguei a almoçar com a família dela. Uma das paredes está repleta de posters de bandas e atores."
    "Assim que eu entro ela rapidamente tranca a porta atrás de mim, e a expressão dela fica mais tensa."

    hide j happy
    show j sad
    with dissolve1
   
    "E como se toda força que ela tentou mostrar momentos atrás esvaziasse dela."
    j "Eu…nem sei por onde começar."
    "Também sem saber o que dizer, e notando que ela parece que vai chorar eu abraço a Jenny"
    "A noite foi bem longa. A Jenny me conta como foi a sua última semana e porque ela não me ligou nenhuma vez naquele tempo."
    "Que ela me disse que tem passado pelo pior momento da vida dela. O pai dela aparentemente pegou algo no trabalho que o deixou internado num hospital pelas últimas 2 semanas, e que ultimamente ela vem se sentido muito mal."
    "Começou com um cansaço durante a manhã que ficou cada vez mais intenso conforme os dias passavam. Ela cogitou contar para a sua mãe o que estava acontecendo, mas quando as alucinações começaram ela mudou de ideia."
    j "Eu não sei o que fazer, às vezes eu ouço alguém à noite. Como se tivesse alguém no meu quarto."
    j "Eu sei que isso não é real, mas me assusta toda vez. Eu nem consigo mais dormir durante a noite e essas vozes e sons estão me levando à loucura. Elas me dizem para fazer coisas também…"
    "Eu não sei o que dizer, eu quero confortá-la, mas eu não sei se ela está no melhor estado."
    "Ela também me diz que sua mãe foi visitar uma amiga do outro lado da cidade e ela não quis passar a noite sozinha."


    "Talvez eu possa passar a noite com ela, eu não sei o que eu faria depois, mas eu não posso deixar ela sozinha numa casa vazia ouvindo sons e vozes estranhas."
    "Mas se ela pegou alguma doença do pai dela trabalhando no centro da cidade então talvez essa não seja a melhor ideia."

    
    $ variB = None
    menu:
        j "Adam?."
        
        "Eu posso passar a noite com você. Se isso vai te fazer se sentir melhor":
            jump escolha1_deixar_beber
        "Jenny, você precisa de atendimento médico.":
            jump escolha1_nao_deixar

    label escolha1_deixar_beber:

        $ mordida = True

        j "Obrigada."
        "Uma expressão de alívio passa pelo seu rosto, enquanto ela se senta na cama."
        j "Eu tenho ficado tão sozinha ultimamente, mas eu não aguentava guardar isso só pra mim; eu tive medo que se alguém descobrisse eu seria colocada em um hospital contra a minha vontade."
        j "Quando a minha mãe disse que iria sair de casa eu entrei em pânico. Eu liguei pra você logo depois dela sair."
        menu:
            "Porque você não contou pra mim?":
                j "porque, eu... não sei...eu..."
                "Eu sinto algum arrependimento de ter perguntado."
                "Ela devia estar com medo que eu ligasse para os pais dela, mesmo que só por preocupação."
                "Mas não é como se a situação dela fosse melhorar repentinamente a esse ponto."
                "Ela precisa de ajuda profissional. Não tem muito que eu possa fazer por mim mesmo."
                pause
                "Não tem razão pra questionar agora. Ela precisa de ajuda agora, não julgamento."
                "Amanhã eu vou tentar convencer ela a ir para o hospital. Eu posso pedir para o meu amigo Paul levar a gente."

            "*apenas abraçar a Jenny*":
                "Eu abracei ela por um bom tempo. Não sei se nada que eu falar vai melhorar a situação."
                "Ela precisa de mim agora e eu não preciso preocupar ela com a possibilidade de ser levada para um sanatório."
                "É a doença, eu tenho certeza."
                "Talvez eu consiga convencer ela ir ao hospital amanhã. Eu posso pedir para o meu amigo Paul levar a gente."
                "Mas agora a melhor coisa é tentar confortá-la."

        "Eu deito num colchão improvisado com vários cobertores e travesseiros. Não é muito confortável, mas eu não acho uma boa ideia dormir na mesma cama que a Jenny."
        "Eu sei que ela fica muito nervosa com esse tipo de intimidade às vezes, mas é ainda pior nessas situações."
        "Mas ela me surpreende"
        j "você pode deitar comigo um pouco?"
        j "Até eu dormir pelo menos. Você pode voltar para o chão depois se quiser mas eu não me importo se você quiser ficar."
        "Sem pensar muito eu aceito e subo na cama junto dela."
        pause
        "Nós estamos deitados juntos na cama. Eu fico atrás dela com o meu braço sobre o seu corpo segurando a mão dela."
        "Apesar da posição ser bem íntima, eu sinto mais do que qualquer coisa uma certa...satisfação?"
        "Tem algo bem confortante em saber que eu estou ajudando a Jenny simplesmente por estar aqui."
        "Que no momento de maior fraqueza dela ela confiou em mim para ficar com ela."
        "Eu não sei o que vai acontecer amanhã, mas eu sei que ela vai confiar em mim."
        "Esse sentimento me conforta conforme o sono vai tomando conta de mim."
        pause
        a "hm?"
        "Eu acordei, mas ainda é de noite."
        "Eu olho para a minha direita, a Jenny parece que conseguiu cair no sono."
        "Eu puxo o meu braço debaixo do pescoço da Jenny. Ele ficou dormente por ter sido espremido por muito tempo."
        "Quando eu recupero a minha circulação eu olho para o meu relógio de pulso."
        "Já tá bem tarde. Eu deveria voltar para casa, não é uma boa ideia voltar de manhã e ser interrogado pelos meus pais."
        "Eu arrumo minhas coisas e saio. Mas antes eu dei um beijo na testa da Jenny."
        jump sidewalk_encounter
        

    label escolha1_nao_deixar:
    
        $ mordida = False

        "Ela engole seco."
        jump sidewalk_encounter
       
        
label sidewalk_encounter:
    
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
        "Ele não responde, ele apenas fica parado e depois de um tempo começa a se aproximar"

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