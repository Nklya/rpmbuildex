Name:		app-ptest
Version:	%{getenv:RELEASE_NUMBER}
Release:	%{getenv:BUILD_BUILDID}
Summary:	simple python app

Group:		Applications/System
License:	MIT
URL:		http://null.com
Source0:	app-ptest

%description
app-ptest is a simple python app designed for testing purposes (rpm build, test TFS pipeline)

%prep


%build


%install
mkdir -p %{buildroot}/%{_bindir}
install -p -m 755 %{SOURCE0} %{buildroot}/%{_bindir}

%files
%{_bindir}/app-ptest



%changelog
* Thu Aug 10 2017 John Doe <jdoe@example.com>
- Initial RPM release
