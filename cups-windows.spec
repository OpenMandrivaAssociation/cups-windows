%define name    cups-windows
%define version 6.0
%define release %mkrel 2

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
cp %{source1} %{buildroot}%{_docdir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%_datadir/cups/drivers
%{_docdir}/%{name}
