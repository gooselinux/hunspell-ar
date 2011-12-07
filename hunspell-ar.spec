Name: hunspell-ar
Summary: Arabic hunspell dictionaries
%define upstreamid 20080110
Version: 0.%{upstreamid}
Release: 4.1%{?dist}
Source: http://downloads.sourceforge.net/ayaspell/hunspell-ar_%{upstreamid}.tar.gz
Group: Applications/Text
URL: http://ayaspell.sourceforge.net/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
License: GPLv2 or LGPLv2 or MPLv1.1
BuildArch: noarch

Requires: hunspell

%description
Arabic (Egypt, Algeria, etc.) hunspell dictionaries

%prep
%setup -q -n %{name}_%{upstreamid}

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/myspell
cp -p ar.dic $RPM_BUILD_ROOT/%{_datadir}/myspell/ar_TN.dic
cp -p ar.aff $RPM_BUILD_ROOT/%{_datadir}/myspell/ar_TN.aff

pushd $RPM_BUILD_ROOT/%{_datadir}/myspell/
ar_TN_aliases="ar_AE ar_BH ar_DJ ar_DZ ar_EG ar_ER ar_IL ar_IN ar_IQ ar_JO ar_KM ar_KW ar_LB ar_LY ar_MA ar_MR ar_OM ar_PS ar_QA ar_SA ar_SD ar_SO ar_SY ar_TD ar_YE"
for lang in $ar_TN_aliases; do
	ln -s ar_TN.aff $lang.aff
	ln -s ar_TN.dic $lang.dic
done
popd

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog-ar COPYING README-ar THANKS
%{_datadir}/myspell/*

%changelog
* Mon Nov 30 2009 Dennis Gregorovic <dgregor@redhat.com> - 0.20080110-4.1
- Rebuilt for RHEL 6

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20080110-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed May 06 2009 Caolan McNamara <caolanm@redhat.com> - 0.20080110-3
- extend aliases

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20080110-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Apr 28 2008 Caolan McNamara <caolanm@redhat.com> - 0.20080110-1
- use the much lighter ayaspell data instead of Buckwalter

* Wed Jun 06 2007 Caolan McNamara <caolanm@redhat.com> - 0.20060208-1
- initial version
