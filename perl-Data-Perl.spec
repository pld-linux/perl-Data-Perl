#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	Data
%define		pnam	Perl
Summary:	Data::Perl - Base classes wrapping fundamental Perl data types.
Name:		perl-Data-Perl
Version:	0.002009
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Data/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	2c38f8d7b50a986602a93b93a3cfe40f
URL:		http://search.cpan.org/dist/Data-Perl/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Class-Method-Modifiers
BuildRequires:	perl-List-MoreUtils
BuildRequires:	perl-Module-Runtime
BuildRequires:	perl-Role-Tiny
BuildRequires:	perl-strictures
BuildRequires:	perl-Test-Deep
BuildRequires:	perl-Test-Fatal
BuildRequires:	perl-Test-Output
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Data::Perl is a collection of classes that wrap fundamental data types that
exist in Perl. These classes and methods as they exist today are an attempt to
mirror functionality provided by Moose's Native Traits. One important thing to
note is all classes currently do no validation on constructor input.

Data::Perl is a container class for the following classes:

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Data/*.pm
%{perl_vendorlib}/Data/Perl
%{_mandir}/man3/*
