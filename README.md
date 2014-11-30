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
  http://www.cloudera.com/content/cloudera/en/documentation/core/latest/topics/installation_installation.html  
  http://archive-primary.cloudera.com/cdh5/redhat/6/x86_64/cdh/5.2.0/RPMS/x86_64/  

  or below url(in Japanese)  
  http://d.hatena.ne.jp/acro-engineer/20111123/1322059295  


## Installing storm package

1.Unzip downloaded zip archive.  
  https://github.com/acromusashi/storm-installer/wiki/Download  

2.Install the Storm RPM:
```
# su -
# rpm -ivh apache-storm-0.9.3-1.el6.x86_64.rpm  
# rpm -ivh apache-storm-service-0.9.3-1.el6.x86_64.rpm  
```

3.Set the zookeeper host and nimbus host to below property.  
  (Reference: http://nathanmarz.github.com/storm/doc/backtype/storm/Config.html )  
* storm.zookeeper.servers (STORM_ZOOKEEPER_SERVERS)  
* nimbus.host             (NIMBUS_HOST)  

```
# vi /opt/storm/conf/storm.yaml
```

Setting Example:
```
########### These MUST be filled in for a storm configuration
storm.zookeeper.servers:
    - "192.168.100.101"         ## zookeeper host

nimbus.host: "192.168.100.101"  ## nimbus host
```

4.Start or stop storm cluster by following commands:

Start
```
# service storm-nimbus start  
# service storm-ui start  
# service storm-drpc start  
# service storm-logviewer start  
# service storm-supervisor start  
```

Stop
```
# service storm-supervisor stop  
# service storm-logviewer stop  
# service storm-drpc stop  
# service storm-ui stop  
# service storm-nimbus stop  
```


## Caution
In case this installer uses, worker's log name becomes below format.  
```
[TopologyID]worker-[port].log
```

So, Storm-UI Component summary screen's port link is distabled.   
If you want to use port link, execute below command and modify log setting.
```
# vi /opt/storm/logback/cluster.xml
```

storm-installer initial:
```
<configuration scan="true" scanPeriod="60 seconds">
 <appender name="A1" class="ch.qos.logback.core.rolling.RollingFileAppender">
    <file>${storm.home}/logs/${storm.id:-}${logfile.name}</file>
    <rollingPolicy class="ch.qos.logback.core.rolling.FixedWindowRollingPolicy">
      <fileNamePattern>${storm.home}/logs/${storm.id:-}${logfile.name}.%i</fileNamePattern>
      <minIndex>1</minIndex>
      <maxIndex>9</maxIndex>
    </rollingPolicy>
```

modify after:
```
<configuration scan="true" scanPeriod="60 seconds">
 <appender name="A1" class="ch.qos.logback.core.rolling.RollingFileAppender">
    <file>${storm.home}/logs/${logfile.name}</file>
    <rollingPolicy class="ch.qos.logback.core.rolling.FixedWindowRollingPolicy">
      <fileNamePattern>${storm.home}/logs/${logfile.name}.%i</fileNamePattern>
      <minIndex>1</minIndex>
      <maxIndex>9</maxIndex>
    </rollingPolicy>
```


## Dependency libraries

Project    : Storm  
Version    : 0.9.2-incubating  
Lisence    : Apache License Version 2.0  
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
This software is released under the MIT License, see LICENSE.txt.

