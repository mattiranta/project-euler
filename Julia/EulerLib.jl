# PRIME NUMBERS:

function find_nth_prime(n)
    # A good guess of how far we have to go, to include nth prime
    max = int(ceil(1.2n * log(n)))
    sieve_of_erastothenes(max, n)[n]
end

function sieve_of_erastothenes(max, n = -1)
    if n == -1
        n = max
    end

    primes = Int64[]
    count = 0
    sieve = trues(max)
    for p in 2:max
        if sieve[p]
            push!(primes, p)
            count =+ 1

            if count >= n
                return primes
            end  
            
            for i = [p^2:p:max]
                sieve[i] = false
            end
        end
    end
    primes
end

function is_prime(n)
    if n == 1
        return false
    end

    for i in 2:floor(sqrt(n))
        if rem(n, i) == 0
            return false
        end
    end
    
    true
end

# Enumerate the multiples of n up to some strict upper bound.
# function bounded_multiples(bound, n)
#     if rem(bound, n) == 0
#         [0:n:(n * (div(bound, n) - 1))]
#     else
#         [0:n:(n * div(bound, n))]
#     end
# end


# STRING MANIPULATION:

function is_palindrome(n::String)
    n == reverse(n)
end