Summary:     Support Utilities for ncpfs, the free netware client for Linux.
Summary(de): Support-Dienstprogramme f�r ncpfs, den kostenlosen Netware-Client
Summary(fr): Gestionnaires pour ncpfs, le client Netware libre pour Linux.
Summary(tr): Linux i�in Netware istemcisi destek yaz�l�mlar�
Summary(pl): Darmowy klient Netware dla Linuxa wraz z dodatkowymi programami
Name:        ncpfs
Version:     2.2.0.16
Release:     1
Copyright:   GPL
#ftp:	     //platan.vc.cvut.cz
#path0:		/pub/linux/ncpfs/ncpfs-2.2.0.16
#path1:		/pub/linux/ncpfs/pam/
Source0: 	%name-%version.tgz
Source1:	pam-ncplogin.tar.gz
Group:       Networking/Utilities
Group(pl):   Sieciowe/U�ytki
Requires:    %name-ipxutils
Prereq:	     /sbin/ldconfig
Buildroot:   /tmp/%{name}-%{version}-root

%define	_prefix	/usr

%description
This package contains tools to help configure and use the ncpfs filesysten,
which is a linux filesystem which understands the NCP protocol. This
protocol is used by Novell NetWare clients use to talk to NetWare servers. 

%description -l pl
Pakiet zawiera narz�dzia pomocne w konfigurowaniu i u�ywaniu systemu
plik�w ncpfs. Dzi�ki ncpfs mo�liwe jest pod��czanie wolumen�w serwer�w
Netware i modyfikowanie ich zawarto�ci.

%package ipxutils
Summary:	Utilities for IPX configuration
Summary(de):	Utilities f�r IPX-Konfiguration 
Summary(fr):	Utilitaires pour la configuration IPX
Summary(tr):	IPX yap�land�rma yaz�l�mlar�
Summary(pl):	Narz�dzia do konfigurowania IPX
Group:		Networking/Utilities
Group(pl):	Sieciowe/U�ytki
Version:	1.0
Release:	1

%description ipxutils
This package includes utilities necessary for configuring and debugging
IPX interfaces and networks under Linux. IPX is the low-level protocol
used by NetWare to transfer data.

%description -l de ipxutils
Dieses Paket enth�lt Dienstprogramme zum Konfigurieren und Debuggen
von IPX-Schnittstellen und -Netzwerken unter Linux. IPX ist das von 
NetWare zur Daten�bertragung verwendete Low-Level-Protokoll.

%description -l de
Dieses Paket enth�lt Tools zum Konfigurieren und Einsatz 
des ncpfs-Dateisystems, einem Linux-Dateisystem, das das NCP-Protokoll
versteht. Dieses Protokoll wird von Novell NetWare-Clients zur Kommunikation
mit NetWare-Servern verwendet.

%description -l fr ipxutils
Ce package contient les utilitaires n�cessires � pour la configuration
et le d�boggage des r�seaux et interfaces IPX sous Linux. IPX est un
protocole de bas niveau utilis� par NetWare pour transf�rer des donn�es.

%description -l fr
Ce package contient des outils pour aider a configuer et � utiliser le
syst�me de fichiers ncpfs, qui est un syst�me de fichiers Linux adapt�
au protocole NCP. Ce protocole est utilis� par les clients Novell NetWare
pour communiquer avec les serveurs NetWare.

%description -l tr ipxutils
Bu paket NetWare taraf�ndan kullan�lan IPX protokol�n� yap�land�rmak ve
hatalar�n� ay�klamak i�in kullan�labilecek bir dizi uygulama i�ermektedir.

%description -l tr
Bu paket Linux'un Novell'in NCP protokolunu kullanabilmesi i�in gereken
yard�mc� yaz�l�mlar� i�ermektedir.

%description -l pl ipxutils
Pakiet zawiera narz�dzia niezb�dne do konfigurowania interfejs�w i sieci
IPX pod Linuxem. Protoko�u IPX u�ywa Netware do przesy�ania danych.

%prep
%setup -q
#%patch0 -p1
#%patch1 -p1 
#%patch2 -p1 
#%patch3 -p0 
#%patch4 -p1 

#rm -f sutil/ncplib.h

%build
./configure %{_target_platform} \
	--prefix=%{_prefix} \
	--enable-pam \
	--infodir=%{_prefix}/share/info \
	--mandir=%{_prefix}/share/man \
	--enable-nls 

make OPT_FLAGS="$RPM_OPT_FLAGS -w" 
make -C ipxdump OPT_FLAGS="$RPM_OPT_FLAGS -w"

%clean
rm -rf $RPM_BUILD_ROOT

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_bindir},%{_libdir}}
install -d $RPM_BUILD_ROOT/sbin
install -d $RPM_BUILD_ROOT/lib
install -d $RPM_BUILD_ROOT%{_mandir}/{man1,man5,man8}

#make prefix=$RPM_BUILD_ROOT%{_prefix} install DESTDIR=$RPM_BUILD_ROOT%{_prefix}

## instal intl
make prefix=$RPM_BUILD_ROOT%{_prefix} -C intl install  

## install po
make prefix=$RPM_BUILD_ROOT%{_prefix} -C po install

## install lib
install -s lib/libncp.so.2.3.0 $RPM_BUILD_ROOT%{_libdir}

## install sutil
install -s sutil/nwsfind sutil/ncpmount sutil/ncpumount $RPM_BUILD_ROOT%{_bindir}

## instal util 

for i in slist pqlist nwfsinfo pserver nprint nsend nwpasswd nwbols nwbocreate nwborm nwboprops pqstat pqrm nwbpcreate nwbprm nwbpvalues nwbpadd nwbpset nwgrant nwrevoke nwuserlist nwrights nwauth nwfstime nwvolinfo nwtrustee nwpurge nwdir nwfsctrl nwdpvalues ncopy ; do
	install -s util/$i $RPM_BUILD_ROOT%{_bindir}
done	

install -s util/nwmsg $RPM_BUILD_ROOT/sbin

#make prefix=$RPM_BUILD_ROOT%{_prefix} -C util install

## install man

install man/*.1 $RPM_BUILD_ROOT%{_mandir}/man1
install man/*.5 $RPM_BUILD_ROOT%{_mandir}/man5
install man/*.8 $RPM_BUILD_ROOT%{_mandir}/man8

## install ipx-1.0

install -s ipx-1.0/ipx_configure ipx-1.0/ipx_interface ipx-1.0/ipx_internal_net ipx-1.0/ipx_route ipx-1.0/ipx_cmd $RPM_BUILD_ROOT/%{_bindir}

install ipx-1.0/ipx_configure.8 ipx-1.0/ipx_interface.8 ipx-1.0/ipx_internal_net.8 ipx-1.0/ipx_route ipx-1.0/ipx_cmd $RPM_BUILD_ROOT%{_mandir}/man8

## install PAM
	install -d $RPM_BUILD_ROOT/lib/security
install contrib/pam/pam_ncp_auth.so $RPM_BUILD_ROOT/lib/security

install -s ipxdump/ipxdump ipxdump/ipxparse $RPM_BUILD_ROOT%{_bindir}

chmod 755 $RPM_BUILD_ROOT%{_libdir}/*.so.*

bzip2 -9 ABOUT-NLS BUGS Changes FAQ README* ncpfs-* 

## bzipped man pages
bzip2 -9 $RPM_BUILD_ROOT%{_mandir}/man[158]/*

%find_lang ncpfs

cd $RPM_BUILD_ROOT/sbin
ln -sf ../usr/bin/ncpmount mount.ncp

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files -f ncpfs.lang
%defattr(644,root,root,755)
%doc ABOUT-NLS.bz2 BUGS.bz2 Changes.bz2 FAQ.bz2 README*.bz2 ncpfs-*.bz2 

%attr(755,root,root) %{_bindir}/[^i]*
%attr(755,root,root) %{_libdir}/libncp.so*
%attr(755,root,root) /lib/security/pam_ncp_auth.so
%attr(755,root,root) /sbin/nwmsg
%attr(  -,root,root) /sbin/mount.ncp

%attr(644,root, man) %{_mandir}/man8/[^i]*
%attr(644,root, man) %{_mandir}/man1/*
%attr(644,root, man) %{_mandir}/man5/*

%files ipxutils
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ipx*
%attr(644,root, man) %{_mandir}/man8/ipx*
