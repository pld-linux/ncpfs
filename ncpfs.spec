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
Summary(de):	Support-Dienstprogramme f�r ncpfs, den kostenlosen Netware-Client
Summary(es):	Utilitarios de soporte para ncpfs, que es el cliente Linux free para netware
Summary(fr):	Gestionnaires pour ncpfs, le client Netware libre pour Linux
Summary(ja):	ncpfs �ե����륷���ƥ�桼�ƥ���ƥ���Linux �� NetWare ���饤����ȡ�
Summary(pl):	Darmowy klient Netware dla Linuksa wraz z dodatkowymi programami
Summary(pt_BR):	Utilit�rios de suporte para ncpfs, que � o cliente Linux free para netware
Summary(ru):	������� ��� �������� ������� ncpfs, ������� NetWare ��� Linux
Summary(tr):	Linux i�in Netware istemcisi destek yaz�l�mlar�
Summary(uk):	���̦�� ��� ������ϧ ������� ncpfs, �̦���� NetWare ��� Linux
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
Dieses Paket enth�lt Tools zum Konfigurieren und Einsatz des
ncpfs-Dateisystems, einem Linux-Dateisystem, das das NCP-Protokoll
versteht. Dieses Protokoll wird von Novell NetWare-Clients zur
Kommunikation mit NetWare-Servern verwendet.

%description -l es
Este paquete contiene herramientas para ayudar a configurar y usar el
sistema de archivos ncpfs, que es un sistema de archivos Linux capaz
de entender el protocolo NCP. Este es el protocolo que los clientes
Novell NetWare usan para "conversar" con servidores NetWare.

%description -l fr
Ce package contient des outils pour aider a configuer et � utiliser le
syst�me de fichiers ncpfs, qui est un syst�me de fichiers Linux adapt�
au protocole NCP. Ce protocole est utilis� par les clients Novell
NetWare pour communiquer avec les serveurs NetWare.

%description -l ja
ncpfs �� Novell NetWare(TM) NCP �Ȥ������򤵤��ե����륷���ƥ�Ǥ���
��ǽŪ�ˤϡ�NCP �ϡ�NFS �� TCP/IP ���������Ѥ�����褦�ˡ�NetWare ��
�Ѥ����ޤ���Linux �����ƥब NetWare
�ե����륷���ƥ��ޥ���Ȥ���ˤϡ�
���̤ʥޥ���ȥץ���बɬ�פǤ���ncpfs
�ѥå������Ϥ��Τ褦�ʥޥ���� �ץ����ȡ�ncpfs
�ե����륷���ƥ����������ѤΤ���Υġ����ޤߤޤ���

Novell NetWare �Υե����뤫�����ӥ���Ȥ������ ncpfs
�ե����륷���ƥ�� �Ѥ���ɬ�פ�����ʤ顢ncpfs
�ѥå������򥤥󥹥ȡ��뤷�ޤ��礦��

%description -l pl
Pakiet zawiera narz�dzia pomocne w konfigurowaniu i u�ywaniu systemu
plik�w ncpfs. Dzi�ki ncpfs mo�liwe jest pod��czanie wolumen�w serwer�w
Netware i modyfikowanie ich zawarto�ci.

%description -l pt_BR
Este pacote cont�m ferramentas para ajudar a configurar e usar o
sistema de arquivos ncpfs, que � um sistema de arquivos Linux que
entende o protocolo NCP. Esse � o protocolo que os clientes Novell
NetWare usam para "conversar" com servidores NetWare.

%description -l ru
Ncpfs - ��� �������� ������� ������ ��������� Novell NetWare(TM) NCP.
�������������, NCP ������ � NetWare �� �� ����, ��� NFS � ���� TCP/IP.
��� ����, ����� ������� Linux ������������ �������� ������� NetWare,
�� ����� ����������� ��������� ������������. ����� ncpfs ��������
����� ��������� ���� ������ ����������� ��� ���������������� �
������������� �������� ������� ncpfs.

%description -l tr
Bu paket Linux'un Novell'in NCP protokolunu kullanabilmesi i�in
gereken yard�mc� yaz�l�mlar� i�ermektedir.

%description -l uk
Ncpfs - �� ������� ������� ������ ��������� Novell NetWare(TM) NCP. ��
����æ���, NCP צĦ���� � NetWare �� � ����, �� NFS � �צԦ TCP/IP.
��� ����, ��� ������� Linux ���������� ������� ������� NetWare, ��
���Ҧ��� ���æ����� �������� ����������. ����� ncpfs ͦ����� ����
�������� ���� ��ۦ ����������� ��� ���Ʀ��������� �� ������������
������ϧ ������� ncpfs.

%package -n pam-pam_ncp_auth
Summary:	PAM module for authenticate using using login/password stored on Netware server
Summary(pl):	Modu� PAM uwierzytelniaj�cy poprzez login i has�o trzymane na serwerze Netware
Group:		Networking/Utilities
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	pam_ncp_auth

%description -n pam-pam_ncp_auth
The pam_ncp_auth module is PAM module for authenticate using
login/password stored on Netware server.

%description -n pam-pam_ncp_auth -l pl
Modu� pam_ncp_auth to modu� PAM s�u��cy do uwierzytelniania przy
u�yciu loginu i has�a przechowywanych na serwerze Netware.

%package -n php-auth_nds
Summary:	PHP module for authenticate using using login/password stored on Netware server
Summary(pl):	Modu� PHP uwierzytelniaj�cy poprzez login i has�o trzymane na serwerze Netware
Summary(pl):	Narz�dzia do konfigurowania IPX
Group:		Networking/Utilities
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description -n php-auth_nds
The php-auth_nds module is PHP module for authenticate using
login/password stored on Netware server.

%description -n php-auth_nds -l pl
Modu� php-ncp_auth to modu� PHP s�u��cy do uwierzytelniania przy
u�yciu loginu i has�a przechowywanych na serwerze Netware.

%package -n ipxutils
Summary:	Utilities for IPX configuration
Summary(de):	Utilities f�r IPX-Konfiguration
Summary(es):	Utilitarios para configuraci�n IPX
Summary(fr):	Utilitaires pour la configuration IPX
Summary(ja):	IPX ���󥿥ե������ȥͥåȥ��������ȥǥХå��Τ���Υġ��롣
Summary(pl):	Narz�dzia do konfigurowania IPX
Summary(pt_BR):	Utilit�rios para configura��o IPX
Summary(ru):	������� ��� ���������������� � ������� IPX ����������� � �����
Summary(tr):	IPX yap�land�rma yaz�l�mlar�
Summary(uk):	���̦�� ��� ���Ʀ��������� � צ������ IPX ��������Ӧ� �� �����
Group:		Networking/Utilities
Obsoletes:	ipx
Obsoletes:	ncpfs-ipxutils

%description -n ipxutils
This package includes utilities necessary for configuring and
debugging IPX interfaces and networks under Linux. IPX is the
low-level protocol used by NetWare to transfer data.

%description -n ipxutils -l de
Dieses Paket enth�lt Dienstprogramme zum Konfigurieren und Debuggen
von IPX-Schnittstellen und -Netzwerken unter Linux. IPX ist das von
NetWare zur Daten�bertragung verwendete Low-Level-Protokoll.

%description -n ipxutils -l es
Este paquete incluye los utilitarios necesarios a configuraci�n y
depuraci�n de interfaces y redes IPX en Linux. IPX es el protocolo de
bajo nivel usado por el NetWare para transferir datos.

%description -n ipxutils -l fr
Ce package contient les utilitaires n�cessires � pour la configuration
et le d�boggage des r�seaux et interfaces IPX sous Linux. IPX est un
protocole de bas niveau utilis� par NetWare pour transf�rer des
donn�es.

%description -n ipxutils -l ja
ipxutils �ѥå������ϡ�Linux �� IPX
���󥿥ե������ȥͥåȥ���������
�ǥХå��򤹤뤿��Υ桼�ƥ���ƥ���ޤߤޤ���IPX �� Novell NetWare ��
�ե����륷���ƥ�ǥǡ�����ž������Τ��Ѥ�������������ץ�ȥ���Ǥ���

�ͥåȥ���� IPX ����򤹤�ɬ�פ�����С�ipxutils
�򥤥󥹥ȡ��뤷�ޤ��礦��

%description -n ipxutils -l pl
Pakiet zawiera narz�dzia niezb�dne do konfigurowania interfejs�w i
sieci IPX pod Linuxem. Protoko�u IPX u�ywa Netware do przesy�ania
danych.

%description -n ipxutils -l pt_BR
Este pacote inclui os utilit�rios necess�rios � configura��o e
depura��o de interfaces e redes IPX no Linux. IPX � o protocolo de
baixo n�vel usado pelo NetWare para transferir dados.

%description -n ipxutils -l ru
���� ����� �������� �������, ����������� ��� ������������ � �������
IPX ����������� � ����� ��� Linux. IPX - ��� �������������� ��������,
����������� NetWare ��� �������� ������.

%description -n ipxutils -l tr
Bu paket NetWare taraf�ndan kullan�lan IPX protokol�n� yap�land�rmak
ve hatalar�n� ay�klamak i�in kullan�labilecek bir dizi uygulama
i�ermektedir.

%description -n ipxutils -l uk
��� ����� ͦ����� ���̦��, ����Ȧ�Φ ��� ���Ʀ��������� �� צ������
IPX ��������Ӧ� �� ����� Ц� Linux. IPX - �� ������Ҧ������ ��������,
�� ����������դ���� � NetWare ��� ������ަ �����.

%package devel
Summary:	Files for developing NCP-aware software
Summary(es):	Archivos de inclusi�n y bibliotecas para NCPfs
Summary(pl):	Pliki do tworzenia oprogramowania u�ywaj�cego NCP
Summary(pt_BR):	Arquivos de inclus�o e bibliotecas para o NCPfs
Summary(ru):	����� ��� ���������� � �������������� ���������� ncpfs
Summary(uk):	����� ��� �������� � ������������� ¦�̦����� ncpfs
Group:		Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description devel
Files for developing NCP-aware software.

%description devel -l es
Este paquete contiene los archivos de inclusi�n y bibliotecas que se
necesitan para desarrollar programas que usan NCPfs.

%description devel -l pl
Pliki do tworzenia oprogramowania u�ywaj�cego NCP.

%description devel -l pt_BR
Este pacote cont�m os arquivos de inclus�o e bibliotecas que s�o
necess�rios para desenvolver programas que usam o NCPfs.

%description devel -l ru
���� ����� �������� �����, ����������� ��� ���������� �������� �
�������������� ���������� ncpfs.

%description devel -l uk
��� ����� ͦ����� �����, ����Ȧ�Φ ��� �������� ������� �
������������� ¦�̦����� ncpfs.

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
