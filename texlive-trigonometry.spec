Name:		texlive-trigonometry
Version:	43006
Release:	2
Summary:	Demonstration code for cos and sin in TeX macros
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/trigonometry
License:	knuth
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/trigonometry.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/trigonometry.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
A document that both provides macros that are usable elsewhere,
and demonstrates the macros. The code uses the "classical"
analytical expansion of sin and cos (the more recent trig uses
a "numerical analyst's" expansion).

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/generic/trigonometry
%doc %{_texmfdistdir}/doc/generic/trigonometry

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
