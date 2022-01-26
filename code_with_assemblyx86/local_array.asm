.586
.model flat, stdcall
.stack 4096
includelib libcmt.lib
includelib legacy_stdio_definitions.lib

ExitProcess PROTO, dwExitCode:DWORD
extern printf:NEAR
extern scanf:NEAR

.data
	format_out BYTE "a = %d , b = %d", 0Ah, 0

.code
	swap:
		push ebp
		mov ebp, esp
		sub esp, 4

		lea ecx, [ebp+4]
		mov ecx, ebx
		mov ebx, eax
		mov eax, ecx

		add esp, 4
		pop ebp
		ret

	main PROC c
        push ebp
        mov ebp, esp
        sub esp, 8

        lea ebx, [ebp-4]
        lea ecx, [ebp-8]
        mov eax, 10
        mov ebx, 20
        call Swap
        push ebx
        push eax
        push offset format_out
        call printf

        add esp, 12
        pop ebp

	pop ebp
	INVOKE ExitProcess, 0
	main endp

end