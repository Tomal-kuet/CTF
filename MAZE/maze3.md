```assembly
08048060 <_start>:
 8048060:	58                   	pop    %eax
 8048061:	48                   	dec    %eax
 8048062:	75 32                	jne    8048096 <fine>
 8048064:	e8 14 00 00 00       	call   804807d <_start+0x1d>
 8048069:	2e 2f                	cs das 
 804806b:	6c                   	insb   (%dx),%es:(%edi)
 804806c:	65 76 65             	gs jbe 80480d4 <d1+0x9>
 804806f:	6c                   	insb   (%dx),%es:(%edi)
 8048070:	34 20                	xor    $0x20,%al
 8048072:	65 76 30             	gs jbe 80480a5 <fine+0xf>
 8048075:	6c                   	insb   (%dx),%es:(%edi)
 8048076:	63 6d 64             	arpl   %bp,0x64(%ebp)
 8048079:	73 21                	jae    804809c <fine+0x6>
 804807b:	0a 00                	or     (%eax),%al
 804807d:	b8 04 00 00 00       	mov    $0x4,%eax
 8048082:	bb 01 00 00 00       	mov    $0x1,%ebx
 8048087:	59                   	pop    %ecx
 8048088:	ba 14 00 00 00       	mov    $0x14,%edx
 804808d:	cd 80                	int    $0x80
 804808f:	b8 01 00 00 00       	mov    $0x1,%eax
 8048094:	cd 80                	int    $0x80

08048096 <fine>:
 8048096:	58                   	pop    %eax
 8048097:	b8 7d 00 00 00       	mov    $0x7d,%eax
 804809c:	bb 60 80 04 08       	mov    $0x8048060,%ebx
 80480a1:	81 e3 00 f0 ff ff    	and    $0xfffff000,%ebx
 80480a7:	b9 97 00 00 00       	mov    $0x97,%ecx
 80480ac:	ba 07 00 00 00       	mov    $0x7,%edx
 80480b1:	cd 80                	int    $0x80
 80480b3:	8d 35 cb 80 04 08    	lea    0x80480cb,%esi
 80480b9:	89 f7                	mov    %esi,%edi
 80480bb:	b9 2c 00 00 00       	mov    $0x2c,%ecx
 80480c0:	ba 78 56 34 12       	mov    $0x12345678,%edx

080480c5 <l1>:
 80480c5:	ad                   	lods   %ds:(%esi),%eax
 80480c6:	31 d0                	xor    %edx,%eax
 80480c8:	ab                   	stos   %eax,%es:(%edi)
 80480c9:	e2 fa                	loop   80480c5 <l1>

080480cb <d1>:
 80480cb:	20 d7                	and    %dl,%bh
 80480cd:	0c cc                	or     $0xcc,%al
 80480cf:	b8 61 27 67 61       	mov    $0x61672761,%eax
 80480d4:	67 f4                	addr16 hlt 
 80480d6:	42                   	inc    %edx
 80480d7:	10 79 1b             	adc    %bh,0x1b(%ecx)
 80480da:	61                   	popa   
 80480db:	10 3e                	adc    %bh,(%esi)
 80480dd:	1b 70 11             	sbb    0x11(%eax),%esi
 80480e0:	38 bd f1 28 05 bd    	cmp    %bh,-0x42fad70f(%ebp)
 80480e6:	f3 49                	repz dec %ecx
 80480e8:	84 84 19 b5 d6 8c 13 	test   %al,0x138cd6b5(%ecx,%ebx,1)
 80480ef:	78 56                	js     8048147 <d1+0x7c>
 80480f1:	34 23                	xor    $0x23,%al
 80480f3:	a3                   	.byte 0xa3
 80480f4:	15                   	.byte 0x15
 80480f5:	f9                   	stc    
 
```



This problem we need to examine the sequential execution one by one.

The l1 step by step execution continues from the _start function to fine function**.** 

**fine:** what fine does in basically calls the *mprotect(0x8048000, 151, PROT_READ|PROT_WRITE|PROT_EXEC)* by int $0x80 syscall which point to mprotect

​	mprotect changes the access permission and sets the read write and execute permission starting from address  0x8048000 untill 151 byes. set break point at  0x80480b1. Examine the register values to check the address in ebx is the starting address and the value in ecx the length. The registers value are given below: info reg

```assembly
eax            0x7d	125
ecx            0x97	151
edx            0x7	7
ebx            0x8048000	134512640
esp            0xffffd768	0xffffd768
ebp            0x0	0x0
esi            0x0	0
edi            0x0	0
eip            0x80480b1	0x80480b1 <fine+27>
eflags         0x206	[ PF IF ]
cs             0x23	35
ss             0x2b	43
ds             0x2b	43
es             0x2b	43
fs             0x0	0
gs             0x0	0

```



After the fine function execute it goes to the l1 function because there is no jump. There for sequential execution goes to the l1.  examine the l1 function execution. It loops over lods, xor and stos instructions. Interesting thing to note that in changes the code in d1() function check the code in d1 after each. Set break point at the starting of the l1() function. and check the register values.

```assembly
eax            0x0	0
ecx            0x2c	44
edx            0x12345678	305419896
ebx            0x8048000	134512640
esp            0xffffd768	0xffffd768
ebp            0x0	0x0
esi            0x80480cb	134512843
edi            0x80480cb	134512843
eip            0x80480c5	0x80480c5 <l1>
eflags         0x206	[ PF IF ]
cs             0x23	35
ss             0x2b	43
ds             0x2b	43
es             0x2b	43
fs             0x0	0
gs             0x0	0

```

at this point l1() takes  44*4 = 176 steps to change the code on d1(). then continues to the d1 function.

**Manipulated code of d1:**

```assembly
(gdb) stepi 176
0x080480cb in d1 ()
```

```assembly
(gdb) disas d1
Dump of assembler code for function d1:
=> 0x080480cb <+0>:	pop    %eax
   0x080480cc <+1>:	cmpl   $0x1337c0de,(%eax)
   0x080480d2 <+7>:	jne    0x80480ed <d1+34>
   0x080480d4 <+9>:	xor    %eax,%eax
   0x080480d6 <+11>:	push   %eax
   0x080480d7 <+12>:	push   $0x68732f2f
   0x080480dc <+17>:	push   $0x6e69622f
   0x080480e1 <+22>:	mov    %esp,%ebx
   0x080480e3 <+24>:	push   %eax
   0x080480e4 <+25>:	push   %ebx
   0x080480e5 <+26>:	mov    %esp,%ecx
   0x080480e7 <+28>:	xor    %edx,%edx
   0x080480e9 <+30>:	mov    $0xb,%al
   0x080480eb <+32>:	int    $0x80
   0x080480ed <+34>:	mov    $0x1,%eax
   0x080480f2 <+39>:	xor    %ebx,%ebx
   0x080480f4 <+41>:	inc    %ebx
   0x080480f5 <+42>:	int    $0x80
End of assembler dump.

```

**This looks like a shell code.**



Now examine the d1+1 line cmpl instruction. set a break point there and check the eax value, which turns out to be our given argument to the elf file maze3.

```assembly
(gdb) info reg
eax            0xffffd8a8	-10072
ecx            0x0	0
edx            0x12345678	305419896
ebx            0x8048000	134512640
esp            0xffffd76c	0xffffd76c
ebp            0x0	0x0
esi            0x804817b	134513019
edi            0x804817b	134513019
eip            0x80480cc	0x80480cc <d1+1>
eflags         0x206	[ PF IF ]
cs             0x23	35
ss             0x2b	43
ds             0x2b	43
es             0x2b	43
fs             0x0	0
gs             0x0	0

```

Check the content of eax which is compared to fixed value 0x1337c0de.

```assembly
(gdb) x/s 0xffffd8a8
0xffffd8a8:	"AAAA"

```

There for we can see the in the value matches the fixed value it gives us the shell. which is all we need.

Now execute the binary with the parameter of the fixed value to solve this step and get the password for next label.

```
maze3@maze:/maze$ ./maze3 $(python -c 'print "\xde\xc0\x37\x13"')
$ cat /etc/maze_pass/maze4
deekaihiek

```

**Password: ** deekaihiek

