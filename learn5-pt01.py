def greetings():
    """问候语（迫真）"""
    print("Cyka Blyat!")


greetings()

userName = input("Enter you name:")


def GreetUser(userName):
    print("Cyka Blyat, " + userName.title() + "!")


GreetUser(userName)

a = 114
a = str(a)
b = 514
b = str(b)


def Aerodyanmics(lift, drag):
    print("\nResult: " + lift + " " + drag + ".")


Aerodyanmics(a, b)
Aerodyanmics("1919N", "810N")


def Car(color, type='tanker'):
    print("This is a " + color + " " + type + " car.")


Car(color='Black', type='Limousine')  # 黑色高级车


def vehicle(functions, design, addition='No addition'):
    highlights = functions + ', ' + design + ', ' + addition
    return highlights.title()


project = vehicle('rocket', 'streamline')
altn_project = vehicle('rocket', 'streamline', 'parachute')
print(project)
print(altn_project)


def build_destroyer(cannon, torpedo):
    destroyer = {'cannons': cannon, 'torpedos': torpedo}
    return destroyer


new_destroyer = build_destroyer('130mm', '533mm')
print(new_destroyer)


def hello(names):
    for greet in names:
        msg = "Cyka Blyat, " + greet + "!"
        print(msg)


newnames = ['A', 'B', 'C']
hello(newnames)