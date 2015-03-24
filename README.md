<h1><img src="https://raw.githubusercontent.com/c0ding/walnut/master/doc/walnut.png" height=85 alt="walnut" title="walnut"> walnut</h1>

[![PyPi Version](http://img.shields.io/pypi/v/walnut.svg)](https://pypi.python.org/pypi/walnut/)   [![Downloads](http://img.shields.io/pypi/dm/walnut.svg)](https://pypi.python.org/pypi/walnut/)
[![Code Health](https://landscape.io/github/c0ding/walnut/master/landscape.svg)](https://landscape.io/github/c0ding/walnut/master)

**walnut** is an APACHE licensed library written in Python designed to provide a simple and pythonic way to parse the _/proc/cpuinfo_ file on LINUX based systems.

## Installation:

From source use

		$ python setup.py install

or install from PyPi

		$ pip install walnut
		
## Documentation:

- Basic use:

```
>>> from walnut import CpuInfo
>>> cpu = CpuInfo()
>>> cpu
processor	: 0
vendor_id	: GenuineIntel
cpu family	: 6
model		: 42
model name	: Intel(R) Core(TM) i3-2130 CPU @ 3.40GHz
stepping	: 7
microcode	: 0x28
cpu MHz		: 1600.257
cache size	: 3072 KB
physical id	: 0
siblings	: 4
core id		: 0
cpu cores	: 2
apicid		: 0
initial apicid	: 0
fpu		: yes
fpu_exception	: yes
cpuid level	: 13
wp		: yes
flags		: fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush dts acpi mmx fxsr sse sse2 ss ht tm pbe syscall nx rdtscp lm constant_tsc arch_perfmon pebs bts rep_good nopl xtopology nonstop_tsc aperfmperf eagerfpu pni pclmulqdq dtes64 monitor ds_cpl vmx est tm2 ssse3 cx16 xtpr pdcm pcid sse4_1 sse4_2 popcnt tsc_deadline_timer xsave avx lahf_lm arat epb xsaveopt pln pts dtherm tpr_shadow vnmi flexpriority ept vpid
bogomips	: 6784.56
clflush size	: 64
cache_alignment	: 64
address sizes	: 36 bits physical, 48 bits virtual
power management:

processor	: 1
vendor_id	: GenuineIntel
cpu family	: 6
model		: 42
model name	: Intel(R) Core(TM) i3-2130 CPU @ 3.40GHz
stepping	: 7
microcode	: 0x28
cpu MHz		: 1600.523
cache size	: 3072 KB
physical id	: 0
siblings	: 4
core id		: 1
cpu cores	: 2
apicid		: 2
initial apicid	: 2
fpu		: yes
fpu_exception	: yes
cpuid level	: 13
wp		: yes
flags		: fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush dts acpi mmx fxsr sse sse2 ss ht tm pbe syscall nx rdtscp lm constant_tsc arch_perfmon pebs bts rep_good nopl xtopology nonstop_tsc aperfmperf eagerfpu pni pclmulqdq dtes64 monitor ds_cpl vmx est tm2 ssse3 cx16 xtpr pdcm pcid sse4_1 sse4_2 popcnt tsc_deadline_timer xsave avx lahf_lm arat epb xsaveopt pln pts dtherm tpr_shadow vnmi flexpriority ept vpid
bogomips	: 6784.56
clflush size	: 64
cache_alignment	: 64
address sizes	: 36 bits physical, 48 bits virtual
power management:

processor	: 2
vendor_id	: GenuineIntel
cpu family	: 6
model		: 42
model name	: Intel(R) Core(TM) i3-2130 CPU @ 3.40GHz
stepping	: 7
microcode	: 0x28
cpu MHz		: 1595.476
cache size	: 3072 KB
physical id	: 0
siblings	: 4
core id		: 0
cpu cores	: 2
apicid		: 1
initial apicid	: 1
fpu		: yes
fpu_exception	: yes
cpuid level	: 13
wp		: yes
flags		: fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush dts acpi mmx fxsr sse sse2 ss ht tm pbe syscall nx rdtscp lm constant_tsc arch_perfmon pebs bts rep_good nopl xtopology nonstop_tsc aperfmperf eagerfpu pni pclmulqdq dtes64 monitor ds_cpl vmx est tm2 ssse3 cx16 xtpr pdcm pcid sse4_1 sse4_2 popcnt tsc_deadline_timer xsave avx lahf_lm arat epb xsaveopt pln pts dtherm tpr_shadow vnmi flexpriority ept vpid
bogomips	: 6784.56
clflush size	: 64
cache_alignment	: 64
address sizes	: 36 bits physical, 48 bits virtual
power management:

processor	: 3
vendor_id	: GenuineIntel
cpu family	: 6
model		: 42
model name	: Intel(R) Core(TM) i3-2130 CPU @ 3.40GHz
stepping	: 7
microcode	: 0x28
cpu MHz		: 1599.062
cache size	: 3072 KB
physical id	: 0
siblings	: 4
core id		: 1
cpu cores	: 2
apicid		: 3
initial apicid	: 3
fpu		: yes
fpu_exception	: yes
cpuid level	: 13
wp		: yes
flags		: fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush dts acpi mmx fxsr sse sse2 ss ht tm pbe syscall nx rdtscp lm constant_tsc arch_perfmon pebs bts rep_good nopl xtopology nonstop_tsc aperfmperf eagerfpu pni pclmulqdq dtes64 monitor ds_cpl vmx est tm2 ssse3 cx16 xtpr pdcm pcid sse4_1 sse4_2 popcnt tsc_deadline_timer xsave avx lahf_lm arat epb xsaveopt pln pts dtherm tpr_shadow vnmi flexpriority ept vpid
bogomips	: 6784.56
clflush size	: 64
cache_alignment	: 64
address sizes	: 36 bits physical, 48 bits virtual
power management:
```

- Return output as dict:

```
>>> mem.dict()
{
    "1": {
        "cpu cores": "2",
        "bogomips": "6784.56",
        "core id": "1",
        "apicid": "2",
        "fpu_exception": "yes",
        "stepping": "7",
        "cache_alignment": "64",
        "clflush size": "64",
        "microcode": "0x28",
        "cache size": "3072 KB",
        "cpuid level": "13",
        "fpu": "yes",
        "model name": "Intel(R) Core(TM) i3-2130 CPU @ 3.40GHz",
        "siblings": "4",
        "physical id": "0",
        "address sizes": "36 bits physical, 48 bits virtual",
        "cpu family": "6",
        "vendor_id": "GenuineIntel",
        "wp": "yes",
        "power management": "",
        "flags": "fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush dts acpi mmx fxsr sse sse2 ss ht tm pbe syscall nx rdtscp lm constant_tsc arch_perfmon pebs bts rep_good nopl xtopology nonstop_tsc aperfmperf eagerfpu pni pclmulqdq dtes64 monitor ds_cpl vmx est tm2 ssse3 cx16 xtpr pdcm pcid sse4_1 sse4_2 popcnt tsc_deadline_timer xsave avx lahf_lm arat epb xsaveopt pln pts dtherm tpr_shadow vnmi flexpriority ept vpid",
        "cpu MHz": "1683.398",
        "model": "42",
        "processor": "1",
        "initial apicid": "2"
    },
    "0": {
        "cpu cores": "2",
        "bogomips": "6784.56",
        "core id": "0",
        "apicid": "0",
        "fpu_exception": "yes",
        "stepping": "7",
        "cache_alignment": "64",
        "clflush size": "64",
        "microcode": "0x28",
        "cache size": "3072 KB",
        "cpuid level": "13",
        "fpu": "yes",
        "model name": "Intel(R) Core(TM) i3-2130 CPU @ 3.40GHz",
        "siblings": "4",
        "physical id": "0",
        "address sizes": "36 bits physical, 48 bits virtual",
        "cpu family": "6",
        "vendor_id": "GenuineIntel",
        "wp": "yes",
        "power management": "",
        "flags": "fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush dts acpi mmx fxsr sse sse2 ss ht tm pbe syscall nx rdtscp lm constant_tsc arch_perfmon pebs bts rep_good nopl xtopology nonstop_tsc aperfmperf eagerfpu pni pclmulqdq dtes64 monitor ds_cpl vmx est tm2 ssse3 cx16 xtpr pdcm pcid sse4_1 sse4_2 popcnt tsc_deadline_timer xsave avx lahf_lm arat epb xsaveopt pln pts dtherm tpr_shadow vnmi flexpriority ept vpid",
        "cpu MHz": "1601.187",
        "model": "42",
        "processor": "0",
        "initial apicid": "0"
    },
    "3": {
        "cpu cores": "2",
        "bogomips": "6784.56",
        "core id": "1",
        "apicid": "3",
        "fpu_exception": "yes",
        "stepping": "7",
        "cache_alignment": "64",
        "clflush size": "64",
        "microcode": "0x28",
        "cache size": "3072 KB",
        "cpuid level": "13",
        "fpu": "yes",
        "model name": "Intel(R) Core(TM) i3-2130 CPU @ 3.40GHz",
        "siblings": "4",
        "physical id": "0",
        "address sizes": "36 bits physical, 48 bits virtual",
        "cpu family": "6",
        "vendor_id": "GenuineIntel",
        "wp": "yes",
        "power management": "",
        "flags": "fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush dts acpi mmx fxsr sse sse2 ss ht tm pbe syscall nx rdtscp lm constant_tsc arch_perfmon pebs bts rep_good nopl xtopology nonstop_tsc aperfmperf eagerfpu pni pclmulqdq dtes64 monitor ds_cpl vmx est tm2 ssse3 cx16 xtpr pdcm pcid sse4_1 sse4_2 popcnt tsc_deadline_timer xsave avx lahf_lm arat epb xsaveopt pln pts dtherm tpr_shadow vnmi flexpriority ept vpid",
        "cpu MHz": "1612.476",
        "model": "42",
        "processor": "3",
        "initial apicid": "3"
    },
    "2": {
        "cpu cores": "2",
        "bogomips": "6784.56",
        "core id": "0",
        "apicid": "1",
        "fpu_exception": "yes",
        "stepping": "7",
        "cache_alignment": "64",
        "clflush size": "64",
        "microcode": "0x28",
        "cache size": "3072 KB",
        "cpuid level": "13",
        "fpu": "yes",
        "model name": "Intel(R) Core(TM) i3-2130 CPU @ 3.40GHz",
        "siblings": "4",
        "physical id": "0",
        "address sizes": "36 bits physical, 48 bits virtual",
        "cpu family": "6",
        "vendor_id": "GenuineIntel",
        "wp": "yes",
        "power management": "",
        "flags": "fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush dts acpi mmx fxsr sse sse2 ss ht tm pbe syscall nx rdtscp lm constant_tsc arch_perfmon pebs bts rep_good nopl xtopology nonstop_tsc aperfmperf eagerfpu pni pclmulqdq dtes64 monitor ds_cpl vmx est tm2 ssse3 cx16 xtpr pdcm pcid sse4_1 sse4_2 popcnt tsc_deadline_timer xsave avx lahf_lm arat epb xsaveopt pln pts dtherm tpr_shadow vnmi flexpriority ept vpid",
        "cpu MHz": "1600.125",
        "model": "42",
        "processor": "2",
        "initial apicid": "1"
    }
}
```

- Search (is case insensitive):

```
>>> cpu.search('CPU Mhz')
['cpu MHz\t\t: 1599.062\n', 'cpu MHz\t\t: 1600.125\n', 'cpu MHz\t\t: 1598.398\n', 'cpu MHz\t\t: 1601.320\n']
```



## License:

```
	Apache v2.0 License
	Copyright 2014-2015 Martin Simon

	 Licensed under the Apache License, Version 2.0 (the "License");
	 you may not use this file except in compliance with the License.
	 You may obtain a copy of the License at

		 http://www.apache.org/licenses/LICENSE-2.0

	 Unless required by applicable law or agreed to in writing, software
	 distributed under the License is distributed on an "AS IS" BASIS,
	 WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
	 See the License for the specific language governing permissions and
	 limitations under the License.

```

## Buy me a coffee?

If you feel like buying me a coffee (or a beer?), donations are welcome:

```
WDC : WbcWJzVD8yXt3yLnnkCZtwQo4YgSUdELkj
HBN : F2Zs4igv8r4oJJzh4sh4bGmeqoUxLQHPki
DOGE: DRBkryyau5CMxpBzVmrBAjK6dVdMZSBsuS
```