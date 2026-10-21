# locale_language_url_rewrite_session()

- **Type:** Function
- **File:** [`includes/locale.inc`](_file.md), lines 495–525 · [local source](../../../source/includes/locale.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/locale.inc#L495-L525)
- **Topics:** [locale-languages-negotiation](../../topics/locale-languages-negotiation.md)

## Signature

```php
function locale_language_url_rewrite_session(&$path, &$options)
```

## Documentation

```text
Rewrite URLs for the Session language provider.
```

## Code

```php
function locale_language_url_rewrite_session(&$path, &$options) {
  static $query_rewrite, $query_param, $query_value;

  // The following values are not supposed to change during a single page
  // request processing.
  if (!isset($query_rewrite)) {
    global $user;
    if (!$user->uid) {
      $languages = language_list('enabled');
      $languages = $languages[1];
      $query_param = check_plain(variable_get('locale_language_negotiation_session_param', 'language'));
      $query_value = isset($_GET[$query_param]) ? check_plain($_GET[$query_param]) : NULL;
      $query_rewrite = isset($languages[$query_value]) && language_negotiation_get_any(LOCALE_LANGUAGE_NEGOTIATION_SESSION);
    }
    else {
      $query_rewrite = FALSE;
    }
  }

  // If the user is anonymous, the user language provider is enabled, and the
  // corresponding option has been set, we must preserve any explicit user
  // language preference even with cookies disabled.
  if ($query_rewrite) {
    if (is_string($options['query'])) {
      $options['query'] = drupal_get_query_array($options['query']);
    }
    if (!isset($options['query'][$query_param])) {
      $options['query'][$query_param] = $query_value;
    }
  }
}
```

---
_Drupal 7.103 · [includes/locale.inc](https://github.com/drupal/drupal/blob/7.103/includes/locale.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
