Name: storm-service
Version: 0.8.2
Release: 1%{?dist}
Summary: Storm Complex Event Processing	Daemon Package
Group: Applications/Internet
License: EPLv1
URL: http://storm-project.net
Source: https://github.com/acromusashi/storm-install/storm-service-%{version}.tgz
BuildRoot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
Requires: storm
%description
Storm is a distributed realtime computation system. 
Similar to how Hadoop provides a set of general primitives for doing batch processing, 
Storm provides a set of general primitives for doing realtime computation. Storm is simple, 
can be used with any programming language, is used by many companies, and is a lot of fun to use!

The Rationale page on the wiki explains what Storm is and why it was built.
This presentation is also a good introduction to the project.

Storm has a website at storm-project.net.

%prep
%setup -q

# This SPEC build is Only Packaging.
%build

%install
# Clean out any previous builds not on slash (lol)
[ "%{buildroot}" != "/" ] && %{__rm} -rf %{buildroot}

# Copy the storm file to the right places
%{__mkdir_p} %{buildroot}/etc/sysconfig
%{__mkdir_p} %{buildroot}/etc/init.d
%{__mkdir_p} %{buildroot}/var/log/storm

%{__mv} init.d/storm-nimbus init.d/storm-supervisor init.d/storm-ui init.d/storm-drpc %{buildroot}/etc/init.d
%{__mv} sysconfig/storm %{buildroot}/etc/sysconfig/storm


# Form a list of files for the files directive
echo $(cd %{buildroot} && find . -type f | cut -c 2-) | tr ' ' '\n' > files.txt
# Grab the symlinks too
echo $(cd %{buildroot} && find . -type l | cut -c 2-) | tr ' ' '\n' >> files.txt

%clean
[ "%{buildroot}" != "/" ] && %{__rm} -rf %{buildroot}

%files -f files.txt
%defattr(-,root,root,-)
%attr (755, root, root) %{_sysconfdir}/init.d/storm-*

%preun
if [ "$1" = "0" ]; then
    /sbin/service storm-ui stop
    /sbin/service storm-nimbus stop
    /sbin/service storm-supervisor stop
    /sbin/chkconfig storm-ui off
    /sbin/chkconfig storm-nimbus off
    /sbin/chkconfig storm-supervisor off
fi
exit 0

%changelog
* Thu Feb 07 2013 Acroquest Technology
- Storm-0.8.2 Packaging

* Tue Oct 26 2012 Acroquest Technology
- Initial Packaging


