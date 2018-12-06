#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-MooseX-Role-Parameterized
Version  : 1.10
Release  : 5
URL      : https://cpan.metacpan.org/authors/id/E/ET/ETHER/MooseX-Role-Parameterized-1.10.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/E/ET/ETHER/MooseX-Role-Parameterized-1.10.tar.gz
Summary  : 'Moose roles with composition parameters'
Group    : Development/Tools
License  : Artistic-1.0-Perl
Requires: perl-MooseX-Role-Parameterized-license = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(CPAN::Meta::Check)
BuildRequires : perl(Module::Build::Tiny)
BuildRequires : perl(Module::Runtime)
BuildRequires : perl(Moose)
BuildRequires : perl(Moose::Exporter)
BuildRequires : perl(Moose::Meta::Role)
BuildRequires : perl(Moose::Role)
BuildRequires : perl(Moose::Util)
BuildRequires : perl(Moose::Util::TypeConstraints)
BuildRequires : perl(MooseX::Role::WithOverloading)
BuildRequires : perl(Test::Fatal)
BuildRequires : perl(Test::Moose)
BuildRequires : perl(Test::Requires)
BuildRequires : perl(namespace::autoclean)
BuildRequires : perl(namespace::clean)

%description
This archive contains the distribution MooseX-Role-Parameterized,
version 1.10:
Moose roles with composition parameters

%package dev
Summary: dev components for the perl-MooseX-Role-Parameterized package.
Group: Development
Provides: perl-MooseX-Role-Parameterized-devel = %{version}-%{release}

%description dev
dev components for the perl-MooseX-Role-Parameterized package.


%package license
Summary: license components for the perl-MooseX-Role-Parameterized package.
Group: Default

%description license
license components for the perl-MooseX-Role-Parameterized package.


%prep
%setup -q -n MooseX-Role-Parameterized-1.10

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-MooseX-Role-Parameterized
cp LICENSE %{buildroot}/usr/share/package-licenses/perl-MooseX-Role-Parameterized/LICENSE
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.28.1MooseX/Role/Parameterised.pm
/usr/lib/perl5/vendor_perl/5.28.1MooseX/Role/Parameterized.pm
/usr/lib/perl5/vendor_perl/5.28.1MooseX/Role/Parameterized/Extending.pod
/usr/lib/perl5/vendor_perl/5.28.1MooseX/Role/Parameterized/Meta/Role/Parameterized.pm
/usr/lib/perl5/vendor_perl/5.28.1MooseX/Role/Parameterized/Meta/Trait/Parameterizable.pm
/usr/lib/perl5/vendor_perl/5.28.1MooseX/Role/Parameterized/Meta/Trait/Parameterized.pm
/usr/lib/perl5/vendor_perl/5.28.1MooseX/Role/Parameterized/Parameters.pm
/usr/lib/perl5/vendor_perl/5.28.1MooseX/Role/Parameterized/Tutorial.pod

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/MooseX::Role::Parameterised.3
/usr/share/man/man3/MooseX::Role::Parameterized.3
/usr/share/man/man3/MooseX::Role::Parameterized::Extending.3
/usr/share/man/man3/MooseX::Role::Parameterized::Meta::Role::Parameterized.3
/usr/share/man/man3/MooseX::Role::Parameterized::Meta::Trait::Parameterizable.3
/usr/share/man/man3/MooseX::Role::Parameterized::Meta::Trait::Parameterized.3
/usr/share/man/man3/MooseX::Role::Parameterized::Parameters.3
/usr/share/man/man3/MooseX::Role::Parameterized::Tutorial.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-MooseX-Role-Parameterized/LICENSE
