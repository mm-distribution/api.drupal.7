# locale_language_from_user()

- **Type:** Function
- **File:** [`includes/locale.inc`](_file.md), lines 213–223 · [local source](../../../source/includes/locale.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/locale.inc#L213-L223)
- **Topics:** [locale-languages-negotiation](../../topics/locale-languages-negotiation.md)

## Signature

```php
function locale_language_from_user($languages)
```

## Documentation

```text
Identify language from the user preferences.

@param $languages
  An array of valid language objects.

@return
  A valid language code on success, FALSE otherwise.
```

## Code

```php
function locale_language_from_user($languages) {
  // User preference (only for logged users).
  global $user;

  if ($user->uid) {
    return $user->language;
  }

  // No language preference from the user.
  return FALSE;
}
```

---
_Drupal 7.103 · [includes/locale.inc](https://github.com/drupal/drupal/blob/7.103/includes/locale.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
