# _openid_nonce()

- **Type:** Function
- **File:** [`modules/openid/openid.inc`](_file.md), lines 393–400 · [local source](../../../../source/modules/openid/openid.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/openid/openid.inc#L393-L400)
- **Module/theme:** openid

## Signature

```php
function _openid_nonce()
```

## Documentation

```text
Return a nonce value - formatted per OpenID spec.

NOTE: This nonce is not cryptographically secure and only suitable for use
by the test framework.
```

## Code

```php
function _openid_nonce() {
  // YYYY-MM-DDThh:mm:ssZ, plus some optional extra unique characters.
  return gmdate('Y-m-d\TH:i:s\Z') .
    chr(mt_rand(0, 25) + 65) .
    chr(mt_rand(0, 25) + 65) .
    chr(mt_rand(0, 25) + 65) .
    chr(mt_rand(0, 25) + 65);
}
```

---
_Drupal 7.103 · [modules/openid/openid.inc](https://github.com/drupal/drupal/blob/7.103/modules/openid/openid.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
