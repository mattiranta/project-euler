include("EulerLib.jl")

###############################################################################
# Starting in the top left corner of a 2×2 grid, and only being able to
# move to the right and down, there are exactly 6 routes to the bottom right corner.

# How many such routes are there through a 20×20 grid?
###############################################################################

# Answer: 40!/20!/20! = 137846528820

function main()
    n = factorial(BigInt(40), BigInt(20)) / factorial(BigInt(20))
    @printf("Number of routes: %d\n", n)
end

@time main()

