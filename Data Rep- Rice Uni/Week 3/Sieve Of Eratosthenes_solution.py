def compute_primes(bound):
    """
    Return a list of the prime numbers in range(2, bound)
    """
    
    answer = list(range(2, bound))
    for divisor in range(2, bound):
        for i in range(2,bound):
            num=divisor*i
            print(str(num) + " ")
            if num in answer:
                answer.remove(num)
            if num>bound:
                break
    return answer

print(compute_primes(100))
'''
def compute_primes(bound):
    list(range(2,bound))
    '''