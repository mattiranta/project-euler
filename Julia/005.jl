include("EulerLib.jl")

###############################################################################
# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
###############################################################################

function main()
    n = -1
    divisors = 20:-1:1
    n = reduce(lcm, divisors)
    println("Smallest positive number evenly divisible by all $(divisors[1])..$(divisors[end]): $n")
end

@time main()

