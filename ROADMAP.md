# Pythinux Roadmap
### As of 14/2/2023
## Beta 14
Current release.
## Beta 15 - Beta ?
These releases will add documentation and implement the following features:
* Standard Library
* WinHub
	- Implements several Windows-only functions:  
		+ Sound playback
		+ Registry editing
		+ DNS Resolver Cache Clearing
			* And other network functions
		+ Etc.
		
* RemoveUser support
* Lift/drop commands for Files
	- Lift
		+ Format: lift [filename]
		+ Will print the BASE64 Data of [filename].
	- Drop
		+ Format: drop [filename]|[data]
		+ Will save the base64 [data] to [filename]
		+ Used in conjunction with `lift`
		
* Custom Manual Support that actually works
	- Fix current
	- Manual explorer
	
* PKM Upgrade update
	- Compares versions before upgrading
	
* Documentation overhaul
	- A lot of it is outdated, and needs updating
	- A lot of it needs to be redone to make it less confusing
	- Proper documentation, rather than tutorials
	
* etc.

## 1.0.0
This will be the final release and will be stable. Several manuals will be removed for irrelevancy
## Beyond that
There will be more features implemented that should be added at some point.
