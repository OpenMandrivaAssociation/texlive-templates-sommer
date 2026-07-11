%global tl_name templates-sommer
%global tl_revision 79121

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Templates for TeX usage
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/info/templates/sommer
License:	lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/templates-sommer.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/templates-sommer.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
A set of templates for using LaTeX packages that the author uses,
comprising: Hausarbeit.tex: for students of the Lehrstuhl Volkskunde an
der Friedrich-Schiller-Universitat Jena Psycho-Dipl.tex: for diploma
theses in psychology

