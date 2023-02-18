import time
import multiprocessing

def DisplayEven(No):
    for i in range(1,No,1):
        if(i%2 == 0) :
            print("Even number:",i)

def DisplayOdd(No):
    for i in range(1,No,1):
        if(i%2 != 0):
            print("Odd number:",i)    

def main():
    print("Demonstration of a Parallel Programming using multiple processes")
    Number = 200

    p1 = multiprocessing.process(target = DisplayEven,args = (Number,))
    p2 = multiprocessing.process(target = DisplayOdd,args = (Number,))
    
    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("End of main")

if __name__ == "__main__":
    start_time = time.process_time()
    main()
    end_time = time.process_time()
    print("Execution time is :",end_time - start_time)
