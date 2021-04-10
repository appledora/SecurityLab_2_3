echo "----- Generating HMAC ----"
echo "\nMD5 Key=abcdefg"
openssl dgst -md5 -hmac "abcdefg" hmac_input.txt
echo "\nMD5 Key=abcd"
openssl dgst -md5 -hmac "abcd" hmac_input.txt
echo "\nSHA256 Key=abcdefg"
openssl dgst -sha256 -hmac "abcdefg" hmac_input.txt
echo "\nSHA256 Key=abcd"
openssl dgst -sha256 -hmac "abcd" hmac_input.txt
echo "\nSHA1 Key=ab"
openssl dgst -sha1 -hmac "ab" hmac_input.txt
echo "\nSHA1 Key=abcdefghijklmnop"
openssl dgst -sha1 -hmac "abcdefghijklmnop" hmac_input.txt
