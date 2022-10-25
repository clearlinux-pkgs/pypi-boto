#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-boto
Version  : 2.49.0
Release  : 92
URL      : https://files.pythonhosted.org/packages/c8/af/54a920ff4255664f5d238b5aebd8eedf7a07c7a5e71e27afcfe840b82f51/boto-2.49.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/c8/af/54a920ff4255664f5d238b5aebd8eedf7a07c7a5e71e27afcfe840b82f51/boto-2.49.0.tar.gz
Summary  : Amazon Web Services Library
Group    : Development/Tools
License  : MIT
Requires: pypi-boto-bin = %{version}-%{release}
Requires: pypi-boto-python = %{version}-%{release}
Requires: pypi-boto-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(httpretty)
BuildRequires : pypi(mock)
BuildRequires : pypi(nose)
BuildRequires : pypi(pbr)
BuildRequires : pypi(pip)
BuildRequires : pypi(requests)
BuildRequires : pypi(setuptools)
BuildRequires : python3-dev

%description
boto
        ####
        boto 2.49.0

%package bin
Summary: bin components for the pypi-boto package.
Group: Binaries

%description bin
bin components for the pypi-boto package.


%package python
Summary: python components for the pypi-boto package.
Group: Default
Requires: pypi-boto-python3 = %{version}-%{release}

%description python
python components for the pypi-boto package.


%package python3
Summary: python3 components for the pypi-boto package.
Group: Default
Requires: python3-core
Provides: pypi(boto)

%description python3
python3 components for the pypi-boto package.


%prep
%setup -q -n boto-2.49.0
cd %{_builddir}/boto-2.49.0
pushd ..
cp -a boto-2.49.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1656362108
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
python2 tests/test.py default || :
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 setup.py build

popd
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -tt setup.py build install --root=%{buildroot}-v3
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/asadmin
/usr/bin/bundle_image
/usr/bin/cfadmin
/usr/bin/cq
/usr/bin/cwutil
/usr/bin/dynamodb_dump
/usr/bin/dynamodb_load
/usr/bin/elbadmin
/usr/bin/fetch_file
/usr/bin/glacier
/usr/bin/instance_events
/usr/bin/kill_instance
/usr/bin/launch_instance
/usr/bin/list_instances
/usr/bin/lss3
/usr/bin/mturk
/usr/bin/pyami_sendmail
/usr/bin/route53
/usr/bin/s3put
/usr/bin/sdbadmin
/usr/bin/taskadmin

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
