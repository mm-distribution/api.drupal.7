# language_provider_invoke()

- **Type:** Function
- **File:** [`includes/language.inc`](_file.md), lines 427–459 · [local source](../../../source/includes/language.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/language.inc#L427-L459)
- **Topics:** [language_negotiation](../../topics/language_negotiation.md)

## Signature

```php
function language_provider_invoke($provider_id, $provider = NULL)
```

## Documentation

```text
Helper function used to cache the language negotiation providers results.

@param $provider_id
  The language negotiation provider's identifier.
@param $provider
  (optional) An associative array of information about the provider to be
  invoked (see hook_language_negotiation_info() for details). If not passed
  in, it will be loaded through language_negotiation_info().

@return
  A language object representing the language chosen by the provider.
```

## Code

```php
function language_provider_invoke($provider_id, $provider = NULL) {
  $results = &drupal_static(__FUNCTION__);

  if (!isset($results[$provider_id])) {
    global $user;

    // Get languages grouped by status and select only the enabled ones.
    $languages = language_list('enabled');
    $languages = $languages[1];

    if (!isset($provider)) {
      $providers = language_negotiation_info();
      $provider = $providers[$provider_id];
    }

    if (isset($provider['file'])) {
      require_once DRUPAL_ROOT . '/' . $provider['file'];
    }

    // If the language negotiation provider has no cache preference or this is
    // satisfied we can execute the callback.
    $cache = !isset($provider['cache']) || $user->uid || $provider['cache'] == variable_get('cache', 0);
    $callback = isset($provider['callbacks']['language']) ? $provider['callbacks']['language'] : FALSE;
    $langcode = $cache && function_exists($callback) ? $callback($languages) : FALSE;
    $results[$provider_id] = isset($languages[$langcode]) ? $languages[$langcode] : FALSE;
  }

  // Since objects are resources, we need to return a clone to prevent the
  // language negotiation provider cache from being unintentionally altered. The
  // same providers might be used with different language types based on
  // configuration.
  return !empty($results[$provider_id]) ? clone($results[$provider_id]) : $results[$provider_id];
}
```

---
_Drupal 7.103 · [includes/language.inc](https://github.com/drupal/drupal/blob/7.103/includes/language.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
