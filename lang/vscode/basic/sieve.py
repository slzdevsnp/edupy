import os

def main():
    sieve = [True] * 101
    for i in range(2, 100):
        if sieve[i]:
            print(i)
            for j in range(i*i, 100, i):
                sieve[j] = False    
    print('Done')            


if __name__ == '__main__':
    main()
            