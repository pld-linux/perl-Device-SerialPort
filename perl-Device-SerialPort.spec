#
# Conditional build:
%bcond_with	tests	# perform "make test"

%include	/usr/lib/rpm/macros.perl
%define	pdir	Device
%define	pnam	SerialPort
Summary:	Device::SerialPort - Linux/POSIX emulation of Win32::SerialPort functions
Summary(pl):	Device::SerialPort - zgodna z POSIX emulacja funcji Win32::SerialPort w Linuksie
Name:		perl-Device-SerialPort
Version:	1.000001
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	45a545acee35128ae2017a65e1e96935
BuildRequires:	perl-devel >= 1:5.8.0
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
%attr(755,root,root) %{_bindir}/modemtest
%{perl_vendorarch}/%{pdir}/*.pm
%{perl_vendorarch}/auto/%{pdir}/%{pnam}/
%attr(755,root,root) %{_examplesdir}/%{name}-%{version}
%{_mandir}/*/*
