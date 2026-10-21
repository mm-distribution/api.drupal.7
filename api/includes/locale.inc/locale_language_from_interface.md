# locale_language_from_interface()

- **Type:** Function
- **File:** [`includes/locale.inc`](_file.md), lines 114–117 · [local source](../../../source/includes/locale.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/locale.inc#L114-L117)
- **Topics:** [locale-languages-negotiation](../../topics/locale-languages-negotiation.md)

## Signature

```php
function locale_language_from_interface()
```

## Documentation

```text
Identifies the language from the current interface language.

@return
  The current interface language code.
```

## Code

```php
function locale_language_from_interface() {
  global $language;
  return isset($language->language) ? $language->language : FALSE;
}
```

---
_Drupal 7.103 · [includes/locale.inc](https://github.com/drupal/drupal/blob/7.103/includes/locale.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
