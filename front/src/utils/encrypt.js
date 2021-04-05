import JSEncrypt from "jsencrypt/bin/jsencrypt.min";

export function encrypt(field) {
  var enCrypt = new JSEncrypt();
  var public_key =
    "-----BEGIN PUBLIC KEY-----" +
    "MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDN4So578mc79elF0gQwG608w1G" +
    "EyBVHKl8sxHMH0uNDij+nvowfHcZC5YSYskiGP3mZj6iqYCfvHnqt/cY+MoZ2vn4" +
    "I7ve/uL0Jk0uYCvK7yDFdNtHmZ8HF2oAn3CQFcWs1joikE8Uxk1Ru0zJJzUe19HF" +
    "iCK3/SEnebYDzmAq8wIDAQAB" +
    "-----END PUBLIC KEY-----";
  enCrypt.setPublicKey(public_key);
  return enCrypt.encrypt(field.trim());
}
