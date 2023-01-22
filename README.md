
Нужен для создания больших тестовых CRL, когда сертификаты генерировать придётся очень долго. Зависимостей нет. certindex передавать в OpenSSL.

Пример ca.conf

    # Mainly copied from:
    # http://swearingscience.com/2009/01/18/openssl-self-signed-ca/
    
    [ ca ]
    default_ca = myca
    
    [ crl_ext ]
    # issuerAltName=issuer:copy  #this would copy the issuer name to altname
    authorityKeyIdentifier=keyid:always
    
     [ myca ]
     dir = ./
     new_certs_dir = $dir
     unique_subject = no
     certificate = $dir/ca.crt
     database = $dir/certindex
     private_key = $dir/ca.key
     serial = $dir/certserial
     default_days = 730
     default_md = sha1
     policy = myca_policy
     x509_extensions = myca_extensions
     crlnumber = $dir/crlnumber
     default_crl_days = 730
    
     [ myca_policy ]
     commonName = supplied
     stateOrProvinceName = supplied
     countryName = optional
     emailAddress = optional
     organizationName = supplied
     organizationalUnitName = optional
    
     [ myca_extensions ]
     basicConstraints = CA:false
     subjectKeyIdentifier = hash
     authorityKeyIdentifier = keyid:always
     keyUsage = digitalSignature,keyEncipherment
     extendedKeyUsage = serverAuth
     crlDistributionPoints = URI:http://example.com/root.crl
     subjectAltName  = @alt_names
    
     [alt_names]
     DNS.1 = example.com
     DNS.2 = *.example.com

 
 Пример создания CRL(по данным из certindex):

     openssl ca -config ca.conf -gencrl -out rootca.crl
