Name            : xLempCP
Summary         : Management scripts for LEMP web servers
Version         : 0.1.%{BUILD_NUMBER}
Release         : 1
BuildArch       : noarch
Requires        : php56w
Requires        : php56w-fpm
Requires        : php56w-cli
Requires        : php56w-gd
Requires        : php56w-mbstring
Requires        : php56w-mcrypt
Requires        : php56w-pdo
Requires        : php56w-xml
Requires        : php56w-pear
Requires        : php56w-pecl-xdebug
Requires        : php-composer
Requires        : nginx >= 1.6.3
Requires        : bash
Requires        : wget
Requires        : zip
Requires        : unzip
Requires        : dialog
Prefix          : /usr/bin/xLempCP
%define  _rpmfilename  %%{NAME}-%%{VERSION}-%%{RELEASE}.noarch.rpm
%define  USERNAME  xLempCP

License         : GPA-3
Group           : Server Platform
Packager        : PoiXson <support@poixson.com>
URL             : http://xlemp.poixson.com/

%description
Management scripts for LEMP web servers (Linux/Nginx/MySQL/PHP)



### Prep ###
%prep
# ensure xLempCP user exists
if id -u "%{USERNAME}" >/dev/null 2>&1 ; then
	echo "Found existing user: %{USERNAME}"
else
	echo "Creating user: %{USERNAME}"
	sudo adduser -s /bin/false "%{USERNAME}" || {
		echo "Failed to create user!"
		exit 1
	}
	if id -u "%{USERNAME}" >/dev/null 2>&1 ; then
		echo "Created user: %{USERNAME}"
	else
		echo "User creation failed!"
		exit 1
	fi
fi
echo
echo


### Build ###
%build



### Install ###
%install
echo
echo "Install.."
# delete existing rpm's
%{__rm} -fv "%{_rpmdir}/%{name}-"*.noarch.rpm
# create directories
%{__install} -d -m 0755 \
	"${RPM_BUILD_ROOT}%{prefix}/" \
	"${RPM_BUILD_ROOT}%{prefix}/shell/" \
	"${RPM_BUILD_ROOT}%{prefix}/website/" \
		|| exit 1
# /etc/skel
%{__install} -d -m 0755 \
	"${RPM_BUILD_ROOT}%{_sysconfdir}/skel/" \
	"${RPM_BUILD_ROOT}%{_sysconfdir}/skel/public_html/" \
	"${RPM_BUILD_ROOT}%{_sysconfdir}/skel/etc/" \
	"${RPM_BUILD_ROOT}%{_sysconfdir}/skel/logs/" \
	"${RPM_BUILD_ROOT}%{_sysconfdir}/skel/ssl/" \
		|| exit 1
pushd "${RPM_BUILD_ROOT}%{_sysconfdir}/skel/"
ln -s public_html/ www
popd

#install -c -m644 %SOURCE1 $RPM_BUILD_ROOT/etc/skel/.bashrc

# /home/xLempCP
#%{__install} -d \
#	"${RPM_BUILD_ROOT}/home/" \
#		|| exit 1
#%{__install} -d -m 700 -o xLempCP -g xLempCP \
#	"${RPM_BUILD_ROOT}/home/xLempCP/" \
#		|| exit 1
# copy xLempCP.tar.gz

%{__install} -m 700 \
	"%{SOURCE_ROOT}/target/%{name}-%{version}.tar.gz" \
	"${RPM_BUILD_ROOT}%{prefix}/" \
		|| exit 1



%clean
#if [ ! -z "%{_topdir}" ]; then
#	%{__rm} -rf --preserve-root "%{_topdir}" \
#		|| echo "Failed to delete build root (probably fine..)"
#fi



%post
pushd "%{prefix}/"
tar -xvzf "%{name}-%{version}.tar.gz" \
	|| exit 1
popd



%preun
%{__rm} -Rvf --preserve-root %{prefix}/shell
%{__rm} -Rvf --preserve-root %{prefix}/website



### Files ###
%files
%defattr(-,root,root,-)
"%{prefix}/%{name}-%{version}.tar.gz"
%dir "%{_sysconfdir}/skel/"
%dir "%{_sysconfdir}/skel/public_html/"
%dir "%{_sysconfdir}/skel/etc/"
%dir "%{_sysconfdir}/skel/logs/"
%dir "%{_sysconfdir}/skel/ssl/"
%config(noreplace) %{_sysconfdir}/skel/*

# % {prefix}/composer.json
# % {_sysconfdir}/profile.d/xLemp.sh
# % {prefix}/xlemp-install.sh
# % {prefix}/xlemp-install_utils.sh
# % {prefix}/inc.php
# % {prefix}/ClassLoader.php
# % {prefix}/config.php.original
# % {prefix}/engine/engine.class.php
# % {prefix}/engine/loader.class.php
# % {prefix}/engine/block.class.php
# % {prefix}/engine/template/template_interface.class.php
# % {prefix}/engine/template/phpclss.class.php
# % {prefix}/engine/template/tpl.class.php
# % {_sysconfdir}/httpd/conf.d/xLemp.conf
# % {_sysconfdir}/php.d/xLemp.ini
