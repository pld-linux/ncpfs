Summary:	Support Utilities for ncpfs, the free netware client for Linux.
Summary(de):	Support-Dienstprogramme für ncpfs, den kostenlosen Netware-Client
Summary(fr):	Gestionnaires pour ncpfs, le client Netware libre pour Linux.
Summary(tr):	Linux için Netware istemcisi destek yazýlýmlarý
Summary(pl):	Darmowy klient Netware dla Linuxa wraz z dodatkowymi programami
Name:		ncpfs
Version:	2.2.0.17
Release:	1
Copyright:	GPL
Source:		ftp://platan.vc.cvut.cz/pub/linux/%{name}/%{name}-%{version}/%name-%version.tgz
Group:		Networking/Utilities
Group(pl):	Sieciowe/U¿ytki
Requires:	%name-ipxutils
Requires:	pam
BuildRequires:	glibc-devel
Prereq:		/sbin/ldconfig
Patch:		%name-lang.patch
Buildroot:	/tmp/%{name}-%{version}-root

%define	_prefix	/usr

%description
This package contains tools to help configure and use the ncpfs filesysten,
which is a linux filesystem which understands the NCP protocol. This
protocol is used by Novell NetWare clients use to talk to NetWare servers. 

%description -l pl
Pakiet zawiera narzêdzia pomocne w konfigurowaniu i u¿ywaniu systemu
plików ncpfs. Dziêki ncpfs mo¿liwe jest pod³±czanie wolumenów serwerów
Netware i modyfikowanie ich zawarto¶ci.

%package ipxutils
Summary:	Utilities for IPX configuration
Summary(de):	Utilities für IPX-Konfiguration 
Summary(fr):	Utilitaires pour la configuration IPX
Summary(tr):	IPX yapýlandýrma yazýlýmlarý
Summary(pl):	Narzêdzia do konfigurowania IPX
Group:		Networking/Utilities
Group(pl):	Sieciowe/U¿ytki
Version:	1.0
Release:	1

%description ipxutils
This package includes utilities necessary for configuring and debugging
IPX interfaces and networks under Linux. IPX is the low-level protocol
used by NetWare to transfer data.

%description -l de ipxutils
Dieses Paket enthält Dienstprogramme zum Konfigurieren und Debuggen
von IPX-Schnittstellen und -Netzwerken unter Linux. IPX ist das von 
NetWare zur Datenübertragung verwendete Low-Level-Protokoll.

%description -l de
Dieses Paket enthält Tools zum Konfigurieren und Einsatz 
des ncpfs-Dateisystems, einem Linux-Dateisystem, das das NCP-Protokoll
versteht. Dieses Protokoll wird von Novell NetWare-Clients zur Kommunikation
mit NetWare-Servern verwendet.

%description -l fr ipxutils
Ce package contient les utilitaires nécessires à pour la configuration
et le déboggage des réseaux et interfaces IPX sous Linux. IPX est un
protocole de bas niveau utilisé par NetWare pour transférer des données.

%description -l fr
Ce package contient des outils pour aider a configuer et à utiliser le
système de fichiers ncpfs, qui est un système de fichiers Linux adapté
au protocole NCP. Ce protocole est utilisé par les clients Novell NetWare
pour communiquer avec les serveurs NetWare.

%description -l tr ipxutils
Bu paket NetWare tarafýndan kullanýlan IPX protokolünü yapýlandýrmak ve
hatalarýný ayýklamak için kullanýlabilecek bir dizi uygulama içermektedir.

%description -l tr
Bu paket Linux'un Novell'in NCP protokolunu kullanabilmesi için gereken
yardýmcý yazýlýmlarý içermektedir.

%description -l pl ipxutils
Pakiet zawiera narzêdzia niezbêdne do konfigurowania interfejsów i sieci
IPX pod Linuxem. Protoko³u IPX u¿ywa Netware do przesy³ania danych.

%prep
%setup -q
%patch -p1

%build
./conf
%configure \
	--enable-pam \
	--enable-mount-v3 \
	--enable-mount-v2 \
	--enable-nds \
	--enable-warnings \
	--enable-nls 

make OPT_FLAGS="$RPM_OPT_FLAGS -w" 
make -C ipxdump OPT_FLAGS="$RPM_OPT_FLAGS -w"

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_bindir},%{_libdir}}
install -d $RPM_BUILD_ROOT/sbin
install -d $RPM_BUILD_ROOT/lib
install -d $RPM_BUILD_ROOT%{_mandir}/{man1,man5,man8}

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

(cd $RPM_BUILD_ROOT%{_mandir}/man8 ; mv ipx_cmd ipx_cmd.8 ; mv ipx_route ipx_route.8)

gzip -9nf ABOUT-NLS BUGS Changes FAQ README* ncpfs-* \
	$RPM_BUILD_ROOT%{_mandir}/man[158]/*

%find_lang ncpfs

cd $RPM_BUILD_ROOT/sbin
ln -sf ../usr/bin/ncpmount mount.ncp

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files -f ncpfs.lang
%defattr(644,root,root,755)
%doc ABOUT-NLS.gz BUGS.gz Changes.gz FAQ.gz README*.gz ncpfs-*.gz 
%attr(755,root,root) %{_bindir}/[^i]*
%attr(755,root,root) %{_libdir}/libncp.so*
%attr(755,root,root) /lib/security/pam_ncp_auth.so
%attr(755,root,root) /sbin/nwmsg
%attr(755,root,root) /sbin/mount.ncp
%{_mandir}/man8/[^i]*
%{_mandir}/man1/*
%{_mandir}/man5/*

%files ipxutils
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ipx*
%{_mandir}/man8/ipx*
