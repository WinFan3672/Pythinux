# Roadmap
This is my long-term plan for the future of Pythinux.
## 2.x
* Package Manager
	- Dependency tracking
		+ Allows for locking dependencies as required for a package.
		
    - Smarter upgrades
	    + Version tracking allows for skipping up-to-date packages.
	    
	- Expected PKM version: 3.0
	- Expected Release: 2.3
	
* Users
	- Custom Groups
	- Group Permissions
	- User Manager
		+ 1.x had one, 2.x should as well.
	- Expected Release: 2.3
## 3.x	
3.0 will implement a proper GUI system, with a window manager and built-in applications. A terminal emulator will allow for running terminal commands, as always. 

However, I have no idea how to approach something like this as using the standard library alone will be an issue.

Perhaps I could make a standalone OS that uses Pythinux as its base. It would allow me to develop a proper window manager and so on, and add an API to Pythinux to integrate it with the system. However, this would massively increase the project's scope and complexity, and I'd have to ditch a pure python codebase. But then again, C support would be really nice.

If you have ideas, let me know.
## Conclusion	
Generally, I implement things as soon as I think of them, but more long-term plans would be more viable.
