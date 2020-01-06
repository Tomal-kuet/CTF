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

C program:

```

```

