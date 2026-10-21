# language_negotiation_get()

- **Type:** Function
- **File:** [`includes/language.inc`](_file.md), lines 230–246 · [local source](../../../source/includes/language.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/language.inc#L230-L246)
- **Topics:** [language_negotiation](../../topics/language_negotiation.md)

## Signature

```php
function language_negotiation_get($type, $provider_id = NULL)
```

## Documentation

```text
Checks whether a language negotiation provider is enabled for a language type.

This has two possible behaviors:
 - If $provider_id is given return its ID if enabled, FALSE otherwise.
 - If no ID is passed the first enabled language negotiation provider is
   returned.

@param $type
  The language negotiation provider type.
@param $provider_id
  The language negotiation provider ID.

@return
  The provider ID if it is enabled, FALSE otherwise.
```

## Code

```php
function language_negotiation_get($type, $provider_id = NULL) {
  $negotiation = variable_get("language_negotiation_$type", array());

  if (empty($negotiation)) {
    return empty($provider_id) ? LANGUAGE_NEGOTIATION_DEFAULT : FALSE;
  }

  if (empty($provider_id)) {
    return key($negotiation);
  }

  if (isset($negotiation[$provider_id])) {
    return $provider_id;
  }

  return FALSE;
}
```

---
_Drupal 7.103 · [includes/language.inc](https://github.com/drupal/drupal/blob/7.103/includes/language.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
