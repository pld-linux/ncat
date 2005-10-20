#
#   TODO:
#	- compres docs/readme but not scripts
#	- add pl desc
#
Summary:	A networking utility which read and write data across a network.
Summary(pl):	Narzêdzie sieciowe do przesy³ania danych
Name:		ncat
Version:	0.10rc1
Release:	0.2
Epoch:		0
License:	GPLv2 with OpenSSL exception
#Vendor:	-
Group:		Applications
#Icon:		-
Source0:	http://surfnet.dl.sourceforge.net/sourceforge/nmap-ncat/%{name}-%{version}.tar.gz
# Source0-md5:	b2624656247db958d1ebb4bbedf4dbd3
URL:		http://sourceforge.net/projects/nmap-ncat/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Ncat is a reimplementation of the Netcat family. Ncat is a subset of
features from the original Netcat but with a complete overhaul. New
features and a combination of the Netcat families features (IPv6
support, SSL support, etc) The port scanning support has been entirely
removed from Ncat.

Under the hood of Ncat, there is IPv4, IPv6 support as well as support
for TCP and UDP in both listen and connect modes. There is also SSL
support for both listen and connect operations too. As well as a new
"Connection Brokering" feature. This enables two (or more.) hosts to
connect that perhaps previously were unable to directly connect to
each other.

%prep
%setup -q

%build
cd nbase
%configure
cd ../nsock/src
%configure
cd ../..

%{__make} -C nbase
%{__make} -C nsock/src
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}
install -d $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
install -d $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}/examples
install -d $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}/examples/logs
install -d $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}/examples/scripts
install -d $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}/examples/scripts/http-scan
install -d $RPM_BUILD_ROOT%{_mandir}
install -d $RPM_BUILD_ROOT%{_mandir}/man1

install ncat $RPM_BUILD_ROOT%{_bindir}
install docs/{AUTHORS,BUGS,CHANGES,HTTP-PROXY,README,TODO} $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
install docs/examples/{ipaccess,README} $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}/examples
install docs/examples/logs/{ascii-output,hex-output} $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}/examples/logs
install docs/examples/scripts/{http-proxy,README} $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}/examples/scripts
install docs/examples/scripts/http-scan/* $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}/examples/scripts/http-scan
install docs/man/* $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
#%doc docs/{AUTHORS,BUGS,CHANGES,HTTP-PROXY,README,TODO}
%docdir %{_docdir}/%{name}-%{version}
%docdir %{_docdir}/%{name}-%{version}/examples
%docdir %{_docdir}/%{name}-%{version}/examples/logs
%docdir %{_docdir}/%{name}-%{version}/examples/scripts
%docdir %{_docdir}/%{name}-%{version}/examples/scripts/http-scan

%attr(755,root,root) %{_bindir}/*
%{_docdir}/%{name}-%{version}/*
%{_mandir}/man1/*
