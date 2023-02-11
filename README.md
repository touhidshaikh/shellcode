# Shellcode (My Collecction)
Hello Friends. I am Tauhid Shaikh. Here i upload some of my shellcode for everyone.
Shellcode is a type of low-level code that is written to be executed directly in the memory of a system, bypassing the normal execution flow of the operating system. It is often used in security exploits and attacks, as it provides a way for an attacker to execute arbitrary code on a target system. Shellcode can be written in various assembly languages and is typically platform-specific, meaning that it is designed to work on a specific architecture and operating system.

### Compilation and Execution of asassmbly program
```bash
nasm -f elf64 shell.asm -o shell.o
```
This command uses the NASM (Netwide Assembler) to compile the assembly program, shell.asm, into an object file, shell.o. The `-f elf64` flag specifies that the target format is the ELF (Executable and Linkable Format) 64-bit format, and the `-o shell.o` flag specifies the output file name.

```bash
ld shell.o -o shell #Making Binary File
```
This command uses the ld linker to link the object file, shell.o, into an executable binary file, shell. The `-o shell` flag specifies the output file name.

```bash
./bin2shell.sh shell #extract hex code from the binary[https://github.com/touhidshaikh/bin2shell]
```
This command executes the script, bin2shell.sh, and passes the binary file, shell, as an argument. The bin2shell.sh script is used to extract the hex code from the binary file, which can be used as shellcode in an exploit.

### Compilation and Execution of C program

```bash
# gcc -fno-stack-protector -z execstack filename.c -o file-shell 
```
This command uses the GCC (GNU Compiler Collection) to compile the C program, filename.c, into an executable binary file, file-shell. The `-fno-stack-protector` flag disables stack protection, and the -z execstack flag marks the stack as executable. The `-o file-shell` flag specifies the output file name.

## Contribution
Your contributions and suggestions are welcome.

## Disclaimer
Using shellcode can be illegal and unethical, and can cause harm to individuals and organizations. It is important to understand the potential consequences of executing shellcode and to handle it with care and caution. Writing and using shellcode for malicious purposes is illegal and unethical, and can result in serious consequences, including criminal charges and damage to individuals and organizations. If you are interested in shellcode for research or educational purposes, it is recommended that you use it in a controlled environment, such as a virtual machine or a sandbox, and always follow relevant laws and regulations. I does not endorse or support the use of shellcode for malicious purposes and assumes no responsibility for any harm or damage that may result from its use.

## Contact
- Touhid shaikh <touhidshaikh22[at]gmail[dot]com>
