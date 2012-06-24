# TODO:
# - fix/write from scrach -devel Summary and %%description
# - fix -devel Group
Summary:	Support Utilities for ncpfs, the free netware client for Linux.
Summary(de):	Support-Dienstprogramme f�r ncpfs, den kostenlosen Netware-Client
Summary(fr):	Gestionnaires pour ncpfs, le client Netware libre pour Linux.
Summary(ja):	ncpfs �ե����륷���ƥ�桼�ƥ���ƥ���Linux �� NetWare ���饤����ȡ�
Summary(pl):	Darmowy klient Netware dla Linuxa wraz z dodatkowymi programami
Summary(tr):	Linux i�in Netware istemcisi destek yaz�l�mlar�
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
Dieses Paket enth�lt Tools zum Konfigurieren und Einsatz des
ncpfs-Dateisystems, einem Linux-Dateisystem, das das NCP-Protokoll
versteht. Dieses Protokoll wird von Novell NetWare-Clients zur
Kommunikation mit NetWare-Servern verwendet.

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

%description -l tr
Bu paket Linux'un Novell'in NCP protokolunu kullanabilmesi i�in
gereken yard�mc� yaz�l�mlar� i�ermektedir.

%package -n pam_ncp_auth
Summary:	PAM module for authenticate using using login/password stored on Netware server
Summary(pl):	Narz�dzia do konfigurowania IPX
Group:		Networking/Utilities
Requires:	%{name} = %{version}

%description -n pam_ncp_auth
The pam_ncp_auth module is PAM module for authenticate using
login/password stored on Netware server.

%package -n ipxutils
Summary:	Utilities for IPX configuration
Summary(de):	Utilities f�r IPX-Konfiguration
Summary(fr):	Utilitaires pour la configuration IPX
Summary(ja):	IPX ���󥿥ե������ȥͥåȥ��������ȥǥХå��Τ���Υġ��롣
Summary(pl):	Narz�dzia do konfigurowania IPX
Summary(tr):	IPX yap�land�rma yaz�l�mlar�
Group:		Networking/Utilities
Obsoletes:	ncpfs-ipxutils

%description -n ipxutils
This package includes utilities necessary for configuring and
debugging IPX interfaces and networks under Linux. IPX is the
low-level protocol used by NetWare to transfer data.

%description -n ipxutils -l de
Dieses Paket enth�lt Dienstprogramme zum Konfigurieren und Debuggen
von IPX-Schnittstellen und -Netzwerken unter Linux. IPX ist das von
NetWare zur Daten�bertragung verwendete Low-Level-Protokoll.

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

%description -n ipxutils -l tr
Bu paket NetWare taraf�ndan kullan�lan IPX protokol�n� yap�land�rmak
ve hatalar�n� ay�klamak i�in kullan�labilecek bir dizi uygulama
i�ermektedir.

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
