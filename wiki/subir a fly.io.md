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

ok, después de mucho averiguar y gracias a la guia de Lecks que casid e inmediato encontró el error, creo avanzamos, pero sigue sin subirse la api, el problema estaba en el procfile, el cual un error decía que no reconocía el comando gunicorn, entonces procedí en instalarlo con un pip install, luego lo configure para que inicie la app que estamos subiendo

```
# Modify this Procfile to fit your needs

web: gunicorn watchmate.wsgi
```

ahora el problema esta en la base de datos

```
Recent Logs
2022-09-14T17:50:30.000 [info]     from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
2022-09-14T17:50:30.000 [info]   File "/layers/paketo-buildpacks_pip-install/packages/lib/python3.10/site-packages/django/contrib/auth/base_user.py", line 49, in <module>
2022-09-14T17:50:30.000 [info]     class AbstractBaseUser(models.Model):
2022-09-14T17:50:30.000 [info]   File "/layers/paketo-buildpacks_pip-install/packages/lib/python3.10/site-packages/django/db/models/base.py", line 141, in __new__
2022-09-14T17:50:30.000 [info]     new_class.add_to_class("_meta", Options(meta, app_label))     
2022-09-14T17:50:30.000 [info]   File "/layers/paketo-buildpacks_pip-install/packages/lib/python3.10/site-packages/django/db/models/base.py", line 369, in add_to_class
2022-09-14T17:50:30.000 [info]     value.contribute_to_class(cls, name)
2022-09-14T17:50:30.000 [info]   File "/layers/paketo-buildpacks_pip-install/packages/lib/python3.10/site-packages/django/db/models/options.py", line 231, in contribute_to_class
2022-09-14T17:50:30.000 [info]     self.db_table, connection.ops.max_name_length()
2022-09-14T17:50:30.000 [info]   File "/layers/paketo-buildpacks_pip-install/packages/lib/python3.10/site-packages/django/utils/connection.py", line 15, in __getattr__
2022-09-14T17:50:30.000 [info]     return getattr(self._connections[self._alias], item)
2022-09-14T17:50:30.000 [info]   File "/layers/paketo-buildpacks_pip-install/packages/lib/python3.10/site-packages/django/utils/connection.py", line 62, in __getitem__
2022-09-14T17:50:30.000 [info]     conn = self.create_connection(alias)
2022-09-14T17:50:30.000 [info]   File "/layers/paketo-buildpacks_pip-install/packages/lib/python3.10/site-packages/django/db/utils.py", line 193, in create_connection
2022-09-14T17:50:30.000 [info]     backend = load_backend(db["ENGINE"])
2022-09-14T17:50:30.000 [info]   File "/layers/paketo-buildpacks_pip-install/packages/lib/python3.10/site-packages/django/db/utils.py", line 113, in load_backend
2022-09-14T17:50:30.000 [info]     return import_module("%s.base" % backend_name)
2022-09-14T17:50:30.000 [info]   File "/layers/paketo-buildpacks_cpython/cpython/lib/python3.10/importlib/__init__.py", line 126, in import_module
2022-09-14T17:50:30.000 [info]     return _bootstrap._gcd_import(name[level:], package, level)   
2022-09-14T17:50:30.000 [info]   File "/layers/paketo-buildpacks_pip-install/packages/lib/python3.10/site-packages/django/db/backends/sqlite3/base.py", line 7, in <module>
2022-09-14T17:50:30.000 [info]     from sqlite3 import dbapi2 as Database
2022-09-14T17:50:30.000 [info]   File "/layers/paketo-buildpacks_cpython/cpython/lib/python3.10/sqlite3/__init__.py", line 57, in <module>
2022-09-14T17:50:30.000 [info]     from sqlite3.dbapi2 import *
2022-09-14T17:50:30.000 [info]   File "/layers/paketo-buildpacks_cpython/cpython/lib/python3.10/sqlite3/dbapi2.py", line 27, in <module>
2022-09-14T17:50:30.000 [info]     from _sqlite3 import *
2022-09-14T17:50:30.000 [info] ImportError: libsqlite3.so.0: cannot open shared object file: No such file or directory
2022-09-14T17:50:30.000 [info] [2022-09-14 17:50:30 +0000] [533] [INFO] Worker exiting (pid: 533)2022-09-14T17:50:30.000 [info] [2022-09-14 17:50:30 +0000] [515] [INFO] Shutting down: Master    
2022-09-14T17:50:30.000 [info] [2022-09-14 17:50:30 +0000] [515] [INFO] Reason: Worker failed to 
boot.
2022-09-14T17:50:31.000 [info] Starting clean up.
***v6 failed - Failed due to unhealthy allocations - no stable job version to auto revert to and 
deploying as v7

Troubleshooting guide at https://fly.io/docs/getting-started/troubleshooting/
Error abort
```

después de muchos intentos, subi una app sensilla, un simple main.py diciendo hola desde fly.io y quedo

lo que hice diferente fue usar otro buildpack, en un tutorial explicaban que era mejor usar el de heroku

``builder = "heroku/buildpacks:latest"`` 

esto se pone en el archivo fly.toml

![[Pasted image 20220914150339.png]]

pero me daba un error, referente a los static y collectstatics, entonces buscando en stack
https://stackoverflow.com/questions/36760549/python-django-youre-using-the-staticfiles-app-without-having-set-the-static-ro

tambien en allowed host le puse ``['*']``


configure eso en settings.py y listooooooo deployed successfuly

![[Pasted image 20220914150502.png]]