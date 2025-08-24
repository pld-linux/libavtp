#
# Conditional build:
%bcond_without	static_libs	# static libraries
#
Summary:	Implementation of Audio Video Transport Protocol (AVTP) specified in IEEE 1722-2016
Summary(pl.UTF-8):	Implementacja Audio Video Transport Protocol (AVTP) opisanego w IEEE 1722-2016
Name:		libavtp
Version:	0.2.0
Release:	1
License:	BSD
Group:		Libraries
#Source0Download: https://github.com/Avnu/libavtp/releases
Source0:	https://github.com/Avnu/libavtp/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	f0b6ecb4cb5ab0d1226067efef7a5a2b
URL:		https://github.com/AVnu/libavtp
BuildRequires:	meson >= 0.46.0
BuildRequires:	ninja >= 1.8.2
BuildRequires:	rpmbuild(macros) >= 2.042
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Open source implementation of Audio Video Transport Protocol (AVTP)
specified in IEEE 1722-2016.

%description -l pl.UTF-8
Mająca otwarte źródła implementacja protokołu transmisji obrazu i
dźwięku AVTP (Audio Video Transport Protocol), opisanego w IEEE
1722-2016.

%package devel
Summary:	Header files for AVTP library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki AVTP
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for AVTP library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki AVTP.

%package static
Summary:	Static AVTP library
Summary(pl.UTF-8):	Statyczna biblioteka AVTP
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static AVTP library.

%description static -l pl.UTF-8
Statyczna biblioteka AVTP.

%prep
%setup -q

%build
%meson \
	%{!?with_static_libs:--default-library=shared} \
	-Dtests=disabled

%meson_build

%install
rm -rf $RPM_BUILD_ROOT

%meson_install

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc LICENSE README.md
%attr(755,root,root) %{_libdir}/libavtp.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libavtp.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libavtp.so
%{_includedir}/avtp*.h
%{_pkgconfigdir}/avtp.pc

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libavtp.a
%endif
