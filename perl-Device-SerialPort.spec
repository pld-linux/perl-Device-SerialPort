#
# Conditional build:
%bcond_with	tests	# perform "make test"

%include	/usr/lib/rpm/macros.perl
%define	pdir	Device
%define	pnam	SerialPort
Summary:	Device::SerialPort - Linux/POSIX emulation of Win32::SerialPort functions
Summary(pl):	Device::SerialPort - zgodna z POSIX emulacja funcji Win32::SerialPort w Linuksie
Name:		perl-Device-SerialPort
Version:	0.22
Release:	1
License:	GPL/Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	4cc2590d89f4475dd3cecaa81087b5b3
BuildRequires:	perl-devel >= 5.8
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Device::SerialPort module provides an object-based user interface
essentially identical to the one provided by the Win32::SerialPort
module.

%description -l pl
Modu³ Device::SerialPort udostêpnia zorientowany obiektowo interfejs,
zasadniczo identyczny z interfejsem udostêpnianym przez modu³
Win32::SerialPort.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a eg/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Change* README TODO
%{perl_vendorarch}/%{pdir}/*.pm
%{perl_vendorarch}/auto/%{pdir}/%{pnam}/
%attr(755,root,root) %{_examplesdir}/%{name}-%{version}
%{_mandir}/man3/*
