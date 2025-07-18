# TODO:
# - update and finish pl.po (lang patch)
#
# Conditional build:
%bcond_without	php	# don't build PHP module
%bcond_without	ipx	# don't build ipxutils

%define		rel	5
%define		php_name	php%{?php_suffix}
Summary:	Support Utilities for ncpfs, the free netware client for Linux
Summary(de.UTF-8):	Support-Dienstprogramme für ncpfs, den kostenlosen Netware-Client
Summary(es.UTF-8):	Utilitarios de soporte para ncpfs, que es el cliente Linux free para netware
Summary(fr.UTF-8):	Gestionnaires pour ncpfs, le client Netware libre pour Linux
Summary(ja.UTF-8):	ncpfs ファイルシステムユーティリティ、Linux 用 NetWare クライアント。
Summary(pl.UTF-8):	Darmowy klient Netware dla Linuksa wraz z dodatkowymi programami
Summary(pt_BR.UTF-8):	Utilitários de suporte para ncpfs, que é o cliente Linux free para netware
Summary(ru.UTF-8):	Утилиты для файловой системы ncpfs, клиента NetWare для Linux
Summary(tr.UTF-8):	Linux için Netware istemcisi destek yazılımları
Summary(uk.UTF-8):	Утиліти для файлової системи ncpfs, клієнта NetWare для Linux
Name:		ncpfs
Version:	2.2.6
Release:	%{rel}%{!?with_ipx:noipx}
Epoch:		1
License:	GPL v2+
Group:		Networking/Utilities
Source0:	ftp://platan.vc.cvut.cz/pub/linux/ncpfs/%{name}-%{version}.tar.gz
# Source0-md5:	a9ab9f135d504440202069393dd9eb36
Patch0:		%{name}-lang.patch
Patch1:		%{name}-nwsfind.patch
Patch2:		%{name}-ac.patch
Patch3:		%{name}-sbindir.patch
Patch6:		%{name}-offsetof.patch
Patch7:		%{name}-ac-php.patch
Patch9:		%{name}-php.patch

# Fedora patches
Patch20:	%{name}-2.2.6-align.patch
Patch21:	%{name}-2.2.6-getuid.patch
Patch22:	%{name}-2.2.6-ldconfig.patch
Patch23:	%{name}-2.2.6-offsetof.patch

# SUSE patches
Patch403:	%{name}-hg-commit-403.patch
Patch404:	%{name}-hg-commit-404.patch
Patch405:	%{name}-hg-commit-405.patch
Patch406:	%{name}-hg-commit-406.patch
Patch407:	%{name}-hg-commit-407.patch
Patch408:	%{name}-hg-commit-408.patch
Patch409:	%{name}-hg-commit-409.patch
Patch410:	%{name}-hg-commit-410.patch
Patch411:	%{name}-hg-commit-411.patch
Patch412:	%{name}-hg-commit-412.patch
Patch413:	%{name}-hg-commit-413.patch
Patch414:	%{name}-hg-commit-414.patch
Patch415:	%{name}-hg-commit-415.patch
Patch416:	%{name}-hg-commit-416.patch
Patch417:	%{name}-hg-commit-417.patch
Patch419:	%{name}-hg-commit-419.patch
Patch420:	%{name}-hg-commit-420.patch
Patch421:	%{name}-hg-commit-421.patch
Patch422:	%{name}-hg-commit-422.patch
Patch423:	%{name}-hg-commit-423.patch
Patch424:	%{name}-hg-commit-424.patch
Patch425:	%{name}-hg-commit-425.patch
Patch426:	%{name}-hg-commit-426.patch
Patch427:	%{name}-hg-commit-427.patch
Patch428:	%{name}-hg-commit-428.patch
Patch429:	%{name}-hg-commit-429.patch
Patch430:	%{name}-hg-commit-430.patch
Patch431:	%{name}-hg-commit-431.patch
Patch432:	%{name}-hg-commit-432.patch
Patch433:	%{name}-hg-commit-433.patch
Patch434:	%{name}-hg-commit-434.patch
Patch435:	%{name}-hg-commit-435.patch
Patch436:	%{name}-hg-commit-436.patch
Patch437:	%{name}-hg-commit-437.patch
Patch438:	%{name}-hg-commit-438.patch
Patch439:	%{name}-hg-commit-439.patch
Patch440:	%{name}-hg-commit-440.patch
Patch441:	%{name}-hg-commit-441.patch
Patch442:	%{name}-hg-commit-442.patch
Patch443:	%{name}-hg-commit-443.patch
Patch444:	%{name}-hg-commit-444.patch
Patch445:	%{name}-hg-commit-445.patch
Patch446:	%{name}-hg-commit-446.patch
Patch447:	%{name}-hg-commit-447.patch
Patch448:	%{name}-hg-commit-448.patch
Patch449:	%{name}-hg-commit-449.patch
Patch450:	%{name}-hg-commit-450.patch
Patch451:	%{name}-hg-commit-451.patch
Patch452:	%{name}-hg-commit-452.patch
Patch453:	%{name}-hg-commit-453.patch
Patch454:	%{name}-hg-commit-454.patch
Patch455:	%{name}-hg-commit-455.patch
Patch456:	%{name}-hg-commit-456.patch
Patch457:	%{name}-hg-commit-457.patch
Patch458:	%{name}-hg-commit-458.patch
Patch1002:	%{name}.LDFLAGS.patch
Patch1003:	%{name}.pam_ncp_auth.syslog.patch
Patch1005:	%{name}.offsetof.patch
Patch1006:	%{name}-shlibext.patch
%{?with_php:BuildRequires:	%{php_name}-devel}
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	gettext-tools
BuildRequires:	libtool
BuildRequires:	pam-devel
BuildRequires:	sed >= 4.0
#Requires:	iconv
%{?with_ipx:Requires:	ipxutils = %{epoch}:%{version}-%{release}}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sbindir	/sbin

%description
This package contains tools to help configure and use the ncpfs
filesysten, which is a linux filesystem which understands the NCP
protocol. This protocol is used by Novell NetWare clients use to talk
to NetWare servers.

%description -l de.UTF-8
Dieses Paket enthält Tools zum Konfigurieren und Einsatz des
ncpfs-Dateisystems, einem Linux-Dateisystem, das das NCP-Protokoll
versteht. Dieses Protokoll wird von Novell NetWare-Clients zur
Kommunikation mit NetWare-Servern verwendet.

%description -l es.UTF-8
Este paquete contiene herramientas para ayudar a configurar y usar el
sistema de archivos ncpfs, que es un sistema de archivos Linux capaz
de entender el protocolo NCP. Este es el protocolo que los clientes
Novell NetWare usan para "conversar" con servidores NetWare.

%description -l fr.UTF-8
Ce package contient des outils pour aider a configuer et à utiliser le
système de fichiers ncpfs, qui est un système de fichiers Linux adapté
au protocole NCP. Ce protocole est utilisé par les clients Novell
NetWare pour communiquer avec les serveurs NetWare.

%description -l ja.UTF-8
ncpfs は Novell NetWare(TM) NCP として理解されるファイルシステムです。
機能的には、NCP は、NFS が TCP/IP の世界で用いられるように、NetWare で
用いられます。Linux システムが NetWare
ファイルシステムをマウントするには、
特別なマウントプログラムが必要です。ncpfs
パッケージはそのようなマウント プログラムと、ncpfs
ファイルシステムの設定と利用のためのツールを含みます。

Novell NetWare のファイルかサービスを使うために ncpfs
ファイルシステムを 用いる必要があるなら、ncpfs
パッケージをインストールしましょう。

%description -l pl.UTF-8
Pakiet zawiera narzędzia pomocne w konfigurowaniu i używaniu systemu
plików ncpfs. Dzięki ncpfs możliwe jest podłączanie wolumenów serwerów
Netware i modyfikowanie ich zawartości.

%description -l pt_BR.UTF-8
Este pacote contém ferramentas para ajudar a configurar e usar o
sistema de arquivos ncpfs, que é um sistema de arquivos Linux que
entende o protocolo NCP. Esse é o protocolo que os clientes Novell
NetWare usam para "conversar" com servidores NetWare.

%description -l ru.UTF-8
Ncpfs - это файловая система поверх протокола Novell NetWare(TM) NCP.
Функционально, NCP играет в NetWare ту же роль, что NFS в мире TCP/IP.
Для того, чтобы система Linux смонтировала файловую систему NetWare,
ей нужна специальная программа монтирования. Пакет ncpfs содержит
такую программу плюс другие инструменты для конфигурирования и
использования файловой системы ncpfs.

%description -l tr.UTF-8
Bu paket Linux'un Novell'in NCP protokolunu kullanabilmesi için
gereken yardımcı yazılımları içermektedir.

%description -l uk.UTF-8
Ncpfs - це файлова система поверх протоколу Novell NetWare(TM) NCP. За
функціями, NCP відіграє в NetWare ту ж роль, що NFS у світі TCP/IP.
Для того, щоб система Linux змонтувала файлову систему NetWare, їй
потрібна спеціальна програма монтування. Пакет ncpfs містить таку
програму плюс інші інструменти для конфігурування та використання
файлової системи ncpfs.

%package devel
Summary:	Files for developing NCP-aware software
Summary(es.UTF-8):	Archivos de inclusión para NCPfs
Summary(pl.UTF-8):	Pliki do tworzenia oprogramowania używającego NCP
Summary(pt_BR.UTF-8):	Arquivos de inclusão para o NCPfs
Summary(ru.UTF-8):	Файлы для разработки с использованием библиотеки ncpfs
Summary(uk.UTF-8):	Файли для розробки з використанням бібліотеки ncpfs
Group:		Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description devel
Files for developing NCP-aware software.

%description devel -l es.UTF-8
Este paquete contiene los archivos de inclusión que se necesitan para
desarrollar programas que usan NCPfs.

%description devel -l pl.UTF-8
Pliki do tworzenia oprogramowania używającego NCP.

%description devel -l pt_BR.UTF-8
Este pacote contém os arquivos de inclusão que são necessários para
desenvolver programas que usam o NCPfs.

%description devel -l ru.UTF-8
Этот пакет содержит файлы, необходимые для разработки программ с
использованием библиотеки ncpfs.

%description devel -l uk.UTF-8
Цей пакет містить файли, необхідні для розробки програм з
використанням бібліотеки ncpfs.

%package -n pam-pam_ncp_auth
Summary:	PAM module for authenticate using using login/password stored on Netware server
Summary(pl.UTF-8):	Moduł PAM uwierzytelniający poprzez login i hasło trzymane na serwerze Netware
Group:		Networking/Utilities
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	pam_ncp_auth

%description -n pam-pam_ncp_auth
The pam_ncp_auth module is PAM module for authenticate using
login/password stored on Netware server.

%description -n pam-pam_ncp_auth -l pl.UTF-8
Moduł pam_ncp_auth to moduł PAM służący do uwierzytelniania przy
użyciu loginu i hasła przechowywanych na serwerze Netware.

%package -n %{php_name}-auth_nds
Summary:	PHP module for authenticate using using login/password stored on Netware server
Summary(pl.UTF-8):	Moduł PHP uwierzytelniający poprzez login i hasło trzymane na serwerze Netware
Group:		Networking/Utilities
%{?requires_php_extension}
Requires:	%{name} = %{epoch}:%{version}-%{release}
Provides:	php(auth_nds) = %{version}

%description -n %{php_name}-auth_nds
The php-auth_nds module is PHP module for authenticate using
login/password stored on Netware server.

%description -n %{php_name}-auth_nds -l pl.UTF-8
Moduł php-ncp_auth to moduł PHP służący do uwierzytelniania przy
użyciu loginu i hasła przechowywanych na serwerze Netware.

%package -n ipxutils
Summary:	Utilities for IPX configuration
Summary(de.UTF-8):	Utilities für IPX-Konfiguration
Summary(es.UTF-8):	Utilitarios para configuración IPX
Summary(fr.UTF-8):	Utilitaires pour la configuration IPX
Summary(ja.UTF-8):	IPX インタフェイスとネットワークの設定とデバッグのためのツール。
Summary(pl.UTF-8):	Narzędzia do konfigurowania IPX
Summary(pt_BR.UTF-8):	Utilitários para configuração IPX
Summary(ru.UTF-8):	Утилиты для конфигурирования и отладки IPX интерфейсов и сетей
Summary(tr.UTF-8):	IPX yapılandırma yazılımları
Summary(uk.UTF-8):	Утиліти для конфігурування і відладки IPX інтерфейсів та мереж
Group:		Networking/Utilities
Obsoletes:	ipx
Obsoletes:	ncpfs-ipxutils

%description -n ipxutils
This package includes utilities necessary for configuring and
debugging IPX interfaces and networks under Linux. IPX is the
low-level protocol used by NetWare to transfer data.

%description -n ipxutils -l de.UTF-8
Dieses Paket enthält Dienstprogramme zum Konfigurieren und Debuggen
von IPX-Schnittstellen und -Netzwerken unter Linux. IPX ist das von
NetWare zur Datenübertragung verwendete Low-Level-Protokoll.

%description -n ipxutils -l es.UTF-8
Este paquete incluye los utilitarios necesarios a configuración y
depuración de interfaces y redes IPX en Linux. IPX es el protocolo de
bajo nivel usado por el NetWare para transferir datos.

%description -n ipxutils -l fr.UTF-8
Ce package contient les utilitaires nécessires à pour la configuration
et le déboggage des réseaux et interfaces IPX sous Linux. IPX est un
protocole de bas niveau utilisé par NetWare pour transférer des
données.

%description -n ipxutils -l ja.UTF-8
ipxutils パッケージは、Linux で IPX インタフェイスとネットワークの設定と
デバッグをするためのユーティリティを含みます。IPX は Novell NetWare の
ファイルシステムでデータを転送するのに用いられる低レヴェルプロトコルです。

ネットワークで IPX 設定をする必要があれば、ipxutils をインストールしましょう。

%description -n ipxutils -l pl.UTF-8
Pakiet zawiera narzędzia niezbędne do konfigurowania interfejsów i
sieci IPX pod Linuksem. Protokołu IPX używa Netware do przesyłania
danych.

%description -n ipxutils -l pt_BR.UTF-8
Este pacote inclui os utilitários necessários à configuração e
depuração de interfaces e redes IPX no Linux. IPX é o protocolo de
baixo nível usado pelo NetWare para transferir dados.

%description -n ipxutils -l ru.UTF-8
Этот пакет содержит утилиты, необходимые для конфигурации и отладки
IPX интерфейсов и сетей под Linux. IPX - это низкоуровневый протокол,
ипользуемый NetWare для передачи данных.

%description -n ipxutils -l tr.UTF-8
Bu paket NetWare tarafından kullanılan IPX protokolünü yapılandırmak
ve hatalarını ayıklamak için kullanılabilecek bir dizi uygulama
içermektedir.

%description -n ipxutils -l uk.UTF-8
Цей пакет містить утиліти, необхідні для конфігурування та відладки
IPX інтерфейсів та мереж під Linux. IPX - це низькорівневий протокол,
що використовується в NetWare для передачі даних.

%prep
%setup -q
%patch -P0 -p1
%patch -P1 -p1
%patch -P3 -p1
%patch -P6 -p1
%patch -P7 -p1
%patch -P9 -p1

%patch -P403 -p1
%patch -P404 -p1
%patch -P405 -p1
%patch -P406 -p1
%patch -P407 -p1
%patch -P408 -p1
%patch -P409 -p1
%patch -P410 -p1
%patch -P411 -p1
%patch -P412 -p1
%patch -P413 -p1
%patch -P414 -p1
%patch -P415 -p1
%patch -P416 -p1
%patch -P417 -p1
%patch -P419 -p1
%patch -P420 -p1
%patch -P421 -p1
%patch -P422 -p1
%patch -P423 -p1
%patch -P424 -p1
%patch -P425 -p1
%patch -P426 -p1
%patch -P427 -p1
%patch -P428 -p1
%patch -P429 -p1
%patch -P430 -p1
%patch -P431 -p1
%patch -P432 -p1
%patch -P433 -p1
%patch -P434 -p1
%patch -P435 -p1
%patch -P436 -p1
%patch -P437 -p1
%patch -P438 -p1
%patch -P439 -p1
%patch -P440 -p1
%patch -P441 -p1
%patch -P442 -p1
%patch -P443 -p1
%patch -P444 -p1
%patch -P445 -p1
%patch -P446 -p1
%patch -P447 -p1
%patch -P448 -p1
%patch -P449 -p1
%patch -P450 -p1
%patch -P451 -p1
%patch -P452 -p1
%patch -P453 -p1
%patch -P454 -p1
%patch -P455 -p1
%patch -P456 -p1
%patch -P457 -p1
%patch -P458 -p1
#
%patch -P1002 -p1
%patch -P1003 -p1
%patch -P1005 -p1

%patch -P2 -p1

%patch -P20 -p1
%patch -P21 -p1
%patch -P22 -p1
%patch -P23 -p1
%patch -P1006 -p0

sed -e '/AM_GNU_GETTEXT/iAM_PROG_MKDIR_P\n' -i configure.ac
sed -e '/AM_ICONV/a\  :' -i configure.ac

%build
%if %{with php}
cd contrib/php
%{__libtoolize}
%{__aclocal}
%{__autoconf}
cd ../..
%endif

%{__gettextize}
%{__aclocal}
%{__autoconf}
%{__autoheader}

%configure \
	--disable-function-sections \
	--disable-rpath \
%if %{with ipx}
	--enable-ipx \
	--enable-ipx-tools \
%else
	--disable-ipx \
	--disable-ipx-tools \
%endif
	--enable-kernel \
	--enable-mount-v2 \
	--enable-mount-v3 \
	--enable-nds \
	--enable-nls \
	--enable-pam=/%{_lib}/security \
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
install -d $RPM_BUILD_ROOT{/etc/rc.d/init.d,%{_includedir},/%{_lib}/security,%{_sbindir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

ln -s $(cd $RPM_BUILD_ROOT%{_libdir}; ls libncp.so.*.*.*) $RPM_BUILD_ROOT%{_libdir}/libncp.so
cp -a include/ncp $RPM_BUILD_ROOT%{_includedir}

%if %{with php}
install -d $RPM_BUILD_ROOT{%{php_extensiondir},%{php_sysconfdir}/conf.d}
cat <<'EOF' > $RPM_BUILD_ROOT%{php_sysconfdir}/conf.d/auth_nds.ini
; Enable auth_nds extension module
extension=php_auth_nds.so
EOF
install -p contrib/php/modules/php_auth_nds.so $RPM_BUILD_ROOT%{php_extensiondir}
%endif

%{__rm} $RPM_BUILD_ROOT%{_mandir}/man8/mount.ncp.8*
echo '.so ncpmount.8' > $RPM_BUILD_ROOT%{_mandir}/man8/mount.ncp.8

%{__rm} $RPM_BUILD_ROOT%{_mandir}/man1/pqrm.1*
echo '.so nwpqjob.1' > $RPM_BUILD_ROOT%{_mandir}/man1/pqrm.1

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc BUGS Changes FAQ README* ncpfs-*
%attr(755,root,root) %{_bindir}/ncopy
%attr(755,root,root) %{_bindir}/ncplogin
%attr(755,root,root) %{_bindir}/ncplogout
%attr(755,root,root) %{_bindir}/ncpmap
%attr(755,root,root) %{_bindir}/ncpmount
%attr(755,root,root) %{_bindir}/ncpumount
%attr(755,root,root) %{_bindir}/nprint
%attr(755,root,root) %{_bindir}/nsend
%attr(755,root,root) %{_bindir}/nw*
%attr(755,root,root) %{_bindir}/pqlist
%attr(755,root,root) %{_bindir}/pqrm
%attr(755,root,root) %{_bindir}/pqstat
%attr(755,root,root) %{_bindir}/pserver
%attr(755,root,root) %{_bindir}/slist
%attr(755,root,root) %{_sbindir}/mount.ncp
%attr(755,root,root) %{_sbindir}/mount.ncpfs
%attr(755,root,root) %{_sbindir}/nwmsg
%attr(755,root,root) %{_libdir}/libncp.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libncp.so.2.3
%{_mandir}/man1/ncopy.1*
%{_mandir}/man1/nprint.1*
%{_mandir}/man1/nsend.1*
%{_mandir}/man1/nw*.1*
%{_mandir}/man1/pqlist.1*
%{_mandir}/man1/pqrm.1*
%{_mandir}/man1/pqstat.1*
%{_mandir}/man1/pserver.1*
%{_mandir}/man1/slist.1*
%{_mandir}/man5/nwclient.5*
%{_mandir}/man8/mount.ncp.8*
%{_mandir}/man8/ncplogin.8*
%{_mandir}/man8/ncpmap.8*
%{_mandir}/man8/ncpmount.8*
%{_mandir}/man8/ncpumount.8*
%{_mandir}/man8/nw*.8*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libncp.so
%{_includedir}/ncp

%files -n pam-pam_ncp_auth
%defattr(644,root,root,755)
%doc contrib/pam/README
%attr(755,root,root) /%{_lib}/security/pam_ncp_auth.so

%if %{with php}
%files -n %{php_name}-auth_nds
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{php_sysconfdir}/conf.d/auth_nds.ini
%attr(755,root,root) %{php_extensiondir}/php_auth_nds.so
%endif

%if %{with ipx}
%files -n ipxutils
%defattr(644,root,root,755)
%attr(755,root,root) %{_sbindir}/ipx_*
%{_mandir}/man8/ipx_*.8*
%endif
