Summary:	Pack of styles for fluxbox
Summary(pl):	Zestaw styli dla fluxbox
Name:		fluxbox-styles
Version:	1.0
Release:	1
License:	GPL
Group:		Themes
Source0:	http://ep09.pld-linux.org/~havner/%{name}.tar.bz2
# Source0-md5:	368b7e351e0f39fc21acb07e044eb5a6
Requires:	fluxbox
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a set of various styles for fluxbox.

%description -l pl
Zestaw ró¿nych styli dla fluxboxa.

%prep
%setup -q -n %{name}

%build

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
