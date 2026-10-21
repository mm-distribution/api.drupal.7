# menu_tail_to_arg()

- **Type:** Function
- **File:** [`includes/menu.inc`](_file.md), lines 838–840 · [local source](../../../source/includes/menu.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/menu.inc#L838-L840)
- **Topics:** [menu](../../topics/menu.md)

## Signature

```php
function menu_tail_to_arg($arg, $map, $index)
```

## Documentation

```text
Returns a string containing the path relative to the current index.
```

## Code

```php
function menu_tail_to_arg($arg, $map, $index) {
  return implode('/', array_slice($map, $index));
}
```

---
_Drupal 7.103 · [includes/menu.inc](https://github.com/drupal/drupal/blob/7.103/includes/menu.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
