from time import sleep
from random import randint
#import tkinter

from pyautogui import keyDown, keyUp, press, click, moveTo, pixelMatchesColor, position

#tkinter.Pack()

leave_game_time = 233.0
wait_to_drop = 0.0
grounded_time = 0.0
yn_debug = 0
server_picker = 0, 0

def short_count_down():
    for i in range(1, 6) [::-1]:
        print(str(i)+'..')
        sleep(1)

def stop_bot():
    print('Stopped THE BOT!')
    sleep(1000000)
    stop_bot()

def check_if_dead():
    if pixelMatchesColor(1637, 960, (255, 255, 255)) is True and pixelMatchesColor(1765, 944, (255, 255, 255)) is True:
        sleep(0.5)
        print('You have died! Bot Restarting.')
        click(1710, 951)
        sleep(2)
        moveTo(854, 569, 1)
        click(button='left', clicks=3, interval=0.5)
        sleep(5)
        fallback_debug_self_fix()
    fallback_debug_self_fix()

def end_game_restart():
    global leave_game_time
    global grounded_time
    print('Bot has completed its task. Restarting!')
    press('escape')
    sleep(3)
    if pixelMatchesColor(875, 591, (255, 255, 255)) is True and pixelMatchesColor(750, 597, (255, 255, 255)) is True:
        click(841, 572, button='left', clicks=3, interval=0.5)
        sleep(5)
        leave_game_time = 233.0
        grounded_time = 0.0
        fallback_debug_self_fix()
    else:
        fallback_debug_self_fix()

def on_land_check():
    global leave_game_time
    global grounded_time

    if yn_debug == 1:
        print('There is '+str(leave_game_time)+' Seconds till the bot leaves the game!')
    if yn_debug == 1:
        print('Landed!')
    leave_game_time -= grounded_time
    sleep(3)
    leave_game_time -= 6
    if yn_debug == 1:
        print('The time reduce amount is '+str(grounded_time)+' Seconds.')
    if yn_debug == 1:
        print('You now have to wait '+str(leave_game_time)+' Seconds till the bot leaves the game!')
    press('z')
    for i in range(1, 200):
        if yn_debug == 1:
            print('Check to see if you are in water #'+str(i))
        if pixelMatchesColor(1207, 1036, (238, 241, 241), tolerance=30) is True and pixelMatchesColor(1227, 1041, (241, 243, 244), tolerance=30) is True:#player animation of standing and laying down
            if yn_debug == 1:
                print('You are in water.')
            for v in range(1, round(leave_game_time)) [::-1]:
                if pixelMatchesColor(1637, 960, (255, 255, 255)) is True and pixelMatchesColor(1765, 944, (255, 255, 255)) is True:
                    check_if_dead()
                if pixelMatchesColor(172, 38, (255, 255, 255)) is True and pixelMatchesColor(172, 53, (255, 255, 255)) is True:#checks to see if you are in a parachute
                    fallback_debug_self_fix()
                if yn_debug == 1:
                    print('Time left before restart: '+str(i)+' ')
                keyDown('space')
                sleep(0.5)
                keyUp('space')
                sleep(0.5)
            end_game_restart()
    if yn_debug == 1:
        print('You are on gound.')
    for i in range(1, round(leave_game_time)) [::-1]:
        if pixelMatchesColor(1637, 960, (255, 255, 255)) is True and pixelMatchesColor(1765, 944, (255, 255, 255)) is True:
            check_if_dead()
        if pixelMatchesColor(172, 38, (255, 255, 255)) is True and pixelMatchesColor(172, 53, (255, 255, 255)) is True:#checks to see if you are in a parachute
            fallback_debug_self_fix()
        if yn_debug == 1:
            print('Time left before restart: '+str(i)+' ')
        sleep(1)
    end_game_restart()
    sleep(1)
    fallback_debug_self_fix()

def parachute_max_distance():
    global grounded_time

    new_time = 0.0
    for i in range(1, 150):
        new_time += 1.5
        if yn_debug == 1:
            print('Time before you can leave is reduced by: '+str(new_time)+' Seconds.')
        grounded_time += 1.5
        if new_time > 80:
            if pixelMatchesColor(1637, 960, (255, 255, 255)) is True and pixelMatchesColor(1765, 944, (255, 255, 255)) is True:# checks to see if you are dead
                check_if_dead()
        if pixelMatchesColor(172, 38, (255, 255, 255)) is True and pixelMatchesColor(172, 53, (255, 255, 255)) is True:#checks to see if you are in a parachute
            keyDown('w')
            sleep(0.5)
            keyUp('w')
            sleep(1)
        elif pixelMatchesColor(172, 38, (255, 255, 255)) is not True and pixelMatchesColor(172, 53, (255, 255, 255)) is not True:
            on_land_check()
        else:
            if yn_debug == 1:
                print('Not still falling or landed? Debugging now.')
            fallback_debug_self_fix()

def playing_game_check():
    global wait_to_drop
    global leave_game_time
    for i in range(1, 200):
        if yn_debug == 1:
            print('Check to see if you are in a plane! #'+str(i)+' ')
        sleep(0.1)
        if pixelMatchesColor(173, 50, (255, 255, 255)) is True and pixelMatchesColor(167, 47, (255, 255, 255)) is True:# checks to see if you are in a plane
            wait_to_drop = randint(1, 35)
            leave_game_time -= wait_to_drop
            if yn_debug == 1:
                print('You are in the plane.')
            if yn_debug == 1:
                print('The random wait time is '+str(wait_to_drop)+' Seconds.')
            if yn_debug == 1:
                print('You have to wait '+str(leave_game_time)+' Seconds till the bot leaves the game!')
            sleep(20)
            if yn_debug == 1:
                print('Dropping in '+str(wait_to_drop)+' Secconds.')
            sleep(wait_to_drop)
            press('f')
            sleep(0.2)
            press('f')
            sleep(0.2)
            if yn_debug == 1:
                print('Bot made you drop!')
            keyDown('w')
            sleep(8.7)
            keyUp('w')
            press('f')
            sleep(0.2)
            press('f')
            if yn_debug == 1:
                print('Bot opened the Parachute!')
            parachute_max_distance()
    if yn_debug == 1:
        print('Never dropped? Debugging now.')
    fallback_debug_self_fix()

def second_in_game_check():
    for i in range(1, 70):
        if yn_debug == 1:
            print('It has been '+str(i)+' seconds checking if the Game Started.')
        sleep(1)
        if pixelMatchesColor(851, 678, (160, 255, 226)) is not True and pixelMatchesColor(952, 687, (160, 255, 226)) is not True:
            if yn_debug == 1:
                print('The game has started!')
            playing_game_check()
    if yn_debug == 1:
        print('Game never started? Debugging now.')
    fallback_debug_self_fix()

def in_game_check():
    for i in range(1, 60):
        if yn_debug == 1:
            print('It has been '+str(i)+' seconds checking if you are on the Game Island.')
        sleep(1)
        if pixelMatchesColor(851, 678, (160, 255, 226)) is True and pixelMatchesColor(952, 687, (160, 255, 226)) is True:
            if yn_debug == 1:
                print('You are in game!')
            second_in_game_check()
    if yn_debug == 1:
        print('Timed out? Debugging now.')
    fallback_debug_self_fix()

def lobby_play_check():
    global leave_game_time
    global grounded_time
    leave_game_time = 233.0
    grounded_time = 0.0
    if pixelMatchesColor(195, 51, (168, 101, 2)) is True and pixelMatchesColor(94, 15, (207, 136, 14)) is True: # Move mouse to play in lobby
        print('Bot has activated!')
        sleep(0.1)
        moveTo(195, 51)
        sleep(0.5)
        click(86, 203)# clicks na server so rest works
        sleep(0.5)
        click(81, 715)# clicks squads
        sleep(0.5)
        start_game_check()
    else:
        sleep(1)
        if yn_debug == 1:
            print('Could not find play button? Debugging now.')
        fallback_debug_self_fix()

def start_game_check():
    sleep(0.5)
    if pixelMatchesColor(185, 719, (20, 20, 20)) is True and pixelMatchesColor(186, 718, (2, 2, 2)) is True:#box is checked and click it then play
        sleep(0.5)
        click(184, 717)#clicked the check box
        sleep(0.5)
        click(server_picker)# clicks the server you picked
        sleep(0.5)
        click(195, 51)#clicked play
        in_game_check()
    elif pixelMatchesColor(185, 719, (255, 255, 255)) is True and pixelMatchesColor(186, 718, (255, 255, 255)) is True:#box is not checked and clicked play
        sleep(0.5)
        click(server_picker)# clicks the server you picked
        sleep(0.5)
        click(195, 51)#clicked play
        print('Starting Game!')
        sleep(0.5)
        in_game_check()
    else:
        sleep(1)
        if yn_debug == 1:
            print('Nothing worked trying to debug now!')
        fallback_debug_self_fix()

def long_start_delay():
    for i in range(1, 10) [::-1]:
        print(str(i)+'..')
        sleep(1)
    lobby_play_check()


def fallback_debug_self_fix():
    print('')
    sleep(1)
    if position() == (0, 0):
        stop_bot()
    if yn_debug == 1:
        print('Issue found we are starting to debug!\nThis'+
              ' will take less than a minute to a few minutes!\n')
    for i in range(1, 300):
        if position() == (0, 0):
            stop_bot()
        sleep(0.1)
        if yn_debug == 1:
            print('Debug check and tried to fix #'+str(i))
        if pixelMatchesColor(892, 591, (255, 255, 255)) is True and pixelMatchesColor(1005, 584, (48, 48, 48)) is True:#home lobby checks if buttons ie confirmed dead
            if yn_debug == 1:
                print('\nFound and Fixed The Issue!#1\n')
            click(892, 591)
            sleep(1)
            lobby_play_check()
        elif pixelMatchesColor(749, 365, (155, 164, 182)) is True and pixelMatchesColor(1086, 358, (155, 164, 182)) is True:
            if yn_debug == 1:
                print('\nFound and Fixed The Issue!#2\n')
            click(961, 652)
            sleep(1)
            lobby_play_check()
        elif pixelMatchesColor(1117, 458, (255, 255, 255)) is True and pixelMatchesColor(808, 475, (255, 255, 255)) is True:
            if yn_debug == 1:
                print('\nFound and Fixed The Issue!#3\n')
            click(963, 533)
            sleep(1)
            lobby_play_check()
        elif pixelMatchesColor(1201, 488, (255, 255, 255)) is True and pixelMatchesColor(961, 510, (255, 255, 255)) is True:
            if yn_debug == 1:
                print('\nFound and Fixed The Issue!#4\n')
            click(1051, 574)
            sleep(1)
            lobby_play_check()
        elif pixelMatchesColor(892, 591, (255, 182, 0)) is True and pixelMatchesColor(1005, 584, (255, 255, 255)) is True:
            if yn_debug == 1:
                print('\nFound and Fixed The Issue!#5\n')
            click(892, 591)
            sleep(1)
            lobby_play_check()
        elif pixelMatchesColor(195, 51, (168, 101, 2)) is True:
            if yn_debug == 1:
                print('\nFound and Fixed The Issue!#6\n')
            sleep(1)
            lobby_play_check()
        elif pixelMatchesColor(963, 363, (155, 164, 182)) is True and pixelMatchesColor(811, 346, (155, 164, 182)) is True:
            if yn_debug == 1:
                print('\nFound and Fixed The Issue!#7\n')
            click(968, 649)
            sleep(1)
            lobby_play_check()
        elif pixelMatchesColor(185, 719, (20, 20, 20)) is True:
            if yn_debug == 1:
                print('\nFound and Fixed The Issue!#8\n')
            sleep(1)
            start_game_check()
        elif pixelMatchesColor(185, 719, (255, 255, 255)) is True:
            if yn_debug == 1:
                print('\nFound and Fixed The Issue!#9\n')
            sleep(1)
            start_game_check()
        elif pixelMatchesColor(86, 720, (159, 159, 159)) is True and pixelMatchesColor(44, 722, (164, 164, 163)) is True:
            if yn_debug == 1:
                print('\nFound and Fixed The Issue!#10\n')
            sleep(1)
            lobby_play_check()
        elif pixelMatchesColor(86, 720, (255, 255, 255)) is True and pixelMatchesColor(44, 722, (255, 255, 255)) is True:
            if yn_debug == 1:
                print('\nFound and Fixed The Issue!#11\n')
            sleep(1)
            lobby_play_check()
        elif pixelMatchesColor(851, 678, (160, 255, 226)) is True and pixelMatchesColor(952, 687, (160, 255, 226)) is True:
            if yn_debug == 1:
                print('\nFound and Fixed The Issue!#12\n')
            sleep(1)
            in_game_check()
        elif pixelMatchesColor(173, 50, (255, 255, 255)) is True and pixelMatchesColor(167, 47, (255, 255, 255)) is True:
            if yn_debug == 1:
                print('\nFound and Fixed The Issue!#13\n')
                print('Timer is probably broken but the bot will keep going and fix it')
            sleep(1)
            playing_game_check()
        elif pixelMatchesColor(172, 38, (255, 255, 255)) is True and pixelMatchesColor(172, 53, (255, 255, 255)) is True and pixelMatchesColor(34, 989, (255, 255, 255)) is True:# had to do 3 checks to see if you are in a parachute
            if yn_debug == 1:
                print('\nFound and Fixed The Issue!#14\n')
                print('Timer is probably broken but the bot will keep going and fix it')
            sleep(1)
            parachute_max_distance()
        elif pixelMatchesColor(38, 1032, (206, 204, 199), tolerance=30) is True and pixelMatchesColor(45, 1002, (248, 248, 248), tolerance=30) is True:#player animation of standing and laying down
            sleep(0.5)
            press('z')
            sleep(1)
            if pixelMatchesColor(38, 1032, (206, 204, 199), tolerance=30) is not True and pixelMatchesColor(45, 1002, (248, 248, 248), tolerance=30) is not True:
                if yn_debug == 1:
                    print('\nFound and Fixed The Issue!#15\n')
                    print('Timer is probably broken but the bot will keep going and fix it')
                sleep(1)
                on_land_check()
            else:
                if yn_debug == 1:
                    print('\nFound and Fixed The Issue!#16\n')
                    print('Timer is probably broken but the bot will keep going and fix it')
                sleep(1)
                on_land_check()
        elif pixelMatchesColor(875, 591, (255, 255, 255)) is True and pixelMatchesColor(750, 597, (255, 255, 255)) is True:
            if yn_debug == 1:
                print('\nFound and Fixed The Issue!#17\n')
            sleep(1)
            end_game_restart()
        elif pixelMatchesColor(1637, 960, (255, 255, 255)) is True and pixelMatchesColor(1765, 944, (255, 255, 255)) is True:
            if yn_debug == 1:
                print('\nFound and Fixed The Issue!#18\n')
            sleep(1)
            check_if_dead()
        elif pixelMatchesColor(840, 345, (155, 164, 182)) is True and pixelMatchesColor(818, 364, (155, 164, 182)) is True:#kicked out of match and clicked ok
            if yn_debug == 1:
                print('\nFound and Fixed The Issue!#19\n')
            click(960, 646)
            sleep(1)
            lobby_play_check()
        elif pixelMatchesColor(829, 475, (255, 255, 255)) is True and pixelMatchesColor(948, 460, (255, 255, 255)) is True and pixelMatchesColor(1054, 450, (255, 255, 255)) is True:#Too many logins error and clicked ok
            if yn_debug == 1:
                print('\nFound and Fixed The Issue!#20\n')
            click(955, 539)
            sleep(1)
            lobby_play_check()
        else:
            if yn_debug == 1:
                print('Cant find anything. Looping over again now!')
    print('Tried to fix for min+ and could not fix the issue\n'+
          'Can you please report what happened to Dustyroo? Take screenshots if you can.')
    stop_bot()

def bot_third_start():
    global yn_debug
    print('Do you want all of the constole functions showing'+
          '(Spaming constole and more lag)\n1) Yes\n2) No(recommended)')
    yn_debug = input('Please enter your Constole Choice: ')
    if yn_debug == '1':
        yn_debug = 1
        print('There is a 10s delay before starting The Bot'+
              ' \nOpen the game and Wait!\nBot Starting in:')
        long_start_delay()
    elif yn_debug == '2':
        yn_debug = 0
        print('There is a 10s delay before starting The Bot'+
              ' \nOpen the game and Wait!\nBot Starting in:')
        long_start_delay()
    else:
        print('You put '+'~'+yn_debug+'~'+' this is not one of the options\nPlease try again in:')
        short_count_down()
        bot_third_start()

def bot_second_start():
    global server_picker
    print('What server do you want to be playing in?')
    print('1) NA Servers\n2) EU Servers\n3) AS Servers\n4) KR/JP Servers\n'+
          '5) OC Servers\n6) SA Servers\n7) SEA Servers\n')
    server_picker = input('Please enter your Server Choice: ')
    if server_picker == '1':
        server_picker = 86, 203
        print('You have chosen: NA Servers\n')
        bot_third_start()
    elif server_picker == '2':
        server_picker = 91, 243
        print('You have chosen: EU Servers\n')
        bot_third_start()
    elif server_picker == '3':
        server_picker = 91, 285
        print('You have chosen: AS Servers\n')
        bot_third_start()
    elif server_picker == '4':
        server_picker = 86, 326
        print('You have chosen: KR/JP Servers\n')
        bot_third_start()
    elif server_picker == '5':
        server_picker = 92, 364
        print('You have chosen: OC Servers\n ')
        bot_third_start()
    elif server_picker == '6':
        server_picker = 92, 403
        print('You have chosen: SA Servers\n ')
        bot_third_start()
    elif server_picker == '7':
        server_picker = 95, 444
        print('You have chosen: SEA Servers\n ')
        bot_third_start()
    else:
        print('You put '+'~'+server_picker+'~'+' this is not one of the options\n'+
              'Please try again in:')
        short_count_down()
        bot_second_start()

def bot_first_start():
    print('Made by: Dustyroo\nVer. 1.75+')
    print('Screen Resolution Choices are:\n1) 1080p\n2) 1440p\n3) 720p'+
          '\n4) Other/ None of the above fit my Screen')
    resolution_choice = input('Please enter your Resolutin Choice: ')
    if resolution_choice == '1':
        print('You have chosen: 1080p\n ')
        bot_second_start()
    elif resolution_choice == '2':
        print('You have chosen: 1440p\nSorry I have not made a support for this resolution.\n'+
              'Please contant dustyroo if you want this resolution implemented!')
        stop_bot()
    elif resolution_choice == '3':
        print('You have chosen: 720p\nSorry I have not made a support for this resolution.\n'+
              'Please contant dustyroo if you want this resolution implemented!')
        stop_bot()
    elif resolution_choice == '4':
        print('If I do not support your resolution contant '+
              'dustyroo about it in detail and it will be implemented.')
        stop_bot()
    else:
        print('You put '+'~'+resolution_choice+'~'+
              ' this is not one of the options\nPlease try again in:')
        short_count_down()
        bot_first_start()
bot_first_start()
