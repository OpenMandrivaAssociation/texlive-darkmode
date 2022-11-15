Name:		texlive-darkmode
Version:	64271
Release:	1
Summary:	General Dark Mode Support for LaTeX-Documents
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/darkmode
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/darkmode.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/darkmode.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/darkmode.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides an API for template and package
developers to create dynamic color schemes for light- and
darkmodes. For those unaware: We refer to dark mode when a
document has a dark background with a light font and to light
mode if it has a dark font with a light background.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/darkmode
%{_texmfdistdir}/tex/latex/darkmode
%doc %{_texmfdistdir}/doc/latex/darkmode

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
