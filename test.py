import foobar
import fizbuz

from attending import Library

library = Library()

print(f"foobar managed by attending? {foobar in library}")
print("fetching foobar's docs")
library.fetch(foobar)
print(f"foobar managed by attending? {foobar in library}")

print(f"fizbuz managed by attending? {fizbuz in library}")
print("fizbuz foobar's docs")
library.fetch(fizbuz)
print(f"fizbuz managed by attending? {fizbuz in library}")
library[fizbuz].diagnose()
