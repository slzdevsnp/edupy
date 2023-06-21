
# How to add a  run/debug configuration for a flask app

- Run/Edit configurations
-  click '+;  select type of config: Flask Server
-  specify name Flask projname
-  Target type : Module Name
-  Target:  flask
-  FLASK_ENV : development
-  FLASK_DEBUG : (ticked)
-  Environment variables: FLASK_APP=./cashman/index.py
-  Python interpreter  (python from virtualenv)
  
# How to use this config to debug flask app

- Menu Run : Debug Flask cashman  to start your flask app in debug mode
- put a breakpoint in a the code .e.g. endpoint
  call an endpoint, see your breakpoint hit

