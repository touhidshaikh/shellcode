To compile and link an assembly program on a 64-bit ARM architecture running a Linux operating system, you can use the following command:

```bash
as -o program.o program.s
ld -o program program.o
```

This will compile the source file `program.s` into an object file `program.o`, and then link the object file into an executable program.

If you want to include libraries in your program, you can use the `-l` flag to specify the library, like this:
```bsah
ld -o program program.o -lm
```

This will link the math library (libm.so) with your program.

Note that the exact commands and options may vary depending on your specific system and toolchain.