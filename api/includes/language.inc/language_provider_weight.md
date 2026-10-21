# language_provider_weight()

- **Type:** Function
- **File:** [`includes/language.inc`](_file.md), lines 470–473 · [local source](../../../source/includes/language.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/language.inc#L470-L473)
- **Topics:** [language_negotiation](../../topics/language_negotiation.md)

## Signature

```php
function language_provider_weight($provider)
```

## Documentation

```text
Returns the passed language negotiation provider weight or a default value.

@param $provider
  A language negotiation provider data structure.

@return
  A numeric weight.
```

## Code

```php
function language_provider_weight($provider) {
  $default = is_numeric($provider) ? $provider : 0;
  return isset($provider['weight']) && is_numeric($provider['weight']) ? $provider['weight'] : $default;
}
```

---
_Drupal 7.103 · [includes/language.inc](https://github.com/drupal/drupal/blob/7.103/includes/language.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
