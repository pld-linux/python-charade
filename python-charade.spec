#
# Conditional build:
%bcond_without	python2	# build CPython 2.x module
%bcond_without	python3	# build CPython 3.x module
#
%define		module	charade
Summary:	Charade - The Universal character encoding detector for Python
Summary(pl.UTF-8):	Charade - uniwersalny moduł Pythona wykrywający kodowanie znaków
Name:		python-%{module}
Version:	1.0.3
Release:	5
License:	LGPL v2.1+
Group:		Development/Languages/Python
Source0:	https://pypi.python.org/packages/source/c/charade/%{module}-%{version}.tar.gz
# Source0-md5:	79ac701a147705c09bdce31b79dfa12e
URL:		https://github.com/sigmavirus24/charade
%if %{with python2}
BuildRequires:	python-modules >= 1:2.6
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.2
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.710
Requires:	python-modules >= 1:2.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Charade: The Universal character encoding detector. This is a port of
Mark Pilgrim's excellent chardet, modified to share codebase for both
Python 2.x and 3.x.

This package contains module built for Python 2.x.

%description -l pl.UTF-8
Moduł Pythona Charade służy do automatycznego wykrywania kodowania
znaków. Jest to port znakomitego modułu chardet Marka Pilgrima,
zmodyfikowany pod kątem współdzielenia kodu między wersjami Pythona
2.x oraz 3.x.

Ten pakiet zawiera moduł zbudowany dla Pythona 2.x.

%package -n python3-charade
Summary:	Charade - The Universal character encoding detector
Summary(pl.UTF-8):	Charade - uniwersalny moduł Pythona wykrywający kodowanie znaków
Group:		Development/Languages/Python
Requires:	python3-modules >= 1:3.2

%description -n python3-charade
Charade: The Universal character encoding detector. This is a port of
Mark Pilgrim's excellent chardet, modified to share codebase for both
Python 2.x and 3.x.

This package contains module built for Python 3.x.

%description -n python3-charade -l pl.UTF-8
Moduł Pythona Charade służy do automatycznego wykrywania kodowania
znaków. Jest to port znakomitego modułu chardet Marka Pilgrima,
zmodyfikowany pod kątem współdzielenia kodu między wersjami Pythona
2.x oraz 3.x.

Ten pakiet zawiera moduł zbudowany dla Pythona 3.x.

%prep
%setup -q -n %{module}-%{version}

%build
%if %{with python2}
%py_build
%endif

%if %{with python3}
%py3_build
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python3}
%py3_install

%{__mv} $RPM_BUILD_ROOT%{_bindir}/charade{,3}
%endif

%if %{with python2}
%py_install
%py_ocomp $RPM_BUILD_ROOT%{py_sitescriptdir}
%py_comp $RPM_BUILD_ROOT%{py_sitescriptdir}
%py_postclean
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc HISTORY.rst README.rst
%attr(755,root,root) %{_bindir}/charade
%{py_sitescriptdir}/%{module}
%{py_sitescriptdir}/%{module}-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-charade
%defattr(644,root,root,755)
%doc HISTORY.rst README.rst
%attr(755,root,root) %{_bindir}/charade3
%{py3_sitescriptdir}/%{module}
%{py3_sitescriptdir}/%{module}-%{version}-py*.egg-info
%endif
