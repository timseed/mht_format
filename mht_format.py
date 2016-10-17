
import email
import email.message
import sys
ifp=open(sys.argv[1],'r')
data=ifp.read()
ifp.close()
em=email.message_from_string(data)

print("These are the parts of the mht file")
for p in em.get_payload():
    ct = p.get_content_type()
    fp = p.get("content-location") or "index.html"
    print("Writing %s to %s, %d bytes...\n" % (ct, fp, len(p.get_payload())))
    open(fp, "wb").write(p.get_payload(decode=True))
