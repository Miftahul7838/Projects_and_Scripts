.586
.model flat, stdcall
.stack 4096
includelib libcmt.lib
includelib legacy_stdio_definitions.lib

ExitProcess PROTO, dwExitCODE:DWORD
extern printf:NEAR
extern scanf:NEAR

.data	; Variables
	number DWORD ?
	count DWORD ?
	temp DWORD ?
	format_in BYTE "%d", 0
	format_out1 BYTE "Enter 3 numbers:", 0Ah, 0
	format_out2 BYTE "Maximum is %d\n", 0Ah, 0

.code
	main PROC c
		mov eax, 0
		mov count, 0
		mov temp, 0
		
		prompt:
		cmp count, 3
		je elseblock
		push offset format_out1
		call printf
		add esp, 4

		push offset number
		push offset format_in
		call scanf
		add esp, 8

		mov eax, number

		cmp count, 3
		je elseblock
		add count, 1
		cmp eax, temp
		jl prompt
		mov temp, eax
		jmp prompt

		elseblock:
		mov ecx, temp 
		push ecx
		push offset format_out2
		call printf
		add esp, 8
		
	INVOKE ExitProcess, 0
	main endp

end