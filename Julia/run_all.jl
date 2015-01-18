#!/usr/bin/julia

using TimeIt

for (i, f) in enumerate(filter(r"[0-9]+.jl$" ,readdir(".")))
    println("File: $f")
    include("$f")
    @timeit main()
    if i >= 1
        break
    end
end
