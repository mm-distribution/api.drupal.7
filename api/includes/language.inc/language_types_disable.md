# language_types_disable()

- **Type:** Function
- **File:** [`includes/language.inc`](_file.md), lines 166–174 · [local source](../../../source/includes/language.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/language.inc#L166-L174)
- **Topics:** [language_negotiation](../../topics/language_negotiation.md)

## Signature

```php
function language_types_disable($types)
```

## Documentation

```text
Disables the given language types.

@param $types
  An array of language types.
```

## Code

```php
function language_types_disable($types) {
  $enabled_types = variable_get('language_types', drupal_language_types());

  foreach ($types as $type) {
    unset($enabled_types[$type]);
  }

  variable_set('language_types', $enabled_types);
}
```

---
_Drupal 7.103 · [includes/language.inc](https://github.com/drupal/drupal/blob/7.103/includes/language.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
