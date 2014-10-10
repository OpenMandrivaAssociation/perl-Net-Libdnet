%define upstream_name    Net-Libdnet
%define upstream_version 0.98
Name:       perl-%{upstream_name}
Version:    %perl_convert_version 0.98
Release:	2

Summary:    Perl interface to libdnet
License:    BSD
Group:		Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Net/Net-Libdnet-0.98.tar.gz
BuildRequires:  libdnet-devel
BuildRequires:  perl(Class::Gomor::Array)
BuildRequires:	perl-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

%description
perl-Net-Libdnet provides perl bindings to the dnet library

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%serverbuild
%{__perl} Makefile.PL INSTALLDIRS=vendor OPTIMIZE="$CFLAGS -fno-PIE" LIBS="-L%{_libdir} -ldnet" INC="-I%{_includedir}"
%make LD_RUN_PATH=""

%check
make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc Changes LICENSE README
%{_bindir}/*
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/Net
%{_mandir}/man?/*


%changelog
* Sun Feb 12 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 0.960.0-2
+ Revision: 773487
- really ensure -fno-PIE...
- new version
- svn commit -m mass rebuild of perl extension against perl 5.14.2

* Sun May 15 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.950.0-1
+ Revision: 674919
- new version

* Wed Feb 02 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.940.0-1
+ Revision: 635205
- update to new version 0.94

* Wed Jul 29 2009 Jérôme Quelin <jquelin@mandriva.org> 0.920.0-1mdv2010.0
+ Revision: 404095
- rebuild using %%perl_convert_version

* Sun May 17 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.92-1mdv2010.0
+ Revision: 376727
- update to new version 0.92

* Tue Dec 09 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.91-1mdv2009.1
+ Revision: 312183
- update to new version 0.91

* Tue Dec 02 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.90-1mdv2009.1
+ Revision: 309340
- new version

* Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 0.01-6mdv2009.0
+ Revision: 258054
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 0.01-5mdv2009.0
+ Revision: 246154
- rebuild

* Wed Jan 23 2008 Thierry Vignaud <tv@mandriva.org> 0.01-3mdv2008.1
+ Revision: 157264
- rebuild with fixed %%serverbuild macro

* Tue Jan 15 2008 Thierry Vignaud <tv@mandriva.org> 0.01-2mdv2008.1
+ Revision: 152220
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Fri Jul 20 2007 Oden Eriksson <oeriksson@mandriva.com> 0.01-1mdv2008.0
+ Revision: 53925
- Import perl-Net-Libdnet



* Fri Jul 20 2007 Oden Eriksson <oeriksson@mandriva.com> 0.01-1mdv2008.0
- initial Mandriva package

