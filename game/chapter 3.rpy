label confrontar_visitante:
    $ amigo = False

    "Eu chuto a porta derrubando a criatura e começo a ataca-lo."
    "Mas antes que eu pudesse fazer mais algum estrago eu sou puxado para o grama por outro par de mãos cinzentas."
    "Quando tento me levantar e olhar ao meu redor eu noto que estou cercado."

    if mordida:
        jump jenny_te_ajuda

    else:
        jump jenny_nao_te_ajuda


label ajudar_policial:

    $ amigo = True

    "Você são imediatamente atacados por vampiros."

    "Os vampiros te cercam e você não é páreo para eles"

    if mordida:
        jump jenny_te_ajuda

    else:
        jump jenny_nao_te_ajuda

return

#intercessão
label jenny_te_ajuda:

    "A Jenny está entre os vampiros, e ela consegue te proteger ao chamar a atenção deles para a sua mordida."
    if amigo:
        jump final_2_2

    else:
        jump final_2_1    

label jenny_nao_te_ajuda:

    "A Jenny está entre os vampiros, mas ela não tem como ajuda-lo. Você é apenas um humano."

    if amigo:
        jump final_1_2

    else:
        jump final_1_1

#final 1-1 -Você é morto (sozinho)
label final_1_1:

    "Morri."

    return
#final 1-2 -Você é morto (com amigo)
label final_1_2:

    "Ao menos não morri sozinho."

    return
#final 2-1 -Você sobrevive
label final_2_1:

    "sobrevivi."

    return
#final 2-2 -Você sobrevive (e seu amigo também)
label final_2_2:

    "sobrevive com o meu amigo Paul."

    return

#----------------------

label continuar_dirigindo:

    "Seu amigo vai para outra parte do bairro evitando a sua rua."

    if mordida:

        jump salvos
    else:

        jump eu_sou_vampiro

label salvos:
    if amigo:

        jump final_3_1
    
    else:

        jump final_3_2

label eu_sou_vampiro:
    if amigo:

        jump final_4_2

    else:

        jump final_4_1

label sair_de_casa:

    "Vocês se afastam o maximo possível das casa da sua rua."

#Final 3-1 -Vocês são salvos (amigo)
label final_3_1:

    "Fomos salvos Paul."

    return

#Final 3-2 -Vocês são salvos (irmã)
label final_3_2:

    "Fomos salvos Cheryl."

    return

#Final 4-1 -Você mata (sua irmã)
label final_4_1:

    "Eu acabo matando a minha irmã, porque...vampiro."

    return

#Final 4-2 -Você mata (seu amigo)
label final_4_2:

    "Eu acabo matando o Paul, porque...vampiro."

    return