Summary:	A 2D graphical RPG game
Summary(pl):	Darmowa gra RPG z graficznym interfejsem
Name:		adonthell
Version:	0.3.3
Release:	5
License:	GPL
Group:		X11/Applications/Games
Source0:	http://savannah.nongnu.org/download/adonthell/src/%{name}-%{version}.tar.gz
# Source0-md5:	8ed4a8b02ea24fd393b67bca355cc70b
Patch0:		%{name}-etc_dir.patch
Patch1:		%{name}-lib64.patch
URL:		http://adonthell.linuxgames.com/
BuildRequires:	SDL-devel >= 1.2.0
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	gtk+-devel
BuildRequires:	intltool
BuildRequires:	libtool
BuildRequires:	libvorbis-devel
BuildRequires:	python
BuildRequires:	python-devel
BuildRequires:	python-modules
BuildRequires:	sed >= 4.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_gamedatadir	%{_datadir}/%{name}

%description
Adonthell is a role playing game in development that aims to combine
the best features of the Final Fantasy and Ultima series with an epic
plot. It is set in a detailed virtual world. With the current engine,
a small demo game (Waste's Edge) is available.

%description -l pl
Adonthell jest ci±gle rozwijan± gr± RPG której celem jest po³±czenie
najlepszych cech takich serii jak Final Fantasy i Ultima. Akcja gry
toczy siê w szczegó³owym, wirtualnym ¶wiecie. Razem z obecnym engine
gry jest dostêpna ma³a plansza (Waste's Edge).

%prep
%setup -q
%patch0 -p1
%if "%{_lib}" == "lib64"
%patch1 -p1
%endif
:> acinclude.m4
# ugly workaround for a buggy libtool
sed -i 's/-Wl,-E/-Wl,-Xlinker,-E/' configure.in

%build
%{__gettextize}
%{__libtoolize}
intltoolize --copy --force
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--disable-py-debug

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_gamedatadir}/{modules,games},%{_bindir},adonthell-wastesedge}

cp src/modules/adonthell.py $RPM_BUILD_ROOT%{_gamedatadir}/modules/adonthell.py

%{__make} install \
	prefix=$RPM_BUILD_ROOT%{_prefix} \
	bindir=$RPM_BUILD_ROOT%{_bindir} \
	gamedatadir=$RPM_BUILD_ROOT%{_gamedatadir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog NEWBIE README.* AUTHORS NEWS
%attr(755,root,root) %{_bindir}/adonthell
%dir %{_gamedatadir}
%{_gamedatadir}/modules
%{_gamedatadir}/games
