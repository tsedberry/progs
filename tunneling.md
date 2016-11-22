# SSH Tunneling

For this example, suppose we have a local machine, and a remote server.
The user has full access to the local machine, but only ssh access to
the remove server (e.g. port 22 is open on the remove server, and sshd
is installed and running).

Suppose there is a service on the remove server that broadcasts
information on a specific port. For this exmaple, we will assume port
8000.

You want access to the information being broadcast on the remove server
on port 8000, on your local machine.

The following command will forward any requests made on your local
machine for port 8000 to the remove server port 7777.
```
ssh -L 8000:127.0.0.1:7777 username@servername
```

Now, whenever I try and access port 8000 on my local machine ssh forwards
that request to port 7777 on the remove machine.

# A More Concrete Example

My local machine, azeroth, is a desktop running Ubuntu. I also have a
raspberry pi, outland, running debian. Both machines are connected via
a router/switch.

I have a django website on my raspberry pi, and I want to serve the
project locally on the respberry pi using the django test server and
view the site on my desktop using firefox.

On the raspberry pi, I run
```
<outland> python3 manage.py runserver
```

On my desktop, I run
```
<azeroth> ssh -L 7777:127.0.0.1:8000 thrall@outland
```

Then, on my desktop, I point my firefox browser to:
```
localhost:7777
```
