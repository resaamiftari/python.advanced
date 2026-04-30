informacionet = {
    "name": "John",
    "phone": "123456789",
    "email": "john@gmail.com"
}

informacionet1 = {
    "name": "Jane",
    "phone": "987654321",
    "email": "jane@gmail.com"
    }


print(informacionet)
print(informacionet1)

# Marrja e një vlere
email = informacionet["email"]
print(email)

# Shtimi i një fushe të re
informacionet["age"] = 20
print(informacionet)

# Ndryshimi i një vlere
informacionet1["phone"] = "111111111"
print(informacionet1)

# Fshirja e një fushe
del informacionet["email"]
print(informacionet)






