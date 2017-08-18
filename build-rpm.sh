#!/bin/bash

tmp=`mktemp -d /tmp/rpm-XXXXX`
trap "rm -rf $tmp" EXIT
mkdir $tmp/BUILD $tmp/BUILDROOT $tmp/SOURCES $tmp/RPMS $tmp/SRPMS
cp -v src/* $tmp/SOURCES
rpmbuild -ba --buildroot=$tmp/BUILDROOT --define "_topdir $tmp" app-ptest.spec
mv $tmp/RPMS/*/*rpm .
