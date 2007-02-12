#
#   TODO:
#	- compres docs/readme but not scripts
#
Summary:	A networking utility which read and write data across a network
Summary(pl.UTF-8):   Narzędzie sieciowe do przesyłania danych
Name:		ncat
%define		_rc	rc3
%define		_rel	1
Version:	0.10
Release:	0.%{_rc}.%{_rel}
Epoch:		1
License:	GPLv2 with OpenSSL exception
#Vendor:	-
Group:		Applications
#Icon:		-
Source0:	http://dl.sourceforge.net/nmap-ncat/%{name}-%{version}%{_rc}.tar.gz
# Source0-md5:	5febca55c280c98ffb17977030a9b919
URL:		http://sourceforge.net/projects/nmap-ncat/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Ncat is a reimplementation of the Netcat family. Ncat is a subset of
features from the original Netcat but with a complete overhaul. New
features and a combination of the Netcat families features (IPv6
support, SSL support, etc). The port scanning support has been
entirely removed from Ncat.

Under the hood of Ncat, there is IPv4, IPv6 support as well as support
for TCP and UDP in both listen and connect modes. There is also SSL
support for both listen and connect operations too. As well as a new
"Connection Brokering" feature. This enables two (or more.) hosts to
connect that perhaps previously were unable to directly connect to
each other.

%description -l pl.UTF-8
Ncat to reimplementacja rodziny Netcat. Ncat jest podzbiorem
możliwości z oryginalnego Netcata, ale w pełni sprawdzonym. Dostępne
są nowe możliwości i połączenie możliwości rodziny Netcat (obsługa
IPv6, obsługa SSL itp.). Obsługa skanowania portów została całkowicie
usunięta z Ncata.

Pod kapturem Ncata kryje się obsługa IPv4 i IPv6, a także obsługa TCP
i UDP zarówno w trybie nasłuchiwania, jak i łączenia. Jest także
obsługa SSL przy operacjach nasłuchiwania i łączenia, a także nowa
opcja "pośredniczenia w połączeniach", pozwalająca połączyć się dwóm
(lub więcej) hostom, które normalnie nie mogły się połączyć
bezpośrednio.

%prep
%setup -q -n %{name}-%{version}%{_rc}

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}
install -d $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}/examples/{logs,scripts/http-scan}
install -d $RPM_BUILD_ROOT%{_mandir}/man1

install ncat $RPM_BUILD_ROOT%{_bindir}
install docs/{AUTHORS,BUGS,HTTP-PROXY,README} $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
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
%{_docdir}/%{name}-%{version}
%{_mandir}/man1/*
