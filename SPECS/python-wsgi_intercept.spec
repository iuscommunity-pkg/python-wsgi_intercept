%if ! (0%{?fedora} > 12 || 0%{?rhel} > 5)
%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")}
%endif

#python major version
%{expand: %%define pyver %(%{__python} -c 'import sys;print(sys.version[0:3])')}

Name:		python-wsgi_intercept
Version:	0.5.0
Release:	1.ius%{?dist}
Summary:	installs a WSGI application in place of a real URI for testing

Group:		Applicatons/System
License:	MIT
URL:		http://pypi.python.org/pypi/wsgi_intercept
Source0:	http://pypi.python.org/packages/source/w/wsgi_intercept/wsgi_intercept-0.5.0.tar.gz

BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildArch:	noarch

BuildRequires:	python, python-setuptools
Requires:	python

%description
Testing a WSGI application normally involves starting a server at a local host and port, 
then pointing your test code to that address. Instead, this library lets you intercept calls 
to any specific host/port combination and redirect them into a WSGI application importable by your 
test program. Thus, you can avoid spawning multiple processes or threads to test your Web app.

%prep
%setup -q -n wsgi_intercept-%{version}

%build
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install -O1 \
		    --skip-build \
	     --root %{buildroot}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc PKG-INFO README.txt AUTHORS.txt CHANGELOG.txt LICENSE.txt
%{python_sitelib}/wsgi_intercept-%{version}-py%{pyver}.egg-info/
%{python_sitelib}/wsgi_intercept/


%changelog
* Fri Jun 10 2011 Jeffrey Ness <jeffrey.ness@rackspace.com> - 0.5.0-1.ius
- Initial spec
