%define name psimedia
%define version 1.0.3
%define release %mkrel 1

Summary:	Abstraction layer for providing audio and video RTP Services
Name:		%{name}
Version:	%{version}
License:	GPLv2+
Group:		Networking/Instant messaging 
Release:	%{release}
Source:		http://delta.affinix.com/download/psimedia/%{name}-%{version}.tar.bz2
URL:		http://delta.affinix.com/psimedia/
BuildRoot:	%_tmppath/%name-buildroot
BuildRequires:	qt4-devel
BuildRequires:	libgstreamer-plugins-base-devel
BuildRequires:	liboil-devel
BuildRequires:	speex-devel


%description
PsiMedia is a thick abstraction layer for providing audio and
video RTP services to Psi-like IM clients.  The implementation is based on
GStreamer


%package -n psi-plugin-media
Summary:	Audio and Video plugin for Psi
Group:		Networking/Instant messaging
Requires:	psi => 0.13-0.rc1
%description -n psi-plugin-media
This plugin provides audio and video RTP services to PSI.
This implementation is based on GStreamer.

%files -n psi-plugin-media
%defattr(-,root,root,-)
%{_libdir}/psi/plugins/libgstprovider.so
%doc COPYING README TODO

%prep
%setup -q

%build
./configure
%make

%install
%__rm -rf %{buildroot}
# We only need libgstprovider.so in order to enable audio RTP Services for psi
mkdir -p %{buildroot}/%{_libdir}/psi/plugins
mkdir -p %{buildroor}/%{_datadir}/doc/psi-plugin-media
cp gstprovider/libgstprovider.so  %{buildroot}/%{_libdir}/psi/plugins/
cp COPYING %{buildroor}/%{_datadir}/doc/psi-plugin-media


