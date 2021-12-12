#include <ButtonConstants.au3>
#include <EditConstants.au3>


HotKeySet("{F9}", "premiSpazio")
HotKeySet("{F11}", "premiT")
HotKeySet("{F10}", "pause")
HotKeySet("{F8}", "end")


pause()



Func premiSpazio()
   ConsoleWrite("premi spazio")
   While 1
	  send("{SPACE}")
   WEnd
EndFunc

Func premiT()
   ConsoleWrite("premi t")
   While 1
	  send("t")
   WEnd
EndFunc

Func pause()
   ConsoleWrite("pausa")
   While 1
	  Sleep(1000)
   WEnd
EndFunc

Func end()
   ConsoleWrite("exit")
   Exit
EndFunc
