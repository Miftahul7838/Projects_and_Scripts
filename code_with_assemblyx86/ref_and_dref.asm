.586
.model flat, stdcall
.stack 4086
includelib libcmt.lib
includelib legacy_stdio_definitions.lib

ExitProcess PROTO, dwExitCode:DWORD
extern printf:NEAR

.data
	a DWORD 10		; int a = 10
	b DWORD 20		; int b = 20
	format_out BYTE "eax points to %d\n", 0Ah, 0

.code
	main PROC c
		mov eax, offset a	; int *eax = &a
		mov ebx, offset b	; int *ebx = &b

		mov ecx, a

		add b, ecx	; b += a

		mov ecx, [ebx]	; *eax = *eax + *ebx
		add [eax], ecx
		
		push [eax]
		push offset format_out
		call printf
		add esp, 8
		

		INVOKE ExitProcess, 0
		main endp

end