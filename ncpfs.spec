# TODO:
# - fix/write from scrach -devel Summary and %%description
# - fix -devel Group
Summary:	Support Utilities for ncpfs, the free netware client for Linux.
Summary(de):	Support-Dienstprogramme fЭr ncpfs, den kostenlosen Netware-Client
Summary(es):	Utilitarios de soporte para ncpfs, que es el cliente Linux free para netware
Summary(fr):	Gestionnaires pour ncpfs, le client Netware libre pour Linux.
Summary(ja):	ncpfs ╔у╔║╔╓╔К╔╥╔╧╔ф╔Ю╔Ф║╪╔ф╔ё╔Й╔ф╔ё║╒Linux мя NetWare ╔╞╔И╔╓╔╒╔С╔х║ё
Summary(pl):	Darmowy klient Netware dla Linuxa wraz z dodatkowymi programami
Summary(pt_BR):	UtilitАrios de suporte para ncpfs, que И o cliente Linux free para netware
Summary(ru):	Утилиты для файловой системы ncpfs, клиента NetWare для Linux
Summary(tr):	Linux iГin Netware istemcisi destek yazЩlЩmlarЩ
Summary(uk):	Утил╕ти для файлово╖ системи ncpfs, кл╕╓нта NetWare для Linux
Name:		ncpfs
Version:	2.2.0.18
Release:	9
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

%description -l de
Dieses Paket enthДlt Tools zum Konfigurieren und Einsatz des
ncpfs-Dateisystems, einem Linux-Dateisystem, das das NCP-Protokoll
versteht. Dieses Protokoll wird von Novell NetWare-Clients zur
Kommunikation mit NetWare-Servern verwendet.

%description -l es
Este paquete contiene herramientas para ayudar a configurar y usar el
sistema de archivos ncpfs, que es un sistema de archivos Linux capaz
de entender el protocolo NCP. Este es el protocolo que los clientes
Novell NetWare usan para "conversar" con servidores NetWare.

%description -l fr
Ce package contient des outils pour aider a configuer et Ю utiliser le
systХme de fichiers ncpfs, qui est un systХme de fichiers Linux adaptИ
au protocole NCP. Ce protocole est utilisИ par les clients Novell
NetWare pour communiquer avec les serveurs NetWare.

%description -l ja
ncpfs ╓о Novell NetWare(TM) NCP ╓х╓╥╓фмЩ╡Р╓╣╓Л╓К╔у╔║╔╓╔К╔╥╔╧╔ф╔Ю╓г╓╧║ё
╣║г╫е╙╓к╓о║╒NCP ╓о║╒NFS ╓╛ TCP/IP ╓ню╓Ё╕╓гмя╓╓╓И╓Л╓К╓Х╓╕╓к║╒NetWare ╓г
мя╓╓╓И╓Л╓ч╓╧║ёLinux ╔╥╔╧╔ф╔Ю╓╛ NetWare
╔у╔║╔╓╔К╔╥╔╧╔ф╔Ю╓Р╔ч╔╕╔С╔х╓╧╓К╓к╓о║╒
фцйл╓й╔ч╔╕╔С╔х╔в╔М╔╟╔И╔Ю╓╛и╛мв╓г╓╧║ёncpfs
╔я╔ц╔╠║╪╔╦╓о╓╫╓н╓Х╓╕╓й╔ч╔╕╔С╔х ╔в╔М╔╟╔И╔Ю╓х║╒ncpfs
╔у╔║╔╓╔К╔╥╔╧╔ф╔Ю╓нюъдЙ╓хмЬмя╓н╓©╓А╓н╔д║╪╔К╓Р╢ч╓ъ╓ч╓╧║ё

Novell NetWare ╓н╔у╔║╔╓╔К╓╚╔╣║╪╔с╔╧╓Р╩х╓╕╓©╓А╓к ncpfs
╔у╔║╔╓╔К╔╥╔╧╔ф╔Ю╓Р мя╓╓╓Ки╛мв╓╛╓╒╓К╓й╓И║╒ncpfs
╔я╔ц╔╠║╪╔╦╓Р╔╓╔С╔╧╔х║╪╔К╓╥╓ч╓╥╓Г╓╕║ё

%description -l pl
Pakiet zawiera narzЙdzia pomocne w konfigurowaniu i u©ywaniu systemu
plikСw ncpfs. DziЙki ncpfs mo©liwe jest podЁ╠czanie wolumenСw serwerСw
Netware i modyfikowanie ich zawarto╤ci.

%description -l pt_BR
Este pacote contИm ferramentas para ajudar a configurar e usar o
sistema de arquivos ncpfs, que И um sistema de arquivos Linux que
entende o protocolo NCP. Esse И o protocolo que os clientes Novell
NetWare usam para "conversar" com servidores NetWare.

%description -l ru
Ncpfs - это файловая система поверх протокола Novell NetWare(TM) NCP.
Функционально, NCP играет в NetWare ту же роль, что NFS в мире TCP/IP.
Для того, чтобы система Linux смонтировала файловую систему NetWare,
ей нужна специальная программа монтирования. Пакет ncpfs содержит
такую программу плюс другие инструменты для конфигурирования и
использования файловой системы ncpfs.

%description -l tr
Bu paket Linux'un Novell'in NCP protokolunu kullanabilmesi iГin
gereken yardЩmcЩ yazЩlЩmlarЩ iГermektedir.

%description -l uk
Ncpfs - це файлова система поверх протоколу Novell NetWare(TM) NCP. За
функц╕ями, NCP в╕д╕гра╓ в NetWare ту ж роль, що NFS у св╕т╕ TCP/IP.
Для того, щоб система Linux змонтувала файлову систему NetWare, ╖й
потр╕бна спец╕альна програма монтування. Пакет ncpfs м╕стить таку
програму плюс ╕нш╕ ╕нструменти для конф╕гурування та використання
файлово╖ системи ncpfs.

%package -n pam_ncp_auth
Summary:	PAM module for authenticate using using login/password stored on Netware server
Summary(pl):	NarzЙdzia do konfigurowania IPX
Group:		Networking/Utilities
Requires:	%{name} = %{version}

%description -n pam_ncp_auth
The pam_ncp_auth module is PAM module for authenticate using
login/password stored on Netware server.

%package -n ipxutils
Summary:	Utilities for IPX configuration
Summary(de):	Utilities fЭr IPX-Konfiguration
Summary(es):	Utilitarios para configuraciСn IPX
Summary(fr):	Utilitaires pour la configuration IPX
Summary(ja):	IPX ╔╓╔С╔©╔у╔╖╔╓╔╧╓х╔м╔ц╔х╔О║╪╔╞╓нюъдЙ╓х╔г╔п╔ц╔╟╓н╓©╓А╓н╔д║╪╔К║ё
Summary(pl):	NarzЙdzia do konfigurowania IPX
Summary(pt_BR):	UtilitАrios para configuraГЦo IPX
Summary(ru):	Утилиты для конфигурирования и отладки IPX интерфейсов и сетей
Summary(tr):	IPX yapЩlandЩrma yazЩlЩmlarЩ
Summary(uk):	Утил╕ти для конф╕гурування ╕ в╕дладки IPX ╕нтерфейс╕в та мереж
Group:		Networking/Utilities
Obsoletes:	ipx
Obsoletes:	ncpfs-ipxutils

%description -n ipxutils
This package includes utilities necessary for configuring and
debugging IPX interfaces and networks under Linux. IPX is the
low-level protocol used by NetWare to transfer data.

%description -n ipxutils -l de
Dieses Paket enthДlt Dienstprogramme zum Konfigurieren und Debuggen
von IPX-Schnittstellen und -Netzwerken unter Linux. IPX ist das von
NetWare zur DatenЭbertragung verwendete Low-Level-Protokoll.

%description -n ipxutils -l es
Este paquete incluye los utilitarios necesarios a configuraciСn y
depuraciСn de interfaces y redes IPX en Linux. IPX es el protocolo de
bajo nivel usado por el NetWare para transferir datos.

%description -n ipxutils -l fr
Ce package contient les utilitaires nИcessires Ю pour la configuration
et le dИboggage des rИseaux et interfaces IPX sous Linux. IPX est un
protocole de bas niveau utilisИ par NetWare pour transfИrer des
donnИes.

%description -n ipxutils -l ja
ipxutils ╔я╔ц╔╠║╪╔╦╓о║╒Linux ╓г IPX
╔╓╔С╔©╔у╔╖╔╓╔╧╓х╔м╔ц╔х╔О║╪╔╞╓нюъдЙ╓х
╔г╔п╔ц╔╟╓Р╓╧╓К╓©╓А╓н╔Ф║╪╔ф╔ё╔Й╔ф╔ё╓Р╢ч╓ъ╓ч╓╧║ёIPX ╓о Novell NetWare ╓н
╔у╔║╔╓╔К╔╥╔╧╔ф╔Ю╓г╔г║╪╔©╓Ре╬аВ╓╧╓К╓н╓кмя╓╓╓И╓Л╓КдЦ╔Л╔Т╔╖╔К╔в╔М╔х╔Ё╔К╓г╓╧║ё

╔м╔ц╔х╔О║╪╔╞╓г IPX юъдЙ╓Р╓╧╓Ки╛мв╓╛╓╒╓Л╓п║╒ipxutils
╓Р╔╓╔С╔╧╔х║╪╔К╓╥╓ч╓╥╓Г╓╕║ё

%description -n ipxutils -l pl
Pakiet zawiera narzЙdzia niezbЙdne do konfigurowania interfejsСw i
sieci IPX pod Linuxem. ProtokoЁu IPX u©ywa Netware do przesyЁania
danych.

%description -n ipxutils -l pt_BR
Este pacote inclui os utilitАrios necessАrios Ю configuraГЦo e
depuraГЦo de interfaces e redes IPX no Linux. IPX И o protocolo de
baixo nМvel usado pelo NetWare para transferir dados.

%description -n ipxutils -l ru
Этот пакет содержит утилиты, необходимые для конфигурации и отладки
IPX интерфейсов и сетей под Linux. IPX - это низкоуровневый протокол,
ипользуемый NetWare для передачи данных.

%description -n ipxutils -l tr
Bu paket NetWare tarafЩndan kullanЩlan IPX protokolЭnЭ yapЩlandЩrmak
ve hatalarЩnЩ ayЩklamak iГin kullanЩlabilecek bir dizi uygulama
iГermektedir.

%description -n ipxutils -l uk
Цей пакет м╕стить утил╕ти, необх╕дн╕ для конф╕гурування та в╕дладки
IPX ╕нтерфейс╕в та мереж п╕д Linux. IPX - це низькор╕вневий протокол,
що використову╓ться в NetWare для передач╕ даних.

%package devel
Summary:	Files for developing NCP-aware software
Summary(es):	Archivos de inclusiСn y bibliotecas para NCPfs
Summary(pl):	Pliki do tworzenia oprogramowania u©ywaj╠cego NCP
Summary(pt_BR):	Arquivos de inclusЦo e bibliotecas para o NCPfs
Summary(ru):	Файлы для разработки с использованием библиотеки ncpfs
Summary(uk):	Файли для розробки з використанням б╕бл╕отеки ncpfs
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
Files for developing NCP-aware software.

%description devel -l es
Este paquete contiene los archivos de inclusiСn y bibliotecas que se
necesitan para desarrollar programas que usan NCPfs.

%description devel -l pl
Pliki do tworzenia oprogramowania u©ywaj╠cego NCP.

%description devel -l pt_BR
Este pacote contИm os arquivos de inclusЦo e bibliotecas que sЦo
necessАrios para desenvolver programas que usam o NCPfs.

%description devel -l ru
Этот пакет содержит файлы, необходимые для разработки программ с
использованием библиотеки ncpfs.

%description devel -l uk
Цей пакет м╕стить файли, необх╕дн╕ для розробки програм з
використанням б╕бл╕отеки ncpfs.

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

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc BUGS Changes FAQ README* ncpfs-*
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
%doc contrib/pam/README
%attr(755,root,root) /lib/security/pam_ncp_auth.so

%files -n ipxutils
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ipx*
%{_mandir}/man8/ipx*
