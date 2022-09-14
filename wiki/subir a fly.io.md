instalamos nuestras variables de entorno
pip install python-dotenv python-decouple
Creamos requirements.txt
corremos flyctl launch y seguimos las instrucciones

el primer intento nos da este error 

```
You can detach the terminal anytime without stopping the deployment
Monitoring Deployment

1 desired, 1 placed, 0 healthy, 1 unhealthy [restarts: 2]
v0 failed - Failed due to unhealthy allocations - no stable job version to auto revert to   
***v0 failed - Failed due to unhealthy allocations - no stable job version to auto revert to and deploying as v1 

Troubleshooting guide at https://fly.io/docs/getting-started/troubleshooting/
Error abort
```

ok, una cosa que me falto fue el crear una base de datos, según la documentación debo hacerlo así
https://fly.io/docs/reference/postgres/#creating-a-postgres-app

y me dio lo siguiente, obvio aquí oculto los datos y los puse en el archivo ``.env``
```
? Choose an app name (leave blank to generate one): drf-project
automatically selected personal organization: kei_kusanagi@outlook.com
? Select regions: Los Angeles, California (US) (lax)   
? Select configuration: Development - Single node, 1x shared CPU, 256MB RAM, 1GB disk       
Creating postgres cluster drf-project in organization personal
Postgres cluster drf-project created
  Username:    p*****s
  Password:    6460***************************************bb176
  Hostname:    d*************al
  Proxy Port:  ****2
  Postgres Port: 5****
Save your credentials in a secure place -- you won't be able to see them again!
==> Monitoring deployment

 1 desired, 1 placed, 1 healthy, 0 unhealthy [health checks: 3 total, 3 passing]
--> v0 deployed successfully


Connect to postgres
Any app within the kei_kusanagi@outlook.com organization can connect to postgres using the above credentials and the hostname "drf-project.internal."
For example: postgres://postgres:64**************************************************************************************************************2

Now that you've set up postgres, here's what you need to understand: https://fly.io/docs/reference/postgres-whats-next/
```
y nop, me marca error con el hsotname

```
raceback (most recent call last):
  File "C:\Users\admin\Desktop\Proyectos\Oreilly\drf-project\env\lib\site-packages\django\db\backends\base\base.py", line 282, in ensure_connection
    self.connect()
  File "C:\Users\admin\Desktop\Proyectos\Oreilly\drf-project\env\lib\site-packages\django\utils\asyncio.py", line 26, in inner
    return func(*args, **kwargs)
  File "C:\Users\admin\Desktop\Proyectos\Oreilly\drf-project\env\lib\site-packages\django\db\backends\base\base.py", line 263, in connect
    self.connection = self.get_new_connection(conn_params)
  File "C:\Users\admin\Desktop\Proyectos\Oreilly\drf-project\env\lib\site-packages\django\utils\asyncio.py", line 26, in inner
    return func(*args, **kwargs)
  File "C:\Users\admin\Desktop\Proyectos\Oreilly\drf-project\env\lib\site-packages\django\db\backends\postgresql\base.py", line 215, in get_new_connection
    connection = Database.connect(**conn_params)
  File "C:\Users\admin\Desktop\Proyectos\Oreilly\drf-project\env\lib\site-packages\psycopg2\__init__.py", line 122, in connect
    conn = _connect(dsn, connection_factory=connection_factory, **kwasync)
psycopg2.OperationalError: connection to server at "localhost" (::1), port 5433 failed: Connection refused (0x0000274D/10061)
        Is the server running on that host and accepting TCP/IP connections?
connection to server at "localhost" (127.0.0.1), port 5433 failed: Connection refused (0x0000274D/10061)
        Is the server running on that host and accepting TCP/IP connections?


The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "C:\Users\admin\Desktop\Proyectos\Oreilly\drf-project\manage.py", line 22, in <module>
    main()
  File "C:\Users\admin\Desktop\Proyectos\Oreilly\drf-project\manage.py", line 18, in main   
    execute_from_command_line(sys.argv)
  File "C:\Users\admin\Desktop\Proyectos\Oreilly\drf-project\env\lib\site-packages\django\core\management\__init__.py", line 446, in execute_from_command_line
    utility.execute()
  File "C:\Users\admin\Desktop\Proyectos\Oreilly\drf-project\env\lib\site-packages\django\core\management\__init__.py", line 440, in execute
    self.fetch_command(subcommand).run_from_argv(self.argv)
  File "C:\Users\admin\Desktop\Proyectos\Oreilly\drf-project\env\lib\site-packages\django\core\management\base.py", line 402, in run_from_argv
    self.execute(*args, **cmd_options)
  File "C:\Users\admin\Desktop\Proyectos\Oreilly\drf-project\env\lib\site-packages\django\core\management\base.py", line 448, in execute
    output = self.handle(*args, **options)
  File "C:\Users\admin\Desktop\Proyectos\Oreilly\drf-project\env\lib\site-packages\django\core\management\base.py", line 96, in wrapped
    res = handle_func(*args, **kwargs)
  File "C:\Users\admin\Desktop\Proyectos\Oreilly\drf-project\env\lib\site-packages\django\core\management\commands\migrate.py", line 114, in handle
    executor = MigrationExecutor(connection, self.migration_progress_callback)
  File "C:\Users\admin\Desktop\Proyectos\Oreilly\drf-project\env\lib\site-packages\django\db\migrations\executor.py", line 18, in __init__
    self.loader = MigrationLoader(self.connection)
  File "C:\Users\admin\Desktop\Proyectos\Oreilly\drf-project\env\lib\site-packages\django\db\migrations\loader.py", line 58, in __init__
    self.build_graph()
  File "C:\Users\admin\Desktop\Proyectos\Oreilly\drf-project\env\lib\site-packages\django\db\migrations\loader.py", line 235, in build_graph
    self.applied_migrations = recorder.applied_migrations()
  File "C:\Users\admin\Desktop\Proyectos\Oreilly\drf-project\env\lib\site-packages\django\db\migrations\recorder.py", line 81, in applied_migrations
    if self.has_table():
  File "C:\Users\admin\Desktop\Proyectos\Oreilly\drf-project\env\lib\site-packages\django\db\migrations\recorder.py", line 57, in has_table
    with self.connection.cursor() as cursor:
  File "C:\Users\admin\Desktop\Proyectos\Oreilly\drf-project\env\lib\site-packages\django\utils\asyncio.py", line 26, in inner
    return func(*args, **kwargs)
  File "C:\Users\admin\Desktop\Proyectos\Oreilly\drf-project\env\lib\site-packages\django\db\backends\base\base.py", line 323, in cursor
    return self._cursor()
  File "C:\Users\admin\Desktop\Proyectos\Oreilly\drf-project\env\lib\site-packages\django\db\backends\base\base.py", line 299, in _cursor
    self.ensure_connection()
  File "C:\Users\admin\Desktop\Proyectos\Oreilly\drf-project\env\lib\site-packages\django\utils\asyncio.py", line 26, in inner
    return func(*args, **kwargs)
  File "C:\Users\admin\Desktop\Proyectos\Oreilly\drf-project\env\lib\site-packages\django\db\backends\base\base.py", line 281, in ensure_connection
    with self.wrap_database_errors:
  File "C:\Users\admin\Desktop\Proyectos\Oreilly\drf-project\env\lib\site-packages\django\db\utils.py", line 91, in __exit__
    raise dj_exc_value.with_traceback(traceback) from exc_value
  File "C:\Users\admin\Desktop\Proyectos\Oreilly\drf-project\env\lib\site-packages\django\db\backends\base\base.py", line 282, in ensure_connection
    self.connect()
  File "C:\Users\admin\Desktop\Proyectos\Oreilly\drf-project\env\lib\site-packages\django\utils\asyncio.py", line 26, in inner
    return func(*args, **kwargs)
  File "C:\Users\admin\Desktop\Proyectos\Oreilly\drf-project\env\lib\site-packages\django\db\backends\base\base.py", line 263, in connect
    self.connection = self.get_new_connection(conn_params)
  File "C:\Users\admin\Desktop\Proyectos\Oreilly\drf-project\env\lib\site-packages\django\utils\asyncio.py", line 26, in inner
    return func(*args, **kwargs)
  File "C:\Users\admin\Desktop\Proyectos\Oreilly\drf-project\env\lib\site-packages\django\db\backends\postgresql\base.py", line 215, in get_new_connection
    connection = Database.connect(**conn_params)
  File "C:\Users\admin\Desktop\Proyectos\Oreilly\drf-project\env\lib\site-packages\psycopg2\__init__.py", line 122, in connect
    conn = _connect(dsn, connection_factory=connection_factory, **kwasync)
django.db.utils.OperationalError: connection to server at "localhost" (::1), port 5433 failed: Connection refused (0x0000274D/10061)
        Is the server running on that host and accepting TCP/IP connections?
connection to server at "localhost" (127.0.0.1), port 5433 failed: Connection refused (0x0000274D/10061)
        Is the server running on that host and accepting TCP/IP connections?
```

