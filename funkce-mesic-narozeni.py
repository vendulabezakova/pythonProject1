def monthOfBirth(birthNumber):
    month = birthNumber[2:4]
    month = int(month)
    if month > 50:
        month = month - 50
    return month % 50
print(monthOfBirth("9160246084"))