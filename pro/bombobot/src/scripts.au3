;#RequireAdmin
#AutoIt3Wrapper_UseX64=n
#include <Array.au3>
#include "OpenCV-Match_UDF.au3"
#include <WinAPI.au3>
#include <WindowsConstants.au3>
_OpenCV_Startup()
Global $GameHD = WinGetHandle("Bombcrypto - Google Chrome")

Opt("MouseCoordMode", 2)
Opt("PixelCoordMode", 2)
Opt("CaretCoordMode", 2)

	$iFullDesktopWidth = _WinAPI_GetSystemMetrics(78)
	$iFullDesktopHeight = _WinAPI_GetSystemMetrics(79)
	;ConsoleWrite($iFullDesktopWidth)
	;ConsoleWrite($iFullDesktopHeight)
	_ArrayDisplay(_ScreenSize())
	$Match = _MatchPicture("img/bot_br.png", 0, 0, $iFullDesktopWidth,$iFullDesktopHeight)
	;_ArrayDisplay($Match)
	;WinActive($GameHD)
	;MouseMove(0,0)
	;MouseMove($Match[0], $Match[1])



_OpenCV_Shutdown()