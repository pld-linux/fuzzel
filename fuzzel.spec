Summary:	Application launcher for wlroots based Wayland compositors
Name:		fuzzel
Version:	1.7.0
Release:	1
License:	MIT
Group:		Applications
Source0:	https://codeberg.org/dnkl/fuzzel/archive/%{version}.tar.gz
# Source0-md5:	85614ba43818d3c9ea960b2785ee229e
URL:		https://codeberg.org/dnkl/fuzzel/
BuildRequires:	cairo-devel
BuildRequires:	fcft-devel < 4.0.0
BuildRequires:	fcft-devel >= 3.0.0
BuildRequires:	fontconfig-devel
BuildRequires:	libpng-devel
BuildRequires:	librsvg-devel
BuildRequires:	meson >= 0.53.0
BuildRequires:	ninja
BuildRequires:	pixman-devel
BuildRequires:	pkgconfig
BuildRequires:	rpm-build >= 4.6
BuildRequires:	rpmbuild(macros) >= 1.736
BuildRequires:	scdoc
BuildRequires:	tllist-devel >= 1.0.1
BuildRequires:	wayland-devel
BuildRequires:	wayland-protocols
BuildRequires:	xorg-lib-libxkbcommon-devel
Requires:	fcft < 4.0.0
Requires:	fcft >= 3.0.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Fuzzel is a Wayland-native application launcher, similar to rofi's
drun mode.

%package -n zsh-completion-fuzzel
Summary:	ZSH completion for fuzzel command line
Group:		Applications/Shells
Requires:	%{name} = %{version}-%{release}
Requires:	zsh
BuildArch:	noarch

%description -n zsh-completion-fuzzel
ZSH completion for fuzzel command line.

%prep
%setup -q -n %{name}

%build
%meson build

%ninja_build -C build

%install
rm -rf $RPM_BUILD_ROOT

%ninja_install -C build

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG.md README.md
%attr(755,root,root) %{_bindir}/fuzzel
%{_mandir}/man1/fuzzel.1*

%files -n zsh-completion-fuzzel
%defattr(644,root,root,755)
%{zsh_compdir}/_fuzzel
