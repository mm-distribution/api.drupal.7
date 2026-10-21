# drupal_valid_token()

- **Type:** Function
- **File:** [`includes/common.inc`](_file.md), lines 5380–5383 · [local source](../../../source/includes/common.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/common.inc#L5380-L5383)

## Signature

```php
function drupal_valid_token($token, $value = '', $skip_anonymous = FALSE)
```

## Documentation

```text
Validates a token based on $value, the user session, and the private key.

@param $token
  The token to be validated.
@param $value
  An additional value to base the token on.
@param $skip_anonymous
  Set to true to skip token validation for anonymous users.

@return
  True for a valid token, false for an invalid token. When $skip_anonymous
  is true, the return value will always be true for anonymous users.
```

## Code

```php
function drupal_valid_token($token, $value = '', $skip_anonymous = FALSE) {
  global $user;
  return (($skip_anonymous && $user->uid == 0) || ($token === drupal_get_token($value)));
}
```

---
_Drupal 7.103 · [includes/common.inc](https://github.com/drupal/drupal/blob/7.103/includes/common.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
