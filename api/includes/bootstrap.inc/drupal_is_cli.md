# drupal_is_cli()

- **Type:** Function
- **File:** [`includes/bootstrap.inc`](_file.md), lines 3820–3822 · [local source](../../../source/includes/bootstrap.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/bootstrap.inc#L3820-L3822)

## Signature

```php
function drupal_is_cli()
```

## Documentation

```text
Detects whether the current script is running in a command-line environment.
```

## Code

```php
function drupal_is_cli() {
  return (!isset($_SERVER['SERVER_SOFTWARE']) && (php_sapi_name() == 'cli' || (is_numeric($_SERVER['argc']) && $_SERVER['argc'] > 0)));
}
```

---
_Drupal 7.103 · [includes/bootstrap.inc](https://github.com/drupal/drupal/blob/7.103/includes/bootstrap.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
