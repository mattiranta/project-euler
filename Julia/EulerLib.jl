
function is_prime(n)
    if n == 1
        return false
    end

    for i = 2:floor(sqrt(n))
        if rem(n, i) == 0
            return false
        end
    end
    return true
end

# Enumerate the multiples of n up to some strict upper bound.
function bounded_multiples(bound, n)
  if rem(bound, n) == 0
    [0:n:(n * (div(bound, n) - 1))]
  else
    [0:n:(n * div(bound, n))]
  end
end