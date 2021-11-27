import autoit as it

it.run("notepad.exe")
it.win_wait_active("[CLASS:Notepad]", 3)
it.control_send("[CLASS:Notepad]", "Edit1", "hello world{!}")
it.win_close("[CLASS:Notepad]")
it.control_click("[Class:#32770]", "Button2")