%define script_name winbind-dnsupdate

Name: samba-winbind-dnsupdate
Version: 0.1
Release: alt2

Summary: Dynamic dns update for winbind backend
License: GPLv3
URL: https://github.com/altlinuxteam/samba-winbind-dnsupdate
VCS: https://github.com/altlinuxteam/samba-winbind-dnsupdate

BuildArch: noarch
Group: System/Configuration/Networking
Source: %name-%version.tar

BuildRequires: shellcheck

Requires: samba-winbind

%description
A program that implements dynamic update of addresses
on a DNS server when used as a winbind backend

%prep
%setup

%build
# Change version
sed -i 's/^VERSION=.*/VERSION=%version/' %script_name

%install

install -Dm 755 %script_name %buildroot/%_bindir/%script_name
install -Dm 644 %script_name.bash-completion \
     %buildroot%_datadir/bash-completion/completions/%script_name
install -Dm 644 %script_name.timer %buildroot%_unitdir/%script_name.timer
install -Dm 644 %script_name.service %buildroot%_unitdir/%script_name.service
install -Dm 644 %script_name.sysconfig %buildroot%_sysconfdir/sysconfig/%script_name

%check
shellcheck %script_name

%files
%_bindir/%script_name
%_unitdir/%script_name.timer
%_unitdir/%script_name.service
%_datadir/bash-completion/completions/%script_name
%_sysconfdir/sysconfig/%script_name

%changelog
* Wed Jul 31 2024 Andrey Limachko <liannnix@altlinux.org> 0.1-alt2
- Build for sisyphus.

* Mon Jul 29 2024 Evgenii Sozonov  <arzdez@altlinux.org> 0.1-alt1
- Initial release.
