%define upstream_name    Net-Libdnet
%define upstream_version 0.96

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:	2

Summary:    Perl interface to libdnet
License:    BSD
Group:		Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Net/%{upstream_name}-%{upstream_version}.tar.gz
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
