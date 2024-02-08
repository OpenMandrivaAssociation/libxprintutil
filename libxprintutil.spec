%define major		1
%define libname		%mklibname xprintutil
%define oldlibname	%mklibname xprintutil 1
%define	develname	%mklibname xprintutil -d
%define staticname	%mklibname xprintutil -d -s

Name:    libxprintutil
Summary: The XprintUtil Library
Version: 1.0.1
Release: 17
Group:   Development/X11
License: MIT
URL: http://xorg.freedesktop.org
Source0: http://xorg.freedesktop.org/releases/individual/lib/libXprintUtil-%{version}.tar.bz2

BuildRequires: pkgconfig(x11) >= 1.0.0
BuildRequires: pkgconfig(xau) >= 1.0.0
BuildRequires: pkgconfig(xp) >= 1.0.0
BuildRequires: pkgconfig(xt) >= 1.0.0
BuildRequires: x11-proto-devel >= 1.0.0
BuildRequires: x11-util-macros >= 1.0.1

%description
The XprintUtil Library

#-----------------------------------------------------------

%package -n %{libname}
Summary:  The XprintUtil Library
Group: Development/X11
Conflicts: libxorg-x11 < 7.0
%rename %{oldlibname}
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

%files -n %{develname}
%defattr(-,root,root)
%{_libdir}/libXprintUtil.so
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
#{_libdir}/libXprintUtil.*a

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



%changelog
* Mon May 02 2011 Oden Eriksson <oeriksson@mandriva.com> 1.0.1-12mdv2011.0
+ Revision: 661560
- mass rebuild

* Sun Nov 28 2010 Oden Eriksson <oeriksson@mandriva.com> 1.0.1-11mdv2011.0
+ Revision: 602623
- rebuild

* Tue Mar 16 2010 Oden Eriksson <oeriksson@mandriva.com> 1.0.1-10mdv2010.1
+ Revision: 520970
- rebuilt for 2010.1

* Wed Sep 02 2009 Christophe Fergeau <cfergeau@mandriva.com> 1.0.1-9mdv2010.0
+ Revision: 425933
- rebuild

* Sun Nov 09 2008 Oden Eriksson <oeriksson@mandriva.com> 1.0.1-8mdv2009.1
+ Revision: 301473
- rebuilt against new libxcb

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 1.0.1-7mdv2009.0
+ Revision: 223082
- rebuild

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

  + Paulo Andrade <pcpa@mandriva.com.br>
    - Revert build requires.

* Tue Jan 15 2008 Paulo Andrade <pcpa@mandriva.com.br> 1.0.1-6mdv2008.1
+ Revision: 152864
- Update BuildRequires and rebuild

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild
    - kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Wed Aug 08 2007 Adam Williamson <awilliamson@mandriva.org> 1.0.1-4mdv2008.0
+ Revision: 60445
- rebuild for 2008
- new devel policy
- spec clean


* Wed May 31 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-05-31 18:32:34 (31796)
- rebuild to fix cooker uploading

* Mon May 29 2006 Andreas Hasenack <andreas@mandriva.com>
+ 2006-05-29 14:36:37 (31646)
- renamed mdv to packages because mdv is too generic and it's hosting only packages anyway

* Thu May 04 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-05-04 21:25:17 (26918)
- increment release

* Thu May 04 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-05-04 19:54:51 (26912)
- fixed more dependencies

* Thu Apr 27 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-04-27 04:02:05 (26704)
- Adding X.org 7.0 to the repository

