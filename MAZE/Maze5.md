By running the porgram and checking the assembly we figuire out that user name and password should be 8 byte long.

```assembly
   0x080485e7 <+0>:	push   %ebp
   0x080485e8 <+1>:	mov    %esp,%ebp
   0x080485ea <+3>:	sub    $0x14,%esp
   0x080485ed <+6>:	push   $0x8048760
   0x080485f2 <+11>:	call   0x80483c0 <puts@plt>
   0x080485f7 <+16>:	add    $0x4,%esp
   0x080485fa <+19>:	push   $0x8048772
   0x080485ff <+24>:	call   0x80483b0 <printf@plt>
   0x08048604 <+29>:	add    $0x4,%esp
   0x08048607 <+32>:	lea    -0x9(%ebp),%eax
   0x0804860a <+35>:	push   %eax
   0x0804860b <+36>:	push   $0x804877e
   0x08048610 <+41>:	call   0x8048410 <__isoc99_scanf@plt>
   0x08048615 <+46>:	add    $0x8,%esp
   0x08048618 <+49>:	push   $0x8048782
   0x0804861d <+54>:	call   0x80483b0 <printf@plt>
   0x08048622 <+59>:	add    $0x4,%esp
   0x08048625 <+62>:	lea    -0x12(%ebp),%eax
   0x08048628 <+65>:	push   %eax
   0x08048629 <+66>:	push   $0x804877e
   0x0804862e <+71>:	call   0x8048410 <__isoc99_scanf@plt>
   0x08048633 <+76>:	add    $0x8,%esp
   0x08048636 <+79>:	lea    -0x9(%ebp),%eax
   0x08048639 <+82>:	push   %eax
   0x0804863a <+83>:	call   0x80483f0 <strlen@plt>
   0x0804863f <+88>:	add    $0x4,%esp
   0x08048642 <+91>:	cmp    $0x8,%eax
   0x08048645 <+94>:	jne    0x8048658 <main+113>
   0x08048647 <+96>:	lea    -0x12(%ebp),%eax
   0x0804864a <+99>:	push   %eax
   0x0804864b <+100>:	call   0x80483f0 <strlen@plt>
   0x08048650 <+105>:	add    $0x4,%esp
   0x08048653 <+108>:	cmp    $0x8,%eax
   0x08048656 <+111>:	je     0x804866c <main+133>
   0x08048658 <+113>:	push   $0x804878e
   0x0804865d <+118>:	call   0x80483c0 <puts@plt>
   0x08048662 <+123>:	add    $0x4,%esp
   0x08048665 <+126>:	push   $0xffffffff
   0x08048667 <+128>:	call   0x80483e0 <exit@plt>
   0x0804866c <+133>:	push   $0x0
   0x0804866e <+135>:	push   $0x0
   0x08048670 <+137>:	push   $0x0
   0x08048672 <+139>:	push   $0x0
   0x08048674 <+141>:	call   0x8048420 <ptrace@plt>
   0x08048679 <+146>:	add    $0x10,%esp
   0x0804867c <+149>:	test   %eax,%eax
   0x0804867e <+151>:	je     0x8048694 <main+173>
   0x08048680 <+153>:	push   $0x80487a0
   0x08048685 <+158>:	call   0x80483c0 <puts@plt>
---Type <return> to continue, or q <return> to quit---
   0x0804868a <+163>:	add    $0x4,%esp
   0x0804868d <+166>:	mov    $0x0,%eax
   0x08048692 <+171>:	jmp    0x80486d6 <main+239>
   0x08048694 <+173>:	lea    -0x12(%ebp),%eax
   0x08048697 <+176>:	push   %eax
   0x08048698 <+177>:	lea    -0x9(%ebp),%eax
   0x0804869b <+180>:	push   %eax
   0x0804869c <+181>:	call   0x804853b <foo>
   0x080486a1 <+186>:	add    $0x8,%esp
   0x080486a4 <+189>:	test   %eax,%eax
   0x080486a6 <+191>:	je     0x80486c4 <main+221>
   0x080486a8 <+193>:	push   $0x80487ab
   0x080486ad <+198>:	call   0x80483c0 <puts@plt>
   0x080486b2 <+203>:	add    $0x4,%esp
   0x080486b5 <+206>:	push   $0x80487c3
   0x080486ba <+211>:	call   0x80483d0 <system@plt>
   0x080486bf <+216>:	add    $0x4,%esp
   0x080486c2 <+219>:	jmp    0x80486d1 <main+234>
   0x080486c4 <+221>:	push   $0x80487cb
   0x080486c9 <+226>:	call   0x80483c0 <puts@plt>
   0x080486ce <+231>:	add    $0x4,%esp
   0x080486d1 <+234>:	mov    $0x0,%eax
   0x080486d6 <+239>:	leave  
   0x080486d7 <+240>:	ret    
```

To get over the ptrace check in gdb do following 

```assembly
b *0x08048674
b *0x0804869c
r
jump *0x08048694
```

Now we are at the verge of calling the foo function with user name and key parameter.

Debug and check the foo function  find this portion is interesting something is going to happen :man_pilot:

```assembly
	 0x080485b2 <+119>:	lea    -0x11(%ebp),%edx
   0x080485b5 <+122>:	mov    -0x4(%ebp),%eax
   0x080485b8 <+125>:	add    %edx,%eax
   0x080485ba <+127>:	movzbl (%eax),%edx
   0x080485bd <+130>:	mov    -0x4(%ebp),%ecx
   0x080485c0 <+133>:	mov    0xc(%ebp),%eax
   0x080485c3 <+136>:	add    %ecx,%eax
   0x080485c5 <+138>:	movzbl (%eax),%eax
   0x080485c8 <+141>:	cmp    %al,%dl
```

Set a break point at : 0x080485b2

```assembly
b *0x080485b2
```

set another break point: 0x080485c8

```assembly
b *0x080485c8
```

We have to make eax and edx equal to trigger a different branch. By trial and error found that following input makes it equal:

Username: AAAAAABO

Key: ppehlbbP 

Basic idea is that the binary comares each character in the user name and password we just have to mach those. so i figured it out by this process and checking the eax and edx value each time. Eventually it give us a shell.



**Password: epheghuoli**

