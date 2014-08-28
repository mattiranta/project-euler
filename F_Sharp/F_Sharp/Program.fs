module _main
open System

[<EntryPoint>]
let main argv = 
    let sw = Diagnostics.Stopwatch()
    sw.Start()
    let res = Run()
    printfn "%s" res
    sw.Stop()
    printfn "Time: %.02f ms" sw.Elapsed.TotalMilliseconds
    
    match argv with
        | [|"--wait"|] -> printf "Press any key to quit"; Console.ReadKey(true) |> ignore
        | _ -> ()
    0 
