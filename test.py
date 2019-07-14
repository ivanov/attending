import foobar
import fizbuz
import versionless
import latest

from attending import fetch, fetch_via_module, fetch

fetch(foobar)
fetch_via_module(fizbuz).diagnose()

fetch(latest)
fetch_via_module(versionless)

fetch("ipython", "latest")
# fetch("ipython") #TODO: make this work (without explicit version)
