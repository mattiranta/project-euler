module _main
open System

[<EntryPoint>]
let main argv = 
    let sw = Diagnostics.Stopwatch()
    sw.Start()
    let res = _3.Run()
    printfn "%s" res
    sw.Stop()
    printfn "Time: %.02f ms" sw.Elapsed.TotalMilliseconds
    printf "Press any key to quit"
    let _ = Console.ReadKey(true)
    0 
