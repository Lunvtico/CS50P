def main():
    x= input ("camelCase: ")
    y = mayusfind(x)
    z= y.lower()
    print(f"snake_case: {z}")


def mayusfind(a):
    result = ""
    for i, x in enumerate(a):
        if x.isupper() and i !=0:
            result += "_" + x
        else:
            result += x
    return result


main()
