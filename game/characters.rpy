#Names
define a = Character("Adam", color="#ffffff")
define j = Character("Jenny", color="#ffffff")
define d = Character("Dad", color="#ffffff")
define s = Character("Sister", color="#ffffff")
define p = Character("Paul", color="#ffffff")
define o = Character("Police Officer", color="#ffffff")

define nrt = Character(ctc="ctc_blink", ctc_position="nestled")

#Characters images
layeredimage Jenny:
    always:
        "images/characters/Jenny/jenny.png"
    
    group espressions:
        attribute neutral default:
            "images/characters/Jenny/j neutral.png"
        attribute happy:
            "images/characters/Jenny/j happy.png"


#Text align
default variB = "left"

screen choice(items):
    style_prefix "choice"

    vbox:

        if variB == "left":
            xalign 0.0
        if variB == "right":
            xalign 1.0

        for i in items:
            textbutton i.caption action i.action


#transitions

define dissolve1 = Dissolve(0.5)

#Animations
image ctc_blink:
    zoom 0.8 center
    "images/icons/ctc01.png"        
    linear 0.5 alpha 1.0    
    "images/icons/ctc01.png"         
    easeout 1.0 alpha 0         
    "images/icons/ctc01.png"        
    linear 0.5 alpha 0         
    "images/icons/ctc01.png"        
    easeout 1.0 alpha 1.0    
    repeat
