# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
image BG Black = "BlackBG.png"
image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
image BadEnd = "Bad End.png"
image GoodEnd = "Good End.png"
image YouAreDead = "You Are Dead.png"

# Declare characters used by this game.
define e = Character('John', color="#c8ffc8")
define s = Character('Sarah', color="#9A0000")
define r = Character('Reporter', color="#808080")
define o = Character('Officer', color="#808080")

# Timer
transform alpha_dissolve:
    alpha 0.0
    linear 0.5 alpha 1.0
    on hide:
        linear 0.5 alpha 0
    # This is to fade the bar in and out, and is only required once in your script

screen countdown:
    timer 0.01 repeat True action If(time > 0, true=SetVariable('time', time - 0.01), false=[Hide('countdown'), Jump(timer_jump)])
    bar value time range timer_range xalign 0.5 yalign 0.9 xmaximum 300 at alpha_dissolve
init:
    $ timer_range = 0
    $ timer_jump = 0

# The game starts here.

label start:

    play music "Relaxing Music - Winter Breath.mp3"

    scene BG Black
    with fade

    "I sent the text to my friend, Max."

    $ renpy.movie_cutscene("video/Introphonefinal.mp4", delay=None, loops=0, stop_music=False)

    scene BG Black
    with fade

    "The bus was already 20 minutes late."

    "It was late November . . . and it was cold."

    play movie "video/Frozenbg.mp4" loop
    show movie with dissolve

    "So damn cold."

    "My eyes burned against the outside air, and each intake of breath was like swallowing razor blades."

    "Everything was dim, tinted a dull blue, and all was eerily still, seemingly frozen in time."

    "Mercury in the thermometers had settled to the bottom, stagnant and crystaline."

    "I could see my breath as it shimmered against the thin air, warping and climbing upwards in despair before vanishing."

    "Even the trees, long dead, with crooked, empty limbs, appeared to be shaking against the cold."

    "Frost and ice glinted sharply in the faded sunlight, clinging on and threatening to overtake the trees."

    "The occasional glimmer of sunlight seemed so distant, its hazy blue glow so utterly small and insignificant against the frozen vastness."

    "The crunch of snow could be heard as I walked - a crisp, sharp sound cutting through what was otherwise dead silence."

    hide movie with dissolve
    stop movie

    "I stopped for a minute."

    "It seemed as if I was the only one in this world . . ."

    ". . . a world of cold, of stillness, of nothingness."

    "Neither the heat of a friend, nor the joy of their company existed here."

    "I was taking a note of all this with my eyes closed, so as the keep them from freezing, when I began to hear the crunching of snow."

    play movie "video/Sarahwalkloopfinal.mp4" loop
    show movie with dissolve

    "Huh? Sarah? Strange for her to be late."

    "I always met her at the bus stop . . . or at least had been for the past week or so."

    "I was glad of it too."

    "I used to hang out with my good friend Jenna, but she hadn't been showing up for the past week . . ."

    ". . . and now it was just Sarah to keep me company."

    "She was absolutely beautiful . . . sweet and funny too, but for some reason . . ."

    "I never really saw her with any friends."

    "I suppose this was because she had just moved here to Colorado."

    "That, and because all the guys I knew were too afraid to even talk to her."

    "I guess that's why she was stuck with me all the time."

    "In fact . . ."

    ". . . She actually seemed extremely . . ."

    ". . . Lonely . . ."

    ". . . Interesting . . ."

    ". . ."

    "OH SHIT!"

    "I'm just staring at her!"

    menu:

        "Wave awkwardly and say hello":

            jump wave

        "Just look away and wait for her to reach you":

            jump lookaway

label wave:

    e "Uhh, HEY! Haha . . ."

    s "Hi, John!"

    e "Soooo . . . weather, right? Haha . . ha . . ."

    ". . . Sigh . . ."

    ". . . Good one, John . . ."

    jump giggle

label lookaway:

    "Shit! She's gonna think I'm such a weirdo . . . Good thing my shoes are so interesting . . ."

    "Haha . . ."

    ". . . Ha . . ."

    ". . . . . . . . . . . ha."

    "Fuck."

    jump giggle

label giggle:

    hide movie with dissolve
    stop movie

    play movie "video/Sarah2 Firstfinal.mp4" loop
    show movie with dissolve

    s "*Giggles*"

    s "It's good to see you, John."

    e "Haha, good to see y-"

    "Woah! Wait, WHAT?!"

    e "Sarah?! You're just wearing a T-Shirt and short shorts?!"

    "Is she insane?!"

    menu:

        "Didn't you say it's a 20 minute walk from your house to the bus stop?!":

            jump walk

        "Did you not have time to grab a coat?!":

            jump grabcoat

        "(Offer your coat)":

            jump offer

label walk:

    s "John is worrying about me! I'm so happy!"

    e "Uhh . . . what?"

    s "I didn't . . . have . . ."

    s ". . . time . . ."

    s ". . . I thought . . ."

    s "*Blushes*"

    s ". . . Maybe I could . . ."

    s ". . . Use your coat . . ."

    e "What? Of course, Sarah!"

    jump offer

label grabcoat:

    s "John is worrying about me! I'm so happy!"

    s "I must have simply forgotten . . ."

    s ". . . I thought . . ."

    s "*Blushes*"

    s ". . . Maybe I could . . ."

    s ". . . Use your coat . . ."

    e "What?! Of course, Sarah!"

    jump offer

label offer:

    e "You're crazy! Please take this!"

    $ renpy.sound.play("Jacket Zip Up.mp3", channel = 0)

    hide movie with fade
    stop movie

    play movie "video/Sarah2 Coatfinal.mp4" loop
    show movie with fade

    s "You're too sweet . . ."

    s ". . . Thank you."

    e ". . . . . . . uh . . . ."

    e ". . . Sure . . ."

    e "Happy to help, Sarah, but what has gotten into you?"

    e "The bus is already really late, it might not be coming at all!"

    e "You had plenty of time to get a coat!"

    s "No . . ."

    s ". . . I wanted . . ."

    s ". . . to use your coat."

    e ". . . . . . . . . . "

    e ". . . Um . . . er . . ."

    "I have NO idea what to say to that!"

    "She's never acted like this before!"

    "Why is she being so weird all of the sudden?"

    e "Sarah . . ."

    menu:

        "Ask her why she's acting different":

            e "Heyyoooo . . . Sarah?"

            e "Whats with all the . . .er . . ."

            e "Why are you acting . . . different?"

            jump different

        "Ask why she wanted your coat":

            jump coat

        "(Just smile and nod)":

            jump nod

label different:

    s "What?"

    s "I'm not acting different . . ."

    s ". . . what is it you mean?"

    e "It's just . . ."

    e ". . . well . . . you . . ."

    e ". . . Don't you think you're a acting a bit . . ."

    e ". . . strange?"

    s "Not really."

    s "Why?"

    s "Why do you say that, John?"

    menu:

        "You're right, I'm sorry. Forget it.":

            e "Oh . . . er . . ."

            e "I'm just tired, I guess, haha."

            e "Sorry, forget about it."

            jump nod

        "Well, who doesn't bring a coat just so they can use someone else's?":

            jump coat

label coat:

    e "You're telling me you intentionally left your coat behind?"

    e " . . . just so you could use mine?"

    e ". . . why?"

    s "I didn't leave it at home . . ."

    s ". . . I just didn't wan't you to see . . ."

    s ". . . it."

    hide movie
    stop movie

    play movie "video/Sarahsmile.mp4" loop
    show movie

    $ ui.timer(1.7, ui.jumps("okay"))

    s "You wouldn't want to see it either, John."

label okay:

    hide movie with dissolve
    stop movie

    play movie "video/Sarah2 Coatfinal.mp4" loop
    show movie with dissolve

    s "Okay?"

    s "It's embarassing."

    e ". . . . . . . . . . . ."

    e ". . . . . . . . . . . ."

    e ". . . . okay."

    hide movie with dissolve
    stop movie

    play movie "video/Sarah2 Coatfinal.mp4" loop
    show movie with dissolve

label nod:

    s "*Giggles*"

    s "Awwwww! Won't you be cold now?!"

    "Her hand forcefully grabbed mine."

    "My mouth moved, but words were nowhere to be found."

    e "I . . . uh . . ."

    e "It's . . . It's okay, haha,"

    e "I'll just freeze to death."

    hide movie
    stop movie

    play movie "video/Sarahfreakout.mp4"
    show movie

    $ ui.timer(0.7, ui.jumps("joking"))

    s "NO!!!!"

label joking:

    hide movie
    stop movie

    play movie "video/Sarahcoatscaredfinal.mp4" loop
    show movie with dissolve

    "She began taking off my coat in horror, meaning to give it back"

    e "Wait!"

    "I cried in panic,"

    e "I was joking!"

    "I grabbed her arms to try and stop her."

    "The instant my hands closed around her, her face flushed bright red . . ."

    ". . . She stopped in her tracks . . ."

    $ renpy.sound.play("SmileSpook.mp3", channel = 3)

    $ renpy.movie_cutscene("Sarah8crazysmilefinal.mp4", delay=None, loops=0, stop_music=False)

    play movie "video/Sarah2 Smilefinal.mp4" loop
    show movie with dissolve

    ". . . . . . . . . . . ."

    ". . . . . . . . . . . ."

    e "Sa- . . ."

    e "Sarah?"

    s ". . . . . . . . ."

    "I let go of her instantly."

    "Her sudden grin was so horrific and out of place I felt my skin blister with ice."

    "It crawled across her face like a disease, eating away at her flesh and peeling back cold lips."

    "Where the hell had this come from?!"

    "It was incredibly disturbing, so much so that I began to sweat despite the cold."

    "I had to do something . . ."

    ". . . ANYTHING . . ."

    "To get rid of this ghastly expression . . ."

    menu:

        "Ask if she's excited for school":

            jump school

        "Comment about the weather":

            jump weather

        "Demand that she stop":

            jump bitch

label bitch:

    e "Sarah!"

    e "Cut that out!"

    e "What the fuck has gotten into you?!"

    hide movie
    stop movie

    play movie "video/Sarahcoatscaredfinal.mp4" loop
    show movie with dissolve

    s ". . . . . . . . ."

    s ". . . . . . . . . . . ."

    s "You're acting different . . ."

    s "John."

    s "Don't change . . . don't be like the others."

    hide movie
    stop movie

    play movie "video/Sarahsmile.mp4" loop
    show movie

    $ ui.timer(2.0, ui.jumps("rightb"))

    s ". . . Don't change."

    $ ui.timer(2.0, ui.jumps("rightb"))

    s "I will keep you the same."

label rightb:

    hide movie with dissolve
    stop movie

    play movie "video/Sarah2 Smilefinal.mp4" loop
    show movie with dissolve

    s "Right?"

    s "John?"

    s "Don't you agree this is best?"

    s ". . . for everyone?"

    s "You remaining unchanged?"

    s "You'll be peaceful."

    s "Like everyone else."

    s ". . . . . . . ."

    s "There is no school today."

    s "Can't you tell?"

    s "The bus is not coming."

    s "It is a snowday."

    s "*Giggle*"

    jump a

label school:

    e "Sooo . . . haha . . ."

    e "Ready for school?"

    hide movie with dissolve
    stop movie

    play movie "video/Sarah2 Coatfinal.mp4" loop
    show movie with dissolve

    s "School?"

    "She questioned, straight faced, eyes returning to focus,"

    s "We don't have school today, silly."

    s "It's a snow day because of the incoming storm."

    s "*Giggle*"

    e "What?!"

    e "Seriously?!"

    e "God Dangit!"

    e "I didn't get an email or anything!"

    jump end_giggle

label end_giggle:

    s ". . . . . . . . ."

    "That's when I saw it . . ."

    "A faint grin begining to carve out her face again . . ."

    ". . . Sheepish and hidden . . ."

    e "Wait . . ."

    e "Did-"

    e "Did you . . .?"

    s "I wouldn't have been able to see you . . ."

    hide movie with dissolve
    stop movie

    play movie "video/Sarahcrazysmile.mp4"
    show movie with dissolve

    $ ui.timer(2.3, ui.jumps("a"))

    s ". . . If you knew there was no school . . ."

label a:

    play movie "video/Sarah2 Smilefinal.mp4" loop
    show movie

    "That twisted grin continued to stretch her face further and further, eating away at her pale skin."

    "The wind howled and crystalline needles bit at my exposed skin."

    "Suddenly, she laughed, grabbing onto my waist."

    s "You better stay close!"

    s "Otherwise you'll catch  a cold!"

    "My mind was in full retreat mode now as I began backing up."

    "I tried to wiggle free of her grasp, saying,"

    e "Haha . . . Yeah . . ."

    e "I-"

    e "Uhhhh . . ."

    menu:

        "Try to talk your way out":

            e "Hey . . ."

            e "I think I'll just go home now . . . and maybe get some more coats."

            e "I'll see you tomorrow if the weather improves . . ."

            e "Okay?"

            "Seemingly not hearing me, she snuggled in closer and closed her eyes."

            jump calm

        "Just remain calm":

            "She snuggled in closer and closed her eyes as I tried to steady my breathing."

            jump calm

label weather:

    e "So . . ."

    e ". . . Haha . . . pretty crazy storm right?"

    hide movie with dissolve
    stop movie

    play movie "video/Sarah2 Coatfinal.mp4" loop
    show movie with dissolve

    s "Storm?"

    "She questioned, straight faced, eyes returning to focus,"

    s "Yes . . ."

    s ". . . I suppose . . ."

    s ". . . That . . ."

    s ". . . Must be why the bus isn't coming."

    s "It's been too long."

    s "Where is it?"

    s ". . . . ."

    s "It must be . . ."

    s ". . . a snowday."

    e "Yeah . . ."

    e "You're right."

    e "But I should have gotten an email."

    e "Strange that it didn't get through to me . . ."

    jump end_giggle

label calm:

    "My hands were in the air, my body rigid and taut as my heart convulsed with unease."

    "I drew several shaky breaths and looked down at her . . ."

    ". . . . . . . . . ."

    "Her smile now appeared rather . . ."

    ". . . Peaceful?"

    "Was this really all that bad?"

    "A lot of guys I knew would have done anything to be in this position . . ."

    ". . . She just wanted to see me was all . . ."

    "Yeah."

    "It was actually . . ."

    "Kinda"

    "sweet of her . . ."

    "Albeit, a little drastic."

    hide movie with dissolve
    stop movie

    "That's when I saw the dark crimson stains on her legs."

    play movie "video/Sarah2 Smilefinal.mp4" loop
    show movie with dissolve

    e "Is- . . ."

    e "*Gag*"

    e "Is that . . ."

    e ". . . blood?"

    stop movie
    hide movie

    play movie "video/Sarahsmilenormalbigfinal.mp4" loop
    show movie

    s "Let's go to your house!"

    "She suddenly squealed, ignoring my horror,"

    stop movie
    hide movie

    play movie "video/Sarahsmilenormalsmallfinal.mp4" loop
    show movie

    s "Don't you need your coats?"

    s "I'll take them for you!"

    menu:

        "Ignore the substance and agree":

            jump your_house

        "Push her back and demand an explanation":

                    jump pushback

        "Carefully ask what the substance is":

            jump careful

label pushback:

    e "Sarah!"

    e "What the fuck is that?!"

    $ renpy.sound.play("GlitchStab1.mp3", channel = 1)

    stop movie
    hide movie

    play movie "video/Sarah12sadfinal.mp4" loop
    show movie

    e "Why the fuck is there blood on you?!"

    "As she stumbled back, her eyes flashed with horrid grey, hands twitching at her side."

    "She said nothing."

    "Her eyes stared straight forwards but convulsed with a guesome inability to focus on anything."

    "As if her eyelids were starched open and stretched over a wire frame, she didn't so much as blink."

    e "Hello?!"

    e "Sarah! Answer me!"

    "She remained utterly stagnant . . ."

    "Not a word crawled from her horrid lips."

    menu:

        "Appologize. Drop it.":

            e "Jesus . . . Sarah . . ."

            e "I'm sorry."

            e "Are you okay?"

            e "You're scaring me . . ."

            e "But we're friends . . . I trust you . . ."

            e ". . . and . . ."

            stop movie
            hide movie

            play movie "video/Sarahsmilenormalsmallfinal.mp4" loop
            show movie

            e "We can't stay out here forever . . ."

            e "We'll freeze to death."

            e " . . . It makes me nervous, but if you really want to come over . . ."

            jump your_house

        "Ask again, more forcefuly":

            e "SARAH!"

            e "We're not going anywhere until you fucking explain yourself!"

            e "You're acting like a psycho!"

            e "I'm about to call the police!"

            e "WHY IS THERE BLOOD ON YOU?!"

            "She remained dead silent, skin pulsing with sickly grey."

            s ". . . stop . . ."

            s ". . . stop changing . . ."

            s ". . . you . . . accept me . . ."

            "Her hand twitched."

            menu:

                "Back down. Appologize.":

                    e "Jesus . . . Sarah . . ."

                    e "I'm sorry."

                    e "Are you okay?"

                    e "You're really scaring me . . . but forget about it."

                    e "Of course I accept you, we're friends."

                    e ". . . and . . ."

                    stop movie
                    hide movie

                    play movie "video/Sarahsmilenormalsmallfinal.mp4" loop
                    show movie

                    e ". . . We can't stay out here forever . . ."

                    e " . . . It makes me nervous, but if you really want to come over . . ."

                    jump your_house

                "Call the police":

                    "I slowly reached into my pocket, continuing to back up as I pulled out my phone."

                    s "The blood, John . . ."

                    s ". . . I can't even remember."

                    s "So"

                    s "many"

                    s "people."

                    jump deathA

label deathA:

    stop music

    play movie "video/Deathscene1.mp4"
    show movie

    "A sudden sharp crack slashed my vision to black."

    "The world exploded in warmth . . . vile . . . boiling warmth."

    "I coughed, finding that nothing but more warm liquid rushed from my lips."

    "The rush of short lived warmth rapidly decayed into cold . . ."

    ". . . ice cold . . ."

    ". . . . . . . . . . . . . . everywhere . . . .  . . . . . . . ."

    scene YouAreDead
    with fade

    $ renpy.pause(4.0)

    scene black
    with fade
    show text "Try Again" with dissolve
    $ renpy.pause(3.0)
    hide text with dissolve

return

label careful:

    stop movie
    hide movie

    play movie "video/Sarahsmilenormalsmallfinal.mp4" loop
    show movie

    e "Hey, Sarah?"

    e "Please just tell me if that's blood on you."

    e "You're really worrying me . . ."

    s ". . . . . . ."

    s ". . . . . . . . . . . . . . ."

    s "It's not."

    menu:

        "Believe her":

            e "Oh . . . . . . ."

            e ". . . Alright . . ."

            e "I'm still a bit concerned, but I trust you."

            e "We're friends after all."

            e ". . . and . . ."

            e "We can't stay out here forever . . ."

            e "We'll freeze to death."

            e " . . . It makes me nervous, but if you really want to come over . . ."

            jump your_house

        "Keep questioning":

            e ". . . . . what is it, then?"

            e "Sarah . . . that looks a lot like blood."

            e "Please understand I'm just worried about you . . ."

            s ". . . . . . . . ."

            s ". . . You wouldn't understand . . ."

            s ". . . not yet . . ."

            menu:

                "Demand an explination":

                    e "NO!"

                    e "That's nowhere near good enough!"

                    jump pushback

                "Back down":

                    e "Oh . . . . . . ."

                    e ". . . Alright . . ."

                    e "I'm still a bit concerned, but I trust you."

                    e "We're friends after all."

                    e ". . . and . . ."

                    e "We can't stay out here forever . . ."

                    e "We'll freeze to death."

                    e " . . . It makes me nervous, but if you really want to come over . . ."

                    jump your_house

label your_house:

    hide movie with fade
    stop movie

    play movie "video/walkingfinal.mp4" loop
    show movie with fade

    "I began walking hesitantly . . ."

    "I felt sick, torn between concern and fear."

    "But surely she was just having an off day . . ."

    ". . . or messing with me in a cruel . . . drawn out joke."

    "There was an explination here somewhere . . ."

    "Being suspicious of her was getting me nowhere."

    "She clung to me tightly as we walked."

    "I tried desperately not to shiver and send her on another episode."

    "We were nearly to my driveway when I my phone suddenly buzzed."

    "It emanated a soft ding."

    "Stealing a glance at the screen in my pocket, I could see that it was Max!"

    "He had finally texted me back!"

    menu:

        "Look at the message":

            jump message

        "Ignore it":

            jump nophone

label nophone:

    "I just left the phone in my pocket, feeling Sarah's hand softly grip mine."

    "It wasn't three steps later that I was suddenly jerked back, almost loosing my balance on the slick ice."

    hide movie
    stop movie

    play movie "video/sarah5final.mp4" loop
    show movie

    "I turned around to see that Sarah had stopped cold."

    "Her hands gripped so tight around my own that I could almost hear the bones breaking."

    "I let out a gasp of pain and tried to pull my hand free, but she wouldn't allow it."

    s "Who was that?"

    "The usual cheer was all but gone from her voice."

    s "You think I wouldn't notice?"

    s "Who"

    s "Was"

    s "That?"

    jump phonemenu

label phonemenu:

    menu:

        "Truth: It's Max. Read the Message":

            e "It . . . It's Max!"

            e "My friend?"

            jump itsmax

        "Truth: It's Max. Leave it at that":

            e "It's . . . It's Max!"

            e "My friend?"

            s ". . . . . . . . . . ."

            s "What did he say?"

            e "Uhh . . . er . . ."

            s "Open"

            s "It."

            menu:

                "Look at the message":

                    jump itsmax

                "Refuse: Try to calm her":

                    e "Jesus, Sarah."

                    e "Calm down, what does it matter?"

                    s ". . . . . . . . . ."

                    s "I do not want you talking with others."

                    e "Wh . . . what?"

                    s "I'm scared."

                    s "Scared, John."

                    s "If you spend too much time with others, you may . . ."

                    s ". . . change."

                    e "Sarah?"

                    e "What is all of this all of the sudden?"

                    e "What do you mean 'change?'"

                    s "They are wicked, John."

                    s "Every one of them . . ."

                    s "They cannot be trusted with themselves."

                    s "Only I can see this, John."

                    s "I am scared for you."

                    s "They will try to corrupt you."

                    s ". . . with such filthy things."

                    s ". . . . . . . . . ."

                    s "Open the message."

                    s "He cannot be trusted."

                    menu:

                        "Look at the message":

                            jump itsmax

                        "Refuse":

                            e "No, Sarah."

                            e "You're talking nonsense!"

                            e "You're insane! Are you hearing yourself?!"

                            e "Leave me alone!"

                            e "What the hell is wrong with you today?!"

                            e "Not everyone is 'wicked!'"

                            e "What the hell would make you think that?!"

                            s ". . . . . . . . . . . . ."

                            s ". . . . . . . . . I was once wicked, John."

                            s "Now . . ."

                            s "Only I can prevent further corruption of your soul."

                            s "I have learned that only in one state can others remain unchanged."

                            s "Death, John."

                            s "You will not be corrupted."

                            jump deathA

        "Lie: It just ran out of batteries":

            e "No one."

            e "My phone just died, sorry."

            s ". . . . . . . . . . . . . ."

            s ". . . . . . . . . . ."

            s "Why do you lie to me, John?"

            e "Uh . . ."

            e "What?"

            s "That is your text tone."

            s "I know the sound your phone makes when it dies."

            s "And it's not that."

            s "You are lying to me."

            e "Huh?! . . . How do you-?"

            s "I also have your mother's phone, John."

            s "I took it from her."

            s "You two share the same phone, and the same message tones."

            s "You think I wouldn't know?"

            s "I am too late for you."

            jump deathA

        "Lie: I don't know":

            e "I have no idea Sarah."

            e "Why does it matter?"

            e "You're kinda acting insane! Are you hearing yourself?!"

            e "I have no idea who it was, but you shouldn't care anyway!"

            e "What the hell is wrong with you today?!"

            s ". . . . . . . . . . . . ."

            s "I care, because conversing with others will corrupt you."

            s "Only I can understand what is happening to you."

            s "Only I can prevent further corruption of your soul."

            s "Save you."

            s "Save everyone."

            s "I have learned that only in one state can others remain unchanged."

            s "Death, John."

            s "You will not be corrupted."

            s "Are you talking to others?"

            s "Are you trying to . . ."

            s "leave"

            s "me?"

            menu:

                "WHAT?! If you're going to be such a psycho, then yes!":

                    e "Yes!"

                    e "Of course! Get away from me!"

                    e "You're insane!"

                    s "I am finally sane."

                    s "It is you . . ."

                    s ". . . who must regain your sanity."

                    jump deathA

                "No! Of course not!":

                    e "Er . . . no!"

                    e "I would never . . ."

                    s "Lies . . ."

                    s "Since when do you lie so much?"

                    s "John?"

                    jump deathA

                "(Run)":

                    jump deathA

label message:

    "I slowly wiggled the phone from my pocket with my left hand, as my right was still in Sarah's vice grip."

    "I was still walking as I brought the phone up when I was suddenly jerked back, almost losing my balance on the slick ice. "

    hide movie
    stop movie

    play movie "video/sarah5final.mp4" loop
    show movie

    "I turned around to see that Sarah had stopped cold."

    "Her hand gripped so tight around my own that I could almost hear the bones breaking."

    "I let out a gasp of pain and tried to pull my hand free, but she wouldn't allow it."

    s "Who's that?"

    "The usual cheer was all but gone from her voice."

    jump phonemenu

label itsmax:

    "I drew a breath, still cringing in pain as I opened the message from him,"

    e "He was just telling me about-"

    stop movie
    hide movie

    play movie "video/lookatmessagefinal.mp4" loop
    show movie

    ". . . . . . . . . . . . . . . . ."

    "My blood froze."

    "I stared at the screen as my chest tightened."

    stop movie
    hide movie

    play movie "video/sarah5final.mp4" loop
    show movie

    s "Telling you what?"

    "I turned to look at her, my hands beginning to shake, having nothing to do with the cold."

    "I'm sure my face showed my horror and confusion, but if she saw, she didn't let on."

    "I could feel her chilling gaze stabbing at my numb skin."

    s "Telling you what, John?"

    menu:

        "Lie: Try to keep her calm":

            $ phone = "lied"

            e "Just . . . about . . ."

            e ". . . how much he likes snow . . ."

            jump lie

        "Truth: Confront her about what Max said":

            $ phone = "truthed"

            jump truth

label truth:

    e "He told me he's at school, Sarah."

    "I slowly turned to face her, eyes narrowing."

    e "Today is not a snow day."

    "My heart was hammering . . . the only sound in this barren wasteland."

    s "He's lying."

    "Her expression grew even darker, needle teeth flashing in the dim light."

    s "Max . . ."

    s ". . . is always lying."

    menu:

        "Max is probably just playing a joke, lying about the school day":

            e "Well . . ."

            e "Yeah."

            e "That's kinda true actually."

            e "He was . . . prabably just playing a joke on me."

            e "It wouldn't be unlike him to get me all worked about a school day that didn't exist."

            e "Sorry . . ."

            e "For doubting you."

            jump lie

        "He's telling the truth":

            e "No, Sarah!"

            e "What do you even mean by that?!"

            e "Where is the bus, Sarah?"

            e "Why didn't it ever come?!"

            jump deathA

label lie:

    hide movie with fade
    stop movie

    play movie "video/walkingfinal.mp4" loop
    show movie with fade

    "Slowly, her cute face reappeared and her grip lightened as she smiled at me."

    "We began walking again."

    s ". . . . . . ."

    s "What do you think of him?"

    "There was still a hint of malice in her quiet voice."

    e "What?"

    s "Max."

    s "Is he a good friend of yours?"

    e "Uhhh . . . yeah, I guess?"

    e "I mean, I've known him for a while, is all."

    "Her hands slowly balled into tight fists, nearly crushing my own hand as she muttered something under her breath."

    jump driveway

label driveway:

    hide movie with fade
    stop movie

    play movie "video/houseextfinal.mp4" loop
    show movie with fade

    "That's when she turned into my driveway and started walking down."

    "Leading ME."

    "How did she know where to turn?!"

    "How did she know THIS was my driveway?!?!"

    menu:

        "Stop her":

            jump stopthis

        "Ignore it":

            jump frontdoor

label stopthis:

    stop movie
    hide movie

    play movie "video/Sarah12sadfinal.mp4" loop
    show movie

    "I yanked my hand from hers with all of my might."

    if phone == "lied":

        e "Sarah . . ."

        e ". . . Where is the bus?"

        "She looked devastated, staring at her empty hand, not saying a word."

        "Her irises shook slightly, her face becoming hollow, whatever color she had disintegrating into a grey slag."

        e "Where the hell is the bus, Sarah?!"

        e "Why didn't it ever come?!"

        s "No . . ."

        s ". . . School . . ."

        s ". . . Today . . . . . ."

        "She muttered to herself, eyes once again distant and dim as she fumbled around and tried to reach for my hands blindly."

        e "Yes we do, Sarah!"

        e "We do have school!"

        e "The bus should have been at the stop, but it never came!"

        s "I wanted . . ."

        s ". . . Just the two of us . . ."

        e "And why do you have your backpack if you weren't planning on going to school?!"

        e "HOW DO YOU KNOW WHERE I LIVE?!"

        stop movie
        hide movie

        play movie "video/Sarahsmilehouseext.mp4" loop
        show movie

        "She chose to ignore all of this and instead found my hands again, gripping them tightly and smiling crookedly."

        "In the most unnatural way, she didn’t seem to be feeling emotions, and yet carved them into her face all the same."

        "It was as if she was trying to imitate expressions she had seen others express."

        jump frontdoor

    if phone == "truthed":

        e "Sarah . . ."

        e ". . . Who are you?"

        "She looked devastated, staring at her empty hand, not saying a word."

        "Her irises shook slightly, her face becoming hollow, whatever color she had disintegrating into a grey slag."

        e "Who the hell are you, really?"

        e "Why do you know where I live?!"

        s "No . . ."

        s ". . . School . . ."

        s ". . . Today . . . . . ."

        "She muttered to herself, eyes once again distant and dim as she fumbled around and tried to reach for my hands blindly."

        s "I wanted . . ."

        s ". . . Just the two of us . . ."

        e "And why do you have your backpack if you weren't planning on going to school?!"

        e "WHY ARE YOU ACTING SO INSANE?!"

        stop movie
        hide movie

        play movie "video/Sarahsmilehouseext.mp4" loop
        show movie

        "She chose to ignore all of this and instead found my hands again, gripping them tightly and smiling crookedly."

        "In the most unnatural way, she didn’t seem to be feeling emotions, and yet carved them into her face all the same."

        "It was as if she was trying to imitate expressions she had seen others express."

        jump frontdoor

label frontdoor:

    stop movie
    hide movie

    play movie "video/Sarahsmilehouseext.mp4" loop
    show movie

    "I took a few long breaths and tried to calm myself down."

    s "I'm cold . . ."

    s ". . . We should go inside."

    "My lungs were shaky and weak, my breaths doing very little as I talked to myself."

    "It must have been a misunderstanding . . ."

    "I'm not even sure if I believed that myself,"

    "but it was better than thinking of the alternatives."

    "People didn't just snap like this."

    "There was more going on here, and pushing Sarah away wasn't going to get me any closer to an anwer."

    "And besides . . ."

    ". . . I actually was going to freeze to death out here . . ."

    menu:

        "Appologize for acting suspicious":

            jump console

        "Say nothing: Just go inside":

            $ backstory = "missed"

            jump fronter

label console:

    e "Hey . . . gosh . . . Sarah . . ."

    e "I'm sorry . . ."

    e "This whole day has been a bit . . . weird, I guess."

    e "I keep thinkig strange thoughts . . . like I'm paranoid or something."

    e "I don't even understand it, but you don't deserve to be treated that way."

    e "I know you've been having trouble fitting in at school . . ."

    e ". . . the last thing you need is me acting strange."

    e "I'm sorry . . ."

    e "Listen . . . Sarah . . ."

    e "Thanks . . ."

    e "Thanks for being with me today."

    e "It would certainly be cold with or without you . . ."

    e ". . . but at least this way it's not boring."

    e "I like hanging out with you."

    e "So . . ."

    e ". . . er . . ."

    e "Thanks, and I'm sorry."

    stop movie
    hide movie

    play movie "video/Sarah2 Happysmilefinal.mp4" loop
    show movie

    s ". . . . . !"

    "My heart warmed as I saw her face shift ever so slightly."

    "As if waking from a dream, her eyes glanced around, taking in her surroundings for the first time."

    "Her sunken lifeless features slowly ebbed away as, for the first time today . . ."

    ". . . a believable smile flickered into view."

    "One that didn't appear forced, or fueled by delusions."

    s ". . . no problem, John."

    s "Thank you."

    menu:

          ">>Backstory<<":

              $ backstory = "onecomplete"

              e "Hey, Sarah?"

              s "Yeah?"

              e ". . . could you maybe tell me a little about yourself?"

              s ". . . what?"

              e ". . . . . . . . . ."

              e "You don't have to . . ."

              e "But I just want to maybe . . ."

              e ". . . know a little more about you . . ."

              e "Er . . . I guess."

              s ". . . . . . . . . ."

              s "Okay, John."

              s ". . . . I don't like talking about . . ."

              s ". . . it . . ."

              s "But I can give you some drawings . . ."

              s ". . . I'm not very good."

              s "Promise me you wont look at them until later?"

              hide movie with fade
              stop movie

              stop music fadeout 2

              e ". . . I promise."

              play movie "video/A Cold Love Story Backstory Final 1.mp4"
              $ renpy.pause(10, hard=True)
              pause 135
              stop movie

              play music "Relaxing Music - Winter Breath.mp3"

              play movie "video/Blanksnowfinal.mp4" loop
              show movie with fade

              e "Okay, Sarah, I'll just put these in my backpack for now."

              e ". . . I'll look at them later."

              s ". . . . . . . ."

              s "Thank you, John."

              jump fronter

label fronter:

    hide movie with fade
    stop movie

    play movie "video/houseextfinal.mp4" loop
    show movie with fade

    "As we began walking down the driveway to my house, I looked at her and took a heavy breath . . ."

    ". . . calming my nerves . . ."

    "I only hoped that her strange behavior had subsided for good."

    "We trudged through the softly accumulating snow."

    "I had been too lazy to shovel it with my parents having left for Hawaii a week ago."

    "Ironically, as much as it pissed me off to imagine them on a beach while I was stuck here . . ."

    ". . . I was insanely glad that neither of them would be home for a few days so I wouldn't have to explain Sarah to them."

    "We reached the door and I fumbled for my key . . ."

    "I finally grasped it, unlocked the door, and jumped inside before too much warm air escaped into the bitter cold."

    hide movie with fade
    stop movie

    play movie "video/Houseintfinal.mp4" loop
    show movie with fade

    "I immediately started up a fire, not really realizing how cold I had been until that moment."

    "I looked over at Sarah taking off the jackets and folding them neatly before placing them down gingerly by the entrance."

    "Her movements were strained, her spindly limbs tired and weak."

    "She appeared to have a normal mental state now . . ."

    ". . . but as she finished up, and her eyes glanced at me . . ."

    hide movie
    stop movie

    play movie "video/Sarah6normalsmilefinal.mp4" loop
    show movie

    "I couldn't help but tense a little."

    e "Hey . . . Sarah?"

    "My heart had begun to pound, distrust and fear suddenly reclaiming me."

    "What if . . ."

    ". . . did she know where my room was?"

    "That might be a way to check on whether or not I'm overreacting . . ."

    menu:

        "Ask her if she could grab a hoodie from your room":

            jump grabhoodie

        ". . . Nevermind . . .":

            e "Er . . ."

            e "Nevermind, I'm just going to go get a jacket from my room real quick."

            e "Do you want anything?"

            s "I'm okay, John."

            s "Thank you."

            jump nevermind

label grabhoodie:

    e "Could you maybe . . ."

    e ". . . go to my room and grab me a hoodie?"

    s "Anything for John!"

    "She cried with a big smile, turning to go."

    "She took several steps further into the house."

    "Her pale form walked deliberately at first . . ."

    ". . . but her pace gradually devolved into a strained staggering motion before she eventually came to a complete halt."

    "Still facing away from me, her icy voice quietly seeped out,"

    s "But . . ."

    s ". . . I don't know where your room is."

    "I felt a huge wave of relief."

    "Thank God!"

    "I felt bad for ever doubting her, for giving her such a dumb test."

    e "Haha, sorry, it's right up the st-"

    "I suddenly stopped myself."

    e "You know what?"

    e "Haha, I'll just get it myself . . ."

    e "I need to stop being so lazy anyway."

    "What was wrong with me?"

    "I apparently still felt like I couldn't trust her!"

    "But I just couldn't stop myself."

    "I DIDN'T believe her!"

    "I wanted to know if there was really no school, I wanted to know why she had been acting so strange."

    "The only thing holding me back was the fear of such a question bringing back that other smile."

    "That deranged face."

label nevermind:

    e "Alright then . . ."

    e "I- . . er, I'll be right back, then."

    hide movie with dissolve
    stop movie

    "I quickly ran up the stairs to my room."

    play movie "video/Doorknobfinal.mp4" loop
    show movie with fade

    "I grabbed my doorknob only to recoil in shock."

    "It was freezing."

    "I could feel a draft of frozen air seeping out from under my door."

    "I gingerly grabbed the handle with my fingertips and slowly opened it, letting lose a blast of frigid air."

    hide movie with dissolve
    stop movie

    play movie "video/Roomemptyfinal.mp4" loop
    show movie with fade

    "It felt like . . . a window had been left open . . ."

    " . . . Now that I thought about it, I remembered my room being freezing that morning as well . . ."

    ". . . and really quite drafty for the past week . . ."

    menu:

        "Check the windows":

            ". . . nothing . . ."

            "All the windows were closed tight."

        "Ignore it":

            "I better just grab my coat and get back to Sarah quickly."

    e "Ugh."

    "I would probably just have to sleep downstairs by the fire until I figured out the problem."

    "I quickly grabbed my hoodie and closed the door to my room."

    hide movie with fade
    stop movie

    "I walked back downstairs . . ."

    play movie "video/Houseintfinal.mp4" loop
    show movie with fade

    play music "Right Behind YouV2.mp3" fadeout 2 fadein 5

    ". . . Sarah was gone."

    e "Uhhh . . . hey?"

    e "Sarah?"

    "Where the hell had she gone?!"

    e "Hello?!"

    $ renpy.sound.play("Crash Aluminum Trash Can Filled With Debris Tumbling On Cement 01.wav", channel = 1)

    "A sudden clattering sound resounded from the kitchen."

    "My heart spasmed at the sudden noise, my hand rushing to clutch at my chest."

    menu:

        "Check the kitchen":

            jump kitchen

        "Check your room again":

            jump room

        "Stay still":

            jump still

label kitchen:

    hide movie with dissolve
    stop movie

    "I cautiously walked towards the kitchen, my heart pounding despite my attempts to control it."

    play movie "video/Kitchenemptyfinal.mp4" loop
    show movie with fade

    ". . . There was no one inside."

    "My eyes narrowed."

    "Was that a pan on the floor?"

    "That must have been what caused the sound."

    menu:

        "Call for Sarah":

            e "Uh . . . hey, Sarah?"

            e "Sarah?! Hello?"

            e "Where are you?"

            ". . . . . . . . ."

            ". . . no response . . . "

            menu:

                "Go back to the living room":

                    jump livingrerm

        "Go back to the living room":

            jump livingrerm

label room:

    hide movie with dissolve
    stop movie

    "I ran back to my room."

    play movie "video/Roomemptyfinal.mp4" loop
    show movie with fade

    ". . . there was no one inside."

    menu:

        "Go back to the living room":

            jump livingrerm

        "Go to the kitchen":

            jump kitchen

label still:

    "I just planted my feet, eyes nervously scanning the house . . ."

    ". . . . . . ."

    "Nothing moved."

    menu:

        "Go to the kitchen":

            jump kitchen

        "Go to your room":

            jump room

label livingrerm:

    hide movie with dissolve
    stop movie

    "I hesitantly peered back into the living room, walking slowly."

    play movie "video/Houseintfinal.mp4" loop
    show movie with fade

    ". . . . Where the hell was she?"

    "That's when I suddenly heard someone descending the stairs."

    "I whirled around to see Sarah bounding down them, slinging her backpack over her shoulder . . ."

    hide movie
    stop movie

    play movie "video/Sarah6normalsmilefinal.mp4" loop
    show movie

    "It seemed to be empty now."

    "What the hell?!"

    "Where had she even come from?!"

    "What had she done?!"

    menu:

        "Ask her what she was doing":

            e "Sarah?"

            e "What the heck were you just doing up there?"

            s "It's a surprise, John!"

            "Her smile flashed across her face, once again appearing . . . wrong."

            menu:

                "Ask again, more forcefully":

                    e "That wont cut it!"

                    e "I want to know what you were just doing in my house!"

                    e "I don't want a 'surprise!'"

                    e "Explain yourself!"

                    label ruiningit_1:

                    s ". . . . . . . ."

                    s "You're ruining it, John."

                    s "I wanted you to be surprised . . . It's something that will make you happy, I swear."

                    s "Do I really have to ruin it?"

                    menu:

                        "YES!":

                            label yesh:

                            e "YES!"

                            e "Of course, Sarah!"

                            e "TELL ME!"

                            s ". . . . . ."

                            s "It's our bus driver."

                            s "I brought her over here . . . just for you."

                            ". . . . . . . . ."

                            e "Uh . . . what?"

                            e "What do you mean?"

                            hide movie
                            stop movie

                            play movie "video/Sarah7 1Final.mp4" loop
                            show movie

                            $ renpy.sound.play("Module Production Element Title Imaging Distortion Reverse Whine Feedback 01.wav", channel = 1)

                            s "My backpack isn't very big, John."

                            s "I couldn't quite take all of her."

                            e ". . . . . . ."

                            e ". . . . . . erm . . . . . . ."

                            s "You like faces, right, John?"

                            s "I usually remove the face so they can't look at me . . ."

                            hide movie

                            play movie "video/Sarah7 2Final.mp4" loop
                            show movie

                            $ renpy.sound.play("TVSpook.mp3", channel = 1)

                            s ". . . but you like the way they look at you."

                            s "Don't you, John?"

                            s "Just how I like the way you look at me."

                            s "So I brought that for you . . ."

                            s "I'm sorry I ruined the surprise for you."

                            s "What do you think, John?"

                            s "What do you think?"

                            menu:

                                ". . . . . . . . . .":

                                    jump deathA

                                ". . . . . . . . . .":

                                    jump deathA

                                ". . . . . . . . . .":

                                    jump deathA

                                ". . . . . . . . . .":

                                    jump deathA

                        "Eh . . . fine, nevermind.":

                            label mehvermind_1:

                            e "Oh . . . forget about it, then."

                            menu:

                                "Ask her to leave":

                                    jump leave

                                "Offer hot chocolate":

                                    jump chocolate

                "Go check for yourself":

                    hide movie with fade
                    stop movie

                    "I brushed past her as I walked up the stairs, ignoring her cries of protest."

                    play movie "video/Doorknobfinal.mp4" loop
                    show movie with fade

                    "I reached my room, hesitating slightly as my hand pressed against the cold knob."

                    s "Stop that."

                    s "You'll ruin it."

                    "I slowly turned the handle . . ."

                    jump deathA

                ". . . okay . . .":

                    e "Er . . . alright."

                    e ". . . cool . . ."

                    menu:

                        "Ask her to leave":

                            jump leave

                        "Offer hot chocolate":

                            jump chocolate

        "Ask her what's in her backpack":

            e "Sarah, what the hell is in your backpack?"

            e "What did you take out of it just now?"

            s "It's a surprise, John!"

            "Her smile flashed across her face, once again appearing . . . wrong."

            menu:

                "Ask again, more forcefully":

                    e "That wont cut it!"

                    e "I want to know what you have in there!"

                    e "I don't want a 'surprise!'"

                    e "Explain yourself!"

                    label ruiningit_2:

                    s ". . . . . . . ."

                    s "You're ruining it, John."

                    s "I wanted you to be surprised . . . It's something that will make you happy, I swear."

                    s "Do I really have to ruin it?"

                    menu:

                        "YES!":

                            jump yesh

                        "Eh . . . fine, nevermind.":

                            jump mehvermind_2

                "Eh . . . fine, nevermind.":

                        label mehvermind_2:

                        e "Oh . . . forget about it, then."

                        menu:

                            "Ask her to leave":

                                jump leave

                            "Offer hot chocolate":

                                jump chocolate

        "Ignore it: Offer hot chocolate":

            e "Er, hey, Sarah."

            e ". . . welcome back . . ."

            s "Hey, John!"

            "She smiled cutely."

            label chocolate:

            e "Umm . . . so, if you're staying for a bit . . . how about some hot chocolate . . ."

            e "Or . . . something else . . ."

            e "It's whatever . . ."

            e "Haha . . . ha . . ."

            s "Sure!"

            s "So long as it's okay with you!"

            s "*Giggle*"

            s "Do you like hot chocolate, John?"

            e "Er . . . uh, sure, haha, way more than coffee."

            s "Then I like it too!"

            s "I'll make some for you!"

            menu:

                "Oh, it's okay, I'll do it":

                    e "Don't worry about it, haha."

                    e "I can make it fo-"

                    s "I'll"

                    s "Make"

                    s "It."

                    s "*Giggle*"

                    s "Okay, John?"

                    e ". . . . . . ."

                    e "Yeah . . . alright, haha . . ."

                    e "Thanks."

                    jump chacalate

                "Oh . . . alright, thanks":

                    e "Er . . . alright, haha."

                    e "Thanks, Sarah."

                    s "Sure!"

                    s "Anything for John!"

                    e "Hehe . . . uh . . ."

                    e ". . . yay . . ."

                    jump chacalate

        "Ask her to leave":

            label leave:

            e "Sarah, you have to go."

            e "I'm sorry, but I just can't take it anymore."

            e "You're acting too strange."

            s ". . . . . ."

            s "Okay, John."

            s "I have something to do anyway."

            s "*Giggle*"

            s "I'll see you later!"

            $ renpy.sound.play("Household Door Front Door Close Squeaky 01.wav", channel = 1)

            hide movie with fade
            stop movie

            play movie "video/Houseintfinal.mp4" loop
            show movie with fade

            play music "Scary Horror Piano Music (Creepy Instrumental Music).mp3" fadeout 2 fadein 2

            "She dashed out of my house before I could respond."

            e "No!"

            e "Not 'see you later!'"

            e ". . . . . . ."

            e ". . . ugghhh . . ."

            jump sittingaround

label bye:

    s "Sorry! I've got to go now!"

    s "I'll see you later, okay?"

    "She dashed out of my house before I could even respond."

label chacalate:

    hide movie with fade
    stop movie

    "We walked to the kitchen, Sarah taking the lead."

    play movie "video/Kitchensarahsmilefinal.mp4" loop
    show movie with fade

    "Before long, she had made some hot chocolate,"

    "using water and my little packets of mix, nothing fancy."

    "She held her own cup down at her side, eyes trained on me."

    s "How is it, John?"

    "My chest tightened."

    "What was this feeling?"

    e "Oh . . . it's um . . ."

    menu:

        "Drink some":

            "I slowly lifted the cup, taking a small sip."

            e "Haha, it tastes great!"

            e "Very, er . . . hot chocolate-ey."

            s "*Giggle*"

            "Her eyes again cleared slightly, a sort of calming sanity washing over her."

            menu:

                ">>Backstory<<":

                    if backstory == "onecomplete":

                        $ backstory = "allcomplete"

                        e "Hey . . . Sarah?"

                        s "Er . . . ya, John?"

                        e "Listen . . ."

                        e ". . . I may have looked at those pictures you gave me . . ."

                        hide movie
                        stop movie

                        play movie "video/Kitchensarahscaredfinal.mp4" loop
                        show movie

                        s ". . . . . .!"

                        s "I . . . uh . . ."

                        e "No, no, listen . . . it's okay."

                        e "I . . . had no idea . . ."

                        e "I'm so sorry, Sarah."

                        e "I . . . er . . . listen . . ."

                        e "If it means anything, I promise . . ."

                        e ". . . . ."

                        e "I'll never let something like that happen to you again."

                        s "!!!!!"

                        e "No one deserves . . . any of that . . ."

                        e ". . . I really appreciate you showing me all of that . . ."

                        e ". . . but there's more . . . isn't there?"

                        s ". . . . . . . . . . . . . . ."

                        s ". . . . . ."

                        hide movie with fade
                        stop movie

                        s ". . . This time . . ."

                        s "You really can't look until later . . . okay?"

                        e "Alright."

                        stop music

                        play movie "video/A Cold Love Story Backstory Final 2.mp4"
                        $ renpy.pause(10, hard=True)
                        pause 113
                        stop movie

                        play movie "video/Blanksnowfinal.mp4" loop
                        show movie with fade

                        e "Alright . . . I won't look until later."

                        e "Thank you so much for being so open."

                        s "No . . ."

                        s ". . . . . . . . ."

                        s "Thank you."

                        jump go

                    if backstory == "missed":

                        $ backstory = "missed"

                        e "Hey, Sarah?"

                        s "Yeah?"

                        e ". . . could you maybe tell me a little about yourself?"

                        s ". . . what?"

                        e ". . . . . . . . . ."

                        e "You don't have to . . ."

                        e "But I just want to maybe . . ."

                        e ". . . know a little more about you . . ."

                        e "Er . . . I guess."

                        s ". . . . . . . . . ."

                        s "Okay, John."

                        s ". . . . I don't like talking about . . ."

                        s ". . . it . . ."

                        s "But I can give you some drawings . . ."

                        s ". . . I'm not very good."

                        s "Promise me you wont look at them until later?"

                        e ". . . I promise."

                        hide movie with fade
                        stop movie

                        stop music

                        play movie "video/A Cold Love Story Backstory Final 1.mp4"
                        $ renpy.pause(10, hard=True)
                        pause 135
                        stop movie

                        play movie "video/Kitchensarahsmilefinal.mp4" loop
                        show movie with fade

                        play music "Right Behind YouV2.mp3" fadeout 1 fadein 1

                        e "Okay, Sarah, I'll just put these in my backpack for now."

                        e ". . . I'll look at them later."

                        s ". . . . . . . ."

                        s "Thank you, John."

                        jump bruno

        "Pretend to drink":

            "I slowly lifted the cup feeling the warm liquid press against my pursed lips."

            e "Yeah . . . haha . . ."

            e "Uh . . . great!"

            s ". . . . . . . . ."

            s ". . . . . I'm glad."

            "Her eyes clouded for a brief second before she suddeny snapped upright again."

            jump bruno

label bruno:

    "Suddenly, from within her backpack, her phone rang."

    $ renpy.sound.play("Brunoring.mp3", channel = 1)

    hide movie
    stop movie

    play movie "video/Kitchensarahscaredfinal.mp4" loop
    show movie

    "I couldn’t help but face palm as I heard the ringtone."

    e "Bruno Mars?!"

    e "You're just as bad as my mom!"

    e "Hahaha, I can't believe you two have the same ringtone!"

    "She practically squealed in embarrassment as she fished around in her backpack, quickly tearing out the battery."

    "She sheepishly put the battery in her pocket and looked down at her feet."

    jump go

label go:

    $ renpy.sound.play("Household Door Front Door Close Squeaky 01.wav", channel = 1)

    hide movie with fade
    stop movie

    play movie "video/Kitchenemptyfinal.mp4" loop
    show movie with fade

    play music "Scary Horror Piano Music (Creepy Instrumental Music).mp3" fadeout 2 fadein 2

    "She dashed out of my house before I could respond."

    "Her form dissapeared into the frozen wasteland, slamming the door behind her."

    "I sat stunned for a good minute. "

    "Where the hell did that come from?"

    "She hadn't even taken a coat with her!"

    "Imagining her in just a T-shirt in that brutal cold made me want to run after her . . ."

    ". . . but I knew she was long gone by that point."

    e ". . . . . . ."

    e ". . . *sigh* . . ."

    jump sittingaround

label sittingaround:

    hide movie with fade
    stop movie

    play movie "video/Houseintfinal.mp4" loop
    show movie with fade

    "It was now well past 12:00 . . ."

    "The school would have called by now about my absence if it had been a school day."

    "I let myself relax a little more."

    ". . . . . . ."

    "But it wasn't quite enough."

    "This entire day was just a bit too much to handle."

    "Maybe I was just worrying too much?"

    menu:

        "Send Max another text: Ask about the school day":

            $ Max = "texted"

            "I pulled out my phone, quickly sending Max another text."

            ". . . . . . . . . . ."

            "That would have to do for now."

            "Now all I could do was wait . . ."

            menu:

                "Watch TV":

                    jump tv

                "Do chemistry homework":

                    jump chem

        "Watch TV":

            $ Max = "nottexted"

            jump tv

        "Do chemistry homework":

            $ Max = "nottexted"

            jump chem

label chem:

    hide movie with fade
    stop movie

    play movie "video/Homeworkfinal.mp4" loop
    show movie with fade

    "I sat at my living room desk for a few hours, wracking my brain over the questions . . ."

    ". . . Questions that probably would have been simple if I had actually paid attention."

    "The truth was . . ."

    ". . . Ever since Sarah had moved in, I hadn't really felt like myself."

    "Her constant presence made focusing difficult during school . . . and I almost felt like I needed to keep watch over her."

    "She had been acting strange all of today, but the Sarah I knew . . ."

    ". . . What I could only assume was the real Sarah . . ."

    "Was just a girl who had trouble talking with other people."

    "A girl who always had a bewildered look about her, as if the world was shifting under her feet."

    "A girl who hadn't even been able to look me in the eyes for several days after we first met."

    ". . . . . . ."

    ". . . She never talked about herself . . ."

    "She didn't seem to want to."

    "She would always listen, though."

    "And when she did, her eyes always seemed less piercing, less haunted,"

    "and I was certain she could sit silently for hours while I spoke."

    "I always knew something was off about her . . ."

    ". . . About the way she listened so devotedly."

    e ". . . *Sigh* . . ."

    "God, what do I know?"

    "Maybe I'm just overanalyzing things as per usual."

    ". . . . . ."

    "I'm not making any progress on this stupid worksheet . . ."

    ". . . maybe later . . ."

    menu:

        "Send Max another text: Ask about the school day" if Max == "nottexted":

            "I pulled out my phone, quickly sending Max another text."

            ". . . . . . . . . . ."

            "That would have to do for now."

            "Now all I could do was wait . . ."

            menu:

                "Watch TV":

                    jump tv

        "Watch TV":

            jump tv

label tv:

    hide movie with fade
    stop movie

    play movie "video/Tvrandomfinal.mp4" loop
    show movie with fade

    "I sat on the couch, mindlessly flicking through channels . . ."

    ". . . There was nothing good on . . ."

    jump maxback

label nomaxtext:

    ". . . . . Ugh . . . . ."

    "I suddenly realized that I should have been checking the news."

    "They would hopefully have information about the possibility of school tomorrow."

    "At the rate this storm was going . . . it wasn't likely . . ."

    menu:

        "Check the news":

            jump looknews

label maxback:

    "My phone suddenly buzzed."

    if Max == "nottexted":

        "What? Who could have been texting me?"

        "I hadn't texted Max . . ."

        jump damnitchris

    if Max == "texted":

        "Could that be Max?"

        jump damnitchris

label damnitchris:

    "Pulling out my phone, I realized that it had just run out of batteries."

    e "Ugh . . ."

    "This had gone far enough."

    "Even if there was school today, Max would have been home by now."

    "For him to keep this joke up so long . . ."

    menu:

        "Use your landline to call his house directly.":

            hide movie with fade
            stop movie

            play movie "video/Houseintfinal.mp4" loop
            show movie with fade

            "Groaning, I stood up and picked up my house phone."

            label callmaxhouse:

            "I punched in his number and brought the phone to my ear."

            ". . . . . . . ."

            ". . . Dial tone . . ."

            "I tried again."

            ". . . Dial tone . . ."

            "Frusterated, I looked at the monitor."

            "'No Service' It read."

            e "What?"

            "It was a landline!"

            "How is that even possible?"

            ". . . . . . . . ."

            "Must have something to do with the storm."

            hide movie with fade
            stop movie

            play movie "video/Tvrandomfinal.mp4" loop
            show movie with fade

            jump nomaxtext

        "Check to see if your landline has any messages.":

            hide movie with fade
            stop movie

            play movie "video/Houseintfinal.mp4" loop
            show movie with fade

            ". . . nothing . . ."

            e "*Sigh*"

            jump callmaxhouse

label looknews:

    "I flipped to the channel . . ."

    $ renpy.sound.play("TVSpook.mp3", channel = 1)

    hide movie
    stop movie

    play movie "video/Tvbusfinal.mp4" loop
    show movie

    play music "Right Behind YouV2.mp3" fadeout 1 fadein 1

    ". . . . . . . . . . ."

    ". . . My heart practically stopped."

    "I only heard the tail end,"

    r ". . . Not releasing images, or further details, regarding the bus incident."

    hide movie
    stop movie

    play movie "video/Tvspookfinal.mp4" loop
    show movie

    "Then the camera switched and they began talking about highway conditions."

    "I felt an absolutely horrible sickness gripping me."

    "It couldn't be."

    "Could it?"

    "Surely, that little dialog I had heard couldn't have been about . . ."

    ". . . . . . . . . ."

    "That would be ridiculous!"

    "I wasn't even sure what I heard!"

    "I was definitely overreacting . . ."

    ". . . after all . . ."

label feelbetter:

    menu:

        "Someone would have called me, worried about the massacre!":

            "Not if the police aren't releasing details about where and when it took place!"

            menu:

                "School didn't report me absent!":

                    "That's because my house phone isn't getting service!"

                    menu:

                        "Max was just playing a joke!":

                            "Then why didn't he ever text back?!"

                            jump suck

                "Max was just playing a joke!":

                    "Then why didn't he ever text back?!"

                    menu:

                        "School didn't report me absent!":

                            "That's because my house phone isn't getting service!"

                            jump suck

        "School didn't report me absent!":

            "That's because my house phone isn't getting service!"

            menu:

                "Max was just playing a joke!":

                    "Then why didn't he ever text back?!"

                    menu:

                        "Someone would have called me, worried about the massacre!":

                            "Not if the police aren't releasing details about where and when it took place!"

                            jump suck

                "Someone would have called me, worried about the massacre!":

                    "Not if the police aren't releasing details about where and when it took place!"

                    menu:

                        "Max was just playing a joke!":

                            "Then why didn't he ever text back?!"

                            jump suck

        "Max was just playing a joke!":

            "Then why didn't he ever text back?!"

            menu:

                "School didn't report me absent!":

                    "That's because my house phone isn't getting service!"

                    menu:

                        "Someone would have called me, worried about the massacre!":

                            "Not if the police aren't releasing details about where and when it took place!"

                            jump suck

                "Someone would have called me, worried about the massacre!":

                    "Not if the police aren't releasing details about where and when it took place!"

                    menu:

                        "School didn't report me absent!":

                            "That's because my house phone isn't getting service!"

                            jump suck

label suck:

    "Nothing I said to myself made me feel any better."

    "I tried in vain to calm myself down, but quickly realized that I HAD to know for sure."

    hide movie with fade
    stop movie

    "The house shook with gusts of wind, tremors being send down every dark hallway."

    play movie "video/Livingroomnight.mp4" loop
    show movie with fade

    "I stood up from my couch slowly, glancing at the snow beginning to plaster to the windows."

    "Although grey and dull, the flakes seemed to glow against the oppressive darkness as nightime fell."

    "I secured every layer I could find, grabbing my flashlight and taking several deep breaths."

    hide movie with fade
    stop movie

    $ renpy.sound.play("Household Door Front Door Close Squeaky 01.wav", channel = 1)

    "The frigid night air seemed to ripple with heat distortion as the door swung open."

    "I locked the door behind me, and fumbled the keys into my pocket with shaking hands."

    play movie "video/Walkingnight.mp4" loop
    show movie with fade

    "I began walking the route the bus would have taken, my pace slow . . ."

    ". . . the sickness growing worse with every crunch of snow under my feet."

    "The dim light from my house was becoming more and more distant . . ."

    ". . . disappearing altogether as I turned a corner."

    "It was now just me and the flurry of snow."

    "The skeletal trees surrounding me groaned against the wind."

    "Their twisted black shapes were silhouetted against the deep blue hue of the night."

    "I hadn’t seen another house for some time now."

    "The families in my neighborhood were exceedingly spread apart, and the empty stretches of road seemed to snake on forever at points."

    "More often than not, the snowplows didn’t even find the time to drive as deep into the community as I was going."

    "I slowly came to a stop, hesitation shaking my heart . . ."

    menu:

        "Keep going":

            "I couldn't stop here!"

            "I had come this far . . ."

            jump keepgoing

        "Turn back":

            "This was crazy!"

            "I was going to die out here . . . I was overreacting about the bus."

            "I better just turn around."

            jump turnaround

label keepgoing:

    "It was snowing quite heavily, but I was still certain I would be able to faintly see the tracks of the bus if it had driven anywhere."

    "Despite this, I hadn't seen its tracks in over a mile."

    "Ordinary cars rarely ever drove up the way I was walking . . ."

    ". . . and yet, I noticed that the roadway was layered with the tracks of smaller vehicles."

    "They looked fresh."

    ". . . . . . . . ."

    "That's when I saw something up ahead, barely visible in the haze."

    ". . . . . . . . ."

    "Lights."

    "Flashing red and blue just around the next bend."

    "Whatever sanity I had left was quickly draining."

    menu:

        "Keep going":

            jump keepgoingmore

        "Turn around":

            jump turnaround

label keepgoingmore:

    "I approached the lights and peaked around the corner . . ."

    $ renpy.sound.play("TVSpook.mp3", channel = 3)

    $ renpy.sound.play("Module Production Element Title Imaging Screech Digital Noise 03.wav", channel = 1)

    hide movie
    stop movie

    play movie "video/Busfinal2.mp4" loop
    show movie

    "There, surrounded by ambulances and police cars . . ."

    ". . . a mangled mess of metal and shattered glass . . ."

    ". . . Sat the bus I had been taking for nearly four years"

    "The windows were caked with blood . . . which was still a dark crimson red . . ."

    ". . . perfectly preserved in the cold."

    "The once hot, steaming liquid had frozen solid to the splintered glass, encicling small, bullet sized holes."

    "The ambulances were stuffed with body bags as the surrounding street was scattered with a few severed limbs."

    "I swore I could see steam softly rising from the dead white appendages . . ."

    ". . . as they were ever so slowly covered in drifting snow."

    ". . . . . . . . ."

    "There were several police officers conversing amoungst themselves . . ."

    "Surely, I couldn't be caught here, I looked downright suspicious . . ."

    ". . . Was it worth listening closer?"

    menu:

        "Listen to the officers":

            ". . . I snuck slightly closer, carefully measuring my steps."

            ". . . I could only make out a few words and jumbled phrases:"

            o ". . . hacksaw . . ."

            o ". . . . . removed post-mortem . . . "

            o ". . . . . . . . . . . . ."

            o ". . . a few pieces . . ."

            o ". . . . . . . . . missing."

            "One of them suddenly stood upright, gaze darting around the surrounding area."

            jump getaway

        "Turn back":

            jump getaway

label turnaround:

    "I couldn't do this!"

    "This was just all too much!"

    hide movie with fade
    stop movie

    "I hurridly turned around, scrambling back towards my house."

    play movie "video/Houseextnight.mp4" loop
    show movie with fade

    jump frontdoorspook

label getaway:

    "I staggered back, blind terror forcing me into retreat."

    hide movie with fade
    stop movie

    play movie "video/Houseextnight.mp4" loop
    show movie with fade

    "I began sprinting back to my house, trying to keep my stomach down as my heart lurched rapidly."

label frontdoorspook:

    ". . . . . . . . ."

    hide movie with fade
    stop movie

    play movie "video/Frontdoorfinal.mp4" loop
    show movie with fade

    "I reached my front door and frantically fumbled for the key with my numb fingers, looking behind me into the inky darkness."

    "I finally got the key in the lock and turned it . . ."

    $ renpy.sound.play("Glass Knock.mp3", channel = 1)

    "But suddenly, a knock on glass . . ."

    ". . . coming from above me . . ."

    "I looked up slowly, heart pounding."

    hide movie with fade
    stop movie

    play movie "video/Windowfinal.mp4" loop
    show movie with fade

    "There . . . in the window above me . . . the window to my room . . ."

    "I couldn't see much of anything."

    "The light was off."

    "Which was a problem . . ."

    ". . . because I knew I had left it on."

    $ renpy.sound.play("WindowSpookSound.mp3", channel = 3)

    $ renpy.movie_cutscene("Windowspookfinal.mp4", delay=None, loops=0, stop_music=False)

    play movie "video/Windowfinal.mp4" loop
    show movie

    e "FUUCK!"

    "Was that Sarah?!!?"

    "The realization made me stumble back, fear negating my ability to breath for a second."

    "Her face had been pressed up against the glass . . ."

    ". . . but it was so . . . wrong . . . horrific."

    ". . . That . . . horrible . . ."

    ". . . gut wrenching smile on her face . . ."

    "How the hell did she even get in?!"

    ". . . . . . . . . . ."

    hide movie with fade
    stop movie

    play movie "video/Frontdoorfinal.mp4" loop
    show movie with fade

    "I swallowed hard."

    "Sirens droned behind me in the distance."

    ". . . it was time to make a choice . . ."

    "I could run back to the police . . ."

    ". . . save myself, put this entire thing behind me . . ."

    ". . . never learn anything about what happened here on this cold day . . ."

    ". . . . . . . . . . ."

    ". . . Or . . ."

    ". . . . . . . . . ."

    "I could go inside."

    ". . . . . . . . . ."

    ". . . . . . . . . . . . . . . . . . ."

    hide movie with fade
    stop movie

    play music "myuu - Winter Trouble.wav" fadeout 1 fadein 1

    ". . . . . . . . . ."

    play movie "video/Houseextnight.mp4" loop
    show movie with fade

    menu:

        "Run back to the police":

            jump policebitch

        "Go inside":

            jump goinside

label goinside:

    ". . . . . . . . . . ."

    "I took a deep breath."

    $ renpy.sound.play("Household Door Front Door Close Squeaky 01.wav", channel = 1)

    hide movie with fade
    stop movie

    play movie "video/Entrywayfinal.mp4." loop
    show movie with fade

    e ". . . S- . . ."

    e ". . . Sarah?"

    e ". . . hello? . . ."

    e "What are you doing in here . . .?"

    "My voice trailed off."

    "A wind gust shrieked outside, dim moonlight dancing through the empty rooms of the house."

    "If Sarah was still inside . . ."

    ". . . she wasn't saying anything."

    $ renpy.sound.play("Thumps.mp3", channel = 1)

    ". . . . . . wait . . . . . ."

    "What the hell is that noise?"

    "It sounded as if something was falling down stairs . . ."

    ". . . Something heavy . . ."

    "I could only see the base of the stairs, so unless it fell all the way down . . ."

    stop movie
    hide movie

    $ renpy.sound.play("BodyStairs.mp3", channel = 3)

    $ renpy.movie_cutscene("Bodystairs.mp4", delay=None, loops=0, stop_music=False)

    play movie "video/Sarah9final.mp4" loop
    show movie

    s ". . . . . . ."

    s "You didn't give me time to prepare this one like the others . . ."

    s "Which is a shame . . ."

    s "After all,"

    s ". . . you said he was your friend . . ."

    ". . . . . . . . . ."

    "The gholish head dripped softly in the darkness . . ."

    "It was so pale and mangled that I didn’t immediately recognize it as Max’s."

    "A horrific expression was forever imprinted on his face as his eyes stared straight ahead, wide and unblinking."

    hide movie with fade
    stop movie

    $ renpy.sound.play("BodyFall.mp3", channel = 1)

    s "There, there . . ."

    s "What are you doin on the ground for?"

    s "Are you sick?"

    s "Catch a cold?"

    s "Sarah will make it all better."

    s "Isn't that right, John?"

    s "Right, John?"

    s "You need me to make you better."

    s ". . . make you better . . ."

    menu:

        ". . . . . . . . . . . . . .":

            jump bed

        ". . . . . . . . . . . . . .":

            jump bed

        ". . . . . . . . . . . . . .":

            jump bed

label bed:

    s "*Giggle*"

    s "Watch you feet on the steps . . ."

    s ". . . Don't let go of my hand . . ."

    ". . . . . . . . . ."

    s "Shhhhhh . . ."

    s "It's okay."

    play movie "video/Sarahbedfinal.mp4" loop
    show movie

    $ renpy.pause(2.0)

    s "*Blushes*"

    s ". . . It's cold in here . . . you know?"

    s "Maybe if you just . . ."

    s ". . . held me . . ."

    e ". . . . . . . . ."

    e ". . . . . . . . . . my . . . . . . . . ."

    e ". . . . . . . . . ."

    e ". . . . friends . . . ."

    s "Shhhhhhh . . ."

    s "John's friends are all here . . ."

    s ". . . Mrs. bus driver lady is over there in the corner."

    s "You don't need anyone but me . . ."

    s "Others will try to change you . . ."

    s ". . . corrupt you . . ."

    s "But I didn't want you getting lonely either."

    s "Not like me."

    s "So I kept your friends here."

    s "Most of Jenna is in your closet."

    s ". . . I cut a hole in your roof above the closet so she could stay there longer . . ."

    s "Room temperature is no good for friends."

    s "It must be cold."

    s "Like outside."

    s "I've let her be with you all week . . ."

    s ". . . but there is only me to love now."

    s "Don't you understand how I am protecting you?"

    s ". . . I love you, John."

    s "Much more than your parents . . ."

    s "You parents wanted to leave you but I made them stay with you . . ."

    s "Made them stay . . ."

    s ". . . under your bed."

    s "*Giggle*"

    s "Don't you understand?"

    menu:

        ". . . . . . . . . . . . .":

            jump badend

        ". . . . . . . . . . . . .":

            jump badend

        ". . . . . . . . . . . . .":

            jump badend

        ">>Final Backstory<<" if backstory == "allcomplete":

            jump finalbackstory

label badend:

    "I began thrashing around, trying to scream but only letting out strangled squeaks."

    "She giggled and interlaced her fingers with mine, pinning my arms down and bringing her face inches away, grinning from ear to ear."

    "Her head was tilted to one side, her dull grey eyes swirling with darkness."

    s "Only me to love now . . ."

    s "John loves me now . . ."

    e ". . . . . . ."

    e ". . . no . . ."

    s "You're so funny!"

    s "John loves me, and I love John . . ."

    s ". . . So much."

    s "And if his face looks at me with nothing but distain . . ."

    s ". . . I can change that."

    s ". . . I will change that."

    s ". . . if he has no face . . . I can imagine whatever expression I want."

    s ". . . you . . ."

    s ". . . will . . ."

    s ". . . smile . . ."

    s ". . . you . . ."

    s ". . . will . . ."

    s ". . . love me . . ."

    stop music

    play movie "video/Deathscene1.mp4"

    play music "Eternity Complete Master-2.mp3"

    $ renpy.pause(4.0)

    hide movie
    stop movie

    play movie "video/Creditsfinal.mp4"
    $ renpy.pause(10, hard=True)
    pause 32
    stop movie

    scene BadEnd
    with fade

    $ renpy.pause(4.0)

    scene black
    with fade
    show text "Thanks for Beta Testing" with dissolve
    $ renpy.pause(3.0)
    hide text with dissolve

    return

label finalbackstory:

    e ". . . I think I do . . ."

    hide movie
    stop movie

    play movie "video/Sarahbedscaredfinal.mp4" loop
    show movie

    s ". . . . . . .!"

    s ". . . . . . . what?"

    hide movie with fade
    stop movie

    stop music fadeout 2

    e "I understand."

    stop music

    play movie "video/A Cold Love Story Backstory Final 3.mp4"
    $ renpy.pause(10, hard=True)
    pause 95
    stop movie

    jump goodend

label goodend:

    play music "Eternity Complete Master-2.mp3"

    play movie "video/Sarahbedscaredfinal.mp4" loop
    show movie with fade

    s "You . . . . . ."

    s ". . . . How did you . . . ."

    s "I don't . . ."

    s ". . . . . . . . . . . . . ."

    s ". . . you . . . do . . . understand . . ."

    s ". . . . . . . . . . . . . ."

    s ". . . I"

    s "Love"

    s "You."

    s ". . . . . . . . . . . ."

    s ". . . but after everything I've done . . ."

    s ". . . . . . . . . . . ."

    s "What do you think . . ."

    s ". . . . . . . . . . . ."

    s ". . . of me?"

    s ". . . I will accept it . . ."

    s "Whatever you say . . ."

    s ". . . . . . . . . . . . ."

    s "No matter what."

    menu:

        "I wont leave you":

            e "Sarah . . ."

            e "You are . . . broken."

            e "You are a murderer, and those lives you took can never be replaced."

            e "You need to first understand this."

            e "Your delusions have cost me everything . . ."

            e ". . . . . . . . . . . ."

            e ". . . but I don't think you're beyond repair."

            e ". . . and for anyone to not try . . ."

            e ". . . try to help you past this . . ."

            e ". . . . . . . . . . . ."

            e "Sarah . . . I'll never look at you the same again . . ."

            e ". . . but I'm not going to leave you alone in this."

            s ". . . .!"

            e "What you've done is wrong . . ."

            e ". . . the way you think makes me fear for your life, as well as the lives of others . . ."

            e ". . . . . . . . . . ."

            e "Which is why I can't let you out of my sight ever again."

            s "!!!!!!"

            e "From now on . . . we're in this together."

            e "I won't let you hurt another person . . ."

            e ". . . and I won't let anyone ever hurt you."

            s ". . . . . . . . . . ."

            e "What do I think of you?"

            e ". . . . . . . . . . . ."

            e "I suppose I'll come to find out."

            e ". . . I don't think you know what love is."

            e "I think your delusions have warped the term . . ."

            e "For me to say I love you back . . ."

            e ". . . it would be wrong."

            e ". . . but I will say this . . ."

            e "I certainly hope we can come to love each other."

            e "You're beautiful."

            e "And while your heart may be tainted by a past you couldn't control . . ."

            e "I stand by my earlier statement . . ."

            e "You are not beyond help, not beyond repair."

            e "You are not lost."

            e "I will not lose you."

            e ". . . . . . . . . . ."

            e ". . . no matter what."

            s ". . . . . . . . . . . . . . . . . ."

            s ". . . I . . ."

            hide movie with fade
            stop movie

            s ". . . I would like that . . ."

            s ". . . . . . . . . . . . . ."

            s ". . . . very much . . . ."

            jump gooderend

        "I have to turn you in":

            e "Sarah . . ."

            e "You are . . . broken."

            e "You are a murderer, and you are clearly delusive beyond repair."

            e "I think you've been pushed too far, and I simply can't help you."

            e "I don't think anyone can."

            e "I'm going to have to turn you in."

            e "It's for your own good."

            s ". . . . . . . . . . . . ."

            s ". . . if you think so . . ."

            s ". . . . . . . . . . . . ."

            hide movie with fade
            stop movie

            s ". . . . . . . . . . . . . ."

            s "Then I accept."

            jump baderend

label gooderend:

    play movie "video/Creditsfinal.mp4"
    $ renpy.pause(10, hard=True)
    pause 32
    stop movie

    scene GoodEnd
    with fade

    $ renpy.pause(4.0)

    scene black
    with fade
    show text "Thanks for Beta Testing" with dissolve
    $ renpy.pause(3.0)
    hide text with dissolve

    return

label baderend:

    play movie "video/Creditsfinal.mp4"
    $ renpy.pause(10, hard=True)
    pause 32
    stop movie

    scene BadEnd
    with fade

    $ renpy.pause(4.0)

    scene black
    with fade
    show text "Thanks for Beta Testing" with dissolve
    $ renpy.pause(3.0)
    hide text with dissolve

    return

label policebitch:

    ". . . . . . . . ."

    ". . . yeeaaaaahhh . . . No."

    "I can't do that."

    "If I wanted to be safe, I would have run away a long time ago."

    ". . . it was time to finish this."

    "No way am I going to bitch out like I've done my whole life . . ."

    "It's time to go inside."

    jump goinside

    return
