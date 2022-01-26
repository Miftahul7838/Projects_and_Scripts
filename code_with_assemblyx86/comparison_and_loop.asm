.586
.model flat, stdcall
.stack 4096
includelib libcmt.lib
includelib legacy_stdio_definitions.lib

ExitProcess PROTO, dwExitCODE:DWORD
extern printf:NEAR
extern scanf:NEAR
extern gets:NEAR

.data	; Variables
	count DWORD 0

	str1 BYTE "Hello World!", 0
	str2 BYTE 20 DUP(20)
	format_out BYTE "Enter your string: ", 0Ah, 0
	format_out1 BYTE "%s and %s are the same", 0Ah, 0
	format_out2 BYTE "%s and %s are not the same", 0Ah, 0

.code
	main PROC c
	mov count, 0

	; printf("Enter your string: ")
	push offset format_out
	call printf
	add esp, 4

	; gets(str2) //Reads a line from stdin and stores it into [str2]
	push offset str2
	call gets
	add esp, 4

	startblock:
	cmp count, 13
	je confirmblock
	mov eax, 0
	mov ebx, count
	mov al, BYTE PTR [str1+ebx]
	cmp al, [str2+ebx]
	jne elseblock
	add count, 1
	jmp startblock

	confirmblock:
	push offset str1
	push offset str2
	push offset format_out1
	call printf
	add esp, 12
	jmp endblock

	elseblock:
	push offset str1
	push offset str2
	push offset format_out2
	call printf
	add esp, 12


	endblock:
	INVOKE ExitProcess, 0
	main endp
end