%global tl_name darkmode
%global tl_revision 76924

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.0.1
Release:	%{tl_revision}.1
Summary:	General Dark Mode Support for LaTeX-Documents
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/darkmode
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/darkmode.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/darkmode.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/darkmode.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package provides an API for template and package developers to
create dynamic color schemes for light- and darkmodes. For those
unaware: We refer to dark mode when a document has a dark background
with a light font and to light mode if it has a dark font with a light
background.

