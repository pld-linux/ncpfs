# TODO:
# - fix/write from scrach -devel Summary and %%description
# - fix -devel Group
Summary:	Support Utilities for ncpfs, the free netware client for Linux.
Summary(de):	Support-Dienstprogramme für ncpfs, den kostenlosen Netware-Client
Summary(fr):	Gestionnaires pour ncpfs, le client Netware libre pour Linux.
Summary(ja):	ncpfs ¥Õ¥¡¥¤¥ë¥·¥¹¥Æ¥à¥æ¡¼¥Æ¥£¥ê¥Æ¥£¡¢Linux ÍÑ NetWare ¥¯¥é¥¤¥¢¥ó¥È¡£
Summary(pl):	Darmowy klient Netware dla Linuxa wraz z dodatkowymi programami
Summary(tr):	Linux için Netware istemcisi destek yazýlýmlarý
Name:		ncpfs
Version:	2.2.0.18
Release:	8.1
License:	GPL
Group:		Networking/Utilities
Source0:	ftp://platan.vc.cvut.cz/pub/linux/ncpfs/%{name}-%{version}/%{name}-%{version}.tgz
Patch0:		%{name}-lang.patch
Patch1:		%{name}-largekeys.patch.gz
Patch2:		%{name}-DESTDIR.patch
Patch3:		ftp://platan.vc.cvut.cz/pub/linux/ncpfs/%{name}-%{version}/ncp-pam-update.diff.gz
Patch4:		%{name}-nwsfind.patch
Patch5:		%{name}-ac.patch
BuildRequires:	glibc-devel
BuildRequires:	gettext-devel
BuildRequires:	pam-devel
Requires:	ipxutils
#Requires:	iconv
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

%description -l ja
ncpfs ¤Ï Novell NetWare(TM) NCP ¤È¤·¤ÆÍý²ò¤µ¤ì¤ë¥Õ¥¡¥¤¥ë¥·¥¹¥Æ¥à¤Ç¤¹¡£
µ¡Ç½Åª¤Ë¤Ï¡¢NCP ¤Ï¡¢NFS ¤¬ TCP/IP ¤ÎÀ¤³¦¤ÇÍÑ¤¤¤é¤ì¤ë¤è¤¦¤Ë¡¢NetWare ¤Ç
ÍÑ¤¤¤é¤ì¤Þ¤¹¡£Linux ¥·¥¹¥Æ¥à¤¬ NetWare
¥Õ¥¡¥¤¥ë¥·¥¹¥Æ¥à¤ò¥Þ¥¦¥ó¥È¤¹¤ë¤Ë¤Ï¡¢
ÆÃÊÌ¤Ê¥Þ¥¦¥ó¥È¥×¥í¥°¥é¥à¤¬É¬Í×¤Ç¤¹¡£ncpfs
¥Ñ¥Ã¥±¡¼¥¸¤Ï¤½¤Î¤è¤¦¤Ê¥Þ¥¦¥ó¥È ¥×¥í¥°¥é¥à¤È¡¢ncpfs
¥Õ¥¡¥¤¥ë¥·¥¹¥Æ¥à¤ÎÀßÄê¤ÈÍøÍÑ¤Î¤¿¤á¤Î¥Ä¡¼¥ë¤ò´Þ¤ß¤Þ¤¹¡£

Novell NetWare ¤Î¥Õ¥¡¥¤¥ë¤«¥µ¡¼¥Ó¥¹¤ò»È¤¦¤¿¤á¤Ë ncpfs
¥Õ¥¡¥¤¥ë¥·¥¹¥Æ¥à¤ò ÍÑ¤¤¤ëÉ¬Í×¤¬¤¢¤ë¤Ê¤é¡¢ncpfs
¥Ñ¥Ã¥±¡¼¥¸¤ò¥¤¥ó¥¹¥È¡¼¥ë¤·¤Þ¤·¤ç¤¦¡£

%description -l pl
Pakiet zawiera narzêdzia pomocne w konfigurowaniu i u¿ywaniu systemu
plików ncpfs. Dziêki ncpfs mo¿liwe jest pod³±czanie wolumenów serwerów
Netware i modyfikowanie ich zawarto¶ci.

%description -l tr
Bu paket Linux'un Novell'in NCP protokolunu kullanabilmesi için
gereken yardýmcý yazýlýmlarý içermektedir.

%package -n pam_ncp_auth
Summary:	PAM module for authenticate using using login/password stored on Netware server
Summary(pl):	Narzêdzia do konfigurowania IPX
Group:		Networking/Utilities
Requires:	%{name} = %{version}

%description -n pam_ncp_auth
The pam_ncp_auth module is PAM module for authenticate using
login/password stored on Netware server.

%package -n ipxutils
Summary:	Utilities for IPX configuration
Summary(de):	Utilities für IPX-Konfiguration
Summary(fr):	Utilitaires pour la configuration IPX
Summary(ja):	IPX ¥¤¥ó¥¿¥Õ¥§¥¤¥¹¤È¥Í¥Ã¥È¥ï¡¼¥¯¤ÎÀßÄê¤È¥Ç¥Ð¥Ã¥°¤Î¤¿¤á¤Î¥Ä¡¼¥ë¡£
Summary(pl):	Narzêdzia do konfigurowania IPX
Summary(tr):	IPX yapýlandýrma yazýlýmlarý
Group:		Networking/Utilities
Obsoletes:	ncpfs-ipxutils

%description -n ipxutils
This package includes utilities necessary for configuring and
debugging IPX interfaces and networks under Linux. IPX is the
low-level protocol used by NetWare to transfer data.

%description -n ipxutils -l de
Dieses Paket enthält Dienstprogramme zum Konfigurieren und Debuggen
von IPX-Schnittstellen und -Netzwerken unter Linux. IPX ist das von
NetWare zur Datenübertragung verwendete Low-Level-Protokoll.

%description -n ipxutils -l fr
Ce package contient les utilitaires nécessires à pour la configuration
et le déboggage des réseaux et interfaces IPX sous Linux. IPX est un
protocole de bas niveau utilisé par NetWare pour transférer des
données.

%description -n ipxutils -l ja
ipxutils ¥Ñ¥Ã¥±¡¼¥¸¤Ï¡¢Linux ¤Ç IPX
¥¤¥ó¥¿¥Õ¥§¥¤¥¹¤È¥Í¥Ã¥È¥ï¡¼¥¯¤ÎÀßÄê¤È
¥Ç¥Ð¥Ã¥°¤ò¤¹¤ë¤¿¤á¤Î¥æ¡¼¥Æ¥£¥ê¥Æ¥£¤ò´Þ¤ß¤Þ¤¹¡£IPX ¤Ï Novell NetWare ¤Î
¥Õ¥¡¥¤¥ë¥·¥¹¥Æ¥à¤Ç¥Ç¡¼¥¿¤òÅ¾Á÷¤¹¤ë¤Î¤ËÍÑ¤¤¤é¤ì¤ëÄã¥ì¥ô¥§¥ë¥×¥í¥È¥³¥ë¤Ç¤¹¡£

¥Í¥Ã¥È¥ï¡¼¥¯¤Ç IPX ÀßÄê¤ò¤¹¤ëÉ¬Í×¤¬¤¢¤ì¤Ð¡¢ipxutils
¤ò¥¤¥ó¥¹¥È¡¼¥ë¤·¤Þ¤·¤ç¤¦¡£

%description -n ipxutils -l pl
Pakiet zawiera narzêdzia niezbêdne do konfigurowania interfejsów i
sieci IPX pod Linuxem. Protoko³u IPX u¿ywa Netware do przesy³ania
danych.

%description -n ipxutils -l tr
Bu paket NetWare tarafýndan kullanýlan IPX protokolünü yapýlandýrmak
ve hatalarýný ayýklamak için kullanýlabilecek bir dizi uygulama
içermektedir.

%package devel
Summary:	Files for developing NCP-aware software
Group:		-
Requires:	%{name} = %{version}

%description
Files for developing NCP-aware software

%prep
%setup -q
%patch0 -p1
%patch1 -p0
%patch2 -p1
%patch3 -p0
%patch4 -p1
%patch5 -p1

%build
gettextize --copy --force
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

%{__make} OPT_FLAGS="%{rpmcflags} -w"
%{__make} -C ipxdump OPT_FLAGS="%{rpmcflags} -w"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{/etc/rc.d/init.d,%{_includedir}}

%{__make} install DESTDIR=$RPM_BUILD_ROOT

install lib/libncp.so $RPM_BUILD_ROOT%{_libdir}
cp -a include/ncp $RPM_BUILD_ROOT%{_includedir}

gzip -9nf BUGS Changes FAQ README* ncpfs-* contrib/pam/README

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

%files devel
%defattr(644,root,root,755)
%{_includedir}/ncp
%{_libdir}/libncp.so

%files -n pam_ncp_auth
%defattr(644,root,root,755)
%doc contrib/pam/*.gz
%attr(755,root,root) /lib/security/pam_ncp_auth.so

%files -n ipxutils
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ipx*
%{_mandir}/man8/ipx*
