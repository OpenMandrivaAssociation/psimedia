%define name psimedia
%define version 1.0.3
%define release %mkrel 9

Summary:	Abstraction layer for providing audio and video RTP Services
Name:		%{name}
Version:	%{version}
License:	GPLv2+
Group:		Networking/Instant messaging 
Release:	%{release}
Source0:	http://delta.affinix.com/download/psimedia/%{name}-%{version}.tar.bz2
URL:		http://delta.affinix.com/psimedia/
Patch0:         psimedia-1.0.3-fedora-remove-v4l.patch
Patch1:         psimedia-1.0.3-gentoo-drop-v4lsrc-gst-plugin.patch
BuildRequires:	qt4-devel
BuildRequires:	libgstreamer-plugins-base-devel
BuildRequires:	oil-devel
BuildRequires:	speex-devel

%description
PsiMedia is a thick abstraction layer for providing audio and
video RTP services to Psi-like IM clients.  The implementation is based on
GStreamer

%package -n psi-plugin-media
Summary:	Audio and Video plugin for Psi
Group:		Networking/Instant messaging
# Needed since it's not part of gstreamer0.10-plugins-good
Requires:   gstreamer0.10-speex
Requires:   gstreamer0.10-plugins-good
%description -n psi-plugin-media
This plugin provides audio and video RTP services to PSI.
This implementation is based on GStreamer.

%files -n psi-plugin-media
%doc COPYING README TODO
%{_libdir}/psi/plugins/libgstprovider.so

#----------------------------------------------------------------------------

%prep
%setup -q
%patch0 -p1
%patch1 -p0

%build
sed -i 's|glib/gmacros.h|glib.h|g' gstprovider/gstelements/static/gstelements.h
sed -i 's|glib/gthread.h|glib.h|g' gstprovider/gstcustomelements/gstcustomelements.h
sed -i 's|glib/gmain.h|glib.h|g' gstprovider/gstthread.h
sed -i 's|glib/gmain.h|glib.h|g' gstprovider/rwcontrol.h

./configure

%make

%install
# We only need libgstprovider.so in order to enable audio RTP Services for psi
%__mkdir -p %{buildroot}/%{_libdir}/psi/plugins
%__cp gstprovider/libgstprovider.so  %{buildroot}/%{_libdir}/psi/plugins/
