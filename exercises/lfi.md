**Exercise 5: LFI (Local File Inclusion)**

**Attack Scenario:** Exploit the LFI in http://localhost/rlfi.php to read sensitive files on the server. 

**Goal:** Read the file /etc/passwd

**Question**: Look at the code of rlfi.php. Can you also execute PHP code using this LFI?

**What you learned:** You exploited an LFI vulnerability which allows setting the file name which will be included in the response.



