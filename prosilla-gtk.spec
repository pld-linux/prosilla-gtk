
Summary:	ProSilla - a program which accelerates file transfers over ssh (gtk version)
Summary(pl):	ProSilla - program przyspieszaj�cy pobieranie du�ych plik�w przez ssh (wersja gtk)
Name:		prosilla-gtk
Version:	1.2
Release:	1
License:	GPL
Group:		Applications/Networking
Source0:	http://www.v-lo.krakow.pl/~anszom/prosilla/prosilla-%{version}.tgz
# Source0-md5:	a22c90786122ea1ab6cfd3807001d23e
URL:		http://www.v-lo.krakow.pl/~anszom/prosilla/
BuildRequires:	gtk+-devel
BuildRequires:	libstdc++-devel
BuildRequires:	ncurses-devel
Provides:	prosilla
Obsoletes:	prosilla
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ProSilla is a program which accelerates file transfers over ssh by
opening multiple connections just like other download accelerators.
The only difference is that proSilla uses ssh instead of http/ftp for
download. Of course you must have a shell account on the remote server
to use this program.

%description -l pl
ProSilla to program przyspieszaj�cy pobieranie du�ych plik�w poprzez
otwieranie wielu po��cze� na raz (tak jak inne "przyspieszacze").
Jedyn� r�nic� jest to, �e proSilla u�ywa ssh zamiast http/ftp do
�ci�gania. Oczywi�cie w zwi�zku z tym trzeba mie� konto shellowe na
docelowym serwerze �eby skorzysta� z tego programu.

%prep
%setup -q -n prosilla

%build
%{__make} \
	CFLAGS="%{rpmcflags} -Wall -DVERSION='\$(VERSION)' `gtk-config --cflags` -DWITH_GTK -I/usr/include/ncurses" \
	LDFLAGS="%{rpmldflags} -lutil -lncurses `gtk-config --libs` -lpthread"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

%{__make} install \
	DSTDIR=$RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/*