# language_from_default()

- **Type:** Function
- **File:** [`includes/language.inc`](_file.md), lines 509–511 · [local source](../../../source/includes/language.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/language.inc#L509-L511)
- **Topics:** [language_negotiation](../../topics/language_negotiation.md)

## Signature

```php
function language_from_default()
```

## Documentation

```text
Returns the default language negotiation provider.

@return
  The default language code.
```

## Code

```php
function language_from_default() {
  return language_default()->language;
}
```

---
_Drupal 7.103 · [includes/language.inc](https://github.com/drupal/drupal/blob/7.103/includes/language.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
