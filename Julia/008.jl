include("EulerLib.jl")

###############################################################################
# Find the greatest product of five consecutive digits in the 1000-digit number.
###############################################################################

function myparser(c)
    parseint(string(c))
end

function main()
    s = split(replace(readall("../data/008_input.txt"), '\n', ""), "")
    digits = map((c -> parseint(string(c))), s)
    greatest = 0
    for (i,d) = enumerate(digits)
        if i < 5
            continue
        end
        greatest = max(greatest, digits[i-4] * digits[i-3] * digits[i-2] * digits[i-1] * digits[i])
    end
    println("Greatest product of five consecutive digits: $(greatest)")
end

@time main()

