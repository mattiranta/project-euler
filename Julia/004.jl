include("EulerLib.jl")

###############################################################################
# A palindromic number reads the same both ways.
# The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 * 99.
# Find the largest palindrome made from the product of two 3-digit numbers.
###############################################################################


function is_product_of_two_3_digit_numbers(x::Int64, factors)
    for i in [999:-1:99]
        if x % i == 0 && 99 < x/i < 999
            factors[1] = i
            factors[2] = x/i
            return true
        end
    end
    false
end

function largest_palindrome() 
    factors = [0,0]
    for i in [999^2:-1:1]
        if is_palindrome(string(i)) && is_product_of_two_3_digit_numbers(i, factors)
            return (i, factors[1], factors[2])
        end
    end
    return nothing
end

function main()
    (palindrome, n, m) = largest_palindrome()
    println("Largest palindrome: $(palindrome) = $n x $m")
end

@time main()

