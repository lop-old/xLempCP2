# xLempCP

### Installing

    # You'll first need to install the yum repo which contains the xLempCP package:
    sudo yum install http://yum.poixson.com/latest.rpm
    # and the yum repo which contains the latest versions of php:
    sudo yum install webtatic-release
    # You can then install xLempCP:
    sudo yum install xLempCP


### Building with xbuild

    # in order to build the package, you'll first need to manually create the xlemp user
    groupadd --system xlemp
    adduser --system --shell /sbin/nologin --home-dir /home/xlemp -g xlemp xlemp
    # you'll first need to install the shellscripts package
    yum install shellscripts
    # checkout the repo or fork and checkout your own copy
    git clone https://github.com/PoiXson/xLempCP.git
    # build the package
    xbuild
    # you'll then have an rpm file under target/
