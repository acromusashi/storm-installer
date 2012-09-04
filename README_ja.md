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
  https://ccp.cloudera.com/display/CDH4DOC/CDH4+Installation  
  http://archive.cloudera.com/cdh4/redhat/6/x86_64/cdh/4/RPMS/noarch/  

  ■Taste of Tech Topics Twitter Stormをインストールしてみます！  
  http://d.hatena.ne.jp/acro-engineer/20111123/1322059295  


## 利用手順

1.ダウンロードしたZipアーカイブを展開します。  
  https://github.com/acromusashi/storm-installer/downloads  

2.下記の順にRPMファイルをインストールします。
  uuidに対する依存性の欠如によるエラーが発生した場合、
　下記のページからuuid-1.6.1-10.el6.x86_64.rpmをダウンロードして
　インストールを行ってください。
　http://zid-lux1.uibk.ac.at/linux/rpm2html/centos/6/os/x86_64/Packages/uuid-1.6.1-10.el6.x86_64.html
```
> su -
# rpm -ivh zeromq-2.1.7-1.el6.x86_64.rpm  
# rpm -ivh zeromq-devel-2.1.7-1.el6.x86_64.rpm  
# rpm -ivh jzmq-2.1.0-1.el6.x86_64.rpm  
# rpm -ivh jzmq-devel-2.1.0-1.el6.x86_64.rpm  
# rpm -ivh storm-0.8.0-1.el6.x86_64.rpm  
# rpm -ivh storm-service-0.8.0-1.el6.x86_64.rpm  
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
# service storm-supervisor start  
```

Stop
```
# service storm-nimbus stop  
# service storm-ui stop  
# service storm-supervisor stop  
```


## 配布ライブラリライセンス

名称       : Storm  
バージョン : 0.8.0  
Lisence    : Eclipse Public License 1.0  
Source URL : http://storm-project.net/  

名称       : ZeroMQ  
バージョン : 2.1.7  
Lisence    : LGPLv3  
Source URL : http://www.zeromq.org/  

名称       : JZMQ  
バージョン : 2.1.0  
Lisence    : LGPLv3  
Source URL : https://github.com/zeromq/jzmq  


## License

Distributed under the Eclipse Public License.  
http://opensource.org/licenses/eclipse-1.0.php

