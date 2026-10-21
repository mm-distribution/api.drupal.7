# language_types_info()

- **Type:** Function
- **File:** [`includes/language.inc`](_file.md), lines 110–120 · [local source](../../../source/includes/language.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/language.inc#L110-L120)
- **Topics:** [language_negotiation](../../topics/language_negotiation.md)

## Signature

```php
function language_types_info()
```

## Documentation

```text
Returns all the defined language types.

@return
  An array of language type names. The name will be used as the global
  variable name the language value will be stored in.
```

## Code

```php
function language_types_info() {
  $language_types = &drupal_static(__FUNCTION__);

  if (!isset($language_types)) {
    $language_types = module_invoke_all('language_types_info');
    // Let other modules alter the list of language types.
    drupal_alter('language_types_info', $language_types);
  }

  return $language_types;
}
```

---
_Drupal 7.103 · [includes/language.inc](https://github.com/drupal/drupal/blob/7.103/includes/language.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
