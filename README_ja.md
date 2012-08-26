======================================================================
Storm-Install                                                       
======================================================================

=====
概 要
=====

本パッケージはStormクラスタを簡易に構築可能とするインストーラパッケージ群です。

========
対象環境
========
OS:  
CentOS 6.X  

CPUアーキテクチャ:  
x64  

ミドルウェア:  
JDK6以降がインストールされていること。  
（Oracle JDK、Open JDKどちらでもOK）  


========
前提環境
========
Stormクラスタを動作させる際、  
ZooKeeperクラスタを構築しておく必要があります。  

ZooKeeperのインストールにあたっては  
cdhのZooKeeperパッケージを用いるか、下記のページを参照ください。  
http://d.hatena.ne.jp/acro-engineer/  


========
利用手順
========
1.ダウンロードしたZipアーカイブを展開します。  

2.下記の順にRPMファイルをインストールします。  
  rpm -ivh zeromq-2.1.7-1.el6.x86_64.rpm  
  rpm -ivh zeromq-devel-2.1.7-1.el6.x86_64.rpm  
  rpm -ivh jzmq-2.1.0-1.el6.x86_64.rpm  
  rpm -ivh jzmq-devel-2.1.0-1.el6.x86_64.rpm  
  rpm -ivh storm-X.X.X-1.el6.x86_64.rpm  

3.下記コマンドでStormの起動/停止が可能となります。  
  Start  
    service storm-nimbus start  
    service storm-ui start  
    service storm-supervisor start  
  Stop  
    service storm-nimbus stop  
    service storm-ui stop  
    service storm-supervisor stop  


========================
配布ライブラリライセンス
========================
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


==========
バージョン
==========
2012/08/24 Version1.0  
