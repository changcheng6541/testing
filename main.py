def on_gesture_logo_down():
    print("Why lucas died?")
input.on_gesture(Gesture.LOGO_DOWN, on_gesture_logo_down)

def on_button_pressed_a():
    
    # ask the user for a yes or no question
    answer = input('Do you like Python? ')
    # check if the answer is yes
    if answer == 'yes':
        print('That is great!')
    # check if the answer is no
    elif answer == 'no':
        print('That is too bad!')
    # check if the answer is neither yes or no
    else:
        print('That is a yes or no question!')
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_gesture_shake():
    print("Lucas is a good guy!")
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

def on_gesture_logo_up():
    print("你好傻逼")
input.on_gesture(Gesture.LOGO_UP, on_gesture_logo_up)

def on_button_pressed_ab():
    print("Thank you very much")
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    print("Created by changcheng967")
    basic.show_string("Created by changcheng967")
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_every_interval2():
    print("Created by changcheng967")
    basic.show_string("Created by changcheng967")
loops.every_interval(5000, on_every_interval2)
