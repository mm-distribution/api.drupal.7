# menu_add_link_labels()

- **Type:** Function
- **File:** [`modules/menu/menu.module`](_file.md), lines 457–467 · [local source](../../../../source/modules/menu/menu.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/menu/menu.module#L457-L467)
- **Module/theme:** menu

## Signature

```php
function menu_add_link_labels(&$title, $item)
```

## Documentation

```text
Adds labels to the title of a hidden, unpublished or logged-in menu link.

@param string $title
  The title of the menu link. This will be modified as necessary to add the
  appropriate label in parentheses at the end.
@param array $item
  An array representing the menu link item.
```

## Code

```php
function menu_add_link_labels(&$title, $item) {
  if ($item['hidden']) {
    $title .= ' (' . t('disabled') . ')';
  }
  elseif (!empty($item['node_unpublished'])) {
    $title .= ' (' . t('unpublished') . ')';
  }
  elseif ($item['link_path'] == 'user' && $item['module'] == 'system') {
    $title .= ' (' . t('logged in users only') . ')';
  }
}
```

---
_Drupal 7.103 · [modules/menu/menu.module](https://github.com/drupal/drupal/blob/7.103/modules/menu/menu.module) · Licensed GPL-2.0-or-later (see LICENSE)._
