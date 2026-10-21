# drupal_help_arg()

- **Type:** Function
- **File:** [`includes/menu.inc`](_file.md), lines 1724–1727 · [local source](../../../source/includes/menu.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/menu.inc#L1724-L1727)
- **Topics:** [menu](../../topics/menu.md)

## Signature

```php
function drupal_help_arg($arg = array())
```

## Documentation

```text
Generates elements for the $arg array in the help hook.
```

## Code

```php
function drupal_help_arg($arg = array()) {
  // Note - the number of empty elements should be > MENU_MAX_PARTS.
  return $arg + array('', '', '', '', '', '', '', '', '', '', '', '');
}
```

---
_Drupal 7.103 · [includes/menu.inc](https://github.com/drupal/drupal/blob/7.103/includes/menu.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
