# Storm-Installer

本パッケージはStormクラスタを簡易に構築可能とするインストーラパッケージ群です。

## 対象環境

* OS: CentOS 6.X
* CPU Arch: x64
* Middleware: Needs JDK6 or after（Oracle JDK or Open JDK）


## 前提環境

Stormクラスタを動作させる際、
ZooKeeperクラスタを構築しておく必要があります。

ZooKeeperのインストールにあたっては
cdhのZooKeeperパッケージを用いるか、下記のページを参照ください。  
  ■cdh  
  http://www.cloudera.com/content/cloudera/en/documentation/core/latest/topics/installation_installation.html  
  http://archive-primary.cloudera.com/cdh5/redhat/6/x86_64/cdh/5.2.0/RPMS/x86_64/  

  ■Taste of Tech Topics Twitter Stormをインストールしてみます！  
  http://d.hatena.ne.jp/acro-engineer/20111123/1322059295  


## 利用手順

1.ダウンロードしたZipアーカイブを展開します。  
  https://github.com/acromusashi/storm-installer/wiki/Download 

2.StormのRPMをインストールします。
```
# su -
# rpm -ivh apache-storm-0.9.3-1.el6.x86_64.rpm  
# rpm -ivh apache-storm-service-0.9.3-1.el6.x86_64.rpm  
```

3.設定ファイルにzookeeper hostとnimbus hostを設定します。  
  (参照: http://nathanmarz.github.com/storm/doc/backtype/storm/Config.html )  
* storm.zookeeper.servers (STORM_ZOOKEEPER_SERVERS)  
* nimbus.host             (NIMBUS_HOST)  

```
# vi /opt/storm/conf/storm.yaml
```

設定例:
```
########### These MUST be filled in for a storm configuration
storm.zookeeper.servers:
    - "192.168.100.101"         ## zookeeper host

nimbus.host: "192.168.100.101"  ## nimbus host
```


4.下記コマンドでStormの起動/停止が可能となります。

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

## 注意点
本インストーラを使用した場合、Workerのログ名称は下記の形式となります。  
```
[TopologyID]-worker-[port].log
```

そのため、Storm-UI 「Component summary」画面のPortリンクは使用できません。  
使用したい場合は下記のコマンドを実行し、log出力定義を修正してください。  
```
# vi /opt/storm/logback/cluster.xml
```

修正前:
```
<configuration scan="true" scanPeriod="60 seconds">
 <appender name="A1" class="ch.qos.logback.core.rolling.RollingFileAppender">
    <file>${storm.log.dir}/${storm.id:-storm}-${logfile.name}</file>
    <rollingPolicy class="ch.qos.logback.core.rolling.FixedWindowRollingPolicy">
      <fileNamePattern>${storm.log.dir}/${storm.id:-storm}-${logfile.name}.%i</fileNamePattern>
      <minIndex>1</minIndex>
      <maxIndex>9</maxIndex>
    </rollingPolicy>
```

modify after:
```
<configuration scan="true" scanPeriod="60 seconds">
 <appender name="A1" class="ch.qos.logback.core.rolling.RollingFileAppender">
    <file>${storm.log.dir}/${logfile.name}</file>
    <rollingPolicy class="ch.qos.logback.core.rolling.FixedWindowRollingPolicy">
      <fileNamePattern>${storm.log.dir}/${logfile.name}.%i</fileNamePattern>
      <minIndex>1</minIndex>
      <maxIndex>9</maxIndex>
    </rollingPolicy>
```


## 配布ライブラリライセンス

名称       : Aache-Storm  
バージョン : 0.9.3  
Lisence    : Apache License Version 2.0  
Source URL : https://storm.apache.org/  


## License
This software is released under the MIT License, see LICENSE.txt.

