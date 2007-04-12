%define libxprintutil %mklibname xprintutil 1
Name: libxprintutil
Summary:  The XprintUtil Library
Version: 1.0.1
Release: %mkrel 3
Group: Development/X11
License: MIT
URL: http://xorg.freedesktop.org
Source0: http://xorg.freedesktop.org/releases/individual/lib/libXprintUtil-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-root

BuildRequires: libx11-devel >= 1.0.0
BuildRequires: libxau-devel >= 1.0.0
BuildRequires: libxp-devel >= 1.0.0
BuildRequires: libxt-devel >= 1.0.0
BuildRequires: x11-proto-devel >= 1.0.0
BuildRequires: x11-util-macros >= 1.0.1

%description
The XprintUtil Library

#-----------------------------------------------------------

%package -n %{libxprintutil}
Summary:  The XprintUtil Library
Group: Development/X11
Conflicts: libxorg-x11 < 7.0
Provides: %{name} = %{version}

%description -n %{libxprintutil}
The XprintUtil Library

#-----------------------------------------------------------

%package -n %{libxprintutil}-devel
Summary: Development files for %{name}
Group: Development/X11

Requires: %{libxprintutil} = %{version}
Requires: libx11-devel >= 1.0.0
Requires: libxt-devel >= 1.0.0
Requires: x11-proto-devel >= 1.0.0
Provides: libxprintutil-devel = %{version}-%{release}

Conflicts: libxorg-x11-devel < 7.0

%description -n %{libxprintutil}-devel
Development files for %{name}

%pre -n %{libxprintutil}-devel
if [ -h %{_includedir}/X11 ]; then
	rm -f %{_includedir}/X11
fi

%files -n %{libxprintutil}-devel
%defattr(-,root,root)
%{_libdir}/libXprintUtil.so
%{_libdir}/libXprintUtil.la
%{_libdir}/pkgconfig/xprintutil.pc
%{_includedir}/X11/XprintUtil/xprintutil.h

#-----------------------------------------------------------

%package -n %{libxprintutil}-static-devel
Summary: Static development files for %{name}
Group: Development/X11
Requires: %{libxprintutil}-devel = %{version}
Provides: libxprintutil-static-devel = %{version}-%{release}

Conflicts: libxorg-x11-static-devel < 7.0

%description -n %{libxprintutil}-static-devel
Static development files for %{name}

%files -n %{libxprintutil}-static-devel
%defattr(-,root,root)
%{_libdir}/libXprintUtil.a

#-----------------------------------------------------------

%prep
%setup -q -n libXprintUtil-%{version}

%build
%configure2_5x	--x-includes=%{_includedir}\
		--x-libraries=%{_libdir}

%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -n %{libxprintutil}
%defattr(-,root,root)
%{_libdir}/libXprintUtil.so.1
%{_libdir}/libXprintUtil.so.1.0.0


