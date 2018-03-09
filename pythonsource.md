Compiling python from source with gcc on linux

First, some optional components of python will only build if certain other packages have been installed, so install these first:

$ sudo yum install zlib-devel bzip2-devel openssl-devel ncurses-devel sqlite-devel readline-devel tk-devel gbdm-devel db4-devel libpcap-devel xz-devel

We will install to /usr/local. To avoid adding this to the LD_LIBRARY_PATH, we will pass some extra flags to the compiler:

$ ./configure --prefix=/usr/local --enable-shared LDFLAGS="-Wl,-rpath /usr/local/lib"

To more easily allow multiple different versions of python to live side-by-side in peace, use the nifty --altinstall option:

$ make
$ sudo make altinstall

Depending on the state of umask, certain permissions will need to be relaxed:

$ sudo chmod -R a+rx /usr/local/lib/python3.6/site-packages/setuptools-28.8.0.dist-info/
$ sudo chmod -R a+rx /usr/local/lib/python3.6/site-packages/pip
$ sudo chmod -R a+rx /usr/local/lib/python3.6/lib2to3/Grammar3*
$ sudo chmod -R a+rx /usr/local/lib/python3.6/lib2to3/PatternGrammar3*

You may wish to customize the system /etc/pip.conf, and user ~/.pip.conf files as well.
