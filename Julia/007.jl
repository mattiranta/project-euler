include("EulerLib.jl")

###############################################################################
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13,
# we can see that the 6th prime is 13.
# What is the 10001 prime number?
###############################################################################

function main()
    n = 10001
    p = find_nth_prime(n)
    println("$n prime number: $p")
end

@time main()

