#!/bin/bash
#
#sudo chmod 755 build.sh
#sudo bash build.sh
#

APP="app"


function checkDir () {
    if [ ! -e $1 ]; then
        echo "no such directory: $1"
        echo -e "exit\n"
        exit 0
    fi
}

CURRENT=$(cd $(dirname $0)/$APP;pwd)
checkDir $CURRENT
cd $CURRENT

echo -e "\nRun build...\n"
npm run build

checkDir docs
cd docs

cp -a * /usr/local/apache2/htdocs/
echo "Build completed"