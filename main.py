import Control_servo as cs

def main():
    my_control = cs.Control_servo()
    my_control.start()
    # my_control.run_key(delta = 15)
    my_control.run_buttons(delta = 15)

if __name__ == "__main__":
    main()
#daaaaaasws
