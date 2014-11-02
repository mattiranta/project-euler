open System

//let scriptName = (fsi.CommandLineArgs.[1].Split '.').[0]
//printfn "Running exercise: %s" scriptName
let sw = Diagnostics.Stopwatch()
sw.Start()
let res = Run()
printfn "%s" res
sw.Stop()
printfn "Time: %.02f s" sw.Elapsed.TotalSeconds
