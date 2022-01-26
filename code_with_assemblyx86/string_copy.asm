.586
.model flat, stdcall
.stack 4086
includelib libcmt.lib
includelib legacy_stdio_definitions.lib

ExitProcess PROTO, dwExitCode:DWORD
extern printf:NEAR

.data
	str1 BYTE "ABCDEF", 0
	str2 BYTE "XYZ123", 0
	format_out BYTE "str2 = %s\n", 0Ah, 0 
	string BYTE 7 DUP(0)

.code
	main PROC c

		; Read each character and store it into the registers
		mov eax, 0
		mov al, BYTE PTR [str1]
		mov ebx, 0
		mov bl, BYTE PTR [str1+1]
		mov ecx, 0
		mov cl, BYTE PTR [str1+2]
		mov edx, 0
		mov dl, BYTE PTR [str1+3]

		; Write each character in the registers to the string array
		mov BYTE PTR [str2], al
		mov BYTE PTR [str2+1], bl
		mov BYTE PTR [str2+2], cl
		mov BYTE PTR [str2+3], dl

		; Getting the last two character in str1
		mov al, BYTE PTR [str1+4]
		mov bl, BYTE PTR [str1+5]

		; moving the last 2 character in str1 to str2
		mov BYTE PTR [str2+4], al
		mov BYTE PTR [str2+5], bl

		; print out the str2 in a formated string
		push offset str2
		push offset format_out
		call printf
		add esp, 8

		INVOKE ExitProcess, 0
		main endp

end