# $FreeBSD$

PORTNAME=	libass
PORTVERSION=	0.14.0
CATEGORIES=	multimedia devel

MAINTAINER=	multimedia@FreeBSD.org
COMMENT=	Portable ASS/SSA subtitle renderer

LICENSE=	ISCL
LICENSE_FILE=	${WRKSRC}/COPYING

LIB_DEPENDS=	libfreetype.so:print/freetype2 \
		libfribidi.so:converters/fribidi \
		libfontconfig.so:x11-fonts/fontconfig

USE_GITHUB=	yes

USES=		autoreconf iconv libtool pathfix pkgconfig
GNU_CONFIGURE=	yes
USE_LDCONFIG=	yes
INSTALL_TARGET=	install-strip
LDFLAGS_i386=	-Wl,-znotext

OPTIONS_DEFINE=	HARFBUZZ
OPTIONS_DEFAULT=HARFBUZZ
OPTIONS_EXCLUDE_armv6=HARFBUZZ
OPTIONS_EXCLUDE_armv7=HARFBUZZ
OPTIONS_DEFINE_x86_64=	ASM
OPTIONS_DEFINE_i386=	ASM
OPTIONS_DEFAULT_x86_64=	ASM
OPTIONS_DEFAULT_i386=	ASM

ASM_BUILD_DEPENDS=nasm:devel/nasm
ASM_CONFIGURE_ENABLE=asm

HARFBUZZ_LIB_DEPENDS=libharfbuzz.so:print/harfbuzz
HARFBUZZ_CONFIGURE_ENABLE=harfbuzz
HARFBUZZ_DESC?=	Font shaping via HarfBuzz

.include <bsd.port.mk>
