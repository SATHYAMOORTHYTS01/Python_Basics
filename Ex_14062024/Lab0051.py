def allowed_to_attend_python_class(name):
    match name:
        case "DELL":
            print("DELL is allowed")
        case "Mani":
            print("Mani is allowed")
        case "KKK":
            print("KKK is allowed")
        case _:
            print("Not Allowed")


allowed_to_attend_python_class("KKK")
