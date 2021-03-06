Summary:	Tk Jabber client plugins
Summary(pl.UTF-8):	Wtyczki do klienta Jabbera opartego o Tk
Name:		tkabber-plugins
Version:	1.1.2
Release:	1
License:	GPL
Group:		Applications/Communications
Source0:	http://files.jabber.ru/tkabber/%{name}-%{version}.tar.xz
# Source0-md5:	cc876866fd00ae1068679bff1456e9cf
URL:		http://tkabber.jabber.ru/
Requires:	tkabber >= %{version}-%{release}
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Tkabber (Tk Jabber client) plugins.

%description -l pl.UTF-8
Wtyczki dla Tkabbera - klienta Jabbera opartego o Tk.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/tkabber/plugins

for d in *; do
	[ -d "$d" ] && cp -a "$d" $RPM_BUILD_ROOT%{_datadir}/tkabber/plugins
done

# avoid dependency to wishx (we don't have that yet)
rm -rf $RPM_BUILD_ROOT%{_datadir}/tkabber/plugins/whiteboard

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{_datadir}/tkabber/plugins/*
