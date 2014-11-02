module lib

open System
open System.Numerics
open System.IO
open System.Collections.Generic 

let BigIntSqrt (n:bigint) : bigint =
    bigint(Math.Exp(BigInteger.Log(n) / 2.))


let trialDivisionBigInt (n:bigint) =
    match n with
    | _ when n = 2I -> true
    | _ when n = 3I -> true
    | _ when n % 2I = 0I -> false
    | _ -> 
        let rec check i = 
            match i with
            | i when n % i = 0I -> false
            | i when n < i*i -> true
            | _ -> check (i + 2I)

        check 3I


let trialDivision (n) =
    match n with
    | _ when n = 2L -> true
    | _ when n = 3L -> true
    | _ when n % 2L = 0L -> false
    | _ -> 
        let rec check i = 
            match i with
            | i when n % i = 0L -> false
            | i when n < i*i -> true
            | _ -> check (i + 2L)

        check 3L


let trialDivision_BigInt (n) =
    match n with
    | _ when n = 2I -> true
    | _ when n = 3I -> true
    | _ when n % 2I = 0I -> false
    | _ -> 
        let rec check i = 
            match i with
            | i when n % i = 0I -> false
            | i when n < i*i -> true
            | _ -> check (i + 2I)

        check 3I


let sieveOfErastothenes (limit :int) = 
    seq { 
        yield 2 

        let knownComposites = Array.create (limit + 1) false
        
        // Loop through all odd numbers; evens can't be prime 
        for i in 3 .. 2 .. limit do 
            
            // Check if its in our list, if not, its prime 
            let found = knownComposites.[i]
            if not found then 
                yield i 

            // Add all multiples of i to our sieve, starting 
            // at i and irecementing by i. 
            do for j in i .. i .. limit do 
                knownComposites.[j] <- true
    } 


let findNthPrime (n :int) =
    let limit = int(1.2 * float(n) * Math.Log(float(n)))
    Seq.nth (n-1) (sieveOfErastothenes limit)

let stringReverse (str :string) =
    System.String(Array.rev (str.ToCharArray()))


let isPalindromic n =
    let str_n = n.ToString()
    str_n = stringReverse str_n


let factors n min max = 
    seq { for i in max .. -1 .. min do 
            if n % i = 0 && n/i > min && n/i < max then 
                yield (i, n/i) } |> Seq.tryPick Some


let reduce f list =
    match list with
    | h::t -> List.fold f h t
    | [] -> failwith "Cannot reduce empty list"

    
let rec gcd (a:bigint) (b:bigint) =
    match b with
    | _ when b = 0I -> a
    | _ -> gcd b (a % b)


let lcm (a:int) (b:int) =
    let den = gcd (bigint a) (bigint b)
    let nom = bigint(a) * bigint(b)
    int(nom/den)


let divisors_bruteForce (n: bigint) : int list =
    let rec loop (div) (found: int list) =
        match div with
        | 1 -> 1::found
        | _ when (n % bigint(div)) = 0I -> loop (div - 1) (div::found)
        | _ -> loop (div - 1) found
    

    loop (int(int(n)/2)) [int(n)]


let divisorCount_bruteForce (n:bigint) =
    List.length (divisors_bruteForce n)


let divisorCount_Bigint (n: bigint) =
    let sqrt_n = BigIntSqrt n
    let rec loop (div: bigint) (count: int) =
        if div >= sqrt_n then 
            count
        else if (n % div) = 0I then 
            loop (div + 1I) (count + 2)
        else 
            loop (div + 1I) count

    let divCount = loop 1I 0
    if sqrt_n * sqrt_n = n then divCount - 1 else divCount


let divisorCount (n : uint64)=
    let sqrt_n = uint64(Math.Sqrt (float n))
    let rec loop div count =
        if div >= sqrt_n then 
            count
        else if (n % div) = 0UL then 
            loop (div + 1UL) (count + 2)
        else 
            loop (div + 1UL) count

    let divCount = loop 1UL 0
    if sqrt_n * sqrt_n = n then divCount - 1 else divCount


let fileread f =
    File.ReadAllText(f)


let readlines f =
    File.ReadAllLines f


let replaceText (find:string) (replace:string) (source:string) =
    source.Replace(find, replace)