%define latexmldir %{_texmf_main}/tex/latex/latexml
Name:           LaTeXML
Version:        0.7.0
Release:        1%{?dist}
Summary:        Transforms TeX and LaTeX into XML
License:        Public Domain
Group:          Applications/Publishing
URL:            http://dlmf.nist.gov/LaTeXML/
Source0:        http://dlmf.nist.gov/LaTeXML/releases/LaTeXML-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Parse::RecDescent)
BuildRequires:  perl(Test::Simple)
BuildRequires:  perl(XML::LibXML) >= 1.61
BuildRequires:  perl(XML::LibXSLT) >= 1.58
Requires:       perl(Parse::RecDescent)
Requires:       perl(Test::Simple)
Requires:       perl(XML::LibXML) >= 1.61
Requires:       perl(XML::LibXSLT) >= 1.58
Requires:       perl(DB_File)
Requires:       perl(Image::Magick)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))
Requires:       tex(tex)
Requires(post): tex(tex)
Requires(postun): tex(tex)

%description
METHODS

%prep
%setup -q

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor TEXMF=%{_texmf_main}
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT

# Isn't PERL_INSTALL_ROOT obsolete, or something?
# make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
make pure_install DESTDIR=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%clean
rm -rf $RPM_BUILD_ROOT

%post
mktexlsr >/dev/null 2>&1 || :

%postun
mktexlsr >/dev/null 2>&1 || :

%files
%defattr(-,root,root,-)
%doc Changes manual.pdf README INSTALL
%{_bindir}/*
%{perl_vendorlib}/*
%{_mandir}/man1/*
%{_mandir}/man3/*
%{latexmldir}/*

%changelog
* Fri Mar 13 2009 Bruce Miller <bruce.miller@nist.gov> 0.7.0-1
- Specfile autogenerated by cpanspec 1.77.
