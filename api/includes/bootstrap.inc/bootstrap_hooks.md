# bootstrap_hooks()

- **Type:** Function
- **File:** [`includes/bootstrap.inc`](_file.md), lines 1701–1703 · [local source](../../../source/includes/bootstrap.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/bootstrap.inc#L1701-L1703)

## Signature

```php
function bootstrap_hooks()
```

## Documentation

```text
Defines the critical hooks that force modules to always be loaded.
```

## Code

```php
function bootstrap_hooks() {
  return array('boot', 'exit', 'watchdog', 'language_init');
}
```

---
_Drupal 7.103 · [includes/bootstrap.inc](https://github.com/drupal/drupal/blob/7.103/includes/bootstrap.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
