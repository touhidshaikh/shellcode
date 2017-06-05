#include<stdio.h>
#include<string.h>

unsigned char code[] = "";


main()
{
	printf("Touhid Shaikh (http://touhidshaikh.com)\n");
	printf("Shellcode Length:  %d\n", (int)strlen(code));

	int (*ret)() = (int(*)())code;

	ret();

}

	
