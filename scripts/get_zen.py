import io
from contextlib import redirect_stdout

stdout = io.StringIO()

with redirect_stdout(stdout):
    import this

stdout.getvalue()