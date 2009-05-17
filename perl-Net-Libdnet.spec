%define module Net-Libdnet

Summary:        Perl interface to libdnet
Name:		perl-%{module}
Version:        0.92
Release:        %mkrel 1
License:        BSD
Group:		Development/Perl
Url:        http://search.cpan.org/dist/%{module}
Source:     http://www.cpan.org/modules/by-module/Net/%{module}-%{version}.tar.gz
BuildRequires:	perl-devel
BuildRequires:  libdnet-devel
BuildRequires:  perl(Class::Gomor::Array)
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
perl-Net-Libdnet provides perl bindings to the dnet library

%prep

%setup -q -n %{module}-%{version}

%build
%serverbuild

%{__perl} Makefile.PL INSTALLDIRS=vendor OPTIMIZE="$CFLAGS" LIBS="-L%{_libdir} -ldnet" INC="-I%{_includedir}"

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
