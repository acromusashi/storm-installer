Name: apache-storm-service
Version: 0.9.4
Release: 1%{?dist}
Summary: Storm Complex Event Processing	Daemon Package
Group: Applications/Internet
License: Apache License Version 2.0
Source: https://github.com/acromusashi/storm-installer/apache-storm-service-0.9.4.tgz
URL: https://storm.apache.org/
BuildRoot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
Requires: apache-storm
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
%{__mkdir_p} %{buildroot}%{_sysconfdir}/sysconfig
%{__mkdir_p} %{buildroot}%{_initddir}/
%{__mkdir_p} %{buildroot}%{_localstatedir}/run/storm

%{__cp} init.d/* %{buildroot}%{_initddir}/
%{__chmod} +x  %{buildroot}%{_initddir}/*
%{__cp} sysconfig/storm %{buildroot}%{_sysconfdir}/sysconfig/storm

%files 
%defattr(-,root,root,-)
%{_sysconfdir}/sysconfig/storm
%{_initddir}/storm-drpc
%{_initddir}/storm-logviewer
%{_initddir}/storm-nimbus
%{_initddir}/storm-supervisor
%{_initddir}/storm-ui
%defattr(-,storm,storm,-)
/var/run/storm

%clean
[ "%{buildroot}" != "/" ] && %{__rm} -rf %{buildroot}

%preun
if [ "$1" = "0" ]; then
    /sbin/service storm-ui stop
    /sbin/service storm-nimbus stop
    /sbin/service storm-supervisor stop
    /sbin/service storm-drpc stop
    /sbin/service storm-logviewer stop
    /sbin/chkconfig storm-ui off
    /sbin/chkconfig storm-nimbus off
    /sbin/chkconfig storm-supervisor off
    /sbin/chkconfig storm-drpc off
    /sbin/chkconfig storm-logviewer off
fi
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

* Tue Mar 12 2013 spudone
- Fixed to run Storm under a non-root account
- Fixed uninstall cleanup

* Thu Feb 07 2013 Acroquest Technology
- Storm-0.8.2 Packaging

* Tue Oct 26 2012 Acroquest Technology
- Initial Packaging


