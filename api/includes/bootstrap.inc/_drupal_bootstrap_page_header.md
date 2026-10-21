# _drupal_bootstrap_page_header()

- **Type:** Function
- **File:** [`includes/bootstrap.inc`](_file.md), lines 2894–2901 · [local source](../../../source/includes/bootstrap.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/bootstrap.inc#L2894-L2901)

## Signature

```php
function _drupal_bootstrap_page_header()
```

## Documentation

```text
Invokes hook_boot(), initializes locking system, and sends HTTP headers.
```

## Code

```php
function _drupal_bootstrap_page_header() {
  bootstrap_invoke_all('boot');

  if (!drupal_is_cli()) {
    ob_start();
    drupal_page_header();
  }
}
```

---
_Drupal 7.103 · [includes/bootstrap.inc](https://github.com/drupal/drupal/blob/7.103/includes/bootstrap.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
