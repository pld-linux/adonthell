Summary:	A 2D graphical RPG game
Summary(pl):	Darmowa gra RPG z graficznym interfejsem
Name:		adonthell
Version:	0.3.3
Release:	1
License:	GPL
Source0:	http://savannah.nongnu.org/download/adonthell/src/%{name}-%{version}.tar.gz
URL:		http://adonthell.linuxgames.com
Group:		X11/Applications/Games
BuildRequires:	SDL-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_gamedatadir	share/%{name}

%description
Adonthell is a role playing game in development that aims to combine
the best features of the Final Fantasy and Ultima series with an epic
plot. It is set in a detailed virtual world. With the current engine,
a small demo game (Waste's Edge) is available.

%description -l pl
Adonthell jest ci�gle rozwijan� gr� RPG kt�rej celem jest po��czenie
najlepszych cech takich serii jak Final Fantasy i Ultima. Akcja gry
toczy si� w szczeg�owym, wirtualnym �wiecie. Razem z obecnym engine
gry jest dost�pna ma�a plansza(Waste's Edge).

%prep
%setup -q

%build
%configure2_13 \
	--disable-py-debug

%{__make}


%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_prefix}/%{_gamedatadir}/{modules,games},%{_bindir},adonthell-wastesedge}
cp src/modules/adonthell.py $RPM_BUILD_ROOT%{_prefix}/%{_gamedatadir}/modules/adonthell.py

%{__make} prefix=$RPM_BUILD_ROOT%{_prefix} bindir=$RPM_BUILD_ROOT%{_bindir} gamedatadir=$RPM_BUILD_ROOT%{_prefix}/%{_gamedatadir} install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_prefix}/%{_gamedatadir}/modules/*
%{_prefix}/%{_gamedatadir}/games
%attr(755,root,root)%{_bindir}/adonthell
%doc ChangeLog NEWBIE README.* AUTHORS COPYING NEWS
