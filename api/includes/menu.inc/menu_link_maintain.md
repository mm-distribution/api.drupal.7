# menu_link_maintain()

- **Type:** Function
- **File:** [`includes/menu.inc`](_file.md), lines 3474–3496 · [local source](../../../source/includes/menu.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/menu.inc#L3474-L3496)
- **Topics:** [menu](../../topics/menu.md)

## Signature

```php
function menu_link_maintain($module, $op, $link_path, $link_title)
```

## Documentation

```text
Inserts, updates, or deletes an uncustomized menu link related to a module.

@param $module
  The name of the module.
@param $op
  Operation to perform: insert, update or delete.
@param $link_path
  The path this link points to.
@param $link_title
  Title of the link to insert or new title to update the link to.
  Unused for delete.

@return
  The insert op returns the mlid of the new item. Others op return NULL.
```

## Code

```php
function menu_link_maintain($module, $op, $link_path, $link_title) {
  switch ($op) {
    case 'insert':
      $menu_link = array(
        'link_title' => $link_title,
        'link_path' => $link_path,
        'module' => $module,
      );
      return menu_link_save($menu_link);
      break;
    case 'update':
      $result = db_query("SELECT * FROM {menu_links} WHERE link_path = :link_path AND module = :module AND customized = 0", array(':link_path' => $link_path, ':module' => $module))->fetchAll(PDO::FETCH_ASSOC);
      foreach ($result as $link) {
        $link['link_title'] = $link_title;
        $link['options'] = unserialize($link['options']);
        menu_link_save($link);
      }
      break;
    case 'delete':
      menu_link_delete(NULL, $link_path);
      break;
  }
}
```

---
_Drupal 7.103 · [includes/menu.inc](https://github.com/drupal/drupal/blob/7.103/includes/menu.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
