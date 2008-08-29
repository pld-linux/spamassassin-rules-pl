Summary:	Polish rules for SpamAssassin
Name:		spamassassin-rules-pl
Version:	20080829
Release:	1
License:	Apache v2.0
Group:		Applications/Mail
Source0:	http://wiki.apache.org/spamassassin-data/attachments/BodyTestsPl/attachments/25_body_tests_pl.cf
# Source0-md5:	0bdb1e069852f8300f47791c28593f3f
URL:		http://wiki.apache.org/spamassassin/BodyTestsPl
Requires:	perl-Mail-SpamAssassin
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Polish body tests for SpamAssassin.

%prep
%setup -q -c -T

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/spamassassin/

install %{SOURCE0} $RPM_BUILD_ROOT%{_datadir}/spamassassin/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_datadir}/spamassassin/*.cf
