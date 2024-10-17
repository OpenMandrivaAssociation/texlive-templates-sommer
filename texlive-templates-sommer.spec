Name:		texlive-templates-sommer
Version:	15878
Release:	2
Summary:	Templates for TeX usage
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/info/templates/sommer
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/templates-sommer.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/templates-sommer.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg

%description
A set of templates for using LaTeX packages that the author
uses, comprising: - Hausarbeit.tex: for students of the
Lehrstuhl Volkskunde an der Friedrich-Schiller-Universitat
Jena; - Psycho-Dipl.tex: for diploma theses in psychology.

#-----------------------------------------------------------------------
%files
%doc %{_texmfdistdir}/doc/latex/templates-sommer/Hausarbeit.bib
%doc %{_texmfdistdir}/doc/latex/templates-sommer/Hausarbeit.tex
%doc %{_texmfdistdir}/doc/latex/templates-sommer/Logo.jpg
%doc %{_texmfdistdir}/doc/latex/templates-sommer/Psycho-Dipl.bib
%doc %{_texmfdistdir}/doc/latex/templates-sommer/Psycho-Dipl.tex
%doc %{_texmfdistdir}/doc/latex/templates-sommer/README.de

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar doc %{buildroot}%{_texmfdistdir}
