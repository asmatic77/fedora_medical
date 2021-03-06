%global octpkg dicom
%global __provides_exclude_from ^%{octpkglibdir}/.*\\.oct$

Name:           octave-%{octpkg}
Version:        0.1.1
Release:        4%{?dist}
Summary:        Dicom processing for Octave
Group:          Applications/Engineering
License:        GPLv3+
URL:            http://octave.sourceforge.net/dicom/
Source0:        http://downloads.sourceforge.net/octave/%{octpkg}-%{version}.tar.gz
Patch0:         0001-Changed-gdcm-include-location.patch
Patch1:         0002-Drop-link-to-charls.patch

BuildRequires:  octave-devel
BuildRequires:	gdcm-devel

Requires:       octave(api) = %{octave_api}
Requires(post): octave
Requires(postun): octave

%description
The Octave-forge Image package provides functions for processing 
Digital communications in medicine (DICOM) files.

%prep
%setup -q -n %{octpkg}
%patch0 -p1
%patch1 -p1

%build
%octave_pkg_build

%install
%octave_pkg_install

%post
%octave_cmd pkg rebuild

%preun
%octave_pkg_preun

%postun
%octave_cmd pkg rebuild

%files
%{octpkglibdir}
%{octpkgdir}/


%changelog
* Mon May 13 2013 Mario Ceresa <mrceresa@fedoraproject.org> 0.1.1-4
- Fixed license
- Dropped buildroot removal in install section
- Excluded *.oct from provides

* Mon May 13 2013 Mario Ceresa <mrceresa@fedoraproject.org> 0.1.1-3
- Removed duplicated include in files
- Dropped obsolated octave-forge

* Mon May 13 2013 Mario Ceresa <mrceresa@fedoraproject.org> 0.1.1-2
- Fixed some initial problems found by fedora-review

* Mon May 13 2013 Mario Ceresa <mrceresa@fedoraproject.org> 0.1.1-1
- Initial Fedora package

