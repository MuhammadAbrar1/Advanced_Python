# choice=input("Enter choice: ")

# match choice:
#     case "1":
#         print("Add student")
#     case "2":
#         print("Remove Student")
#     case "3":
#         print("View Student")
#     case _:
#         print("Invalid Choice")


# while True:
#     weather=input("Enter weather: ")
#     match weather:
#         case "cold":
#             print("wear jacket")
#         case "sunny":
#             print("wear sunglasses")
#         case "rainy":
#             print("take umbrella")
#         case "hot":
#             print("drik more water")
#         case _:
#             print("wrong entry")


while True:
    light = input ("enter trafic light: ")
    match light:
        case "red":
            print("stop")
        case "green":
            print("go")
        case "yellow":
            print("be careful")
        case _:
            print("invalid color")