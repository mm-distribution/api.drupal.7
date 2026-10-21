# menu_link_delete()

- **Type:** Function
- **File:** [`includes/menu.inc`](_file.md), lines 3075–3085 · [local source](../../../source/includes/menu.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/menu.inc#L3075-L3085)
- **Topics:** [menu](../../topics/menu.md)

## Signature

```php
function menu_link_delete($mlid, $path = NULL)
```

## Documentation

```text
Delete one or several menu links.

@param $mlid
  A valid menu link mlid or NULL. If NULL, $path is used.
@param $path
  The path to the menu items to be deleted. $mlid must be NULL.
```

## Code

```php
function menu_link_delete($mlid, $path = NULL) {
  if (isset($mlid)) {
    _menu_delete_item(db_query("SELECT * FROM {menu_links} WHERE mlid = :mlid", array(':mlid' => $mlid))->fetchAssoc());
  }
  else {
    $result = db_query("SELECT * FROM {menu_links} WHERE link_path = :link_path", array(':link_path' => $path));
    foreach ($result as $link) {
      _menu_delete_item($link);
    }
  }
}
```

---
_Drupal 7.103 · [includes/menu.inc](https://github.com/drupal/drupal/blob/7.103/includes/menu.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
