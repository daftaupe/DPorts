# Created by: Brendan Molloy <brendan+freebsd@bbqsrc.net>
# $FreeBSD$

PORTNAME=	signedjson
PORTVERSION=	1.1
CATEGORIES=	security devel python
MASTER_SITES=	CHEESESHOP
PKGNAMEPREFIX=	${PYTHON_PKGNAMEPREFIX}

MAINTAINER=	sunpoet@FreeBSD.org
COMMENT=	Sign JSON with Ed25519 signatures

LICENSE=	APACHE20
LICENSE_FILE=	${WRKSRC}/LICENSE

RUN_DEPENDS=	${PYTHON_PKGNAMEPREFIX}canonicaljson>=1.0.0:devel/py-canonicaljson@${PY_FLAVOR} \
		${PYTHON_PKGNAMEPREFIX}pynacl>=0.3.0:security/py-pynacl@${PY_FLAVOR} \
		${PY_TYPING} \
		${PYTHON_PKGNAMEPREFIX}typing-extensions>=3.5:devel/py-typing-extensions@${PY_FLAVOR} \
		${PYTHON_PKGNAMEPREFIX}unpaddedbase64>=1.0.1:devel/py-unpaddedbase64@${PY_FLAVOR}
TEST_DEPENDS=	${PYTHON_PKGNAMEPREFIX}pytest>0:devel/py-pytest@${PY_FLAVOR}

USES=		python
USE_PYTHON=	autoplist concurrent distutils

NO_ARCH=	yes

do-test:
	@(cd ${WRKSRC} && ${PYTHON_CMD} -m pytest tests)

.include <bsd.port.mk>
