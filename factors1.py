def main():
    print("Enter number :")
    No = int (input())

    print("Factore are :")
    for i in range(1,No,1):
        if No % i == 0:
            print(i)
        i = i +1
if__name__ == "__main__":
    main()
