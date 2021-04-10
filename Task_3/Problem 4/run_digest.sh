echo "----- Generating Hash ----"
echo "\nMD5"
openssl dgst -md5 digest_input.txt
echo "\nSHA256"
openssl dgst -sha256 digest_input.txt
echo "\nSHA1"
openssl dgst -sha1 digest_input.txt
