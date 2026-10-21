# language_types()

- **Type:** Function
- **File:** [`includes/bootstrap.inc`](_file.md), lines 3112–3114 · [local source](../../../source/includes/bootstrap.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/bootstrap.inc#L3112-L3114)

## Signature

```php
function language_types()
```

## Documentation

```text
Returns an array of the available language types.

@return
  An array of all language types where the keys of each are the language type
  name and its value is its configurability (TRUE/FALSE).
```

## Code

```php
function language_types() {
  return array_keys(variable_get('language_types', drupal_language_types()));
}
```

---
_Drupal 7.103 · [includes/bootstrap.inc](https://github.com/drupal/drupal/blob/7.103/includes/bootstrap.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
