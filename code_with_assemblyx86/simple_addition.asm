.586
.model flat, stdcall
.stack 4096
includelib libcmt.lib
includelib legacy_stdio_definitions.lib

ExitProcess PROTO, dwExitCode: DWORD

.data 
	; Variables go here
	var1 DWORD 15			;int var1 = 15

.code
	main PROC c
		;Assembly instruction for main function go here
		mov eax, var1
		mov ebx, 4
		mov edx, 0
		div ebx
		add eax, 2
		mov ebx, 5
		mul ebx
		mov ebx, eax

		INVOKE ExitProcess, 0   ;end(0)
		main endp

end