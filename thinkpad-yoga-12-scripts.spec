Name:	thinkpad-yoga-12-scripts	
Version:	1
Release:	1%{?dist}
Summary:	

Group:		
License:	
URL:		
Source0:	

BuildRequires:	
Requires:	python, xrandr, xinput, xbindkeys, kbd, systemd, gawk, xsetwacom, onboard

%description


%prep
%setup -q


%build
%configure
make %{?_smp_mflags}


%install
%make_install


%files
%doc



%changelog

