# TODO:
# - fix/write from scrach -devel Summary and %%description
# - fix -devel Group
# - review php-auth_nds Summary and %%description
# - register php module in php.ini like other modules from php.spec (?)
#
# Conditional build:
%bcond_without php	# don't build PHP module
%bcond_without ipx	# don't build ipx utils
#
Summary:	Support Utilities for ncpfs, the free netware client for Linux
Summary(de):	Support-Dienstprogramme für ncpfs, den kostenlosen Netware-Client
Summary(es):	Utilitarios de soporte para ncpfs, que es el cliente Linux free para netware
Summary(fr):	Gestionnaires pour ncpfs, le client Netware libre pour Linux
Summary(ja):	ncpfs ¥Õ¥¡¥¤¥ë¥·¥¹¥Æ¥à¥æ¡¼¥Æ¥£¥ê¥Æ¥£¡¢Linux ÍÑ NetWare ¥¯¥é¥¤¥¢¥ó¥È¡£
Summary(pl):	Darmowy klient Netware dla Linuksa wraz z dodatkowymi programami
Summary(pt_BR):	Utilitários de suporte para ncpfs, que é o cliente Linux free para netware
Summary(ru):	õÔÉÌÉÔÙ ÄÌÑ ÆÁÊÌÏ×ÏÊ ÓÉÓÔÅÍÙ ncpfs, ËÌÉÅÎÔÁ NetWare ÄÌÑ Linux
Summary(tr):	Linux için Netware istemcisi destek yazýlýmlarý
Summary(uk):	õÔÉÌ¦ÔÉ ÄÌÑ ÆÁÊÌÏ×Ï§ ÓÉÓÔÅÍÉ ncpfs, ËÌ¦¤ÎÔÁ NetWare ÄÌÑ Linux
Name:		ncpfs
Version:	2.2.4
Release:	2%{!?with_ipx:noipx}
Epoch:		1
License:	GPL
Group:		Networking/Utilities
Source0:	ftp://platan.vc.cvut.cz/pub/linux/ncpfs/%{name}-%{version}.tar.gz
# Source0-md5:	5fd2ec0680ba7e66df142637e17a5ac9
Patch0:		%{name}-lang.patch
Patch1:		%{name}-nwsfind.patch
Patch2:		%{name}-ac.patch
Patch3:		%{name}-sbindir.patch
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	libtool
BuildRequires:	pam-devel
%{?with_php:BuildRequires:	php-devel}
%{?with_ipx:Requires:	ipxutils}
#Requires:	iconv
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sbindir	/sbin

%description
This package contains tools to help configure and use the ncpfs
filesysten, which is a linux filesystem which understands the NCP
protocol. This protocol is used by Novell NetWare clients use to talk
to NetWare servers.

%description -l de
Dieses Paket enthält Tools zum Konfigurieren und Einsatz des
ncpfs-Dateisystems, einem Linux-Dateisystem, das das NCP-Protokoll
versteht. Dieses Protokoll wird von Novell NetWare-Clients zur
Kommunikation mit NetWare-Servern verwendet.

%description -l es
Este paquete contiene herramientas para ayudar a configurar y usar el
sistema de archivos ncpfs, que es un sistema de archivos Linux capaz
de entender el protocolo NCP. Este es el protocolo que los clientes
Novell NetWare usan para "conversar" con servidores NetWare.

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

%description -l pt_BR
Este pacote contém ferramentas para ajudar a configurar e usar o
sistema de arquivos ncpfs, que é um sistema de arquivos Linux que
entende o protocolo NCP. Esse é o protocolo que os clientes Novell
NetWare usam para "conversar" com servidores NetWare.

%description -l ru
Ncpfs - ÜÔÏ ÆÁÊÌÏ×ÁÑ ÓÉÓÔÅÍÁ ÐÏ×ÅÒÈ ÐÒÏÔÏËÏÌÁ Novell NetWare(TM) NCP.
æÕÎËÃÉÏÎÁÌØÎÏ, NCP ÉÇÒÁÅÔ × NetWare ÔÕ ÖÅ ÒÏÌØ, ÞÔÏ NFS × ÍÉÒÅ TCP/IP.
äÌÑ ÔÏÇÏ, ÞÔÏÂÙ ÓÉÓÔÅÍÁ Linux ÓÍÏÎÔÉÒÏ×ÁÌÁ ÆÁÊÌÏ×ÕÀ ÓÉÓÔÅÍÕ NetWare,
ÅÊ ÎÕÖÎÁ ÓÐÅÃÉÁÌØÎÁÑ ÐÒÏÇÒÁÍÍÁ ÍÏÎÔÉÒÏ×ÁÎÉÑ. ðÁËÅÔ ncpfs ÓÏÄÅÒÖÉÔ
ÔÁËÕÀ ÐÒÏÇÒÁÍÍÕ ÐÌÀÓ ÄÒÕÇÉÅ ÉÎÓÔÒÕÍÅÎÔÙ ÄÌÑ ËÏÎÆÉÇÕÒÉÒÏ×ÁÎÉÑ É
ÉÓÐÏÌØÚÏ×ÁÎÉÑ ÆÁÊÌÏ×ÏÊ ÓÉÓÔÅÍÙ ncpfs.

%description -l tr
Bu paket Linux'un Novell'in NCP protokolunu kullanabilmesi için
gereken yardýmcý yazýlýmlarý içermektedir.

%description -l uk
Ncpfs - ÃÅ ÆÁÊÌÏ×Á ÓÉÓÔÅÍÁ ÐÏ×ÅÒÈ ÐÒÏÔÏËÏÌÕ Novell NetWare(TM) NCP. úÁ
ÆÕÎËÃ¦ÑÍÉ, NCP ×¦Ä¦ÇÒÁ¤ × NetWare ÔÕ Ö ÒÏÌØ, ÝÏ NFS Õ Ó×¦Ô¦ TCP/IP.
äÌÑ ÔÏÇÏ, ÝÏÂ ÓÉÓÔÅÍÁ Linux ÚÍÏÎÔÕ×ÁÌÁ ÆÁÊÌÏ×Õ ÓÉÓÔÅÍÕ NetWare, §Ê
ÐÏÔÒ¦ÂÎÁ ÓÐÅÃ¦ÁÌØÎÁ ÐÒÏÇÒÁÍÁ ÍÏÎÔÕ×ÁÎÎÑ. ðÁËÅÔ ncpfs Í¦ÓÔÉÔØ ÔÁËÕ
ÐÒÏÇÒÁÍÕ ÐÌÀÓ ¦ÎÛ¦ ¦ÎÓÔÒÕÍÅÎÔÉ ÄÌÑ ËÏÎÆ¦ÇÕÒÕ×ÁÎÎÑ ÔÁ ×ÉËÏÒÉÓÔÁÎÎÑ
ÆÁÊÌÏ×Ï§ ÓÉÓÔÅÍÉ ncpfs.

%package -n pam-pam_ncp_auth
Summary:	PAM module for authenticate using using login/password stored on Netware server
Summary(pl):	Modu³ PAM uwierzytelniaj±cy poprzez login i has³o trzymane na serwerze Netware
Group:		Networking/Utilities
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	pam_ncp_auth

%description -n pam-pam_ncp_auth
The pam_ncp_auth module is PAM module for authenticate using
login/password stored on Netware server.

%description -n pam-pam_ncp_auth -l pl
Modu³ pam_ncp_auth to modu³ PAM s³u¿±cy do uwierzytelniania przy
u¿yciu loginu i has³a przechowywanych na serwerze Netware.

%package -n php-auth_nds
Summary:	PHP module for authenticate using using login/password stored on Netware server
Summary(pl):	Modu³ PHP uwierzytelniaj±cy poprzez login i has³o trzymane na serwerze Netware
Summary(pl):	Narzêdzia do konfigurowania IPX
Group:		Networking/Utilities
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description -n php-auth_nds
The php-auth_nds module is PHP module for authenticate using
login/password stored on Netware server.

%description -n php-auth_nds -l pl
Modu³ php-ncp_auth to modu³ PHP s³u¿±cy do uwierzytelniania przy
u¿yciu loginu i has³a przechowywanych na serwerze Netware.

%package -n ipxutils
Summary:	Utilities for IPX configuration
Summary(de):	Utilities für IPX-Konfiguration
Summary(es):	Utilitarios para configuración IPX
Summary(fr):	Utilitaires pour la configuration IPX
Summary(ja):	IPX ¥¤¥ó¥¿¥Õ¥§¥¤¥¹¤È¥Í¥Ã¥È¥ï¡¼¥¯¤ÎÀßÄê¤È¥Ç¥Ð¥Ã¥°¤Î¤¿¤á¤Î¥Ä¡¼¥ë¡£
Summary(pl):	Narzêdzia do konfigurowania IPX
Summary(pt_BR):	Utilitários para configuração IPX
Summary(ru):	õÔÉÌÉÔÙ ÄÌÑ ËÏÎÆÉÇÕÒÉÒÏ×ÁÎÉÑ É ÏÔÌÁÄËÉ IPX ÉÎÔÅÒÆÅÊÓÏ× É ÓÅÔÅÊ
Summary(tr):	IPX yapýlandýrma yazýlýmlarý
Summary(uk):	õÔÉÌ¦ÔÉ ÄÌÑ ËÏÎÆ¦ÇÕÒÕ×ÁÎÎÑ ¦ ×¦ÄÌÁÄËÉ IPX ¦ÎÔÅÒÆÅÊÓ¦× ÔÁ ÍÅÒÅÖ
Group:		Networking/Utilities
Obsoletes:	ipx
Obsoletes:	ncpfs-ipxutils

%description -n ipxutils
This package includes utilities necessary for configuring and
debugging IPX interfaces and networks under Linux. IPX is the
low-level protocol used by NetWare to transfer data.

%description -n ipxutils -l de
Dieses Paket enthält Dienstprogramme zum Konfigurieren und Debuggen
von IPX-Schnittstellen und -Netzwerken unter Linux. IPX ist das von
NetWare zur Datenübertragung verwendete Low-Level-Protokoll.

%description -n ipxutils -l es
Este paquete incluye los utilitarios necesarios a configuración y
depuración de interfaces y redes IPX en Linux. IPX es el protocolo de
bajo nivel usado por el NetWare para transferir datos.

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

%description -n ipxutils -l pt_BR
Este pacote inclui os utilitários necessários à configuração e
depuração de interfaces e redes IPX no Linux. IPX é o protocolo de
baixo nível usado pelo NetWare para transferir dados.

%description -n ipxutils -l ru
üÔÏÔ ÐÁËÅÔ ÓÏÄÅÒÖÉÔ ÕÔÉÌÉÔÙ, ÎÅÏÂÈÏÄÉÍÙÅ ÄÌÑ ËÏÎÆÉÇÕÒÁÃÉÉ É ÏÔÌÁÄËÉ
IPX ÉÎÔÅÒÆÅÊÓÏ× É ÓÅÔÅÊ ÐÏÄ Linux. IPX - ÜÔÏ ÎÉÚËÏÕÒÏ×ÎÅ×ÙÊ ÐÒÏÔÏËÏÌ,
ÉÐÏÌØÚÕÅÍÙÊ NetWare ÄÌÑ ÐÅÒÅÄÁÞÉ ÄÁÎÎÙÈ.

%description -n ipxutils -l tr
Bu paket NetWare tarafýndan kullanýlan IPX protokolünü yapýlandýrmak
ve hatalarýný ayýklamak için kullanýlabilecek bir dizi uygulama
içermektedir.

%description -n ipxutils -l uk
ãÅÊ ÐÁËÅÔ Í¦ÓÔÉÔØ ÕÔÉÌ¦ÔÉ, ÎÅÏÂÈ¦ÄÎ¦ ÄÌÑ ËÏÎÆ¦ÇÕÒÕ×ÁÎÎÑ ÔÁ ×¦ÄÌÁÄËÉ
IPX ¦ÎÔÅÒÆÅÊÓ¦× ÔÁ ÍÅÒÅÖ Ð¦Ä Linux. IPX - ÃÅ ÎÉÚØËÏÒ¦×ÎÅ×ÉÊ ÐÒÏÔÏËÏÌ,
ÝÏ ×ÉËÏÒÉÓÔÏ×Õ¤ÔØÓÑ × NetWare ÄÌÑ ÐÅÒÅÄÁÞ¦ ÄÁÎÉÈ.

%package devel
Summary:	Files for developing NCP-aware software
Summary(es):	Archivos de inclusión y bibliotecas para NCPfs
Summary(pl):	Pliki do tworzenia oprogramowania u¿ywaj±cego NCP
Summary(pt_BR):	Arquivos de inclusão e bibliotecas para o NCPfs
Summary(ru):	æÁÊÌÙ ÄÌÑ ÒÁÚÒÁÂÏÔËÉ Ó ÉÓÐÏÌØÚÏ×ÁÎÉÅÍ ÂÉÂÌÉÏÔÅËÉ ncpfs
Summary(uk):	æÁÊÌÉ ÄÌÑ ÒÏÚÒÏÂËÉ Ú ×ÉËÏÒÉÓÔÁÎÎÑÍ Â¦ÂÌ¦ÏÔÅËÉ ncpfs
Group:		Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description devel
Files for developing NCP-aware software.

%description devel -l es
Este paquete contiene los archivos de inclusión y bibliotecas que se
necesitan para desarrollar programas que usan NCPfs.

%description devel -l pl
Pliki do tworzenia oprogramowania u¿ywaj±cego NCP.

%description devel -l pt_BR
Este pacote contém os arquivos de inclusão e bibliotecas que são
necessários para desenvolver programas que usam o NCPfs.

%description devel -l ru
üÔÏÔ ÐÁËÅÔ ÓÏÄÅÒÖÉÔ ÆÁÊÌÙ, ÎÅÏÂÈÏÄÉÍÙÅ ÄÌÑ ÒÁÚÒÁÂÏÔËÉ ÐÒÏÇÒÁÍÍ Ó
ÉÓÐÏÌØÚÏ×ÁÎÉÅÍ ÂÉÂÌÉÏÔÅËÉ ncpfs.

%description devel -l uk
ãÅÊ ÐÁËÅÔ Í¦ÓÔÉÔØ ÆÁÊÌÉ, ÎÅÏÂÈ¦ÄÎ¦ ÄÌÑ ÒÏÚÒÏÂËÉ ÐÒÏÇÒÁÍ Ú
×ÉËÏÒÉÓÔÁÎÎÑÍ Â¦ÂÌ¦ÏÔÅËÉ ncpfs.

%prep
%setup -q

%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
cd contrib/php
%{__libtoolize}
%{__aclocal}
%{__autoconf}
cd ../..

%if %{with ipx}
IPX="--enable-ipx --enable-ipx-tools"
%else
IPX="--disable-ipx --disable-ipx-tools"
%endif

./conf
%configure \
	--disable-rpath \
	$IPX \
	--enable-kernel \
	--enable-mount-v2 \
	--enable-mount-v3 \
	--enable-nds \
	--enable-nls \
	--enable-pam \
	%{?with_php:--enable-php} \
	--enable-reentrant \
	--enable-signatures \
	--enable-trace \
	--enable-udp \
	--enable-versions \
	--enable-warnings

%{__make} \
	OPT_FLAGS="%{rpmcflags} -w"

%{__make} -C ipxdump \
	OPT_FLAGS="%{rpmcflags} -w"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{/etc/rc.d/init.d,%{_includedir},/%{_lib}/security} \
	$RPM_BUILD_ROOT{%{_sbindir},/usr/%{_lib}/php}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

ln -s $(cd $RPM_BUILD_ROOT%{_libdir}; ls libncp.so.*.*) $RPM_BUILD_ROOT%{_libdir}/libncp.so
cp -a include/ncp $RPM_BUILD_ROOT%{_includedir}

%if %{with php}
install -m755 contrib/php/modules/php_auth_nds.so $RPM_BUILD_ROOT/usr/%{_lib}/php
%endif

rm -f $RPM_BUILD_ROOT%{_mandir}/man8/mount.ncp.8*
echo '.so ncpmount.8' > $RPM_BUILD_ROOT%{_mandir}/man8/mount.ncp.8

rm -f $RPM_BUILD_ROOT%{_mandir}/man1/pqrm.1*
echo '.so nwpqjob.1' > $RPM_BUILD_ROOT%{_mandir}/man1/pqrm.1

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc BUGS Changes FAQ README* ncpfs-*
%attr(755,root,root) %{_bindir}/[!i]*
%attr(755,root,root) %{_sbindir}/[!i]*
%attr(755,root,root) %{_libdir}/libncp.so.*

%{_mandir}/man8/[!i]*
%{_mandir}/man1/*
%{_mandir}/man5/*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libncp.so
%{_includedir}/ncp

%files -n pam-pam_ncp_auth
%defattr(644,root,root,755)
%doc contrib/pam/README
%attr(755,root,root) /%{_lib}/security/pam_ncp_auth.so

%if %{with php}
%files -n php-auth_nds
%defattr(644,root,root,755)
%attr(755,root,root) /usr/%{_lib}/php/*.so
%endif

%if %{with ipx}
%files -n ipxutils
%defattr(644,root,root,755)
%attr(755,root,root) %{_sbindir}/ipx*
%{_mandir}/man8/ipx*
%endif
