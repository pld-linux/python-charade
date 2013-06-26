# Conditional build:
%bcond_without  python2         # build python 2 module
%bcond_without  python3         # build python 3 module
#
%define 	module	charade
Summary:	The Universal character encoding detector
Name:		python-%{module}
Version:	1.0.3
Release:	1
License:	LGPL 2.1+
Group:		Development/Languages/Python
Source0:	https://pypi.python.org/packages/source/c/charade/%{module}-%{version}.tar.gz
# Source0-md5:	79ac701a147705c09bdce31b79dfa12e
URL:		https://github.com/sigmavirus24/charade
%if %{with python2}
BuildRequires:	python-modules >= 1:2.6
%endif
%if %{with python3}
BuildRequires:	python3-modules
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
Requires:	python-modules >= 1:2.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Charade: The Universal character encoding detector. This is a port of
Mark Pilgrim's excellent chardet. Previous two versions needed to be
maintained: one that supported python 2.x and one that supported
python 3.x. With the minor amount of work placed into this port,
charade now supports both in one codebase. The base for the work was
Mark's last available copy of the chardet source for python 3000.

%package -n python3-charade
Summary:	The Universal character encoding detector
Group:		Development/Languages/Python
Requires:	python3-modules

%description -n python3-charade
Charade: The Universal character encoding detector. This is a port of
Mark Pilgrim's excellent chardet. Previous two versions needed to be
maintained: one that supported python 2.x and one that supported
python 3.x. With the minor amount of work placed into this port,
charade now supports both in one codebase. The base for the work was
Mark's last available copy of the chardet source for python 3000.

%prep
%setup -q -n %{module}-%{version}

%build
%if %{with python2}
%{__python} setup.py build -b py2
%endif

%if %{with python3}
%{__python3} setup.py build -b py3
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%{__python} setup.py \
	build -b py2 \
	install \
	--skip-build \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT
%py_ocomp $RPM_BUILD_ROOT%{py_sitescriptdir}
%py_comp $RPM_BUILD_ROOT%{py_sitescriptdir}
%py_postclean
%endif

%if %{with python3}
%{__python3} setup.py  \
	build -b py3 \
	install \
	--skip-build \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc HISTORY.rst README.rst
%{py_sitescriptdir}/%{module}
%if "%{py_ver}" > "2.4"
%{py_sitescriptdir}/%{module}-%{version}-py*.egg-info
%endif
%endif

%if %{with python3}
%files -n python3-charade
%defattr(644,root,root,755)
%doc HISTORY.rst README.rst
%{py3_sitescriptdir}/%{module}
%{py3_sitescriptdir}/%{module}-%{version}-py*.egg-info
%endif
