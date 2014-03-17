Name:    spawn-fcgi
Version: 1.6.3
Release: 1
Summary: Simple program for spawning FastCGI processes
License: BSD
Group:   System/Servers
URL:     http://redmine.lighttpd.net/projects/spawn-fcgi/
Source0: http://www.lighttpd.net/download/spawn-fcgi-%{version}.tar.bz2

%description
This package contains the spawn-fcgi program used for spawning FastCGI
processes, which can be local or remote.

%prep
%setup -q

%build
%configure2_5x
%make

%install
%makeinstall_std

%files
%doc AUTHORS COPYING NEWS README
%{_bindir}/spawn-fcgi
%{_mandir}/man1/spawn-fcgi.1*
