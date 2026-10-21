# drupal_get_token()

- **Type:** Function
- **File:** [`includes/common.inc`](_file.md), lines 5362–5364 · [local source](../../../source/includes/common.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/common.inc#L5362-L5364)

## Signature

```php
function drupal_get_token($value = '')
```

## Documentation

```text
Generates a token based on $value, the user session, and the private key.

@param $value
  An additional value to base the token on.

The generated token is based on the session ID of the current user. Normally,
anonymous users do not have a session, so the generated token will be
different on every page request. To generate a token for users without a
session, manually start a session prior to calling this function.

@return string
  A 43-character URL-safe token for validation, based on the user session ID,
  the hash salt provided from drupal_get_hash_salt(), and the
  'drupal_private_key' configuration variable.

@see drupal_get_hash_salt()
```

## Code

```php
function drupal_get_token($value = '') {
  return drupal_hmac_base64($value, session_id() . drupal_get_private_key() . drupal_get_hash_salt());
}
```

---
_Drupal 7.103 · [includes/common.inc](https://github.com/drupal/drupal/blob/7.103/includes/common.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
