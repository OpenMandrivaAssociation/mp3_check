Name:      mp3_check 
Summary:   A utility which analyzes mp3 files for errors and standards conformance
Version:   1.98
Release:   12
Group:     Sound
URL:	   https://sourceforge.net/project/?group_id=6126
License:   GPL
Source:    ftp://ftp.thedeepsky.com/outgoing/mp3_check-%version.tar.bz2

%define debug_package %{nil}

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
mkdir -p %{buildroot}%{_bindir}
install -s -m 755 mp3_check %{buildroot}%{_bindir}

%files
%{_bindir}/mp3_check
%doc NOTES README THANKYOU WISHLIST MY_NOTES GOALS FOR_TESTING
%doc MILESTONE* TODO
