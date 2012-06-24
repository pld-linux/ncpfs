Summary:	Support Utilities for ncpfs, the free netware client for Linux.
Summary(de):	Support-Dienstprogramme f�r ncpfs, den kostenlosen Netware-Client
Summary(fr):	Gestionnaires pour ncpfs, le client Netware libre pour Linux.
Summary(tr):	Linux i�in Netware istemcisi destek yaz�l�mlar�
Summary(pl):	Darmowy klient Netware dla Linuxa wraz z dodatkowymi programami
Name:		ncpfs
Version:	2.2.0.18
Release:	4
License:	GPL
Source0:	ftp://platan.vc.cvut.cz/pub/linux/%{name}/%{name}-%{version}/%{name}-%{version}.tgz
Patch0:		%{name}-lang.patch
Patch1:		%{name}-largekeys.patch.gz
Patch2:		%{name}-DESTDIR.patch
Group:		Networking/Utilities
Group(pl):	Sieciowe/Narz�dzia
Requires:	%{name}-ipxutils
BuildRequires:	glibc-devel
BuildRequires:	gettext-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sbindir	/sbin

%description
This package contains tools to help configure and use the ncpfs
filesysten, which is a linux filesystem which understands the NCP
protocol. This protocol is used by Novell NetWare clients use to talk
to NetWare servers.

INFO: Recompoile this package if ANY changes in kernel was made.

%description -l de
Dieses Paket enth�lt Tools zum Konfigurieren und Einsatz des
ncpfs-Dateisystems, einem Linux-Dateisystem, das das NCP-Protokoll
versteht. Dieses Protokoll wird von Novell NetWare-Clients zur
Kommunikation mit NetWare-Servern verwendet.

%description -l fr
Ce package contient des outils pour aider a configuer et � utiliser le
syst�me de fichiers ncpfs, qui est un syst�me de fichiers Linux adapt�
au protocole NCP. Ce protocole est utilis� par les clients Novell
NetWare pour communiquer avec les serveurs NetWare.

%description -l pl
Pakiet zawiera narz�dzia pomocne w konfigurowaniu i u�ywaniu systemu
plik�w ncpfs. Dzi�ki ncpfs mo�liwe jest pod��czanie wolumen�w serwer�w
Netware i modyfikowanie ich zawarto�ci.

%description -l tr
Bu paket Linux'un Novell'in NCP protokolunu kullanabilmesi i�in
gereken yard�mc� yaz�l�mlar� i�ermektedir.

%package -n pam_ncp_auth
Summary:	PAM module for authenticate using using login/password stored on Netware server
Summary(pl):	Narz�dzia do konfigurowania IPX
Group:		Networking/Utilities
Group(pl):	Sieciowe/Narz�dzia
Requires:	%{name} = %{version}

%description -n pam_ncp_auth
The pam_ncp_auth module is PAM module for authenticate using login/password
stored on Netware server.

%package -n ipxutils
Summary:	Utilities for IPX configuration
Summary(de):	Utilities f�r IPX-Konfiguration 
Summary(fr):	Utilitaires pour la configuration IPX
Summary(pl):	Narz�dzia do konfigurowania IPX
Summary(tr):	IPX yap�land�rma yaz�l�mlar�
Group:		Networking/Utilities
Group(pl):	Sieciowe/Narz�dzia
Obsoletes:	ncpfs-ipxutils

%description -n ipxutils
This package includes utilities necessary for configuring and
debugging IPX interfaces and networks under Linux. IPX is the
low-level protocol used by NetWare to transfer data.

%description -l de -n ipxutils
Dieses Paket enth�lt Dienstprogramme zum Konfigurieren und Debuggen
von IPX-Schnittstellen und -Netzwerken unter Linux. IPX ist das von
NetWare zur Daten�bertragung verwendete Low-Level-Protokoll.

%description -l fr -n ipxutils
Ce package contient les utilitaires n�cessires � pour la configuration
et le d�boggage des r�seaux et interfaces IPX sous Linux. IPX est un
protocole de bas niveau utilis� par NetWare pour transf�rer des
donn�es.

%description -l pl -n ipxutils
Pakiet zawiera narz�dzia niezb�dne do konfigurowania interfejs�w i
sieci IPX pod Linuxem. Protoko�u IPX u�ywa Netware do przesy�ania
danych.

%description -l tr -n ipxutils
Bu paket NetWare taraf�ndan kullan�lan IPX protokol�n� yap�land�rmak
ve hatalar�n� ay�klamak i�in kullan�labilecek bir dizi uygulama
i�ermektedir.

%prep
%setup -q
%patch0 -p1
%patch1 -p0
%patch2 -p1

%build
gettextize --copy --force
LDFLAGS="-s"; export LDFLAGS
./conf
%configure \
	--enable-pam \
	--enable-mount-v3 \
	--enable-mount-v2 \
	--enable-nds \
	--enable-udp \
	--enable-ipx \
	--enable-signatures \
	--enable-kernel \
	--enable-reentrant \
	--enable-trace \
	--enable-warnings \
	--enable-nls \
	--disable-versions

%{__make} OPT_FLAGS="$RPM_OPT_FLAGS -w" 
%{__make} -C ipxdump OPT_FLAGS="$RPM_OPT_FLAGS -w"

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT/etc/rc.d/init.d

make install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf BUGS Changes FAQ README* ncpfs-* contrib/pam/README \
	$RPM_BUILD_ROOT%{_mandir}/man[158]/*

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc BUGS.gz Changes.gz FAQ.gz README*.gz ncpfs-*.gz 
%attr(755,root,root) %{_bindir}/[^i]*
%attr(755,root,root) %{_sbindir}/*
%attr(755,root,root) %{_libdir}/libncp.so*

%{_mandir}/man8/[^i]*
%{_mandir}/man1/*
%{_mandir}/man5/*

%files -n pam_ncp_auth
%defattr(644,root,root,755)
%doc contrib/pam/*.gz
%attr(755,root,root) /lib/security/pam_ncp_auth.so

%files -n ipxutils
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ipx*
%{_mandir}/man8/ipx*
