%global srcname css-parser
%global sum Parse and build Cascading Style Sheets

Name:           python-css-parser
Version:        1.0.4
Release:        1%{?dist}
Summary:        Parse and build Cascading Style Sheets

License:        LGPLv3
URL:            https://github.com/ebook-utils/css-parser
Source0:        https://github.com/ebook-utils/css-parser/archive/v%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel
# for tests
BuildRequires:  python3-chardet

%description
A fork of the cssutils project based on version 1.0.2. This fork includes
general bug fixes and extensions specific to editing and working with ebooks.

%package -n python3-%{srcname}
Summary:        %{sum}
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
A fork of the cssutils project based on version 1.0.2. This fork includes
general bug fixes and extensions specific to editing and working with ebooks.

%prep
%autosetup -n %{srcname}-%{version}

%build
%py3_build

%install
%py3_install

%check
%{__python3} run_tests.py

%files -n python3-%{srcname}
%{python3_sitelib}/*
%doc README.md
%license COPYING COPYING.LESSER

%changelog
* Sun May 19 2019 Xxx Xxx <xxx@xxx.xxx> - 1.0.4-1
- Initial packaging
