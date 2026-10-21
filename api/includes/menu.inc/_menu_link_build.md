# _menu_link_build()

- **Type:** Function
- **File:** [`includes/menu.inc`](_file.md), lines 2874–2894 · [local source](../../../source/includes/menu.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/menu.inc#L2874-L2894)
- **Topics:** [menu](../../topics/menu.md)

## Signature

```php
function _menu_link_build($item)
```

## Documentation

```text
Builds a link from a router item.
```

## Code

```php
function _menu_link_build($item) {
  // Suggested items are disabled by default.
  if ($item['type'] == MENU_SUGGESTED_ITEM) {
    $item['hidden'] = 1;
  }
  // Hide all items that are not visible in the tree.
  elseif (!($item['type'] & MENU_VISIBLE_IN_TREE)) {
    $item['hidden'] = -1;
  }
  // Note, we set this as 'system', so that we can be sure to distinguish all
  // the menu links generated automatically from entries in {menu_router}.
  $item['module'] = 'system';
  $item += array(
    'menu_name' => 'navigation',
    'link_title' => $item['title'],
    'link_path' => $item['path'],
    'hidden' => 0,
    'options' => empty($item['description']) ? array() : array('attributes' => array('title' => $item['description'])),
  );
  return $item;
}
```

---
_Drupal 7.103 · [includes/menu.inc](https://github.com/drupal/drupal/blob/7.103/includes/menu.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
