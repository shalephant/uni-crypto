# task 1
echo "This file contains top secret information." > secret.txt
openssl enc -aes-128-cbc -in secret.txt -out secret.enc -k mypassword
openssl enc -d -aes-128-cbc -in secret.enc -out decrypted.txt -k mypassword
cat decrypted.txt

# task 2 
openssl ecparam -name prime256v1 -genkey -noout -out ecc_private.pem
openssl ec -in ecc_private.pem -pubout -out ecc_public.pem
echo "Elliptic Curves are efficient." > ecc.txt
openssl dgst -sha256 -sign ecc_private.pem -out signature.bin ecc.txt
openssl dgst -sha256 -verify ecc_public.pem -signature signature.bin ecc.txt

# task 3

echo "Never trust, always verify." > data.txt
sha256sum data.txt
