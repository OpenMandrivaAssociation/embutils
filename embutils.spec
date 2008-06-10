Summary:	Small system utilities for embedded systems
Name:		embutils
Version:	0.17
Release:	%mkrel 3
License:	GPL
Group:		System/Base
URL:		http://www.fefe.de/
Source0:	http://www.fefe.de/embutils/%{name}-%{version}.tar.bz2
Source1:	http://www.fefe.de/embutils/%{name}-%{version}.tar.bz2.sig
BuildRequires:	dietlibc-devel >= 0.32
Prefix:		%{_libdir}/%{name}
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
Most of the typical Unix userland typically comes from either the
GNU project or the BSD people. Those sources are ancient and 
optimized for features, not for small size, and now that computers
are fast enough and have lots of RAM, implementations became 
larger and larger. Features like internationalization eat lots of
memory and disk space.

For embedded system and boot disks (and desktops and servers for 
purist Unix users), you rather want small than internationalized 
versions of the utilities. That's why I started to reimplement a 
few important typical userland programs that I need on boot and 
rescue disks, making sure that you can link it against diet libc
to create very small statically linked binaries.

%prep

%setup -q

%build

make

%install
rm -rf %{buildroot}

install -d %{buildroot}%{prefix}/bin

make DESTDIR="%{buildroot}%{prefix}" prefix="" install

# fix softlinks...
ln -snf chown %{buildroot}%{prefix}/bin/chgrp
ln -snf mv %{buildroot}%{prefix}/bin/cp
ln -snf mknod %{buildroot}%{prefix}/bin/mkfifo

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc CHANGES TODO
%{prefix}/bin/allinone
%{prefix}/bin/arch
%{prefix}/bin/basename
%{prefix}/bin/cat
%{prefix}/bin/chgrp
%{prefix}/bin/chmod
%{prefix}/bin/chown
%{prefix}/bin/chroot
%{prefix}/bin/chvt
%{prefix}/bin/clear
%{prefix}/bin/cmp
%{prefix}/bin/cp
%{prefix}/bin/dd
%{prefix}/bin/df
%{prefix}/bin/dirname
%{prefix}/bin/dmesg
%{prefix}/bin/domainname
%{prefix}/bin/du
%{prefix}/bin/echo
%{prefix}/bin/env
%{prefix}/bin/false
%{prefix}/bin/head
%{prefix}/bin/hostname
%{prefix}/bin/id
%{prefix}/bin/install
%{prefix}/bin/kill
%{prefix}/bin/ln
%{prefix}/bin/ls
%{prefix}/bin/md5sum
%{prefix}/bin/mesg
%{prefix}/bin/mkdir
%{prefix}/bin/mkfifo
%{prefix}/bin/mknod
%{prefix}/bin/mktemp
%{prefix}/bin/mv
%{prefix}/bin/nice
%{prefix}/bin/nohup
%{prefix}/bin/pwd
%{prefix}/bin/rm
%{prefix}/bin/rmdir
%{prefix}/bin/sleep
%{prefix}/bin/sleep2
%{prefix}/bin/soscp
%{prefix}/bin/sosln
%{prefix}/bin/soslns
%{prefix}/bin/sosmv
%{prefix}/bin/sosrm
%{prefix}/bin/sync
%{prefix}/bin/tail
%{prefix}/bin/tar
%{prefix}/bin/tee
%{prefix}/bin/touch
%{prefix}/bin/tr
%{prefix}/bin/true
%{prefix}/bin/truncate
%{prefix}/bin/tty
%{prefix}/bin/uname
%{prefix}/bin/uniq
%{prefix}/bin/uudecode
%{prefix}/bin/uuencode
%{prefix}/bin/wc
%{prefix}/bin/which
%{prefix}/bin/whoami
%{prefix}/bin/write
%{prefix}/bin/yes
%{prefix}/bin/strings
%{prefix}/bin/test
%{prefix}/bin/date
%{prefix}/bin/mount
%{prefix}/bin/umount
%{prefix}/bin/printenv
%{prefix}/bin/insmod
%{prefix}/bin/lsmod
%{prefix}/bin/pivot_root
%{prefix}/bin/rmmod
