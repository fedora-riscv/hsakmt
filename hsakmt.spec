Name:           hsakmt
Version:        1.0.0
Release:        5%{?dist}
Summary:        AMD's HSA thunk library

Group:          System Environment/Libraries
# The entire source code is MIT except auto-generated file ltmain.sh which is GPLv2
License:        MIT and GPLv2
URL:            http://cgit.freedesktop.org/amd/hsakmt/
Source0:        http://xorg.freedesktop.org/archive/individual/lib/hsakmt-%{version}.tar.bz2
ExcludeArch:    %{arm} %{ix86}
BuildRequires:  automake autoconf libtool

%description
hsakmt is a thunk library for AMD's HSA Linux kernel driver (amdkfd)

%package devel
Summary: AMD HSA thunk library development package
Group: Development/Libraries
Requires: %{name}%{?isa} = %{version}-%{release}
Requires: pkgconfig

%description devel
Development library for hsakmt.

%prep
%setup -q -n hsakmt-%{version}

%build
%configure \
  --disable-static

make %{?_smp_mflags} V=1

%install
make install DESTDIR=%{buildroot}

find %{buildroot} -type f -name "*.la" -delete

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%license COPYING
%{_libdir}/libhsakmt-1*.so.*

%files devel
%dir %{_includedir}/hsakmt-1
%{_includedir}/hsakmt-1/hsakmt.h
%{_includedir}/hsakmt-1/hsakmttypes.h
%{_libdir}/libhsakmt-1*.so
%{_libdir}/pkgconfig/hsakmt-1.pc

%changelog
* Fri Nov 13 2015 Oded Gabbay <oded.gabbay@gmail.com> 1.0.0-5
- Don't build for arm and i686

* Fri Nov 13 2015 Oded Gabbay <oded.gabbay@gmail.com> 1.0.0-4
- Rename package back to hsakmt

* Sun Nov 1 2015 Oded Gabbay <oded.gabbay@gmail.com> 1.0.0-3
- Rename package to libhsakmt

* Thu Oct 29 2015 Oded Gabbay <oded.gabbay@gmail.com> 1.0.0-2
- Changed doc to license
- Added GPLv2 to license
- Changed RPM_BUILD_ROOT to {buildroot}

* Sat Oct 24 2015 Oded Gabbay <oded.gabbay@gmail.com> 1.0.0-1
- Initial release of hsakmt, ver. 1.0.0
