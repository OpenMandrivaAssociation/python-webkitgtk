%define oname pywebkitgtk

%if %{_use_internal_dependency_generator}
%define __noautoreq 'pkgconfig\(.*\)'
%else
%define _requires_exceptions pkgconfig\(.*\)
%endif

Summary:	Python bindings for WebKitGtk
Name:		python-webkitgtk
Version:	1.1.8
Release:	5
License:	LGPLv2+
Group:		Development/Python
URL:		http://code.google.com/p/pywebkitgtk/
Source0:	http://pywebkitgtk.googlecode.com/files/%{oname}-%{version}.tar.bz2
Source1:	python-webkitgtk.rpmlintrc
BuildRequires:	webkitgtk-devel
BuildRequires:	pygtk2.0-devel
BuildRequires: 	python
Provides:	%{oname} = %{version}-%{release}

%description
PyWebKitGtk provides an API for developers to program WebKit/Gtk using
Python.

%prep
%setup -q -n %{oname}-%{version}

%build
%configure2_5x
%make LIBS="`python-config --libs`"

%install
%makeinstall_std LIBS="`python-config --libs`"

%files
%doc AUTHORS MAINTAINERS NEWS README
%{py_platsitedir}/webkit/*.py
%{py_platsitedir}/webkit/webkit.*
%{_datadir}/pywebkitgtk/defs/webkit-*.defs
%{_libdir}/pkgconfig/*.pc


%changelog
* Mon Jun 20 2011 Funda Wang <fwang@mandriva.org> 1.1.8-2mdv2011.0
+ Revision: 686117
- rebuild for new webkit

* Sun Apr 10 2011 Funda Wang <fwang@mandriva.org> 1.1.8-1
+ Revision: 652201
- new version 1.1.8

* Sat Apr 09 2011 Funda Wang <fwang@mandriva.org> 1.1.7-3
+ Revision: 652109
- link with libpython

* Sun Oct 31 2010 John Balcaen <mikala@mandriva.org> 1.1.7-2mdv2011.0
+ Revision: 590927
- Rebuild for python 2.7
- Add BR for python
- Remove %%py_requires macro

* Wed Dec 30 2009 Frederik Himpe <fhimpe@mandriva.org> 1.1.7-1mdv2010.1
+ Revision: 483945
- Update to new version 1.1.7

* Thu Jul 09 2009 Frederik Himpe <fhimpe@mandriva.org> 1.1.5-1mdv2010.0
+ Revision: 394016
- Update to new version 1.1.5
- Remove build fix integrated upstream

* Thu Mar 12 2009 Frederik Himpe <fhimpe@mandriva.org> 1.0.2-2mdv2009.1
+ Revision: 354409
- Rebuild for new webkit major

* Fri Dec 26 2008 Adam Williamson <awilliamson@mandriva.org> 1.0.2-1mdv2009.1
+ Revision: 319497
- add build.patch: fix build (from upstream SVN)
- rebuild with python 2.6
- new release 1.0.2

  + Funda Wang <fwang@mandriva.org>
    - rebuild for new python

* Fri Aug 22 2008 Adam Williamson <awilliamson@mandriva.org> 1.0.1-1mdv2009.0
+ Revision: 275141
- br pygtk2.0-devel
- add python requires / br
- import python-webkitgtk


