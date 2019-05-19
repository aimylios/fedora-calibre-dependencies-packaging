%global srcname dukpy
%global sum JavaScript runtime environment

Name:           python-dukpy
Version:        0.3
Release:        1%{?dist}
Summary:        JavaScript runtime environment

License:        MIT
URL:            https://github.com/kovidgoyal/dukpy
Source0:        https://github.com/kovidgoyal/dukpy/archive/v%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  python3-devel

%description
dukpy is a JavaScript runtime environment for Python using the duktape
embeddable JavaScript engine. With dukpy, you can run JavaScript in Python.

%package -n python3-%{srcname}
Summary:        %{sum}
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
dukpy is a JavaScript runtime environment for Python using the duktape
embeddable JavaScript engine. With dukpy, you can run JavaScript in Python.

%prep
%autosetup -n %{srcname}-%{version}

%build
%py3_build

%install
%py3_install

%files -n python3-%{srcname}
%{python3_sitearch}/dukpy*
%doc README.rst
%license LICENSE.txt

%changelog
* Sun May 19 2019 Xxx Xxx <xxx@xxx.xxx> - 0.3-1
- Initial packaging
