# listen.py
Just a python-script to listen on a raw socket

It binds to any (int) port. Leave host blank to bind to any/all interface(s).

The script should probably only be used for testing, as there are a huge load of drawbacks to the simplicity of it (no threading, no handling of multiple incoming connections, no modularity, no handling of telnet special characters, pretty much no proper exception handling etc.)
