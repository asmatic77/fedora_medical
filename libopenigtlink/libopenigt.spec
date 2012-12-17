Name:		libopenigt
Version:	1.0
Release:	1%{?dist}
Summary:	Free, open-source network communication library for image-guided therapy

License:	BSD
URL:		https://github.com/openigtlink/OpenIGTLink/
Source0:	https://github.com/openigtlink/OpenIGTLink/tarball/development

BuildRequires:  

%description
OpenIGTLink provides a standardized mechanism for communications among computers
and devices in operating rooms (OR) for wide variety of image-guided therapy (IGT)
applications. Examples of such applications include:

* Stereotactic surgical guidance using optical position sensor.
* Intraoperative image guidance using real-time MRI.
* Robot-assisted intervention using robotic device and surgical planning software 

OpenIGTLink is a set of digital messaging formats and rules (protocol) used for data 
exchange on a local area network (LAN). The specification of OpenIGTLink and its 
reference implementation, the OpenIGTLink Library, are available free of charge 
for any purpose including commercial use. 

An OpenIGTLink interface is available in popular medical image processing and 
visualization software 3D Slicer.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%setup -q


%build
mkdir -p %{_target_platform}
pushd %{_target_platform}
%cmake .. \
    -DBUILD_SHARED_LIBS:BOOL=ON \
    -DBUILD_EXAMPLES:BOOL=OFF \
    -DCMAKE_BUILD_TYPE:STRING="RelWithDebInfo"\
    -DCMAKE_VERBOSE_MAKEFILE=ON\
    -DBUILD_TESTING=OFF

popd

make %{?_smp_mflags} -C %{_target_platform}

%install
rm -rf $RPM_BUILD_ROOT
%make_install -C %{_target_platform}

find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'


%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files
%doc
%{_libdir}/*.so.*

%files devel
%doc
%{_includedir}/*
%{_libdir}/*.so


%changelog
* Mon Dec 17 2012 Mario Ceresa mrceresa fedoraproject org libOpenIGTLink 1.0-1%{?dist}
- Initial import


