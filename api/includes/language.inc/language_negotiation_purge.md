# language_negotiation_purge()

- **Type:** Function
- **File:** [`includes/language.inc`](_file.md), lines 318–336 · [local source](../../../source/includes/language.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/language.inc#L318-L336)
- **Topics:** [language_negotiation](../../topics/language_negotiation.md)

## Signature

```php
function language_negotiation_purge()
```

## Documentation

```text
Removes any unused language negotiation providers from the configuration.
```

## Code

```php
function language_negotiation_purge() {
  // Ensure that we are getting the defined language negotiation information. An
  // invocation of module_enable() or module_disable() could outdate the cached
  // information.
  drupal_static_reset('language_negotiation_info');
  drupal_static_reset('language_types_info');

  $defined_providers = language_negotiation_info();
  foreach (language_types_info() as $type => $type_info) {
    $weight = 0;
    $negotiation = array();
    foreach (variable_get("language_negotiation_$type", array()) as $id => $provider) {
      if (isset($defined_providers[$id])) {
        $negotiation[$id] = $weight++;
      }
    }
    language_negotiation_set($type, $negotiation);
  }
}
```

---
_Drupal 7.103 · [includes/language.inc](https://github.com/drupal/drupal/blob/7.103/includes/language.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
