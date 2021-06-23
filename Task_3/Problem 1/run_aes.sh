echo "---- Starting AES mode testing ----"
echo "Encryption with CBC with 128 keys\n"
openssl enc -aes-128-cbc -e -in AEStrial.txt -out AEStrialCBC-128.bin \-K 00112233445566778889aabbccddeeff \-iv 0102030405060708
echo "Encryption with CBF with 192 keys\n"
openssl enc -aes-192-cfb -e -in AEStrial.txt -out AEStrialCFB-192.bin \-K 00112233445566778889aabbccddeeff \-iv 0102030405060708
echo "Encryption with OBF with 256 keys\n"
openssl enc -aes-256-ofb -e -in AEStrial.txt -out AEStrialOFB-256.bin \-K 00112233445566778889aabbccddeeff \-iv 0102030405060708

echo "---- Starting Decryption with AES modes ----"
echo "Decryption with CBC with 128 keys\n"
openssl enc -aes-128-cbc -d -in AEStrialCBC-128.bin  -out AEStrialValCBC-128.bin \-K 00112233445566778889aabbccddeeff \-iv 0102030405060708
echo "Decryption with CBF with 192 keys\n"
openssl enc -aes-192-cfb -d -in AEStrialCFB-192.bin  -out AEStrialValCFB-192.bin \-K 00112233445566778889aabbccddeeff \-iv 0102030405060708
echo "DEcryption with OBF with 256 keys\n"
openssl enc -aes-256-ofb -d -in AEStrialOFB-256.bin  -out AEStrialValOFB-256.bin \-K 00112233445566778889aabbccddeeff \-iv 0102030405060708
echo "Congratulations!!!"
