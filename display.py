#!/usr/bin/env python

import I2C_LCD_driver
import time
import random

mylcd = I2C_LCD_driver.lcd()

#adding the spaces after each word is just a jank way of making sure the screen is clear every time run_display executes
#we at 233
firstLineData = ["hello               ",
        "good morning                    ",
        "fox n'                       ",
        "good morning                     ",
        "HEAD ON APPLY                    ",
        "whatcha doin                   ",
        "call your                  ",
        "call your                  ",
        "love you                  ",
        "try some                  ",
        "wonder if u                   ",
        "im a peepee                  ",
        "belle was                  ",
        "call ur                   ",
        "wonder how aunt                  ",
        "Even monkeys                  ",
        "Saru mo ki                  ",
        "Sumeba                  ",
        "Nana korobi,                  ",
        "Kappa mo                  ",
        "Juunin                  ",
        "Neko ni                  ",
        "Deru kugi wa                  ",
        "He wo hitte,                  ",
        "Ningen banji                  ",
        "May I take                  ",
        "SASAGEYO                  ",
        "ice cream                  ",
        "flip flop                  ",
        "handycap                  ",
        "bench press                  ",
        "omae wa                  ",
        "pandas                  ",
        "Go eat some                  ",
        "Want some pork                  ",
        "Tango                  ",
        "La                  ",
        "I like                  ",
        "Txt park                  ",
        "Screeny                 ",
        "Super                  ",
        "Try some                  ",
        "wake up wake up                  ",
        "the dew is on                  ",
        "wonder how                  ",
        "wonder how brycer                  ",
        "brush ur                   ",
        "did u                   ",
        "did u brush                  ",
        "bingo bayngo                  ",
        "How dusty                  ",
        "Read a                  ",
        "park is coding                  ",
        "get a haircut                  ",
        "today will                  ",
        "   :c               ",
        "        (^o^)          ",
        " ;)          ",
        " ;-]                ",
        "  X-p                  ",
        "  X-P                  ",
        "  :-P                 ",
        " :-X                  ",
        " O:-)                  ",
        " %-)                  ",
        " >:-)                  ",
        "  :-####                  ",
        "  <-<                  ",
        " >_>                  ",
        " <_>                  ",
        " :E                  ",
        " =:0]                 ",
        " )_)                  ",
        "    8-D             ",
        "   ;-]               ",
        "    :-P              ",
        "     :-0             ",
        "    <_<              ",
        "     =:o]             ",
        "    7:^]              ",
        "  <3 <3 <3                ",
        "   0-0              ",
        "   o_____o               ",
        "   >.<               ",
        "  V.v.V                ",
        "the early bird                  ",
        "pain is weakness                  ",
        "lets blow this                  ",
        "u need a                  ",
        "how bout u do                  ",
        "google 'kowloon                 ",
        "google 'north                  ",
        "where the fuck                  ",
        "r/evilbuildings                  ",
        "change ur sheets                  ",
        "6852 islands                  ",
        "P. Sherman 42                  ",
        "mornin'                  ",
        "the hash                  ",
        "rawr                  ",
        "try some                  ",
        "go pet                  ",
        "buy a lottery                  ",          
        "tokyocyborg                  ",
        "watch Lost in                  ",
        "play valorant                  ",
        "cook some dang                  ",
        "hi                  ",
        "i am a                  ",
        "a shrimps heart                  ",
        "Shaq only ever                  ",
        "90% of hmns live                  ",
        "mor trees on                  ",
        "ylw stripes on                   ",
        "the word bed                  ",
        "xD                  ",
        " 0_____0                  ",
        " o_____o                 ",
        "  8===D                ",
        "   X_X               ",
        "    UwU              ",
        " 911 benbrook                ",
        "  501                ",
        "  1f900                ",
        "  UV3C0                ",
        "  scratch                ",
        "  more like 10                ",
        "kasha                 ",
        "neon                  ",
        "double                  ",
        "full focus:                  ",
        "boil em                  ",
        "stick em in                  ",
         "fire in                    ",
        "i've got                    ",
        "hoof kick hoof                    ",
        "Mario kart                    ",
        "Lizzie                    ",
        "get up and                    ",
        "wake up wake up                    ",
        "im a little                    ",
        "im missez...                    ",
        "am i just...                    ",
        "what....                    ",
        "i suggest                    ",
        "wake me up                    ",
        "gawrsh                    ",
        "Good Mornin.                    ",
        "Administratively                    ",
        "Parsimonious                    ",
        "multiprogramming                    ",
        "counterbalancing                    ",
        "incomprehensible                    ",
        "enviornmentalism                    ",
        "Christianization                    ",
        "undifferentiated                    ",
        "undiscriminating                    ",
        "snowdrops bow their                    ",
        "Delightful display                    ",
        "Like crunchy                    ",
        "gold leaves                    ",
        "The chill,                    ",
        "Summer tongue                    ",
        "peace and quiet                    ",
        "strokes of                    ",
        "madness of world                    ",
        "Mellow, mild,                    ",
        "I sleep                    ",
        "coolness fills                    ",
        "your eyes                    ",
        "their image burnt                    ",
        "scarred by                    ",
        "picking up                    ",
        "or seashells strewn                    ",
        "pure                    ",
        "when it's                    ",
        "what will begin                    ",
        "will it                    ",
        "Fresh spring                    ",
        "That's the sound                    ",
        "The presence                    ",
        "Glorious                       ",
        "Decorating the                       ",
        "Awaiting                       ",
        "Bees nudged the                       ",
        "babies peeped out                       ",
        "One fine                       ",
        "Full strawberry                       ",
        "High tides fill                       ",
        "Rain hits                       ",
        "A heavenly                       ",
        "Winter fights                       ",
        "flowers bloomed                       ",
        "ur.....                       ",
        "stop                       ",
        "masturbation                       ",
        "molly n'                          ",
        "Frank                          ",
        "cookoo                          ",
        "Chop                          ",
        "Quit that ecig                          ",
        "change ur                           ",
        "change ur pillow                          ",
        "clean ur mouse                          ",
        "clean ur keyboard                          ",
        "wash mousepad w/                          ",
        "2nite u will                          ",
        "pork liver                          ",
        "fuck                          ",
        "eat me                          ",
        "I'm                          ",
        "Ak47                      ",
        "Erin                      ",
        "Mikasa                      ",
        "Sasha                      ",
        "Hange                      ",
        "Armin                      ",
        "Reiner                      ",
        "Levi                      ",
        "Annie                      ",
        "Erwin                      ",
        "Jean                      ",
        "Hitagi                      ",
        "Nadeko                      ",
        "Koyomi                      ",
        "Shinobu                      ",
        "Tsubasa                       ",
        "Meme                       ",
        "Mayoi                       ",
        "Karen                       ",
        "Suruga                       ",
        "Tsukihi                       ",
        "bloody                       ",

        ]

secondLineData = ["you damn fucker               ",
        "fella                    ",
        "falco                       ",
        "and good night                     ",
        "TO FOREHEAD                    ",
        "benny                   ",
        "mother                  ",
        "father                  ",
        "bwudda                  ",
        "oat milk                  ",
        "had nitemares                  ",
        "boy                  ",
        "a good pup                  ",
        "dang sister                  ",
        "Kim is doin'                  ",
        "fall from trees                  ",
        "kara ochiru                  ",
        "Miyako                  ",
        "ya oki                  ",
        "kawa nagare                  ",
        "tou iro                  ",
        "koban                  ",
        "utareru                  ",
        "shiri tsubome                  ",
        "saiou ga uma                  ",
        "Your Hat Sir?                  ",
        "SASAGEYOOO                  ",
        "soda                  ",
        "no feet                  ",
        "but eat meat                  ",
        "chest work                  ",
        "mou shinde iru                  ",
        "231                  ",
        "ramen 2day                  ",
        "liver paste?                  ",
        "Sucka!                  ",
        "Bambi!                  ",
        "Frozen Hotsauce                  ",
        "'persimmon man'                  ",
        "hungy 0_0                  ",
        "Salad?                  ",
        "boba tea 2day                  ",
        "the sun is up                  ",
        "the buttercup                  ",
        "nene is doin'                  ",
        "is doin'                  ",
        "teeth 2day?                  ",
        "floss 2day?                  ",
        "ur tongue 2day?                  ",
        "bongo                  ",
        "is that PC boi                 ",
        "fkn book                  ",
        "me at 8:43am                  ",
        "hippie                  ",
        "be lovely :D                 ",
        "                  ",
        "                  ",
        "                  ",
        "                  ",
        "                  ",
        "                  ",
        "                  ",
        "                  ",
        "                  ",
        "                  ",
        "                  ",
        "                  ",
        "                  ",
        "                  ",
        "                  ",
        "                  ",
        "                  ",
        "                  ",
        "                  ",
        "                  ",
        "                  ",
        "                  ",
        "                  ",
        "                  ",
        "                  ",
        "                  ",
        "                  ",
        "                  ",
        "                  ",
        "                  ",
        "gets the worm                  ",
        "leaving ur body                 ",
        "popsicle stand                 ",
        "break 2day bub                  ",
        "25 jumpin jacks                  ",
        "walled city'                  ",
        "sentinel island'                  ",
        "i am?                 ",
        "good sub                  ",
        "damn boi                  ",
        "in japan                  ",
        "Wallaby Way                  ",
        "  :D                ",
        "slingin' slasher               ",
        " XD                 ",
        "kombucha 2day                  ",
        "an animal                  ",
        "ticket bish                  ",
        "Vol.1 playlist                  ",
        "Translation                  ",
        "w/ bwudda                  ",
        "pasta 2day                  ",
        "sfop                  ",
        "sentient being                  ",
        "is in its head                  ",
        "made 1 3 pointr                  ",
        "in north hemsphr                  ",
        "Earth than stars                  ",
        "rd 10 feet long                  ",
        "look like a bed                  ",
        "random                  ",
        "                  ",
        "                  ",
        "                  ",
        "                  ",
        "                  ",
        "  circle                ",
        "  kirby                ",
        "  90eaa                ",
        "                  ",
        " fadidaleedoe                 ",
        " slow fingers                 ",
        "funk                  ",
        "gyuren                  ",
        "waitaminute                  ",
        "water breath                  ",
        "mash em                 ",
        "a stew                  ",
        "the hole                    ",
        "your trail                    ",
        "kick bah bah bah                    ",
        "wee                    ",
        "loves you <3                    ",
        "stretch yo                    ",
        "the sun is up                    ",
        "teacup                    ",
        "nezbit                    ",
        "a screen?                    ",
        "am I???                    ",
        "u need chicfila                    ",
        "wake me up inside                    ",
        "sora                    ",
        "Mr. Corbitt                    ",
        "Amazing                    ",
        "Parsimmon                    ",
        "hydroelectricity                    ",
        "dermatosclerosis                    ",
        "emotionalization                    ",
        "characterisation                    ",
        "hyperventalation                    ",
        "responsibilities                    ",
        "authoratarianism                    ",
        "pure white heads                    ",
        "to the sun's glory                    ",
        "cornflakes                    ",
        "rustle underfoot                    ",
        "worming in                    ",
        "awakes                    ",
        "reigns                    ",
        "affection                    ",
        "locked away                    ",
        "May day                    ",
        "peacefully                    ",
        "the air                    ",
        "are fire                    ",
        "into my soul                    ",
        "beauty                    ",
        "pebbles                    ",
        "on soft sand                    ",
        "relaxation                    ",
        "all over                    ",
        "in its place?                    ",
        "be better?                    ",
        "morning time                    ",
        "of solitude                    ",
        "of peace                    ",
        "Sunset                       ",
        "night sky                       ",
        "the moon                       ",
        "flowers                       ",
        "of the nest                       ",
        "crisp morning                       ",
        "moon                       ",
        "the dune                       ",
        "my windows                       ",
        "sound                       ",
        "to stay                       ",
        "today                       ",
        "gay                       ",
        "procrastinating                       ",
        "station                       ",
        "frank                          ",
        "Sinatra meow                          ",
        "bean boy                          ",
        "Suey!                          ",
        "boyo                          ",
        "sheets boi                          ",
        "case damn                          ",
        "ew nasty                          ",
        "ew nasty                          ",
        "dishsoap n water                          ",
        "dream of me                          ",
        "paste                          ",
        "you                          ",
        "poop                          ",
        "pregnant                          ",
        "2700                      ",
        "Yeagar                      ",
        "Ackerman                      ",
        "Blouse                      ",
        "Zoe                      ",
        "Arlert                      ",
        "Braun                      ",
        "Ackerman                      ",
        "Leonhart                      ",
        "Smith                      ",
        "Kirstein                      ",
        "Senjougahara                      ",
        "Sengoku                      ",
        "Araragi                      ",
        "Oshino                      ",
        "Hanekawa                       ",
        "Oshino                       ",
        "Hachikuji                       ",
        "Araragi                       ",
        "Kanbaru                       ",
        "Araragi                       ",
        "hell                       ",
        ]

"                  ",
"                  ",
"                  ",
"                  ",
"                  ",
"                  ",
"                  ",
"                  ",
"                  ",
"                  ",
"                  ",
"                  ",


### this is the original stuff to make the time and date display
# while True:
#     mylcd.lcd_display_string(time.strftime('%I:%M:%S %p'), 1)
#     mylcd.lcd_display_string(time.strftime('%a:%b:%d 20%y'), 2)

#function to make sure another function only runs once
def run_once(f):
    def wrapper(*args, **kwargs):
        if not wrapper.has_run:
            wrapper.has_run = True
            return f(*args, **kwargs)
    wrapper.has_run = False
    return wrapper



@run_once
def run_display():
#         while True:
            listItemCorrelator = random.randint(231,232)
            #we use list(list)[number] to grab the list item w/ the same index as each other in both lists
            mylcd.lcd_display_string(list(firstLineData)[listItemCorrelator], 1)
            mylcd.lcd_display_string(list(secondLineData)[listItemCorrelator], 2)
#             time.sleep(10)

#right now this only clears the display once.
#Find a way to clear the display after every time run_display executes
def clear_display():
    mylcd.lcd_display_string("", 1)
    mylcd.lcd_display_string("", 2)
                       
run_display()
clear_display()