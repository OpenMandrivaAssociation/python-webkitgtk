%define oname	pywebkitgtk

Summary:	Python bindings for WebKitGtk
Name:		python-webkitgtk
Version:	1.1.7
Release:	%mkrel 2
Source0:	http://pywebkitgtk.googlecode.com/files/%{oname}-%{version}.tar.bz2
License:	LGPLv2+
Group:		Development/Python
URL:		http://code.google.com/p/pywebkitgtk/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	webkitgtk-devel
BuildRequires:	pygtk2.0-devel
BuildRequires:  python

Provides:	%{oname} = %{version}-%{release}

%description
PyWebKitGtk provides an API for developers to program WebKit/Gtk using
Python.

%prep
%setup -q -n %{oname}-%{version}

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc AUTHORS MAINTAINERS NEWS README
%{py_platsitedir}/webkit/*.py
%{py_platsitedir}/webkit/webkit.*
%{_datadir}/pywebkitgtk/defs/webkit-*.defs

