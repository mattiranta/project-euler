include("EulerLib.jl")

###############################################################################
# Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.
###############################################################################


function main()
    l = readlines(open("../data/013_input.txt"))
    s = BigInt(0)
    for i in l
        s += BigInt(i)
    end
    println("First ten digits of the sum: $(string(s)[1:10])")
end

@time main()

