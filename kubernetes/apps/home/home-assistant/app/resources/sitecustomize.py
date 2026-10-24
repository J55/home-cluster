"""Workaround for gurumitts/pylutron-caseta#217 (Python 3.14.8+).

pylutron-caseta builds a PROTOCOL_TLS_CLIENT context (hostname checking on) but connects
with server_hostname="" to suppress SNI. Python 3.14.8+ rejects that combination, so the
Lutron Caseta integration never connects. Turn hostname checking off on that context only;
CERT_REQUIRED and the paired CA/client certificates stay in place.

Self-limiting: harmless once the library fixes this itself. Remove together with the
`patches` persistence entry and PYTHONPATH in the HelmRelease once HA ships a fixed version.
"""


def _patch():
    try:
        from pylutron_caseta import smartbridge

        original = smartbridge.Smartbridge._create_tls_context

        def _create_tls_context(*args, **kwargs):
            context = original(*args, **kwargs)
            context.check_hostname = False
            return context

        smartbridge.Smartbridge._create_tls_context = staticmethod(_create_tls_context)
    except Exception:  # library missing or reshaped: leave everything untouched
        pass


_patch()
