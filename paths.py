wake_up = {
    "text": [
        "You awaken to find yourself in total darkness, disoriented and sore from a fall.",
        "Coughing, you slowly come back to your senses. Brushing off dirt,",
        "you push yourself off the crumbley rubble floor and rise to your feet."
    ],
    "choices": {
        "look around": {
            "text": [
                "As your eyes adjust, you realize you've stumbled across a cavern. No light seems",
                "to reach down here. You try but fail to brush away the thoughts of how deep",
                "underground you could actually be. Your only chance of survival is to find a way",
                "out. Your heart races as you take a deep breath and prepare to make your escape."
            ],
            "path": "wagon_hole"
        }
    }
}

wagon_hole = {
    "text": [
        "To the left of the eerie cave walls, theres a wrecked wagon rolled over on its side, on the right,",
        "a small almost hallway like crack, maybe big enough to fit yourself through.",
        "Do you 'walk over to the wagon' or 'check out the hole'?"
    ],
    "choices": {
        "walk over to the wagon": {
            "text": [
                "As your eyes adjust, you realize you've stumbled across a cavern. No light seems",
                "to reach down here. You try but fail to brush away the thoughts of how deep",
                "underground you could actually be. Your only chance of survival is to find a way",
                "out. Your heart races as you take a deep breath and prepare to make your escape."
            ],
            "path": "wagon"
        },
        "check out the hole": {
            "text": [
                "Walking over the rubbled rocks, you make your way over to the gaping hole in the wall.",
                "Its taller than you thought, but alot thinner. You could make your way through, but it'd",
                "be a tight fit."
            ],
            "path": "hole"
        }
    }
}

wagon = {
    "text": ["Do you try to 'help the man' or awkwardly walk away and 'check out the hole'?"],
    "choices": {
        "help the man": {
            "text": [
                "You crouch down, offering to help the man. After much stuggle, the wagon wont seem to",
                "budge. The man, a trader of some sort, seems to have given up on trying to get out,",
                " his lips dry and his face gaunt. Who knows however many days he has left.",
                "'leave me be' he says, his voice parched and dusty. 'get out while you still can.'",
                " Theres fear in his eyes, and you're surprised at how strong his grip is despite his",
                "state. 'dont let it pull you in!'",
                "Slowly, the man manages raise his hand, a twisted finger pointed to the corner.",
                " 'Folks who go down there dont come out' he whispers. 'Theres a magikin down there...'",
                "You tell him to rest, and he closes his eyes, maybe for the final time."
            ],
            "path": "help_the_man"
        },
        "check out the hole": {
            "text": [
                "Walking over the rubbled rocks, you make your way over to the gaping hole in the wall.",
                "Its taller than you thought, but alot thinner. You could make your way through, but it'd",
                "be a tight fit."
            ],
            "path": "the_hole"
        }
    }
}

hole = {
    "text": ["Do you try to shimmey your way'through the hole'or'walk over to the wagon'?"],
    "choices": {
        "walk over to the wagon": {
            "text": [
                "You walk over to the toppled wagon, carefully stepping over broken wood shattered",
                "off its wheels and base. Out of the corner of your eye, you see something squirming beneath the",
                "wagon. Its a man!"
            ],
            "path": "wagon"
        },
        "through the hole": {
            "text": [
                "Slowly slowly you make your way through the hole. Regret starts to fill your body as",
                "the whole gets smaller and smaller, till you can barely fit. Finally, after holding",
                "your breath and squeezing your cheaks clenched for what seems like forever, you make it",
                "out to the other side. Aint no way are you going back through there...",
                "You take in your new surroundings. Theyre honestly not much different to the last, a",
                "slightly bigger cavern maybe? Definitely much taller, but still a cave nevertheless...",
                "On the far side appears to be a river with running water, but it goes down a bend you",
                "cant see past. On the other side, an almost handcarved looking archway lies."
            ],
            "path": "cavern"
        }
    }
}

help_the_man = {
    "text": ["Should you follow his advice, steering clear and 'check out the hole',",
             "or should you 'climb down the hatch' he told you not to?"],
    "choices": {
        "climb down the hatch": {
            "text": [
                "Lowering yourself down the hole, you catch a glance at the man. He lays on the floor",
                "motionless, and you cant help but feel guilty that your curiosity has gotten the better",
                "of you. Climbing down, you're met with a brightly lit tunnel, golden torches lining the",
                "walls. You look back up as the hatch behind you seals closed. You hope you've made",
                " the right choice.",
                "You walk down the tunnel for what seems like forever, the torches never ceasing and the",
                "end never seeming nearer."
            ],
            "path": "the_tunnel"
        },
        "check out the hole": {
            "text": [
                "Walking over the rubbled rocks, you make your way over to the gaping hole in the wall.",
                "Its taller than you thought, but alot thinner. You could make your way through, but it'd",
                "be a tight fit."
            ],
            "path": "hole"
        }
    }
}

the_tunnel = {
    "text": ["do you 'keep walking' in the hopes that you might move, or take a rest and 'look around'?"],
    "choices": {
        "keep walking": {
            "text": [
                "You walk for what seems like forever. Theres no end in sight. You should have followed",
                "the old mans warning.",
                "",
                "Ending 1/16. 'Till my feet fall off'."
            ]
        },
        "look around": {
            "text": [
                "Your feet hurt from walking and this hallway doesnt seem to be going anywhere anytime soon.",
                "Curiosity piques again and you make your way over to the torches. Upon closer",
                "inspection, the base of the torch becomes clearer. On each handle, an animal seems",
                "to be carved deeply in. Maybe its not carved, but a button!",
                "Lion, Eagle, Snake, Leopard, Wolf, Bear, Lion, Eagle, Snake, Leopard, Wolf, Bear,",
                "over an over again. But which one to pick? You've seen enough Diana Jones movies",
                "to know one wrong move could be your doom..."
            ],
            "path": "torch"
        }
    }
}

torch = {
    "text": ["There must be some pattern here... 'Lion', 'Eagle', 'Snake', 'Leopard', 'Wolf' or 'Bear'?"],
    "choices": {
        "snake": {
            "text": [
                "whether it was luck or pure genius, the snake is the only reptile there. As you push",
                "the animal in, you hear a soft click. You jump back in shock as the flames shoot up",
                " and for a moment you panic. It was snake ...right? From red to blue, the flames flared",
                " up",
                "As the flames finally die down, smoke seeps out the wall, and the stones push themselves",
                "out of place. Stepping forward, you press your hands on the wall, and with a little",
                " effort, it swings open violently, leaving you stumbling inside. The wall swings",
                "shut behind you. oops...",
                "The room in front of you is dimmly lit, crystals and candles deck the shelves that",
                "aren't littered with books. In the middle of the room stands an alter. You cant tell",
                "if its the brightest or darkest thing in the room, something about it avoids your eyes.",
                "You can feel yourself being dragged in towards it."
            ],
            "path": "alter"
        },
        "lion": {
            "text": [
                "It's only as you press the animal deeper into the handle do you realise your mistake.",
                "The flames jum out at you, burning brighter and higher. The roof starts synging as",
                "hungry flames lick the ceiling, growing with every second. You can't see whats infront",
                "of you now, the room so hot its scewing your vision. You fall backwards to the floor",
                "as the hallway is ingulfed in flames. From red to white. Then black.",
                "",
                "Ending 2.1/16. 'At least you dont need a coffin...'"
            ]
        },
        "eagle": {
            "text": [
                "It's only as you press the animal deeper into the handle do you realise your mistake.",
                "The flames jum out at you, burning brighter and higher. The roof starts synging as",
                "hungry flames lick the ceiling, growing with every second. You can't see whats infront",
                "of you now, the room so hot its scewing your vision. You fall backwards to the floor",
                "as the hallway is ingulfed in flames. From red to white. Then black.",
                "",
                "Ending 2.2/16. 'Bit toasty warm...'"
            ]
        },
        "leopard": {
            "text": [
                "It's only as you press the animal deeper into the handle do you realise your mistake.",
                "The flames jum out at you, burning brighter and higher. The roof starts synging as",
                "hungry flames lick the ceiling, growing with every second. You can't see whats infront",
                "of you now, the room so hot its scewing your vision. You fall backwards to the floor",
                "as the hallway is ingulfed in flames. From red to white. Then black.",
                "",
                "Ending 2.3/16. 'I can relate to the gingerbread witch'"
            ]
        },
        "wolf": {
            "text": [
                "It's only as you press the animal deeper into the handle do you realise your mistake.",
                "The flames jum out at you, burning brighter and higher. The roof starts synging as",
                "hungry flames lick the ceiling, growing with every second. You can't see whats infront",
                "of you now, the room so hot its scewing your vision. You fall backwards to the floor",
                "as the hallway is ingulfed in flames. From red to white. Then black.",
                "",
                "Ending 2.4/16. 'Like a brick chimney, only without the promise of bacon...'"
            ]
        },
        "bear": {
            "text": [
                "It's only as you press the animal deeper into the handle do you realise your mistake.",
                "The flames jum out at you, burning brighter and higher. The roof starts synging as",
                "hungry flames lick the ceiling, growing with every second. You can't see whats infront",
                "of you now, the room so hot its scewing your vision. You fall backwards to the floor",
                "as the hallway is ingulfed in flames. From red to white. Then black.",
                "",
                "Ending 2.5/16. 'Never actually liked the cold, couldnt ever bear it...'"
            ]
        }
    }
}

alter = {
    "text": ["Its almost as if the voices call to you... ",
             "do you go up and 'touch the alter' or 'back away' and resist temptation?"],
    "choices": {
        "touch the alter": {
            "text": [
                "As you near closer, the voices get louder and louder. You press your hand down on the base",
                " and the voices start roaring. You can feel them, like worms writhing in the earth,",
                "hundreds of voices calling out to you, trying to force their way into your mind."
            ],
            "path": "voices"
        },
        "back away": {
            "text": [
                "You back away, whatever freaky shebang is going on there, you dont want it. As you step",
                "away, you trip over a poorly placed crystal, tumbling down to the ground. Two tumbles",
                "too many in your opinion. Rubbing your scraped knee, you look around at what you've",
                "fallen into. Just great, a creepy lookin magic circle and youre smack bang in the middle",
                "of it. On your right, a dusty book lies splayed open, and next to it, a chunk of sigils",
                "seems to be missing from the circle..."
            ],
            "path": "magic_circle"
        }
    }
}

voices = {
    "text": ["Do you 'accept the voices' and let them in or do you 'refuse' to let bodiless entity rack your brain?"],
    "choices": {
        "accept the voices": {
            "text": [
                "They flow through your mind, raging through it like a flood, wrecking everything in",
                "sight. Memorys, thoughts, ideas, pain, grief, love, life. They twist through you till",
                "you cant tell where they start and you end. You feel tears stream down your face, and now",
                "with all possiblities, thoughts, past present and future, you know all there is to posess,",
                " but even without them you understnand. There is nowhere else you could belong.",
                "Here forever you will stay.",
                "",
                "Ending 3/16. 'After the things ive seen, I'll need more than bleach...'"
            ]
        },
        "refuse": {
            "text": [
                "you stumble backwards, the voices piecing through your head, stabbing at your thoughts.",
                "It's too late to go back now, you can hear them hissing at you, bubbling in your",
                "skull like hot tar. You writhe in pain as they scrape away from inside your head",
                "pushing out behind your eyes and bleeding out your nose. You lose conciousness you",
                "think, or maybe they though. It's hard to tell where they start and you end.",
                "",
                "Ending 4/16. 'A Colony of seagulls - mine mine mine mine mine mine mine mine mine'"
            ]
        }
    }
}

magic_circle = {
    "text": ["Do you either 'draw the sigils' from the book or 'try to leave' the magic circle?"],
    "choices": {
        "draw the sigils": {
            "text": [
                "You dont dare to brush the dust off the book in the fear that you might brush away",
                "the pages aswell, but after careful oservation, you draw the final sigils. Nothing",
                "happens at first, but as you turn around, the blood from your scrapped knee smears",
                "against the floor and the circle catches alight almost instantly. In a blaze of white and rushing wind",
                "you feel your stomach drop, squash and fold all in one. You shut your eyes in the hope",
                "that you dont throw up from whatevers happening right now. When you open them again",
                " you think you might have died the lights so bright. After a few seconds, you dare",
                "to look again. Sunlight streams down on you and you cant help but grin. You're free.",
                "",
                "Ending 5/16. 'teleported the food out of my body too...'"
            ]
        },
        "try to leave": {
            "text": [
                "No way hozay are you getting twisted up in any of this madness. How did you not even",
                "see this giant circle in the first place? You really should have just listened to",
                "that poor nice man. In a huff, you turn to get up, shuffling onto your knees and",
                "hands as you slowly stand back up. As you do, you feel the chalk(?) beneath",
                "your skin shift in place, smuding and smearing along the floor. You can feel the",
                "portal activate beneath you, the sounds of errors and mistakes ringing through your",
                "ears. Whoever made this was a monster. Oh shi-",
                "",
                "Secret 'Ending' - 'Blue Screen of Death. Please Wait for your Life to Restart'"
            ],
            "path": "wake_up"
        }
    }
}

cavern = {
    "text": ["Do you decide to take a dip and 'follow the river' or do you make your way 'through the archway'?"],
    "choices": {
        "follow the river": {
            "text": [
                "Following the stream of running water, you walk down the banks of the cave. Any dry",
                " land next to the river very quickly disapears and slowly you emerge yourself",
                "in the cold running water. As the river widens, the current starts to pull stronger, forcing",
                "you out into the middle of its depths. Your feet have no hopes of touching the bottom",
                "now as the winding water drags you along, the current getting stronger and faster",
                " pulling you down into its depths."
            ],
            "path": "river"
        },
        "through the archway": {
            "text": [
                "You're glad to see that this archway is much more reliable than the other, a wide",
                "path at all times and a solid metre round you at all times. At the end of the hallway,",
                "there looks to be some sort of old wooden door. Decorated only by a simple brass doorknob",
                "and a keyhole. A faint chanting can be heard, growing louder and louder as you near",
                "it. '16! 16! 16! 16!'"
            ],
            "path": "door"
        }
    }
}

river = {
    "text": ["Do you try and 'grip onto the sides' or 'follow the stream', wherever it may lead?"],
    "choices": {
        "grip onto the sides": {
            "text": [
                "If theres one thing you remember from the surf life saving club, its Dont Panic",
                "Slip Slop Slap, the flags are yellow and red so colourblind people can see them and when",
                "caught in a rip, swim to the side! Not so gracefully, you make your way over to",
                "the edge and cling on for dear life. up ahead, a small ledge seems to stick out.",
                "Carefully, you slide yourself over, dragging yourself out of the water like a dead slug.",
                "Ahead of you, there lies a sliver of a tunnel. At the end, a single beam of light",
                "shines down. Shivering and drenched, you make your way over, the stone turns to rocks",
                "and from rocks to dirt. A single ring of blue mushrooms surrounds the beam of light."
            ],
            "path": "beam_of_light"
        },
        "follow the stream": {
            "text": [
                "Unsure if youre strong enough to grip on to the sides, and curious to see where the",
                "water will lead, you cannot help but go flow with the stream as it pulls you in,",
                "faster and harder, grabbing at your ankles and pulling you down, ripping the air form",
                "your lungs and your body from the surface. At some point the cavern shrinks down, the",
                "ceiling now scraping the skin off your hands as you thrash violently for air. Whoever",
                "said that drowning was a peaceful death was a complete liar. Suddenly I feel myself shoot",
                "out the other side, air underneath me and the roaring crash of water below me.",
                "Death by waterfall... great",
                "",
                "Ending 6/16. 'Going with the flowing a little too much there man... not narly bro'"
            ]
        }
    }
}

beam_of_light = {
    "text": ["Do you 'dig at the dirt' or do you check out the 'sussy mushy'?"],
    "choices": {
        "dig at the dirt": {
            "text": [
                "You test the dirt, slowly dusting away as to not get any in your eyes, but as the breeze",
                "outside blows and the weight of the cave grows, you cannot help but start to claw at",
                "the soft dirt, breaking away at it till youre diggin upwards like some wild desperate",
                "animal. It falls down into your eyes and mouth, clinging to your hair and underneath",
                "your nails. Dirt is coming down in chunks now, falling around you till the whole roof",
                "collapses. Knowing this could be it for you, you give one final push. How dare you",
                "give up when youre so close now. The dirt around you will not be your grave.",
                "",
                "Out of the darkness, you gasp, pulling yourself up out of the dirt into the fresh air above.",
                "Youre wet and cold and covered in dirt, but at least you are free. As you lie down",
                "to rest, you feel the grass tickle your skin and the sun on your face. you close your eyes",
                "and breathe.",
                "",
                "Ending 7/16. 'photosynthesis at its finest.'"
            ]
        },
        "sussy mushy": {
            "text": [
                "You're not sure why but you feel as though youve seen this before. A simple kick",
                "of a mushroom and the circle is broken, maybe you were an electrician before this...",
                "As the magic mushroom circle fades away, so does the hole in the ceiling, and your one",
                "sense of hope turns into a flimsy lightbulb covered by a cheap magic trick of an illusion.",
                "Behind it though, the wall of dirt seemed to fade, or more accurately, crumble away.",
                "What were left were two sets of stairs. Up, and down... Why did this feel like another",
                "trick?"
            ],
            "path": "stairs"
        }
    }
}

stairs = {
    "text": ["'Up' or 'down?'"],
    "choices": {
        "up": {
            "text": [
                "You walk up the stairs. After all this, your calves are burning, but what else is",
                "there to do? After walking upwards for a while, you finally enter a room. Its a big",
                "room, massive even. Like something out of a harry potter scene, staircases everywhere,",
                " up, down, through a wall, moving and turning and twisting. At one point while youre",
                "walking you swear youre upsidedown, and another, you think you might have even seen",
                "yourself looking the other way, like one of those infinite public bathroom mirrors.",
                "The infinite labyrinth trap. You saw that on reddit once. Either way, youre not getting",
                "out any time soon...",
                "",
                "Ending 9/16. 'Are we there yet?'"
            ]
        },
        "down": {
            "text": [
                "You've played enough of these games to know its a trick, a trap of false sweetness",
                "and comfort. You go down. The stairs wind in a spiralling slope for what seems like",
                "forever. At some point, youre not sure where the roof and the floor are, they've sort",
                "of blended together? Your suspision confirms it when at the end of the stairs, the",
                "trap door is on the wall infront of you instead of the floor. At this point, theres",
                "really no where else to go. Climbing through and out of the floor, youve made it",
                "to the other side. The wind blows in your face and the sun shines on your back. You",
                "close the trapdoor and dont look back.",
                "",
                "Ending 8/16. 'Dont ask me, i dont know'"
            ]
        }
    }
}

door = {
    "text": ["Do you dare to 'look in the keyhole' or do you waltz in unannounced and",
             "'jiggle the door knob'?"],
    "choices": {
        "look in the keyhole": {
            "text": [
                "As you bend over, you slowly bring your face forward to catch a better glimpse of",
                "whoever migh be on the other side. As you look in, the chanting stops momentarily,",
                "and you catch a glimpse of green skin and fur pelts. Just as you get a look, something jabs",
                "you in the eye, HARD. You stumble back in surprise clutching at your face as behind the",
                "door erupts in cheers. '17! 7! 17! 17! 17!'",
                "Falling backwards, you feel the ground shift underneath you, and then completely cave",
                "in. The trap door leave you in a dark pit filled with nothing but cold mushrooms and",
                "musty air. Infact, its probably not must but spores, seeping into your lungs. You",
                "cant stay here. On the far side of the low lying cavern theres a small hole. Probably",
                "too small..."
            ],
            "path": "trapped"
        },
        "jiggle the door knob": {
            "text": [
                "After much jiggling, the door does not budge. The chanting stops and the sound of squabbling",
                "chatter can be heard on the other side of the door. Slowly and cautiously, the door",
                "opens, and a single goblin steps out. 'What you want?' his tone sharp and his english",
                "poor. He looks uneasy and angry, or awkward and constipated... its kinda hard to tell..."
            ],
            "path": "goblin"
        }
    }
}

trapped = {
    "text": ["Do you try to 'crawl through the hole' even though you might get stuck,",
             "or do you want to try and 'wait it out'?"],
    "choices": {
        "crawl through the hole": {
            "text": [
                "It's a tight fit bit you've managed to squeeze yourself in. The hole is almost suffocating as you",
                "slowly crawl your way through. Theres barely enough room to move forward and definitely",
                "no way to turn around now. You go on for what seems like forever. Theres no light with you",
                "down there. No way to know if the tunnel is going to end or go on forever. You cant tell",
                "when it'll start to get bigger, if it ever does.",
                "Hours pass maybe. Youre not sure. Theres no way of telling.",
                "Finally, after your knees are bloody and your hands blistered, you feel infront of",
                "you a drop, a room, open space. You crawl out, collapsing on the floor in relief.",
                "But you rejoice too soon. The same room as before lies before your eyes, with only one",
                "way in and one way out."
            ],
            "path": "despair"
        },
        "wait it out": {
            "text": [
                "You wait, and wait, the hole in the wall staring at you, its darkness inviting you in.",
                "You can feel the spores in your chest, your breathing is heavy now. Strained.",
                "You cant keep doing this much longer. You feel yourself slip away as your eyes roll back.",
                "This is how it is?",
                "",
                "Ending 10/16. 'I ordered meatlovers, not mushrooms!'"
            ]
        }
    }
}

despair = {
    "text": ["What else is there to do? The hole stares at you, dark and forboding.",
             "Do you 'go back in' or 'wait it out'?"],
    "choices": {
        "go back in": {
            "text": [
                "Theres nothing else you can do. You have to go back in. You cant cry, theres not enough",
                "air, space or energy for that. You just have to keep going forward. Forward",
                "And forward",
                "Your knees burn and scream and your hands are bloody and filled with rocks. Then, when",
                "you think you cant take any more, the path stops. A dead end. How could that even",
                "be possible, when you had just crawled down this path a few hours ago. You scream. you",
                "know you shouldnt, but what else could you do. You scream and you cry and claw at the",
                " wall and sob with your head in your hands and blood on your cheaks. You pound",
                "on the wall, the bangs echoing through the tunnel. The bangs? BANGS! ITS HOLLOW",
                "Scratching at the walls, digging away at the dirt, there underneath is a wooden board.",
                "You cant help but laugh as you rip the wood, splinters stinging your hand.",
                "Light, Grass, Wind.",
                "You breath a fresh breath of air for what seems like the first time in forever.",
                "",
                "Ending 12/16. 'He had us in the first half ngl'"
            ]
        },
        "wait it out": {
            "text": [
                "You wait, and wait, the hole in the wall staring at you, its darkness inviting you in.",
                "You can feel the spores in your chest, your breathing is heavy now. Strained.",
                "You cant keep doing this much longer. You feel yourself slip away as your eyes roll back.",
                "This is how it is?",
                "",
                "Ending 11/16. 'You should go to the doctors if your chest is feeling so spore...'"
            ]
        }
    }
}

goblin = {
    "text": ["Do you try to 'talk with him' or are you putting your hackles up,'ready for a fight'?"],
    "choices": {
        "talk with him": {
            "text": [
                "You try, after much squabbling and difficulty, to tell him about your situation. Trapped",
                "underground and looking for a way out, any way out. After much confering with his fellow friends",
                "and suspicious looks, the goblins come to a conclusion. 'answer riddle, help you out.",
                "Get wrong, we eat!' Not exactly the best deal, but hey, its better than nothing...",
                " maybe...",
                "",
                "'oki, hahem.' Still cold and wet, youre not really in the mood for waiting for little",
                "green pointy teethed men, but what can you do. 'when young, i tall. when old, short.",
                "what candle an i? O-' The goblins eyes widen in fear, as he turns back to his friends.",
                "They dont seem to have noticed, I'm pretty sure hes the only one smart enough to",
                "speak."
            ],
            "path": "riddle"
        },
        "ready for a fight": {
            "text": [
                "You tense up and the goblin can see it. His dark eyes squint as he smells the fear",
                "seep off you. Slowly he draws out his stone carved knife and you raise your arms.",
                "Not sure what youre going to do with them considering your fighting experience",
                "against a goblin is little none, but you get ready noneoftheless. The little green",
                "menace screams and you scream back. You can take him! Sure, maybe you could have",
                "taken the one half your size, but definitely not the 26 of them all at once. You very",
                "quickly regret your decisions.",
                "",
                "When you wake back to conciousness, you see youve been tied up to a pole and chucked on",
                "some dreadfully cold alter. Marble may look nice but it is FREEZING. Around you, four",
                "goblins stand, donned in dark hoods and chanting olden spells. One approaches, and as",
                "he nears, you see the knife glint in the light of the candles..."
            ],
            "path": "sacrifice"
        }
    }
}

riddle = {
    "text": ["Theres only really two options here. Act thoughful and wise, pondering till you",
             "come to the conclusion 'candle', or lie for the sake of the goblin, and say something",
             "else, anything else...'an egg'...?"],
    "choices": {
        "candle": {
            "text": [
                "Looking as thoughtful as you could and making MANY pondering and thinking noises,",
                "You finally make the decision. As the goblin nervously converys the news to his mates,",
                "you relax in your secured victory. Reluctantly, the goblins let you through the door,",
                "The smartest one leading the way. Once we're out of earshot, the goblin Bursts into",
                "conversation. He discusses the history of the mines, how they were built and where the",
                "came from, leading you all the way to the top. You thank him, and he bows, flashing",
                "a toothy grin. You step out of the cave mouth and wave the goblin goodbye. Who",
                "knows what adventures lie ahead of you...",
                "",
                "Ending 13/16. 'His name was goblin gary.'"
            ]
        },
        "an egg": {
            "text": [
                "The goblin stares up at you baffled and you flash him a awkward smile...  Aw shit,",
                "you forgot about the getting eaten promise... Before you even know whats happening",
                "The goblin has stabbed you in the gut. Twisting the blade. 'man wtf-' You dont have",
                "time to finish your sentence, as your body disintergrates into nothing but pixles.",
                "'GAME OVER. RESPAWN' You find yourself awake at the enterance of a cave. Picking yourself",
                "up, you promptly walk the other direction. You think youve had enough caves for one",
                "day.",
                "",
                "Ending 14/16. 'Its all a simulation, matrix style!'"
            ]
        }
    }
}

sacrifice = {
    "text": ["The goblin raises the knife over you, its gleam sharp and promising.",
             "Do you 'accept your fate' or 'fight' till your last breath?"],
    "choices": {
        "accept your fate": {
            "text": [
                "The blade comes down. You've tried your best, It just wasnt enough. You close your eyes.",
                "It was swift",
                "and painless.",
                "",
                "Ending 16/16. 'The final Sleep.'"
            ]
        },
        "fight": {
            "text": [
                "Thrashing around on the cold marble altar, you will not go down without a",
                "fight. Your hands and legs may be tied but they were foolish in not gagging",
                "your mouth. You bite down on the little green mans hands, The taste of his",
                "blood in you mouth. You spit it on the marble as the goblin howls in",
                "pain. A flash of green as the magic circle lights up around you. You grin.",
                "Adios! When you awake, youre above ground, damp dirt beneath your skin",
                "and droplets speckled on your face. Tied up, but nevertheless alive.",
                "",
                "Ending 15/16. 'Tastes like a bad spinach smoothy...'"
            ]
        }
    }
}