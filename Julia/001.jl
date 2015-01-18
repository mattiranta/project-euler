include("EulerLib.jl")
using TimeIt

###############################################################################
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. 
# The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.
###############################################################################

global firstrun = true

function main()
    global firstrun
    total = 0
    for i in 1:999
        if i % 3 == 0 || i % 5 == 0
            total += i
        end
    end

    if firstrun == true
        println("Sum of multiples of 3 or 5, below 1000: $total")
        firstrun = false
    end
end

#@timeit main()

