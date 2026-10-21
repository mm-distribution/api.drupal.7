# menu_local_tabs()

- **Type:** Function
- **File:** [`includes/menu.inc`](_file.md), lines 2285–2291 · [local source](../../../source/includes/menu.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/menu.inc#L2285-L2291)
- **Topics:** [menu](../../topics/menu.md)

## Signature

```php
function menu_local_tabs()
```

## Documentation

```text
Returns a renderable element for the primary and secondary tabs.
```

## Code

```php
function menu_local_tabs() {
  return array(
    '#theme' => 'menu_local_tasks',
    '#primary' => menu_primary_local_tasks(),
    '#secondary' => menu_secondary_local_tasks(),
  );
}
```

---
_Drupal 7.103 · [includes/menu.inc](https://github.com/drupal/drupal/blob/7.103/includes/menu.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
