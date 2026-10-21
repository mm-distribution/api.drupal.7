# language_negotiation_get_any()

- **Type:** Function
- **File:** [`includes/language.inc`](_file.md), lines 258–266 · [local source](../../../source/includes/language.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/language.inc#L258-L266)
- **Topics:** [language_negotiation](../../topics/language_negotiation.md)

## Signature

```php
function language_negotiation_get_any($provider_id)
```

## Documentation

```text
Checks if the language negotiation provider is enabled for any language type.

@param $provider_id
  The language negotiation provider ID.

@return
  TRUE if there is at least one language type for which the given language
  provider is enabled, FALSE otherwise.
```

## Code

```php
function language_negotiation_get_any($provider_id) {
  foreach (language_types_configurable() as $type) {
    if (language_negotiation_get($type, $provider_id)) {
      return TRUE;
    }
  }

  return FALSE;
}
```

---
_Drupal 7.103 · [includes/language.inc](https://github.com/drupal/drupal/blob/7.103/includes/language.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
