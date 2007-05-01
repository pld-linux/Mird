Summary:	Mird - low-level database library
Summary(pl.UTF-8):	Mird - niskopoziomowa biblioteka baz danych
Name:		Mird
Version:	1.0.7
Release:	1
License:	BSD-like (see LICENSE)
Group:		Libraries
Source0:	http://www.mirar.org/mird/%{name}-%{version}.tar.gz
# Source0-md5:	0f077b7ae0f0b118edbbe34fd8fe84e9
Patch0:		%{name}-opt.patch
Patch1:		%{name}-soname.patch
URL:		http://www.mirar.org/mird/
BuildRequires:	autoconf
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# many, many warnings
%define		specflags	-fno-strict-aliasing

%description
Mird is a database library, for operating on simple disk-based
databases.

%description -l pl.UTF-8
Mird to biblioteka baz danych do operowania na prostych bazach
przechowywanych na dysku.

%package devel
Summary:	Header files for Mird library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki Mird
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for Mird library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki Mird.

%package static
Summary:	Static Mird library
Summary(pl.UTF-8):	Statyczna biblioteka Mird
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static Mird library.

%description static -l pl.UTF-8
Statyczna biblioteka Mird.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

tail -n +30 docs/tutorial.txt | head -n 44 > README
tail -n +128 docs/tutorial.txt | head -n 55 > LICENSE

%build
cd src
%{__autoconf}
cd ..
# don't run autoconf in main dir, too much hackery
%configure2_13
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_prefix}

%{__make} install \
	lib_prefix=$RPM_BUILD_ROOT%{_libdir} \
	includedir=$RPM_BUILD_ROOT%{_includedir}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README LICENSE
%attr(755,root,root) %{_libdir}/libmird.so.1

%files devel
%defattr(644,root,root,755)
%doc docs/*.html
%attr(755,root,root) %{_libdir}/lib*.so
%{_includedir}/mird.h

%files static
%defattr(644,root,root,755)
%{_libdir}/libmird.a
