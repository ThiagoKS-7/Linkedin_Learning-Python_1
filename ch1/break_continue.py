def loop_break():
    for x in range(5,10):
        if x == 7:
            break
        print(f"o valor de x é: {x}")
        
def loop_continue():
    for x in range(5,10):
        if x == 7:
            continue
        print(f"o valor de x é: {x}")

if __name__ == "__main__":
    loop_break()
    print("")
    loop_continue()