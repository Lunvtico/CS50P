def main():
    x = input ("Input: ")
    y= convert(x)
    print(y)




def convert(p):
    lista= ["a", "e", "i", "o", "u","A", "E", "I", "O", "U"]
    result=""
    for x in p:
        if x not in lista:
            result += "" + x



    return result

main()




