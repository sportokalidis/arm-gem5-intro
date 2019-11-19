# ARM-gem5-Intro
1st project for computer architecture lab

## Answers to questions
### _1. starter_se.py simulation script_
##### SE Simulation
###### Run a simple SE
```console
$ ./build/ARM/gem5.opt -d hello_result configs/example/arm/starter_se.py --cpu="minor" "tests/test-progs/hello/bin/arm/linux/hello"
```

[starter_se.py](): is a simulation python script which defines system parameters<br/><br/>

in **_main_** function (lines: 187-208):
```python
    parser = argparse.ArgumentParser(epilog=__doc__)

    parser.add_argument("commands_to_run", metavar="command(s)", nargs='*',
                        help="Command(s) to run")
    parser.add_argument("--cpu", type=str, choices=cpu_types.keys(),
                        default="atomic",
                        help="CPU model to use")
    parser.add_argument("--cpu-freq", type=str, default="4GHz")
    parser.add_argument("--num-cores", type=int, default=1,
                        help="Number of CPU cores")
    parser.add_argument("--mem-type", default="DDR3_1600_8x8",
                        choices=ObjectList.mem_list.get_names(),
                        help = "type of memory to use")
    parser.add_argument("--mem-channels", type=int, default=2,
                        help = "number of memory channels")
    parser.add_argument("--mem-ranks", type=int, default=None,
                        help = "number of memory ranks per channel")
    parser.add_argument("--mem-size", action="store", type=str,
                        default="2GB",
                        help="Specify the physical memory size")
                        
    args = parser.parse_args()
```

[starter_se.py]() defines default **cpu** and **memory** parameters, however user can puts these parameters as arguments in run command
###### NOTE: in simple SE run command we define cpu model as Minor *(--cpu="Minor")* <br/><br/>
several **cpu models** define in lines 69-79 in this map data stucture:
```python
    cpu_types = {
        "atomic" : ( AtomicSimpleCPU, None, None, None, None),
        "minor" : (MinorCPU,
                   devices.L1I, devices.L1D,
                   devices.WalkCache,
                   devices.L2),
        "hpi" : ( HPI.HPI,
                  HPI.HPI_ICache, HPI.HPI_DCache,
                  HPI.HPI_WalkCache,
                  HPI.HPI_L2)
    }
```


In addition, in class ***SimpleSeSystem*** (lines: 82-141):<br/>
in line 88, define **cache lin size**
```python
    # Use a fixed cache line size of 64 bytes
    cache_line_size = 64
```
in lines 99-100, defines **voltage** and **clock**
```python
    self.voltage_domain = VoltageDomain(voltage="3.3V")
    self.clk_domain = SrcClockDomain(clock="1GHz",voltage_domain=self.voltage_domain)
```

---
### _2. Verification of simulation configs_
---


### _3. In-Order CPUs models_
---
