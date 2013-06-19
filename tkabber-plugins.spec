%define	snap	20130619
Summary:	Tk Jabber client plugins
Summary(pl.UTF-8):	Wtyczki do klienta Jabbera opartego o Tk
Name:		tkabber-plugins
Version:	0.11.2
Release:	0.%{snap}.1
License:	GPL
Group:		Applications/Communications
# http://svn.xmpp.ru/repos/tkabber/trunk/tkabber-plugins/
Source0:	%{name}-%{snap}.tar.bz2
# Source0-md5:	cf898f42de87001f43f2b7f1dd577425
URL:		http://tkabber.jabber.ru/
Requires:	tkabber >= %{version}-%{release}
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Tkabber (Tk Jabber client) plugins.

%description -l pl.UTF-8
Wtyczki dla Tkabbera - klienta Jabbera opartego o Tk.

%prep
%setup -q -n %{name}

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
