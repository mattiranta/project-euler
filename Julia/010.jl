include("EulerLib.jl")

###############################################################################
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.
###############################################################################


function main()
    lim = 2000000
    n = sum(sieve_of_erastothenes(lim))
    println("Sum of primes below $lim: $n")
end

@time main()

