# menu_local_actions()

- **Type:** Function
- **File:** [`includes/menu.inc`](_file.md), lines 2269–2272 · [local source](../../../source/includes/menu.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/menu.inc#L2269-L2272)
- **Topics:** [menu](../../topics/menu.md)

## Signature

```php
function menu_local_actions()
```

## Documentation

```text
Returns the rendered local actions at the current level.
```

## Code

```php
function menu_local_actions() {
  $links = menu_local_tasks();
  return $links['actions']['output'];
}
```

---
_Drupal 7.103 · [includes/menu.inc](https://github.com/drupal/drupal/blob/7.103/includes/menu.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
