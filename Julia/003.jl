include("EulerLib.jl")

###############################################################################
#The prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number 600851475143 ?
###############################################################################

function main(n)    
    sqrt_n = int(sqrt(n))
    largest = -1
    for i in [sqrt_n:-1:1]
        if n % i == 0 && is_prime(i)
            largest = i
            break
        end
    end
    println("Largest prime factor of $n: $largest")
end

@time main(600851475143)

