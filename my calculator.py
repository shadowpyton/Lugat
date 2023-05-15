# a//b= a sonni b songa bo'lgandagi asos
# a**b= a sonni b darajaga ko'tarish
# a*b= a sonni b songa ko'paytirish
# a/b= a sonni b songa bo'lish
# a+b= a songa b sonni qo'shish
# a-b= a sondan b sonni ayirish
# a % b= a sonni b songa bo'lgandagi qoldiqni topish
# a sonni yaxlitlash= round(a)
# |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
amal = input("Nima qilamiz? (+, -, :, *, %=qoldiq, **=daraja, //=bo'linmaning asosi) ")
a = input("Birinchi raqamni kiriting: ")
b = input("Ikkinchi raqamni kiriting: ")
if amal == "+":
    c = int(a) + int(b)
    print("Natija: " + str(c))
if amal == "-":
    c = int(a) - int(b)
    print("Natija: " + str(c))
if amal == ":":
    c = int(a) / int(b)
    print("Natija: " + str(c))
if amal == "*":
    c = int(a) * int(b)
    print("Natija: " + str(c))
if amal == "**":
    c = int(a) ** int(b)
    print("Natija: " + str(c))
if amal == "%":
    c = int(a) % int(b)
    print("Natija: " + str(c))
if amal == "//":
    c = int(a) // int(b)
    print("Natija: " + str(c))
# = input("A ni qiymatini kiriting:)")

