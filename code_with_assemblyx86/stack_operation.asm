.586
.model flat, stdcall
.stack 4086
includelib libcmt.lib
includelib legacy_stdio_definitions.lib

ExitProcess PROTO, dwExitCode:DWORD
extern printf:NEAR

.data
	format_out BYTE "result = %d\n", 0Ah, 0

.code
	main PROC c
	; puts the number in the stack
		push 15
		push 4
		push 10
		push 6
		push 12

	; pops off 12 and 6
		pop eax
		pop ebx

	; multiplies 12 by 6
		mul ebx

	; pops off 10
		pop ebx

	; adds 10 to eax which is (12 * 6)
		add eax, ebx
	
	; pops of 4 from the stack
		pop ebx

	; subtracts 4 from eax which is (10 + (12 * 6))
		sub eax, ebx

	; pops off 15 from the stack
		pop ebx

	; subtracts 15 from the eax which is (10 + (12 * 6) - 4)
		sub eax, ebx
	
	comment !
	end result is printed out which is result = (10 + (12 * 6) - 4 - 15) 
	or (10 + (12 * 6) - (4 + 15))
	!
		push eax
		push offset format_out
		call printf
		add esp, 12


		INVOKE ExitProcess, 0
		main endp

end