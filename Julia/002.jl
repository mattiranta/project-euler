include("EulerLib.jl")

###############################################################################
# Each new term in the Fibonacci sequence is generated by adding the previous two terms.
# By starting with 1 and 2, the first 10 terms will be:
# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
# By considering the terms in the Fibonacci sequence whose values do not exceed four million,
# find the sum of the even-valued terms.
###############################################################################

function main()
    i1, i2 = 1, 2
    sum = 2
    while i1 + i2 < 4000000
        i1, i2 = i2, i1 + i2
        if i2 % 2 == 0
            sum += i2
        end
    end

    println("Sum of even-valued Fibonacci terms: $sum")
end

@time main()

