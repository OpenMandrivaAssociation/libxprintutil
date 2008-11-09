%define name	libxprintutil
%define version	1.0.1
%define release	%mkrel 8

%define major		1
%define libname		%mklibname xprintutil %{major}
%define	develname	%mklibname xprintutil -d
%define staticname	%mklibname xprintutil -d -s

Name: %{name}
Summary:  The XprintUtil Library
Version: %{version}
Release: %{release}
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

%package -n %{libname}
Summary:  The XprintUtil Library
Group: Development/X11
Conflicts: libxorg-x11 < 7.0
Provides: %{name} = %{version}

%description -n %{libname}
The XprintUtil Library

#-----------------------------------------------------------

%package -n %{develname}
Summary: Development files for %{name}
Group: Development/X11

Requires: %{libname} = %{version}
Requires: libx11-devel >= 1.0.0
Requires: libxt-devel >= 1.0.0
Requires: x11-proto-devel >= 1.0.0
Provides: %{name}-devel = %{version}-%{release}
Conflicts: libxorg-x11-devel < 7.0
Obsoletes: %{mklibname xprintutil 1 -d}

%description -n %{develname}
Development files for %{name}

%pre -n %{develname}
if [ -h %{_includedir}/X11 ]; then
	rm -f %{_includedir}/X11
fi

%files -n %{develname}
%defattr(-,root,root)
%{_libdir}/libXprintUtil.so
%{_libdir}/libXprintUtil.la
%{_libdir}/pkgconfig/xprintutil.pc
%{_includedir}/X11/XprintUtil/xprintutil.h

#-----------------------------------------------------------

%package -n %{staticname}
Summary: Static development files for %{name}
Group: Development/X11
Requires: %{develname} = %{version}
Provides: libxprintutil-static-devel = %{version}-%{release}
Conflicts: libxorg-x11-static-devel < 7.0
Obsoletes: %{mklibname xprintutil 1 -d -s}

%description -n %{staticname}
Static development files for %{name}

%files -n %{staticname}
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

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/libXprintUtil.so.%{major}*

