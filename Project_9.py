def main():
    max_prime = int(input("Enter maximum integer (n): "))
    all_prime_nums = []
    other= []
    for i in range(2,max_prime+1):
        all_prime_nums.append(i)
        
    while len(all_prime_nums)>0:
        prime = all_prime_nums.pop(0)

        print(prime, "is a valid prime integer")
        for x in all_prime_nums:
            if x % prime == 0: 
               all_prime_nums.remove(x)
    return other
    print(prime(max_prime))
    
main()
