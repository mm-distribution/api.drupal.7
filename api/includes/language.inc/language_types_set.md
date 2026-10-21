# language_types_set()

- **Type:** Function
- **File:** [`includes/language.inc`](_file.md), lines 179–212 · [local source](../../../source/includes/language.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/language.inc#L179-L212)
- **Topics:** [language_negotiation](../../topics/language_negotiation.md)

## Signature

```php
function language_types_set()
```

## Documentation

```text
Updates the language type configuration.
```

## Code

```php
function language_types_set() {
  // Ensure that we are getting the defined language negotiation information. An
  // invocation of module_enable() or module_disable() could outdate the cached
  // information.
  drupal_static_reset('language_types_info');
  drupal_static_reset('language_negotiation_info');

  // Determine which language types are configurable and which not by checking
  // whether the 'fixed' key is defined. Non-configurable (fixed) language types
  // have their language negotiation settings stored there.
  $defined_providers = language_negotiation_info();
  foreach (language_types_info() as $type => $info) {
    if (isset($info['fixed'])) {
      $language_types[$type] = FALSE;
      $negotiation = array();
      foreach ($info['fixed'] as $weight => $id) {
        if (isset($defined_providers[$id])) {
          $negotiation[$id] = $weight;
        }
      }
      language_negotiation_set($type, $negotiation);
    }
    else {
      $language_types[$type] = TRUE;
    }
  }

  // Save language types.
  variable_set('language_types', $language_types);

  // Ensure that subsequent calls of language_types_configurable() return the
  // updated language type information.
  drupal_static_reset('language_types_configurable');
}
```

---
_Drupal 7.103 · [includes/language.inc](https://github.com/drupal/drupal/blob/7.103/includes/language.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
