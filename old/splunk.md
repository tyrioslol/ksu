23 fake_telnet source="tcp:23" AND sourcetype="fake_telnet"
80 fake_http source="tcp:80" AND sourcetype="fake_http"
445 fake_smb source="tcp:445" AND sourcetype="fake_smb"
22 fake_ssh source="tcp:22" AND sourcetype="fake_ssh"
21 fake_ftp source="tcp:21" AND sourcetype="fake_ftp"
		
		
Entire query:		
(source="tcp:23" AND sourcetype="fake_telnet") OR (source="tcp:80" AND sourcetype="fake_http") OR (source="tcp:445" AND sourcetype="fake_smb") OR (source="tcp:22" AND sourcetype="fake_ssh") OR (source="tcp:21" AND sourcetype="fake_ftp")		
