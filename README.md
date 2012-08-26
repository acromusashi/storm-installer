# Storm-Installer

This package is a package group for ease of setting up a storm cluster.


## Environment

* OS: CentOS 6.X
* CPU Arch: x64
* Middleware: Needs JDK6 or after（Oracle JDK or Open JDK）


## Before you install storm package

Before you install Storm Package on a cluster,
there are some important steps you need to do to prepare your system.

1.Storm needs zookeeper cluster.  
  For zookeeper cluster installation, you find install step on cdh.  
  https://ccp.cloudera.com/display/CDH4DOC/CDH4+Installation  
  http://archive.cloudera.com/cdh4/redhat/6/x86_64/cdh/4/RPMS/noarch/  

  or below url(in Japanese)  
  http://d.hatena.ne.jp/acro-engineer/20111123/1322059295  


## Installing storm package

1.Unzip downloaded zip archive.  
  https://github.com/acromusashi/storm-installer/downloads  

2.Install the RPM:
```
sudo rpm -ivh zeromq-2.1.7-1.el6.x86_64.rpm  
sudo rpm -ivh zeromq-devel-2.1.7-1.el6.x86_64.rpm  
sudo rpm -ivh jzmq-2.1.0-1.el6.x86_64.rpm  
sudo rpm -ivh jzmq-devel-2.1.0-1.el6.x86_64.rpm  
sudo rpm -ivh storm-0.8.0-1.el6.x86_64.rpm  
sudo rpm -ivh storm-service-0.8.0-1.el6.x86_64.rpm  
```
3.Set the niubus host and zookeeper host to below property.  
  (Reference: http://nathanmarz.github.com/storm/doc/backtype/storm/Config.html )
*nimbus.host             (NIMBUS_HOST)
*storm.zookeeper.servers (STORM_ZOOKEEPER_SERVERS)
```
sudo vi /opt/storm/conf/storm.yaml
```

4.Start or stop storm cluster by following commands:

Start
```
sudo service storm-nimbus start  
sudo service storm-ui start  
sudo service storm-supervisor start  
```

Stop
```
sudo service storm-nimbus stop  
sudo service storm-ui stop  
sudo service storm-supervisor stop  
```


## Dependency libraries

Project    : Storm  
Version    : 0.8.0  
Lisence    : Eclipse Public License 1.0  
Source URL : http://storm-project.net/  

Project    : ZeroMQ  
Version    : 2.1.7  
Lisence    : LGPLv3  
Source URL : http://www.zeromq.org/  

Project    : JZMQ  
Version    : 2.1.0  
Lisence    : LGPLv3  
Source URL : https://github.com/zeromq/jzmq  


## License

Distributed under the Eclipse Public License.  
http://opensource.org/licenses/eclipse-1.0.php

