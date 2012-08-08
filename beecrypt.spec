Summary:	The BeeCrypt Cryptography Library
Name:		beecrypt
Version:	4.2.1
Release:	4
Epoch:		2
License:	LGPL
Group:		Libraries
Source0:	http://downloads.sourceforge.net/beecrypt/%{name}-%{version}.tar.gz
# Source0-md5:	8441c014170823f2dff97e33df55af1e
URL:		http://sourceforge.net/projects/beecrypt/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%ifarch %{ix86}
%define		specflags	-mmmx -msse -msse2
%endif

%description
BeeCrypt is an open source cryptography library that contains highly
optimized C and assembler implementations of many well-known
algorithms including Blowfish, MD5, SHA-1, Diffie-Hellman, and
ElGamal.

%package devel
Summary:	The BeeCrypt Cryptography Library - development files
Group:		Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description devel
The BeeCrypt Cryptography Library - development files.

%prep
%setup -q

# avoid stdc++ dependency
%{__sed} -i -e 's/ cppglue\.cxx$//' Makefile.am

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-openmp	\
	--enable-static=no	\
	--without-cplusplus	\
	--without-java		\
	--without-python
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/%{_lib}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{py_sitedir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /usr/sbin/ldconfig
%postun -p /usr/sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS BENCHMARKS BUGS CONTRIBUTORS NEWS README
%attr(755,root,root) %ghost %{_libdir}/libbeecrypt.so.?
%attr(755,root,root) %{_libdir}/libbeecrypt.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libbeecrypt.so
%{_libdir}/libbeecrypt.la
%{_includedir}/beecrypt

