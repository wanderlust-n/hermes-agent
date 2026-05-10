# Debug Scripts

Local debugging utilities live here.

Python debug scripts in this directory are intentionally ignored by Git so they
can be used for ad-hoc investigation without polluting normal commits.

Current local-only examples:
- `mimo_debug_proxy.py`

These helpers are for temporary local investigation only. Do not leave them in
the live provider path after debugging; attach them only for short-lived
captures, then restore the normal upstream endpoint.

If a debug helper becomes generally useful, move it out of `scripts/debug/`
before committing it.
