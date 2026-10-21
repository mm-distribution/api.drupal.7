# menu_node_save()

- **Type:** Function
- **File:** [`modules/menu/menu.module`](_file.md), lines 549–573 · [local source](../../../../source/modules/menu/menu.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/menu/menu.module#L549-L573)
- **Module/theme:** menu

## Signature

```php
function menu_node_save($node)
```

## Documentation

```text
Helper for hook_node_insert() and hook_node_update().
```

## Code

```php
function menu_node_save($node) {
  if (isset($node->menu)) {
    $link = &$node->menu;
    if (empty($link['enabled'])) {
      if (!empty($link['mlid'])) {
        menu_link_delete($link['mlid']);
      }
    }
    elseif (trim($link['link_title'])) {
      $link['link_title'] = trim($link['link_title']);
      $link['link_path'] = "node/$node->nid";
      if (trim($link['description'])) {
        $link['options']['attributes']['title'] = trim($link['description']);
      }
      else {
        // If the description field was left empty, remove the title attribute
        // from the menu link.
        unset($link['options']['attributes']['title']);
      }
      if (!menu_link_save($link)) {
        drupal_set_message(t('There was an error saving the menu link.'), 'error');
      }
    }
  }
}
```

---
_Drupal 7.103 · [modules/menu/menu.module](https://github.com/drupal/drupal/blob/7.103/modules/menu/menu.module) · Licensed GPL-2.0-or-later (see LICENSE)._
