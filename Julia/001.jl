include("EulerLib.jl")
using TimeIt

###############################################################################
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. 
# The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.
###############################################################################


function main()
    total = 0
    for i in 1:999
        if i % 3 == 0 || i % 5 == 0
            total += i
        end
    end

    println("Sum of multiples of 3 or 5, below 1000: $total")

end

@time main()

