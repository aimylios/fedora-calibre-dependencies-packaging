%global srcname unrardll
%global sum Python wrapper for the UnRAR DLL

Name:           python-unrardll
Version:        0.1.3
Release:        1%{?dist}
Summary:        Python wrapper for the UnRAR DLL

License:        BSD
URL:            https://github.com/kovidgoyal/unrardll
Source0:        https://github.com/kovidgoyal/unrardll/archive/v%{version}.tar.gz

BuildRequires:  libunrar-devel
BuildRequires:  python3-devel

%description
Python wrapper for the UnRAR DLL.

%package -n python3-%{srcname}
Summary:        %{sum}
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
Python wrapper for the UnRAR DLL.

%prep
%autosetup -n %{srcname}-%{version}

%build
%py3_build

%install
%py3_install

%files -n python3-%{srcname}
%{python3_sitearch}/unrardll*
%doc README.rst
%license LICENSE

%changelog
* Sun May 19 2019 Xxx Xxx <xxx@xxx.xxx> - 0.1.3-1
- Initial packaging
