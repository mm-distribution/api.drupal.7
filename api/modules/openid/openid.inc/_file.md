# modules/openid/openid.inc

- **Source:** [local](../../../../source/modules/openid/openid.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/openid/openid.inc) · 901 lines
- **Module/theme:** openid

## File documentation

```text
@file
OpenID utility functions.
```

## Functions (derived index)

- [openid_redirect_http()](openid_redirect_http.md) — Performs an HTTP 302 redirect (for the 1.x protocol).
- [openid_redirect()](openid_redirect.md) — Creates a js auto-submit redirect for (for the 2.x protocol)
- [openid_redirect_form()](openid_redirect_form.md)
- [_openid_xrds_parse()](_openid_xrds_parse.md) — Parse an XRDS document.
- [_openid_select_service()](_openid_select_service.md) — Select a service element.
- [_openid_is_xri()](_openid_is_xri.md) — Determine if the given identifier is an XRI ID.
- [openid_normalize()](openid_normalize.md) — Normalize the given identifier.
- [_openid_xri_normalize()](_openid_xri_normalize.md) — OpenID normalization method: normalize XRI identifiers.
- [_openid_url_normalize()](_openid_url_normalize.md) — OpenID normalization method: normalize URL identifiers.
- [_openid_create_message()](_openid_create_message.md) — Create a serialized message packet as per spec: $key:$value\n .
- [_openid_encode_message()](_openid_encode_message.md) — Encode a message from _openid_create_message for HTTP Post
- [_openid_parse_message()](_openid_parse_message.md) — Convert a direct communication message into an associative array.
- [_openid_nonce()](_openid_nonce.md) — Return a nonce value - formatted per OpenID spec.
- [_openid_link_href()](_openid_link_href.md) — Pull the href attribute out of an html link element.
- [_openid_meta_httpequiv()](_openid_meta_httpequiv.md) — Pull the http-equiv attribute out of an html meta element
- [_openid_signature()](_openid_signature.md) — Sign certain keys in a message
- [_openid_hmac()](_openid_hmac.md)
- [_openid_dh_base64_to_long()](_openid_dh_base64_to_long.md)
- [_openid_dh_long_to_base64()](_openid_dh_long_to_base64.md)
- [_openid_dh_binary_to_long()](_openid_dh_binary_to_long.md)
- [_openid_dh_long_to_binary()](_openid_dh_long_to_binary.md)
- [_openid_dh_xorsecret()](_openid_dh_xorsecret.md)
- [_openid_dh_rand()](_openid_dh_rand.md)
- [_openid_get_bytes()](_openid_get_bytes.md)
- [_openid_response()](_openid_response.md)
- [_openid_get_params()](_openid_get_params.md)
- [openid_extract_namespace()](openid_extract_namespace.md) — Extract all the parameters belonging to an extension in a response message.
- [openid_extract_ax_values()](openid_extract_ax_values.md) — Extracts values from an OpenID AX Response.
- [_openid_get_math_library()](_openid_get_math_library.md) — Determine the available math library GMP vs. BCMath, favouring GMP for performance.
- [_openid_math_add()](_openid_math_add.md) — Calls the add function from the available math library for OpenID.
- [_openid_math_mul()](_openid_math_mul.md) — Calls the mul function from the available math library for OpenID.
- [_openid_math_div()](_openid_math_div.md) — Calls the div function from the available math library for OpenID.
- [_openid_math_cmp()](_openid_math_cmp.md) — Calls the cmp function from the available math library for OpenID.
- [_openid_math_mod()](_openid_math_mod.md) — Calls the mod function from the available math library for OpenID.
- [_openid_math_pow()](_openid_math_pow.md) — Calls the pow function from the available math library for OpenID.
- [_openid_math_powmod()](_openid_math_powmod.md) — Calls the mul function from the available math library for OpenID.
- [_openid_invalid_openid_transition()](_openid_invalid_openid_transition.md) — Provides transition for accounts with possibly invalid OpenID identifiers in authmap.

## Constants

### OPENID_DH_DEFAULT_MOD

- Line 16

```php
define('OPENID_DH_DEFAULT_MOD', '155172898181473697471232257763715539915724801' .
       '966915404479707795314057629378541917580651227423698188993727816152646631' .
       '438561595825688188889951272158842675419950341258706556549803580104870537' .
       '681476726513255747040765857479291291572334510643245094715007229621094194' .
       '349783925984760375594985848253359305585439638443');
```

```text
Diffie-Hellman Key Exchange Default Value.

This is used to establish an association between the Relying Party and the
OpenID Provider.

See RFC 2631: http://www.ietf.org/rfc/rfc2631.txt
```

### OPENID_DH_DEFAULT_GEN

- Line 25

```php
define('OPENID_DH_DEFAULT_GEN', '2');
```

```text
Diffie-Hellman generator; used for Diffie-Hellman key exchange computations.
```

### OPENID_SHA1_BLOCKSIZE

- Line 30

```php
define('OPENID_SHA1_BLOCKSIZE', 64);
```

```text
SHA-1 hash block size; used for Diffie-Hellman key exchange computations.
```

### OPENID_RAND_SOURCE

- Line 35

```php
define('OPENID_RAND_SOURCE', '/dev/urandom');
```

```text
Random number generator; used for Diffie-Hellman key exchange computations.
```

### OPENID_NS_2_0

- Line 40

```php
define('OPENID_NS_2_0', 'http://specs.openid.net/auth/2.0');
```

```text
OpenID Authentication 2.0 namespace URL.
```

### OPENID_NS_1_1

- Line 45

```php
define('OPENID_NS_1_1', 'http://openid.net/signon/1.1');
```

```text
OpenID Authentication 1.1 namespace URL; used for backwards-compatibility.
```

### OPENID_NS_1_0

- Line 50

```php
define('OPENID_NS_1_0', 'http://openid.net/signon/1.0');
```

```text
OpenID Authentication 1.0 namespace URL; used for backwards-compatibility.
```

### OPENID_NS_OPENID

- Line 55

```php
define('OPENID_NS_OPENID', 'http://openid.net/xmlns/1.0');
```

```text
OpenID namespace used in Yadis documents.
```

### OPENID_NS_SREG

- Line 60

```php
define('OPENID_NS_SREG', 'http://openid.net/extensions/sreg/1.1');
```

```text
OpenID Simple Registration extension.
```

### OPENID_NS_AX

- Line 65

```php
define('OPENID_NS_AX', 'http://openid.net/srv/ax/1.0');
```

```text
OpenID Attribute Exchange extension.
```

### OPENID_NS_XRD

- Line 70

```php
define('OPENID_NS_XRD', 'xri://$xrd*($v*2.0)');
```

```text
Extensible Resource Descriptor documents.
```

---
_Drupal 7.103 · Licensed GPL-2.0-or-later (see LICENSE)._
