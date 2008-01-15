%define module Net-Libdnet

Summary:        Perl interface to libdnet
Name:		perl-%{module}
Version:        0.01
Release:        %mkrel 2
License:        BSD
Group:		Development/Perl
URL:            http://search.cpan.org/dist/%{module}/
Source0:        http://search.cpan.org/CPAN/authors/id/V/VM/VMAN/%{module}-%{version}.tar.gz
BuildRequires:	perl-devel
BuildRequires:  libdnet-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

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
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/Net
%{_mandir}/man?/*
