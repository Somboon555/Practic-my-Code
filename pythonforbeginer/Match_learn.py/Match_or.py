name = str(input("input your name:"))
match name:
    case "เด็กชาย"|"นาย":
        print("เพศชาย")
    case "เด็กหญิง"|"นางสาว"|"นาง":
        print("เพศหญิง")
    case _ :
        print("LGPTQ+")