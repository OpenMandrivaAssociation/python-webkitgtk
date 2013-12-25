%define oname pywebkitgtk

%if %{_use_internal_dependency_generator}
%define __noautoreq 'pkgconfig\\(.*\\)'
%else
%define _requires_exceptions pkgconfig\(.*\)
%endif

Summary:	Python bindings for WebKitGtk
Name:		python-webkitgtk
Version:	1.1.8
Release:	10
License:	LGPLv2+
Group:		Development/Python
Url:		http://code.google.com/p/pywebkitgtk/
Source0:	http://pywebkitgtk.googlecode.com/files/%{oname}-%{version}.tar.bz2
Patch0:		web_view_get_title.patch
BuildRequires:	pkgconfig(libxslt)
BuildRequires:	pkgconfig(pygtk-2.0)
BuildRequires:	pkgconfig(webkit-1.0)
BuildRequires:	python
Provides:	%{oname} = %{EVRD}

%description
PyWebKitGtk provides an API for developers to program WebKit/Gtk using Python.

%files
%doc AUTHORS MAINTAINERS NEWS README
%{py_platsitedir}/webkit/*.py
%{py_platsitedir}/webkit/webkit.*
%{_datadir}/pywebkitgtk/defs/webkit-*.defs
%{_libdir}/pkgconfig/*.pc

#----------------------------------------------------------------------------

%prep
%setup -qn %{oname}-%{version}
%patch0 -p1

%build
%configure2_5x
%make LIBS="`python-config --libs`"

%install
%makeinstall_std LIBS="`python-config --libs`"

