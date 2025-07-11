#!/bin/bash
echo "This is a secret message." > message.txt
openssl genrsa -out private.pem 2048
openssl rsa -in private.pem -pubout -out public.pem

openssl rsautl -encrypt -inkey public.pem -pubin -in message.txt -out message_rsa_encrypted.bin
openssl rsautl -decrypt -inkey private.pem -in message_rsa_encrypted.bin -out message_rsa_decrypted.txt

openssl rand 32 > aes_key.bin 
openssl rand 16 > aes_iv.bin
openssl enc -aes-256-cbc -in message.txt -out message_aes_encrypted.bin -K $(xxd -p aes_key.bin | tr -d '\n') -iv $(xxd -p aes_iv.bin | tr -d '\n')

openssl enc -d -aes-256-cbc -in message_aes_encrypted.bin -out message_aes_decrypted.txt -K $(xxd -p aes_key.bin | tr -d '\n') -iv $(xxd -p aes_iv.bin | tr -d '\n')

