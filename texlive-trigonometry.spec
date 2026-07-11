%global tl_name trigonometry
%global tl_revision 43006

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Demonstration code for cos and sin in TeX macros
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/generic/trigonometry
License:	knuth
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/trigonometry.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/trigonometry.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
A document that both provides macros that are usable elsewhere, and
demonstrates the macros. The code uses the "classical" analytical
expansion of sin and cos (the more recent trig uses a "numerical
analyst's" expansion).

