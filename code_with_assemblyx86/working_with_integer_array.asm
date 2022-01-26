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
	max DWORD ?
	anarray DWORD 20 DUP(?)
	format_out BYTE "%d ", 0
	format_out2 BYTE "max = %d"

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
	max DWORD ?
	anarray DWORD 20 DUP(?)
	format_out BYTE "%d ", 0
	format_out2 BYTE "max = %d"

.code
	main PROC c
	mov ecx, 0
	
	forbegin:
	cmp ecx, 20		; for (int i = 0;)
	je forend

	mov eax, ecx
	mul ecx
	add eax, 5
	mov edx, 0
	mov ebx, 20
	div ebx

	printing1:
	mov [anarray+4*ecx], edx
	mov ebx, anarray[ecx*4]
	push ecx
	push ebx
	push offset format_out
	call printf
	add esp, 8
	pop ecx
	add ecx, 1
	jmp forbegin

	forend:
	mov ecx, 0
	mov edx, 0

	forebegin2:
	cmp ecx, 20
	je printing2
	mov ebx, anarray[ecx*4]
	add ecx, 1
	cmp ebx, edx
	jle forebegin2
	mov edx, ebx
	jmp forebegin2


	printing2:
	push edx
	push offset format_out2
	call printf
	add esp, 8


	INVOKE ExitProcess, 0
	main endp
end
