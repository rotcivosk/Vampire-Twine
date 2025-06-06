#texto
define a = Character("Adam", color="#ffffff")
define j = Character("Jenny", color="#ffffff")
define d = Character("Dad", color="#ffffff")
define s = Character("Sister", color="#ffffff")
define p = Character("Paul", color="#ffffff")
define o = Character("Police Officer", color="#ffffff")

#

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
