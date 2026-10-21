# drupal_get_bootstrap_phase()

- **Type:** Function
- **File:** [`includes/bootstrap.inc`](_file.md), lines 2910–2912 · [local source](../../../source/includes/bootstrap.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/bootstrap.inc#L2910-L2912)

## Signature

```php
function drupal_get_bootstrap_phase()
```

## Documentation

```text
Returns the current bootstrap phase for this Drupal process.

The current phase is the one most recently completed by drupal_bootstrap().

@see drupal_bootstrap()
```

## Code

```php
function drupal_get_bootstrap_phase() {
  return drupal_bootstrap(NULL, FALSE);
}
```

---
_Drupal 7.103 · [includes/bootstrap.inc](https://github.com/drupal/drupal/blob/7.103/includes/bootstrap.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
