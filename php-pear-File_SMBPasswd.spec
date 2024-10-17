%define		_class		File
%define		_subclass	SMBPasswd
%define		upstream_name	%{_class}_%{_subclass}

Name:		php-pear-%{upstream_name}
Version:	1.0.3
Release:	9
Summary:	Class for managing SAMBA style password files
License:	PHP License
Group:		Development/PHP
URL:		https://pear.php.net/package/File_SMBPasswd/
Source0:	http://download.pear.php.net/package/%{upstream_name}-%{version}.tar.bz2
Requires(post): php-pear
Requires(preun): php-pear
Requires:	php-pear
BuildRequires:	php-pear
BuildArch:	noarch

%description
With this package, you can maintain smbpasswd-files, usualy used by
SAMBA.

%prep
%setup -q -c
mv package.xml %{upstream_name}-%{version}/%{upstream_name}.xml

%install

cd %{upstream_name}-%{version}
pear install --nodeps --packagingroot %{buildroot} %{upstream_name}.xml
rm -rf %{buildroot}%{_datadir}/pear/.??*

rm -rf %{buildroot}%{_datadir}/pear/docs
rm -rf %{buildroot}%{_datadir}/pear/tests

install -d %{buildroot}%{_datadir}/pear/packages
install -m 644 %{upstream_name}.xml %{buildroot}%{_datadir}/pear/packages

%clean



%files
%defattr(-,root,root)
%doc %{upstream_name}-%{version}/examples
%{_datadir}/pear/%{_class}
%{_datadir}/pear/packages/%{upstream_name}.xml


%changelog
* Fri Dec 16 2011 Oden Eriksson <oeriksson@mandriva.com> 1.0.3-6mdv2012.0
+ Revision: 741980
- fix major breakage by careless packager

* Fri May 27 2011 Oden Eriksson <oeriksson@mandriva.com> 1.0.3-5
+ Revision: 679329
- mass rebuild

* Tue Dec 07 2010 Oden Eriksson <oeriksson@mandriva.com> 1.0.3-4mdv2011.0
+ Revision: 613662
- the mass rebuild of 2010.1 packages

* Tue Dec 15 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.0.3-3mdv2010.1
+ Revision: 478823
- spec cleanup
- use pear installer
- don't ship tests, even in documentation
- own all directories
- use rpm filetriggers starting from mandriva 2010.1

* Sun Jun 07 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.0.3-2mdv2010.0
+ Revision: 383768
- don't duplicate spec-helper job
- php-mhash doesn't exist anymore

* Thu Mar 19 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.0.3-1mdv2009.1
+ Revision: 357908
- update to new version 1.0.3

* Thu Jan 01 2009 Oden Eriksson <oeriksson@mandriva.com> 1.0.2-10mdv2009.1
+ Revision: 322027
- rebuild

* Thu Jul 17 2008 Oden Eriksson <oeriksson@mandriva.com> 1.0.2-9mdv2009.0
+ Revision: 236842
- rebuild

* Fri Dec 21 2007 Olivier Blin <blino@mandriva.org> 1.0.2-8mdv2008.1
+ Revision: 136404
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Mon Jun 04 2007 Oden Eriksson <oeriksson@mandriva.com> 1.0.2-8mdv2008.0
+ Revision: 35039
- fix deps


* Sat Nov 11 2006 Oden Eriksson <oeriksson@mandriva.com> 1.0.2-7mdv2007.0
+ Revision: 81590
- Import php-pear-File_SMBPasswd

* Fri Feb 10 2006 Oden Eriksson <oeriksson@mandriva.com> 1.0.2-7mdk
- new group (Development/PHP)

* Fri Aug 26 2005 Oden Eriksson <oeriksson@mandriva.com> 1.0.2-6mdk
- rebuilt to fix auto deps

* Wed Aug 10 2005 Oden Eriksson <oeriksson@mandriva.com> 1.0.2-5mdk
- rebuilt to use new pear auto deps/reqs from pld

* Sun Jul 31 2005 Oden Eriksson <oeriksson@mandriva.com> 1.0.2-4mdk
- fix deps

* Thu Jul 21 2005 Oden Eriksson <oeriksson@mandriva.com> 1.0.2-3mdk
- reworked the %%post and %%preun stuff, like in conectiva
- fix deps

* Wed Jul 20 2005 Oden Eriksson <oeriksson@mandriva.com> 1.0.2-2mdk
- fix deps

* Tue Jul 19 2005 Oden Eriksson <oeriksson@mandriva.com> 1.0.2-1mdk
- initial Mandriva package (PLD import)

