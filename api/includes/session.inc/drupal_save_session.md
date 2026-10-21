# drupal_save_session()

- **Type:** Function
- **File:** [`includes/session.inc`](_file.md), lines 594–603 · [local source](../../../source/includes/session.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/session.inc#L594-L603)

## Signature

```php
function drupal_save_session($status = NULL)
```

## Documentation

```text
Determines whether to save session data of the current request.

This function allows the caller to temporarily disable writing of
session data, should the request end while performing potentially
dangerous operations, such as manipulating the global $user object.
See http://drupal.org/node/218104 for usage.

@param $status
  Disables writing of session data when FALSE, (re-)enables
  writing when TRUE.

@return
  FALSE if writing session data has been disabled. Otherwise, TRUE.
```

## Code

```php
function drupal_save_session($status = NULL) {
  // PHP session ID, session, and cookie handling happens in the global scope.
  // This value has to persist across calls to drupal_static_reset(), since a
  // potentially wrong or disallowed session would be written otherwise.
  static $save_session = TRUE;
  if (isset($status)) {
    $save_session = $status;
  }
  return $save_session;
}
```

---
_Drupal 7.103 · [includes/session.inc](https://github.com/drupal/drupal/blob/7.103/includes/session.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
