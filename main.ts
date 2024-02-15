input.onGesture(Gesture.LogoDown, function on_gesture_logo_down() {
    console.log("Why lucas died?")
})
input.onButtonPressed(Button.A, function on_button_pressed_a() {
    console.log("Helloworld!")
    basic.showString("Helloworld")
})
input.onGesture(Gesture.Shake, function on_gesture_shake() {
    console.log("Lucas is a good guy!")
})
input.onGesture(Gesture.LogoUp, function on_gesture_logo_up() {
    console.log("你好傻逼")
})
input.onButtonPressed(Button.AB, function on_button_pressed_ab() {
    console.log("Lucas is a good guy")
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    console.log("Created by changcheng967")
    basic.showString("Created by changcheng967")
})
loops.everyInterval(5000, function on_every_interval2() {
    console.log("Created by changcheng967")
    basic.showString("Created by changcheng967")
})
