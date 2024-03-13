SELECT Grant_priv, Super_priv, Create_tmp_table_priv, Lock_tables_priv, Create_view_priv, Show_view_priv, Create_routine_priv, Alter_routine_priv, Create_user_priv, Event_priv, Trigger_priv, Create_tablespace_priv
FROM mysql.user
WHERE User IN ('user_0d_1', 'user_0d_2')
  AND Host = 'localhost';

