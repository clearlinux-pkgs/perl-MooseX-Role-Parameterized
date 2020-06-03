#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-MooseX-Role-Parameterized
Version  : 1.11
Release  : 13
URL      : https://cpan.metacpan.org/authors/id/E/ET/ETHER/MooseX-Role-Parameterized-1.11.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/E/ET/ETHER/MooseX-Role-Parameterized-1.11.tar.gz
Summary  : 'Moose roles with composition parameters'
Group    : Development/Tools
License  : Artistic-1.0-Perl
Requires: perl-MooseX-Role-Parameterized-license = %{version}-%{release}
Requires: perl-MooseX-Role-Parameterized-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(CPAN::Meta::Check)
BuildRequires : perl(ExtUtils::Config)
BuildRequires : perl(ExtUtils::Helpers)
BuildRequires : perl(ExtUtils::InstallPaths)
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
BuildRequires : perl(Test::Needs)
BuildRequires : perl(Test::Requires)
BuildRequires : perl(namespace::autoclean)
BuildRequires : perl(namespace::clean)

%description
This archive contains the distribution MooseX-Role-Parameterized,
version 1.11:
Moose roles with composition parameters

%package dev
Summary: dev components for the perl-MooseX-Role-Parameterized package.
Group: Development
Provides: perl-MooseX-Role-Parameterized-devel = %{version}-%{release}
Requires: perl-MooseX-Role-Parameterized = %{version}-%{release}

%description dev
dev components for the perl-MooseX-Role-Parameterized package.


%package license
Summary: license components for the perl-MooseX-Role-Parameterized package.
Group: Default

%description license
license components for the perl-MooseX-Role-Parameterized package.


%package perl
Summary: perl components for the perl-MooseX-Role-Parameterized package.
Group: Default
Requires: perl-MooseX-Role-Parameterized = %{version}-%{release}

%description perl
perl components for the perl-MooseX-Role-Parameterized package.


%prep
%setup -q -n MooseX-Role-Parameterized-1.11
cd %{_builddir}/MooseX-Role-Parameterized-1.11

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
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
cp %{_builddir}/MooseX-Role-Parameterized-1.11/LICENSE %{buildroot}/usr/share/package-licenses/perl-MooseX-Role-Parameterized/02baa9a7c1e8cd4e565c56a6af13a63d650805ef
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
/usr/share/package-licenses/perl-MooseX-Role-Parameterized/02baa9a7c1e8cd4e565c56a6af13a63d650805ef

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.30.3/MooseX/Role/Parameterised.pm
/usr/lib/perl5/vendor_perl/5.30.3/MooseX/Role/Parameterized.pm
/usr/lib/perl5/vendor_perl/5.30.3/MooseX/Role/Parameterized/Extending.pod
/usr/lib/perl5/vendor_perl/5.30.3/MooseX/Role/Parameterized/Meta/Role/Parameterized.pm
/usr/lib/perl5/vendor_perl/5.30.3/MooseX/Role/Parameterized/Meta/Trait/Parameterizable.pm
/usr/lib/perl5/vendor_perl/5.30.3/MooseX/Role/Parameterized/Meta/Trait/Parameterized.pm
/usr/lib/perl5/vendor_perl/5.30.3/MooseX/Role/Parameterized/Parameters.pm
/usr/lib/perl5/vendor_perl/5.30.3/MooseX/Role/Parameterized/Tutorial.pod
