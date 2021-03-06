# $FreeBSD$

PORTNAME=	etc_os-release
PORTVERSION=	0.1
PORTREVISION=	2
CATEGORIES=	sysutils kde gnome
MASTER_SITES=	#
DISTFILES=	#
EXTRACT_ONLY=	#

MAINTAINER=	tcberner@FreeBSD.org
COMMENT=	Operating system identification file

NO_BUILD=	yes

PLIST_FILES=	etc/os-release

VERSION!=	uname -r
VERSION_ID=	${VERSION:C/^([0-9\.]+).*/\1/}

CONTENTS=	'NAME=DragonFly\0'$\
		'VERSION=${VERSION}\0'$\
		'VERSION_ID=${VERSION_ID}\0'$\
		'ID=dragonfly\0'$\
		'ANSI_COLOR="0;32"\0'$\
		'PRETTY_NAME="DragonFly BSD ${VERSION}"\0'$\
		'CPE_NAME=cpe:/o:dragonflybsd:dragonfly:${VERSION_ID}\0'$\
		'SUPPORT_URL=http://chat.efnet.org:9090/?nick=dflynick&channels=%23dragonflybsd&Login=Login\0'$\
		'HOME_URL=https://www.dragonflybsd.org/\0'$\
		'BUG_REPORT_URL=https://bugs.dragonflybsd.org/'

.include <bsd.port.pre.mk>
# FreeBSD base gained /etc/os-release in r354922, which
# corresponds to __FreeBSD_version 1300060
.if ${OPSYS} == FreeBSD && ${OSVERSION} >= 1300060
IGNORE=		/etc/os-release is present in base
.endif

do-install:
	${MKDIR} ${STAGEDIR}${PREFIX}/etc
	${ECHO} -e ${CONTENTS} | ${XARGS} -0 -n 1 >> ${STAGEDIR}${PREFIX}/${PLIST_FILES}

.include <bsd.port.post.mk>
