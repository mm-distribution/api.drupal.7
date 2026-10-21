# filter_default_format()

- **Type:** Function
- **File:** [`modules/filter/filter.module`](_file.md), lines 531–541 · [local source](../../../../source/modules/filter/filter.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/filter/filter.module#L531-L541)
- **Module/theme:** filter

## Signature

```php
function filter_default_format($account = NULL)
```

## Documentation

```text
Returns the ID of the default text format for a particular user.

The default text format is the first available format that the user is
allowed to access, when the formats are ordered by weight. It should
generally be used as a default choice when presenting the user with a list
of possible text formats (for example, in a node creation form).

Conversely, when existing content that does not have an assigned text format
needs to be filtered for display, the default text format is the wrong
choice, because it is not guaranteed to be consistent from user to user, and
some trusted users may have an unsafe text format set by default, which
should not be used on text of unknown origin. Instead, the fallback format
returned by filter_fallback_format() should be used, since that is intended
to be a safe, consistent format that is always available to all users.

@param $account
  (optional) The user account to check. Defaults to the currently logged-in
  user. Defaults to NULL.

@return
  The ID of the user's default text format.

@see filter_fallback_format()
```

## Code

```php
function filter_default_format($account = NULL) {
  global $user;
  if (!isset($account)) {
    $account = $user;
  }
  // Get a list of formats for this user, ordered by weight. The first one
  // available is the user's default format.
  $formats = filter_formats($account);
  $format = reset($formats);
  return $format->format;
}
```

---
_Drupal 7.103 · [modules/filter/filter.module](https://github.com/drupal/drupal/blob/7.103/modules/filter/filter.module) · Licensed GPL-2.0-or-later (see LICENSE)._
