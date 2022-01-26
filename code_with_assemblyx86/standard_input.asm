.586
.model flat, stdcall
.stack 4086
includelib libcmt.lib
includelib legacy_stdio_definitions.lib

ExitProcess PROTO, dwExitCode:DWORD
extern printf:NEAR
extern scanf:NEAR

.data
	a_number DWORD 0
	format_out BYTE "Enter a number: ", 0Ah, 0
	format_out2 BYTE "byte order reversed = %x ", 0Ah, 0
	format BYTE "%x", 0
	rNum DWORD 0

.code
	main PROC c
		push offset format_out
		call printf
		add esp, 4

		push offset a_number
		push offset format
		call scanf
		add esp, 8
		
		mov eax, 0
		mov al, BYTE PTR [a_number]
		mov ebx, 0
		mov bl, BYTE PTR [a_number+1]
		mov ecx, 0
		mov cl, BYTE PTR [a_number+2]
		mov edx, 0
		mov dl, BYTE PTR [a_number+3]

		mov BYTE PTR [rNum], dl
		mov BYTE PTR [rNum+1], cl
		mov BYTE PTR [rNum+2], bl
		mov BYTE PTR [rNum+3], al

		push rNum
		push offset format_out2
		call printf
		add esp, 8

		INVOKE ExitProcess, 0
		main endp

end