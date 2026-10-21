# locale_url_outbound_alter()

- **Type:** Function
- **File:** [`modules/locale/locale.module`](_file.md), lines 1061–1101 · [local source](../../../../source/modules/locale/locale.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.module#L1061-L1101)
- **Module/theme:** locale
- **Implements:** [hook_url_outbound_alter()](../../system/system.api.php/hook_url_outbound_alter.md)

## Signature

```php
function locale_url_outbound_alter(&$path, &$options, $original_path)
```

## Documentation

```text
Implements hook_url_outbound_alter().

Rewrite outbound URLs with language based prefixes.
```

## Code

```php
function locale_url_outbound_alter(&$path, &$options, $original_path) {
  // Only modify internal URLs.
  if (!$options['external'] && drupal_multilingual()) {
    static $drupal_static_fast;
    if (!isset($drupal_static_fast)) {
      $drupal_static_fast['callbacks'] = &drupal_static(__FUNCTION__);
    }
    $callbacks = &$drupal_static_fast['callbacks'];

    if (!isset($callbacks)) {
      $callbacks = array();
      include_once DRUPAL_ROOT . '/includes/language.inc';

      foreach (language_types_configurable() as $type) {
        // Get URL rewriter callbacks only from enabled language providers.
        $negotiation = variable_get("language_negotiation_$type", array());

        foreach ($negotiation as $id => $provider) {
          if (isset($provider['callbacks']['url_rewrite'])) {
            if (isset($provider['file'])) {
              require_once DRUPAL_ROOT . '/' . $provider['file'];
            }
            // Avoid duplicate callback entries.
            $callbacks[$provider['callbacks']['url_rewrite']] = TRUE;
          }
        }
      }

      $callbacks = array_keys($callbacks);
    }

    foreach ($callbacks as $callback) {
      $callback($path, $options);
    }

    // No language dependent path allowed in this mode.
    if (empty($callbacks)) {
      unset($options['language']);
    }
  }
}
```

---
_Drupal 7.103 · [modules/locale/locale.module](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.module) · Licensed GPL-2.0-or-later (see LICENSE)._
