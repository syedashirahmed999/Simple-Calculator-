import math

def inputs_1():

    while True:
        try:
            input_1 = float(input("1st Value: ").strip())
        except ValueError:
           print("Invalid Amount. Please enter a numerical value.")
           continue
        else:
           return input_1
        
def inputs_2():
    while True:
        try:
           input_2 = float(input("2nd Value: ").strip())
        except ValueError:
           print("Invalid Amount. Please enter a numerical value.")
           continue
        else:
           return input_2
        
def yes_no():
    while True:
       answer = input("Again(yes/no): ").lower().strip()
       if answer == "yes" or answer == "no":
           return answer
       else:
           print("invalid Input!")
           continue
       
while True:

    print("1. For Arthmatics Operations")
    print("2. For Squaring/Cubing And Roots")
    print("3. For Trignometric Ratios")
    print("4. For Quitting")

    while True:
        try:
            choose_number = int(input("(1/2/3/4): ").strip())
            if choose_number not in [1,2,3,4]:
                print("input Must Be in 1/2/3/4!")
                continue
            else:
                break
        except ValueError:
            print("input Must Be in 1/2/3/4!")
            continue
    

    while choose_number == 1:

        print("1. To Add")
        print("2. To Subtact")
        print("3. To Multiply")
        print("4. To Divide")
        print("5. To Quit")

        while True:
                try:
                    choose_arthmatics = int(input("(Add/Sub/Mul/div): ").strip())
                    if choose_arthmatics not in [1,2,3,4,5]:
                        print("input Must Be in 1/2/3/4/5!")
                        continue
                    else:
                        break
                except ValueError:
                    print("input Must Be in 1/2/3/4/5!")
                    continue

        while choose_arthmatics == 1:
            print("You Choose Addition!")
            input_1 = inputs_1()
            input_2 = inputs_2()
            print(f"Answer is: {input_1 + input_2}")
            answer = yes_no()
            if answer == "yes":
                continue
            else:
                break
        
        while choose_arthmatics == 2:
            print("You Choose Subtraction!")
            input_1 = inputs_1()
            input_2 = inputs_2()
            print(f"Answer is: {input_1 - input_2}")
            answer = yes_no()
            if answer == "yes":
                continue
            else:
                break

        while choose_arthmatics == 3:
            print("You Choose Multiplication!")
            input_1 = inputs_1()
            input_2 = inputs_2()
            print(f"Answer is: {input_1 * input_2}")
            answer = yes_no()
            if answer == "yes":
                continue
            else:
                break

        while choose_arthmatics == 4:
            print("You Choose Division!")
            try:
                input_1 = inputs_1()
                input_2 = inputs_2()
                print(f"Answer is: {input_1 / input_2}")
            except ZeroDivisionError:
                print("Invalid Amount. Amount Cannot Be Divide by 0!.")
                continue
            answer = yes_no()
            if answer == "yes":
                continue
            else:
                break

        if choose_arthmatics == 5:
            print("Quitting 1.!")
            break

    while choose_number == 2:

        print("1. For Squaring")
        print("2. For Cubing")
        print("3. For Powering")
        print("4. For Roots")
        print("5. For Quitting")

        while True:
            try:
                choose_roots = int(input("(1/2/3/4/5): ").strip())
                if choose_roots not in [1,2,3,4,5]:
                    print("input Must Be in 1/2/3/4/5!")
                    continue
                else:
                    break
            except ValueError:
                print("input Must Be in 1/2/3/4/5!")
                continue

        while choose_roots == 1:
            print("You Choose Squaring")
            input_1 = inputs_1()
            print(f"Answer: {input_1 ** 2}")
            answer = yes_no()
            if answer == "yes":
                continue
            else:
                break

        while choose_roots == 2:
            print("You Choose Cubing")
            input_1 = inputs_1()
            print(f"Answer: {input_1 ** 3}")
            answer = yes_no()
            if answer == "yes":
                continue
            else:
                break

        while choose_roots == 3:
            print("You Choose Powering")
            input_1 = inputs_1()
            input_2 = inputs_2()
            print(math.pow(input_1, input_2))
            answer = yes_no()
            if answer == "yes":
                continue
            else:
                break
        
        while choose_roots == 4:
            try:
                print("You Choose Sq.Root")
                input_1 = inputs_1()
                input_2 = inputs_2()
                print(math.pow(input_1, 1/input_2))
            except ZeroDivisionError:
                print("Input 2 Cannot be Zero")
            answer = yes_no()
            if answer == "yes":
                continue
            else:
                    break 

        if choose_roots == 5:
            print("Quitting 2.")
            break


    while choose_number == 3:

        print("1. For sin")
        print("2. For sin⁻¹")
        print("3. For cos")
        print("4. For cos⁻¹")
        print("5. For tan")
        print("6. For tan⁻¹")
        print("7. For Quitting")
    
        while True:
            try:
                choose_ratios = int(input("(1/2/3/4/5/6/7): ").strip())
                if choose_ratios not in [1,2,3,4,5,6,7]:
                    print("input Must Be in 1/2/3/4/5/6/7!")
                    continue
                else:
                    break
            except ValueError:
                print("input Must Be in 1/2/3/4/5/6/7!")
                continue

        while choose_ratios == 1:
            input_1 = inputs_1()
            print(math.sin(input_1))
            answer = yes_no()
            if answer == "yes":
                continue
            else:
                break

        while choose_ratios == 2:
            try:
                input_1 = inputs_1()
                print(math.asin(input_1))
            except ValueError:
                print("Can't Be more than -1 and 1!")
            answer = yes_no()
            if answer == "yes":
                continue
            else:
                break

                    
        while choose_ratios == 3:
            input_1 = inputs_1()
            print(math.cos(input_1))
            answer = yes_no()
            if answer == "yes":
                continue
            else:
                break

        while choose_ratios == 4:
            try:
                input_1 = inputs_1()
                print(math.acos(input_1))
            except ValueError:
                print("Can't Be more than -1 and 1!")
            answer = yes_no()
            if answer == "yes":
                continue
            else:
                break

        while choose_ratios == 5:
            input_1 = inputs_1()
            print(math.tan(input_1))
            answer = yes_no()
            if answer == "yes":
                continue
            else:
                break

        while choose_ratios == 6:
            try:
                input_1 = inputs_1()
                print(math.atan(input_1))
            except ValueError:
                print("Can't Be more than -1 and 1!")
            answer = yes_no()
            if answer == "yes":
                continue
            else:
                break

        if choose_ratios == 7:
            print("Quitting 7.")
            break
    
    if choose_number == 4:
        print("Calculator Over!")
        break






