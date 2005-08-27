Summary:	Tk Jabber client plugins
Summary(pl):	Wtyczki do Klienta Jabbera opartego o Tk
Name:		tkabber-plugins
Version:	0.9.8
Release:	1
License:	GPL
Group:		Applications/Communications
Source0:	http://files.jabberstudio.org/tkabber/%{name}-%{version}.tar.gz
# Source0-md5:	de03ba77d6b6d28f128acf5cfdd90d28
URL:		http://tkabber.jabber.ru/
Requires:	tkabber >= %{version}-%{release}
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Tkabber plugins.

%description -l pl
Wtyczki dla Tkabbera.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/tkabber/plugins

for d in *; do
	[ -d "$d" ] && cp -a "$d" $RPM_BUILD_ROOT%{_datadir}/tkabber/plugins
done

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{_datadir}/tkabber/plugins/*
