Summary:	Pack of styles for fluxbox
Summary(pl.UTF-8):   Zestaw styli dla fluxboksa
Name:		fluxbox-styles
Version:	1.0
Release:	2
License:	GPL
Group:		Themes
Source0:	http://ep09.pld-linux.org/~havner/%{name}.tar.bz2
# Source0-md5:	05e1eac69ffef0364dfed1863741fcb7
Requires:	fluxbox
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a set of various styles for fluxbox taken from original
fluxbox and modified by havner.

%description -l pl.UTF-8
Zestaw różnych styli dla fluxboksa wziętych z oryginalnego
fluxboksa i zmodyfikowanych przez havnera.

%prep
%setup -q -n %{name}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_datadir}/fluxbox/styles,%{_datadir}/wallpapers}

cp -R styles/* $RPM_BUILD_ROOT%{_datadir}/fluxbox/styles
cp -R wallpapers/* $RPM_BUILD_ROOT%{_datadir}/wallpapers

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_datadir}/fluxbox/styles/*
%{_datadir}/wallpapers/*
