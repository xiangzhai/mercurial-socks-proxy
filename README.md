This is a small extension for the Mercurial DVCS to enable the use of a SOCKS5
 proxy. To use it, download the file and put something like this in your hgrc
 file:

```
[extensions]
socks_proxy = /path/to/socks_proxy.py

[socks_proxy]
host = localhost:1080
```

You'll also need to install socks.py from the [PySocks](https://github.com/Anorov/PySocks)
 project, which is used for the actual SOCKS protocol.
