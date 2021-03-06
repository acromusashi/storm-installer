Name: apache-storm	
Version: 0.9.4
Release: 1%{?dist}
Summary: Storm Complex Event Processing	
Group: Applications/Internet
License: Apache License Version 2.0
URL: https://storm.apache.org/
Source: http://www.apache.org/dyn/closer.cgi/storm/apache-storm-0.9.4/apache-storm-0.9.4.tar.gz
BuildRoot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
Requires(pre): shadow-utils
%description
Storm is a distributed realtime computation system. 
Similar to how Hadoop provides a set of general primitives for doing batch processing, 
Storm provides a set of general primitives for doing realtime computation. Storm is simple, 
can be used with any programming language, is used by many companies, and is a lot of fun to use!

The Rationale page on the wiki explains what Storm is and why it was built.
This presentation is also a good introduction to the project.

Storm has a website at storm-project.net.

%pre
getent group storm >/dev/null || groupadd -r storm
getent passwd storm >/dev/null || \
    useradd -r -g storm -d /opt/storm -s /sbin/nologin \
    -c "Storm Service" storm
exit 0

%prep
%setup -q

# This SPEC build is Only Packaging.
%build

%install
# Copy the storm file to the right places
%{__mkdir_p} %{buildroot}/opt/storm-%{version}
%{__mkdir_p} %{buildroot}/var/opt/storm
%{__cp} -R * %{buildroot}/opt/storm-%{version}/
%{__ln_s} /opt/storm-%{version} %{buildroot}/opt/storm

#update default config
echo "nimbus.host: \"localhost\"" >> %{buildroot}/opt/storm-%{version}/conf/storm.yaml
echo "" >> %{buildroot}/opt/storm-%{version}/conf/storm.yaml
echo "storm.zookeeper.servers:" >> %{buildroot}/opt/storm-%{version}/conf/storm.yaml
echo "     - \"localhost\"" >> %{buildroot}/opt/storm-%{version}/conf/storm.yaml
echo "" >> %{buildroot}/opt/storm-%{version}/conf/storm.yaml
echo "storm.local.dir: \"/opt/storm\"" >> %{buildroot}/opt/storm-%{version}/conf/storm.yaml

#update logback config
sed -i -e 's/${logfile\.name}/${storm.id:-storm}-${logfile.name}/g' %{buildroot}/opt/storm-%{version}/logback/cluster.xml

# Form a list of files for the files directive
echo $(cd %{buildroot} && find . -type f | cut -c 2-) | tr ' ' '\n' > files.txt
# Grab the symlinks too
echo $(cd %{buildroot} && find . -type l | cut -c 2-) | tr ' ' '\n' >> files.txt

%clean
%{__rm} -rf %{buildroot}/opt/storm-%{version}
%{__rm} %{buildroot}/opt/storm

%files -f files.txt

%defattr(644,storm,storm,755)

%post
chown -R storm:storm /opt/storm-%{version}
chmod -R 755 /opt/storm/bin/*
exit 0

%postun
rm -rf /opt/storm-%{version}
exit 0

%changelog
* Tue Nov 30 2014 Acroquest Technology
- Apache-Storm 0.9.3 Packaging

* Tue Jul 09 2014 Acroquest Technology
- Apache-Storm 0.9.2-incubating Packaging

* Tue Apr 08 2014 Acroquest Technology
- Apache-Storm 0.9.1-incubating Packaging

* Mon Dec 05 2013 Acroquest Technology
- Storm-0.9.0 Packaging

* Mon Dec 02 2013 Acroquest Technology
- Storm-0.9.0-rc3 Packaging

* Mon Nov 11 2013 Acroquest Technology
- Storm-0.9.0-rc2 Packaging

* Tue Mar 16 2013 spudone
- Fixed to run Storm under a non-root account
- Fixed uninstall cleanup

* Thu Feb 07 2013 Acroquest Technology
- Storm-0.8.2 Packaging

* Tue Oct 14 2012 Acroquest Technology
- Initial Packaging


