import string
import time

alpha = string.ascii_letters

def ceaser_decrypt_without_key(target):
    print("DECRYPTING....")
    key = 0
    while key <= 26:
        temp = ""
        for char in target:
            if char.isalpha():
                temp += alpha[(alpha.index(char)-int(key)) % 26]
            else:
                temp += char
        print(temp + " ........... key: ", key)
        key = key + 1


def ceaser_decrypt(target, shift):
    print("DECRYPTING....")
    temp = ""
    temp = ""
    for char in target:
        if char.isalpha():
            temp += alpha[(alpha.index(char)-int(shift)) % 26]
        else:
            temp += char
    print(temp)


def main():
    objType = input(
        "type 1 if you want to decrypt a string with a key and 2 if you want to decrypt in Brute-force... \n")
    if (int(objType) == 1):
        target = input(
            "Type the string you want to DECRYPT with a known KEY : \n")
        shift = input("Enter the shift key : \n")
        start_time = time.time()
        ceaser_decrypt(target, shift)
        print("--- %s seconds ---" % (time.time() - start_time))

    elif (int(objType) == 2):
        target = input("Type the string you want to brute-force DECRYPT : \n")
        start_time = time.time()
        ceaser_decrypt_without_key(target)
        print("--- %s seconds ---" % (time.time() - start_time))

    else:
        print("Only select 1 or 2")
        main()
    print("Congratulations!")


if __name__ == "__main__":
    main()
