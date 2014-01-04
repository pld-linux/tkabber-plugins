Summary:	Tk Jabber client plugins
Summary(pl.UTF-8):	Wtyczki do klienta Jabbera opartego o Tk
Name:		tkabber-plugins
Version:	1.0
Release:	1
License:	GPL
Group:		Applications/Communications
Source0:	http://files.jabber.ru/tkabber/tkabber-plugins-1.0.tar.xz
# Source0-md5:	22ffa6241c07ba5f5cfe25e3f3b0204e
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
