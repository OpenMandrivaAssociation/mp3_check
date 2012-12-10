Name:      mp3_check 
Summary:   A utility which analyzes mp3 files for errors and standards conformance
Version:   1.98
Release: %mkrel 10
Group:     Sound
URL:	   https://sourceforge.net/project/?group_id=6126
License:   GPL
Source:    ftp://ftp.thedeepsky.com/outgoing/mp3_check-%version.tar.bz2
Buildroot: %{_tmppath}/mp3_check-root

%description
Identify in explicit detail mp3s that do not correctly follow the mp3
format. Also look for invalid frame headers, missing frames, etc. This
can be especially important when building an archive, and you want
quality mp3s.  

%prep 
%setup -q

%build
%make CFLAGS="%optflags"

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_bindir}
install -s -m 755 mp3_check $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_bindir}/mp3_check
%doc NOTES README THANKYOU WISHLIST MY_NOTES GOALS FOR_TESTING
%doc MILESTONE* TODO


%changelog
* Tue Aug 02 2011 GÃ¶tz Waschk <waschk@mandriva.org> 1.98-10mdv2012.0
+ Revision: 692728
- rebuild

* Tue Jul 29 2008 Thierry Vignaud <tv@mandriva.org> 1.98-9mdv2011.0
+ Revision: 252930
- rebuild

* Tue Feb 12 2008 Thierry Vignaud <tv@mandriva.org> 1.98-7mdv2008.1
+ Revision: 166024
- fix spacing at top of description
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot


* Mon Jul 31 2006 GÃ¶tz Waschk <waschk@mandriva.org> 1.98-1mdv2007.0
- Rebuild

* Mon Feb 06 2006 GÃ¶tz Waschk <waschk@mandriva.org> 1.98-6mdk
- Rebuild
- use mkrel

* Fri Feb 04 2005 Götz Waschk <waschk@linux-mandrake.com> 1.98-5mdk
- rebuild

* Fri Jan 02 2004 Götz Waschk <waschk@linux-mandrake.com> 1.98-4mdk
- routinely rebuild

