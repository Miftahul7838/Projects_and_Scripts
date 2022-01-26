.586
.model flat, stdcall
.stack 4096
includelib libcmt.lib
includelib legacy_stdio_definitions.lib

ExitProcess PROTO, dwExitCode:DWORD
extern printf:NEAR
extern scanf:NEAR

.data
	format_in BYTE "%s",0		; takes in as string format
	format_out BYTE "%c ",0Ah, 0		; prints out as string format

.code
	main PROC c
	push ebp
	mov ebp, esp

	sub esp, 20			

	lea ebx, [ebp-20]
	push ebx
	push offset format_in
	call scanf
	add esp, 8

	mov ecx, 20

	forbegin:
	mov eax, ebp
	sub eax, ecx
	mov al, [eax]
	cmp al, 0
	je elseblock

	push ecx
	push eax
	push offset format_out
	call printf
	add esp, 8
	pop ecx
	sub ecx, 1
	jmp forbegin

	elseblock:

	pop ebp

	INVOKE ExitProcess, 0
	main endp

end