from cryptography import x509
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import rsa

def generate_certificate(public_key):
    # Generate a certificate from the public key (simplified)
    subject = issuer = x509.Name([
        x509.NameAttribute(x509.NameOID.COUNTRY_NAME, u"US"),
        x509.NameAttribute(x509.NameOID.STATE_OR_PROVINCE_NAME, u"California"),
        x509.NameAttribute(x509.NameOID.LOCALITY_NAME, u"San Francisco"),
        x509.NameAttribute(x509.NameOID.ORGANIZATION_NAME, u"FinVault")
    ])

    cert = x509.CertificateBuilder().subject_name(subject).issuer_name(issuer).public_key(public_key).sign(private_key=None, algorithm=hashes.SHA256())
    return cert.public_bytes()
