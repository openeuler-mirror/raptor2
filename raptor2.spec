Name:          raptor2
Version:       2.0.15
Release:       19
Summary:       Raptor RDF parsing and serializing utility
License:       GPLv2+ or LGPLv2+ or ASL 2.0
URL:           http://librdf.org/raptor/
Source:        http://download.librdf.org/source/raptor2-%{version}.tar.gz
Patch0:        CVE-2020-25713.patch
BuildRequires: gcc-c++ curl-devel gtk-doc libicu-devel pkgconfig(libxslt) yajl-devel
Conflicts:     raptor < 1.4.21-10

%description
Raptor is Redland's RDF parser toolkit, which provides a set of independent RDF parsers
to generate triples from RDF / XML or N-Triples.

%package       devel
Summary:       Development files for raptor2
Requires:      %{name} = %{version}-%{release}

%description   devel
Development files for raptor2.

%package       help
Summary:       Help document for raptor2

%description   help
Help document for raptor2.

%prep
%autosetup -n %{name}-%{version} -p1
sed -i -e 's|"/lib /usr/lib|"/%{_lib} %{_libdir}|' configure

%build
%configure --disable-static --enable-release --with-icu-config=/usr/bin/icu-config

%make_build

%install
%make_install
%delete_la

%check
export PKG_CONFIG_PATH=%{buildroot}%{_datadir}/pkgconfig:%{buildroot}%{_libdir}/pkgconfig
test "$(pkg-config --modversion raptor2)" = "%{version}"
make check

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%doc AUTHORS ChangeLog NEWS README
%license COPYING* LICENSE.txt LICENSE-2.0.txt
%{_libdir}/libraptor2.so.0*
%{_bindir}/rapper

%files devel
%doc UPGRADING.html
%{_includedir}/raptor2/
%{_libdir}/libraptor2.so
%{_libdir}/pkgconfig/raptor2.pc
%dir %{_datadir}/gtk-doc
%dir %{_datadir}/gtk-doc/html/
%{_datadir}/gtk-doc/html/raptor2/

%files help
%{_mandir}/man1/rapper*
%{_mandir}/man3/libraptor2*

%changelog
* Wed Jul 20 2022 liangqifeng <liangqifeng@ncti-gba.com> - 2.0.15-19
- Fix CVE-2020-25713

* Mon May 18 2020 wangchen <wangchen137@huawei.com> - 2.0.15-18
- rebuild for raptor2

* Fri Dec 20 2019 shijian <shijian16@huawei.com> - 2.0.15-17
- Package init
