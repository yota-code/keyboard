cat /usr/share/X11/xkb/keycodes/evdev

http://www.typematrix.com/support/user-guide.php

http://www.lexique.org/ et https://github.com/WhiteFangs/lexique.sql
https://maximilian.schalch.de/2018/05/complete-list-of-european-special-characters/

xev permet d'interroger les keycode des touches du clavier

    KeyPress event, serial 35, synthetic NO, window 0x1a00001,
        root 0x4b9, subw 0x0, time 1316378223, (1295,-69), root:(1365,1440),
        state 0x0, keycode 24 (keysym 0x61, a), same_screen YES,
        XLookupString gives 1 bytes: (61) "a"
        XmbLookupString gives 1 bytes: (61) "a"
        XFilterEvent returns: False

Les layouts par langue sont décrit dans cat /usr/share/X11/xkb/symbols/fr
Le lien entre le code xkb et le keycode retrourné par xev se trouve ici /usr/share/X11/xkb/keycodes/evdev

	<AD01> = 24;


