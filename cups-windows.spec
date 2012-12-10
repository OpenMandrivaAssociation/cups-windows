%define name    cups-windows
%define version 6.0
%define release %mkrel 4

Name: %{name}
Version: %{version}
Release: %{release}
Summary: Common UNIX Printing System
License: GPL
Group: System/Printing
Source0: %{name}-%{version}-source.tar.bz2
Source1: README.urpmi
Url: http://www.cups.org/windows/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Requires: cups

%description
The Common UNIX Printing System provides a portable printing
layer for UNIX® operating systems. This is the Windows driver
support package for use with Samba.

%prep
%setup

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/%_datadir/cups/drivers
mkdir -p %{buildroot}%{_docdir}/%{name}

cp i386/* %{buildroot}/%_datadir/cups/drivers
cp LICENSE.txt README.txt %{buildroot}%{_docdir}/%{name}
cp %{SOURCE1} %{buildroot}%{_docdir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%_datadir/cups/drivers
%{_docdir}/%{name}


%changelog
* Thu Dec 09 2010 Oden Eriksson <oeriksson@mandriva.com> 6.0-4mdv2011.0
+ Revision: 617481
- the mass rebuild of 2010.0 packages

* Thu Sep 10 2009 Thierry Vignaud <tv@mandriva.org> 6.0-3mdv2010.0
+ Revision: 437166
- rebuild

* Mon Mar 09 2009 Anne Nicolas <ennael@mandriva.org> 6.0-2mdv2009.1
+ Revision: 353201
- Add README.urpmi

* Thu Feb 26 2009 Anne Nicolas <ennael@mandriva.org> 6.0-1mdv2009.1
+ Revision: 345350
- import cups-windows


