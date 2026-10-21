# drupal_static_reset()

- **Type:** Function
- **File:** [`includes/bootstrap.inc`](_file.md), lines 3813–3815 · [local source](../../../source/includes/bootstrap.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/bootstrap.inc#L3813-L3815)

## Signature

```php
function drupal_static_reset($name = NULL)
```

## Documentation

```text
Resets one or all centrally stored static variable(s).

@param $name
  Name of the static variable to reset. Omit to reset all variables.
  Resetting all variables should only be used, for example, for running unit
  tests with a clean environment.
```

## Code

```php
function drupal_static_reset($name = NULL) {
  drupal_static($name, NULL, TRUE);
}
```

---
_Drupal 7.103 · [includes/bootstrap.inc](https://github.com/drupal/drupal/blob/7.103/includes/bootstrap.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
