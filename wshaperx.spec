%define name wshaperx
%define version 1.1a.x1
%define release 11

Summary:   Helps maintain interactive latency on modem/ADSL/cable
Name:	   %name
Version:   %version
Release:   %release
License:   GPL
Group:     System/Servers
Url:       http://lartc.org/wondershaper/
Source:    %name-%version.tar.bz2
Patch0:	   wshaperx-1.1a.x1-pinit.patch.bz2
BuildRoot: %_tmppath/%name-%version
BuildArch: noarch
Requires(pre): rpm-helper

%description
Maintain low latency for interfactive traffic at all times.

This means that downloading or uploading files should not disturb SSH or 
even telnet. These are the most important things; even 200ms latency is 
sluggish to work over.

Allow 'surfing' at reasonable speeds while up or downloading
Even though http is 'bulk' traffic, other traffic should not drown it out 
too much.

Make sure uploads don't harm downloads, and the other way around. This is a 
much observed phenomenon where upstream traffic simply destroys download 
speed. It turns out that all this is possible, at the cost of a tiny bit of 
bandwidth. The reason that uploads, downloads and ssh hurt eachother is the 
presence of large queues in many domestic access devices like cable or DSL 
modems.

This package (wshaperx) is a branch of wondershaper. It works exactly the
same under the covers, but should be easier to configure it, and to set it
up to run automatically.

%prep
rm -rf $RPM_BUILD_ROOT

%setup -q
%patch0 -p1 -b .pinit

%build

%install

install -D -m 755 %name $RPM_BUILD_ROOT%_sbindir/%name
install -D -m 644 %name.conf $RPM_BUILD_ROOT%_sysconfdir/%name.conf
install -D -m 755 %name.ifup $RPM_BUILD_ROOT%_sysconfdir/sysconfig/network-scripts/ifup.d/%name
install -D -m 755 %name.ifdown $RPM_BUILD_ROOT%_sysconfdir/sysconfig/network-scripts/ifdown.d/%name
install -D -m 755 %name.init $RPM_BUILD_ROOT%_sysconfdir/rc.d/init.d/%name

%clean
rm -rf $RPM_BUILD_ROOT

%post
echo "You will need to read the documentation and set the configuration "
echo "before this package will be of any use to you."

%preun
%_preun_service %name
/usr/sbin/%name stop > /dev/null 2>&1

%files
%defattr(-,root,root)
%doc COPYING README README.wshaper README.wshaperx
%doc INSTALL TODO VERSION ChangeLog
%config(noreplace) %_sysconfdir/wshaperx.conf
%_sbindir/wshaperx
%_sysconfdir/sysconfig/network-scripts/ifup.d/wshaperx
%_sysconfdir/sysconfig/network-scripts/ifdown.d/wshaperx
%_sysconfdir/rc.d/init.d/wshaperx



%changelog
* Wed Sep 09 2009 Thierry Vignaud <tvignaud@mandriva.com> 1.1a.x1-10mdv2010.0
+ Revision: 434982
- rebuild

* Sun Aug 03 2008 Thierry Vignaud <tvignaud@mandriva.com> 1.1a.x1-9mdv2009.0
+ Revision: 262175
- rebuild

* Wed Jul 30 2008 Thierry Vignaud <tvignaud@mandriva.com> 1.1a.x1-8mdv2009.0
+ Revision: 256403
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon Dec 17 2007 Thierry Vignaud <tvignaud@mandriva.com> 1.1a.x1-6mdv2008.1
+ Revision: 129477
- kill re-definition of %%buildroot on Pixel's request
- import wshaperx


* Mon Jan  9 2006 Olivier Blin <oblin@mandriva.com> 1.1a.x1-6mdk
- fix typo in initscript

* Mon Jan  9 2006 Olivier Blin <oblin@mandriva.com> 1.1a.x1-5mdk
- convert parallel init to LSB

* Sun Jan  1 2006 Couriousous <couriousous@mandriva.org> 1.1a.x1-4mdk
- Add parallel init stuff

* Thu Jun 02 2005 Nicolas Lécureuil <neoclust@mandriva.org> 1.1a.x1-3mdk
- Rebuild

* Mon Apr 19 2004 Michael Scherer <misc@mandrake.org> 1.1a.x1-2mdk 
- Birthday rebuild 

* Wed Apr 02 2003 Lenny Cartier <lenny@mandrakesoft.com> 1.1a.x1-1mdk
- from andi payn <payn@myrealbox.com> :
	- 1.1a.x1

* Thu Jan 30 2003 Lenny Cartier <lenny@mandrakesoft.com> 1.1a-2mdk
- rebuild

* Tue May 21 2002 Lenny Cartier <lenny@mandrakesoft.com> 1.1a-1mdk
- 1.1a
