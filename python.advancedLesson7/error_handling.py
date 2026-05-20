try:
    rezultati =10/0
except ZeroDivisionError:
    print("oops , nuk mundesh me pjestu me 0")
else:
    print("Pjestimi eshte realizuar me sukses")
finally:
    print("Hej , ke mrri deri te line 8")

frutat = {
    "mollat":5,
    "banane":7,
    "portokalla":3,
}

try:
    print(frutat["dredhezat"])
except KeyError:
        print("the key does not exist in the directory")

text="this is not a number"

try:
    text_to_int=int(text)
except Exception as e:
    print("Ka ndodh nje error",e)

finally:
    print("Hej , ke mrri deri te line 26")

