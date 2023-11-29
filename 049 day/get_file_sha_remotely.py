import sys
from os.path import basename
from urllib.parse import urlparse
from urllib.request import urlopen
import hashlib

urls = ["https://huggingface.co/TheBloke/WizardCoder-Python-13B-V1.0-GGUF/blob/main/wizardcoder-python-13b-v1.0.Q5_K_M.gguf"]

exitcode = 0
for url in urls:
    with urlopen(url) as response:
        if False and url != response.geturl():
            print("# {} -> {}\n".format(url, response.geturl()))
        sha1 = hashlib.new("SHA1")
        sha256 = hashlib.new("SHA256")
        if response.status == 200:
            size, n = 0, 16484
            buf = bytearray(n)
            while n != 0:
                n = response.readinto(buf)
                size += n
                if n > 0:
                    sha1.update(buf[:n])
                    sha256.update(buf[:n])
            o = urlparse(url)
            if not basename(o.path):
                o = urlparse(response.geturl())
            filename = basename(o.path) or "index.html"
            print("# {}\n{}:\n{} bytes read".format(url, filename, size))
            print("sha1:%s" % sha1.hexdigest().lower())
            print("sha256:%s" % sha256.hexdigest().lower())
        else:
            print(
                "ERROR: %s returned %d (%s)" % (url, response.status, response.reason),
                file=sys.stderr,
            )
else:
    if not sys.argv[1:]:
        print("Usage %s: URL [URL ...]" % basename(__file__), file=sys.stderr)