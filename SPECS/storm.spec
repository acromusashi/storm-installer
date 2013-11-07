Name: storm	
Version: 0.8.2
Release: 1%{?dist}
Summary: Storm Complex Event Processing	
Group: Applications/Internet
License: EPLv1
URL: http://storm-project.net
Source: https://dl.dropbox.com/u/133901206/storm-%{version}.zip
BuildRoot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
Requires: jzmq 
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
%{__mkdir_p} %{buildroot}/opt/storm-%{version}
%{__mkdir_p} %{buildroot}/var/opt/storm
%{__cp} -R * %{buildroot}/opt/storm-%{version}/
%{__ln_s} /opt/storm-%{version} %{buildroot}/opt/storm

# Form a list of files for the files directive
echo $(cd %{buildroot} && find . -type f | cut -c 2-) | tr ' ' '\n' > files.txt
# Grab the symlinks too
echo $(cd %{buildroot} && find . -type l | cut -c 2-) | tr ' ' '\n' >> files.txt

%clean
[ "%{buildroot}" != "/" ] && %{__rm} -rf %{buildroot}

%files -f files.txt
%defattr(-,root,root,-)

%changelog
* Thu Feb 07 2013 Acroquest Technology
- Storm-0.8.2 Packaging

* Tue Oct 14 2012 Acroquest Technology
- Initial Packaging

