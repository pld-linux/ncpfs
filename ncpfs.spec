Summary:	Support Utilities for ncpfs, the free netware client for Linux.
Summary(de):	Support-Dienstprogramme für ncpfs, den kostenlosen Netware-Client
Summary(fr):	Gestionnaires pour ncpfs, le client Netware libre pour Linux.
Summary(tr):	Linux için Netware istemcisi destek yazýlýmlarý
Summary(pl):	Darmowy klient Netware dla Linuxa wraz z dodatkowymi programami
Name:		ncpfs
Version:	2.2.0.18
Release:	1
License:	GPL
Source0:	ftp://platan.vc.cvut.cz/pub/linux/%{name}/%{name}-%{version}/%name-%version.tgz
Source1:	%{name}.init
Patch0:		%{name}-lang.patch
Patch1:		%{name}-largekeys.patch.gz
Patch2:		%{name}-DESTDIR.patch
Group:		Networking/Utilities
Group(pl):	Sieciowe/Narzêdzia
Requires:	%name-ipxutils
Requires:	pam
BuildRequires:	glibc-devel
BuildRequires:	gettext-devel
Prereq:		/sbin/chkconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sbindir	/sbin

%description
This package contains tools to help configure and use the ncpfs
filesysten, which is a linux filesystem which understands the NCP
protocol. This protocol is used by Novell NetWare clients use to talk
to NetWare servers.

INFO: Recompoile this package if ANY changes in kernel was made.

%description -l de
Dieses Paket enthält Tools zum Konfigurieren und Einsatz des
ncpfs-Dateisystems, einem Linux-Dateisystem, das das NCP-Protokoll
versteht. Dieses Protokoll wird von Novell NetWare-Clients zur
Kommunikation mit NetWare-Servern verwendet.

%description -l fr
Ce package contient des outils pour aider a configuer et à utiliser le
système de fichiers ncpfs, qui est un système de fichiers Linux adapté
au protocole NCP. Ce protocole est utilisé par les clients Novell
NetWare pour communiquer avec les serveurs NetWare.

%description -l pl
Pakiet zawiera narzêdzia pomocne w konfigurowaniu i u¿ywaniu systemu
plików ncpfs. Dziêki ncpfs mo¿liwe jest pod³±czanie wolumenów serwerów
Netware i modyfikowanie ich zawarto¶ci.

%description -l tr
Bu paket Linux'un Novell'in NCP protokolunu kullanabilmesi için
gereken yardýmcý yazýlýmlarý içermektedir.

%package ipxutils
Summary:	Utilities for IPX configuration
Summary(de):	Utilities für IPX-Konfiguration 
Summary(fr):	Utilitaires pour la configuration IPX
Summary(pl):	Narzêdzia do konfigurowania IPX
Summary(tr):	IPX yapýlandýrma yazýlýmlarý
Group:		Networking/Utilities
Group(pl):	Sieciowe/Narzêdzia
Version:	1.0
Release:	%{release}

%description ipxutils
This package includes utilities necessary for configuring and
debugging IPX interfaces and networks under Linux. IPX is the
low-level protocol used by NetWare to transfer data.

%description -l de ipxutils
Dieses Paket enthält Dienstprogramme zum Konfigurieren und Debuggen
von IPX-Schnittstellen und -Netzwerken unter Linux. IPX ist das von
NetWare zur Datenübertragung verwendete Low-Level-Protokoll.

%description -l fr ipxutils
Ce package contient les utilitaires nécessires à pour la configuration
et le déboggage des réseaux et interfaces IPX sous Linux. IPX est un
protocole de bas niveau utilisé par NetWare pour transférer des
données.

%description -l pl ipxutils
Pakiet zawiera narzêdzia niezbêdne do konfigurowania interfejsów i
sieci IPX pod Linuxem. Protoko³u IPX u¿ywa Netware do przesy³ania
danych.

%description -l tr ipxutils
Bu paket NetWare tarafýndan kullanýlan IPX protokolünü yapýlandýrmak
ve hatalarýný ayýklamak için kullanýlabilecek bir dizi uygulama
içermektedir.

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

# install ncpfs init scripts
install %{SOURCE1} $RPM_BUILD_ROOT/etc/rc.d/init.d/ncpfs

gzip -9nf BUGS Changes FAQ README* ncpfs-* \
	$RPM_BUILD_ROOT%{_mandir}/man[158]/*

%find_lang ncpfs

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/ldconfig
/sbin/chkconfig --add xntpd

if [ -f /var/lock/subsystem/ncpfs ]; then
	/etc/rc.d/init.d/ncpfs restart >&2
else
	echo "Run \"/etc/rc.d/init.d/ncpfs start\" to start ncpfs daemon."
fi
    
%preun
if [ "$1" = "0" ]; then
	/sbin/chkconfig --del ncpfs
	/etc/rc.d/init.d/ncpfs stop >&2
fi

%postun -p /sbin/ldconfig

%files -f ncpfs.lang
%defattr(644,root,root,755)
%doc BUGS.gz Changes.gz FAQ.gz README*.gz ncpfs-*.gz 
%attr(755,root,root) %{_bindir}/[^i]*
%attr(755,root,root) %{_sbindir}/*
%attr(755,root,root) %{_libdir}/libncp.so*
%attr(755,root,root) /lib/security/pam_ncp_auth.so
%attr(755,root,root) /etc/rc.d/init.d/ncpfs

%{_mandir}/man8/[^i]*
%{_mandir}/man1/*
%{_mandir}/man5/*

%files ipxutils
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ipx*
%{_mandir}/man8/ipx*
