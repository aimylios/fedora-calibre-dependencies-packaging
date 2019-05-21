%global srcname sgmllib
%global sum Parsing text files formatted in SGML

Name:           python-sgmllib
Version:        1.0.0
Release:        1%{?dist}
Summary:        Parsing text files formatted in SGML

License:        BSD
URL:            https://pypi.org/project/sgmllib3k/
Source0:        https://files.pythonhosted.org/packages/9e/bd/3704a8c3e0942d711c1299ebf7b9091930adae6675d7c8f476a7ce48653c/sgmllib3k-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python3-devel

%description
This module defines a class SGMLParser which serves as the basis for parsing
text files formatted in SGML (Standard Generalized Mark-up Language). In fact,
it does not provide a full SGML parser — it only parses SGML insofar as it is
used by HTML, and the module only exists as a base for the htmllib module.
Another HTML parser which supports XHTML and offers a somewhat different
interface is available in the HTMLParser module.

%package -n python3-%{srcname}
Summary:        %{sum}
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
This module defines a class SGMLParser which serves as the basis for parsing
text files formatted in SGML (Standard Generalized Mark-up Language). In fact,
it does not provide a full SGML parser — it only parses SGML insofar as it is
used by HTML, and the module only exists as a base for the htmllib module.
Another HTML parser which supports XHTML and offers a somewhat different
interface is available in the HTMLParser module.

%prep
%autosetup -n %{srcname}3k-%{version}

%build
%py3_build

%install
%py3_install

%files -n python3-%{srcname}
%{python3_sitelib}/*
%doc README

%changelog
* Tue May 21 2019 Xxx Xxx <xxx@xxx.xxx> - 1.0.0-1
- Initial packaging
