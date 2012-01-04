# revision 15878
# category Package
# catalog-ctan /info/templates/sommer
# catalog-date 2008-08-24 10:50:19 +0200
# catalog-license lppl
# catalog-version undef
Name:		texlive-templates-sommer
Version:	20080824
Release:	2
Summary:	Templates for TeX usage
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/info/templates/sommer
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/templates-sommer.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/templates-sommer.doc.tar.xz
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
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar doc %{buildroot}%{_texmfdistdir}
