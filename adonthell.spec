Summary:	A 2D graphical RPG game
Summary(pl):	Darmowa gra RPG z graficznym interfejsem
Name:		adonthell
Version:	0.3.2
Release:	1
License:	GPL
Source0:	http://freesoftware.fsf.org/download/adonthell/%{name}-%{version}.tar.gz
Source1:	http://freesoftware.fsf.org/download/adonthell/wastesedge-0.3.1.tar.gz
Patch0:		%{name}-lib.patch
URL:		http://adonthell.linuxgames.com
Group:		X11/Applications/Games
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define 	_prefix		/usr/X11R6
%define		_bindir		%{_prefix}/bin/
%define		_gamedatadir	share/%{name}

%description
Adonthell is a role playing game in development that aims to combine
the best features of the Final Fantasy and Ultima series with an epic
plot. It is set in a detailed virtual world. With the current engine,
a small demo game (Waste's Edge) is available.

%description -l pl
Adonthell jest ci±gle rozwijan± gr± RPG której celem jest po³±czenie
najlepszych cech takich serii jak Final Fantasy i Ultima. Akcja gry
toczy siê w szczegó³owym, wirtualnym ¶wiecie. Razem z obecnym engine
gry jest dostêpna ma³a plansza(Waste's Edge).

%prep
%setup -q
%patch -p0

%build
%configure2_13

%{__make}


%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_prefix}/%{_gamedatadir}/{modules,games},%{_bindir},adonthell-wastesedge}
cp src/adonthell.py $RPM_BUILD_ROOT%{_prefix}/%{_gamedatadir}/modules/adonthell.py

%{__make} prefix=$RPM_BUILD_ROOT%{_prefix} bindir=$RPM_BUILD_ROOT%{_bindir} gamedatadir=$RPM_BUILD_ROOT%{_prefix}/%{_gamedatadir} install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_prefix}/%{_gamedatadir}/modules/adonthell.py
%{_prefix}/%{_gamedatadir}/games
%attr(755,root,root)%{_bindir}/adonthell
%doc ChangeLog NEWBIE README.* AUTHORS COPYING NEWS
