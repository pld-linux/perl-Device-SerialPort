#
# Conditional build:
%bcond_with	tests	# perform "make test" (uses serial port)

%define		pdir	Device
%define		pnam	SerialPort
Summary:	Device::SerialPort - Linux/POSIX emulation of Win32::SerialPort functions
Summary(pl.UTF-8):	Device::SerialPort - zgodna z POSIX emulacja funcji Win32::SerialPort w Linuksie
Name:		perl-Device-SerialPort
Version:	1.04
Release:	14
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	82c698151f934eb28c65d1838cee7d9e
URL:		http://search.cpan.org/dist/Device-SerialPort/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Device::SerialPort module provides an object-based user interface
essentially identical to the one provided by the Win32::SerialPort
module.

%description -l pl.UTF-8
Moduł Device::SerialPort udostępnia zorientowany obiektowo interfejs,
zasadniczo identyczny z interfejsem udostępnianym przez moduł
Win32::SerialPort.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

# hack device test
%{__perl} -pi -e 's/^    print "\\tchecking.*$/\$file="\$test"; last;/' Makefile.PL

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor \
	TESTPORT="/dev/ttyS1"
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
%{perl_vendorarch}/Device/*.pm
%dir %{perl_vendorarch}/auto/Device/SerialPort
%attr(755,root,root) %{perl_vendorarch}/auto/Device/SerialPort/SerialPort.so
%attr(755,root,root) %{_examplesdir}/%{name}-%{version}
%{_mandir}/man[13]/*
