.. image:: header1.png

=============
Configuration
=============

Basic steps in configuration involves in following categories

Environment variables
---------------------

As to run the main application different applications are associated with it. So, every applications
path should be defined in the system environment

Including system variables in the windows
+++++++++++++++++++++++++++++++++++++++++

1. Path name:- PATH

2. Variable value:- C:\Python26\Scripts;C:\Python26;C:\Program Files\ClustalW2

.. image:: _static/path.jpg


Apache setting
--------------

.. note::
   Make sure that your Apache server is running if you want to run the application with localhost.

Including CGI mode in the apache server
+++++++++++++++++++++++++++++++++++++++

**httpd.conf**

Apache httpd.conf contains all the configurations for the Apache server, so to run our application
we need to add some lines of codes in httpd.conf file. Addition of lines of codes are given below in
a precise way. Please dont forget to add this lines so python CGI mode will be active.



1. Options Indexes FollowSymLinks (default)

   1.1. Options Indexes FollowSymLinks ExecCGI (After adding)

We are using python script on the web server so we need to add handler so apache server can

process python script (.py) in the browser

2. AddHandler cgi-script .cgi (default)

   2.1. AddHandler cgi-script .cgi .py(after adding handler)