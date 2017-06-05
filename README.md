# shellcode

Hello Friends. I am Tauhid Shaikh. Here i upload some of my shellcode for everyone .
It's Free to use , modify and redistribute. 

pay attention on below's instruction for proper execution and compilation.

### Compilation and Execution of asassmbly program
#nasm -f elf64 shell.asm -o shell.o

#ld shell.o -o shell <=== Making Binary File

#./bin2shell.sh shell <== xtract hex code from the binary[https://github.com/touhidshaikh/bin2shell]

### Compilation and Execution of C program

#gcc -fno-stack-protector -z execstack filename.c -o file-shell



FOR ANY ISSUE PLZ REPORT ME .
Thank You.

Touhid shaikh.
touhidshaikh22[at]gmail[dot]com
