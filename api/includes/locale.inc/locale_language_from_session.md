# locale_language_from_session()

- **Type:** Function
- **File:** [`includes/locale.inc`](_file.md), lines 234–253 · [local source](../../../source/includes/locale.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/locale.inc#L234-L253)
- **Topics:** [locale-languages-negotiation](../../topics/locale-languages-negotiation.md)

## Signature

```php
function locale_language_from_session($languages)
```

## Documentation

```text
Identify language from a request/session parameter.

@param $languages
  An array of valid language objects.

@return
  A valid language code on success, FALSE otherwise.
```

## Code

```php
function locale_language_from_session($languages) {
  $param = variable_get('locale_language_negotiation_session_param', 'language');

  // Request parameter: we need to update the session parameter only if we have
  // an authenticated user.
  if (isset($_GET[$param]) && isset($languages[$langcode = $_GET[$param]])) {
    global $user;
    if ($user->uid) {
      $_SESSION[$param] = $langcode;
    }
    return $langcode;
  }

  // Session parameter.
  if (isset($_SESSION[$param])) {
    return $_SESSION[$param];
  }

  return FALSE;
}
```

---
_Drupal 7.103 · [includes/locale.inc](https://github.com/drupal/drupal/blob/7.103/includes/locale.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
