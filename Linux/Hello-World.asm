;Title: Linux/x86 - Print Hello World Shellcode
;Author: Touhid M.Shaikh
;Contact: https://github.com/touhidshaikh
;Category: Shellcode
;Architecture: Linux x86_64


; This code uses the Linux system call interface to perform the following actions:
; 1. Open the file "hello.txt" for writing, creating it if it does not exist.
; 2. Write the message "Hello, World!" to the file.
; 3. Close the file.

.section .data
    filename: .asciz "hello.txt"
    message: .asciz "Hello, World!"

.section .text
    .global main

main:
    mov x0, #5 ; open syscall number
    mov x1, filename ; pointer to filename
    mov x2, #(O_CREAT | O_WRONLY) ; flags
    mov x3, #(S_IRWXU) ; mode
    svc #0 ; invoke open syscall

    ; file descriptor is returned in x0
    mov x1, x0

    mov x0, #4 ; write syscall number
    mov x2, message ; pointer to message
    mov x3, #14 ; length of message
    svc #0 ; invoke write syscall

    mov x0, #6 ; close syscall number
    svc #0 ; invoke close syscall

    mov x0, #60 ; exit syscall number
    mov x1, #0 ; exit status
    svc #0 ; invoke exit syscall

