# toolbar_get_menu_tree()

- **Type:** Function
- **File:** [`modules/toolbar/toolbar.module`](_file.md), lines 292–304 · [local source](../../../../source/modules/toolbar/toolbar.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/toolbar/toolbar.module#L292-L304)
- **Module/theme:** toolbar

## Signature

```php
function toolbar_get_menu_tree()
```

## Documentation

```text
Gets only the top level items below the 'admin' path.

@return
  An array containing a menu tree of top level items below the 'admin' path.
```

## Code

```php
function toolbar_get_menu_tree() {
  $tree = array();
  $admin_link = db_query('SELECT * FROM {menu_links} WHERE menu_name = :menu_name AND module = :module AND link_path = :path', array(':menu_name' => 'management', ':module' => 'system', ':path' => 'admin'))->fetchAssoc();
  if ($admin_link) {
    $tree = menu_build_tree('management', array(
      'expanded' => array($admin_link['mlid']),
      'min_depth' => $admin_link['depth'] + 1,
      'max_depth' => $admin_link['depth'] + 1,
    ));
  }

  return $tree;
}
```

---
_Drupal 7.103 · [modules/toolbar/toolbar.module](https://github.com/drupal/drupal/blob/7.103/modules/toolbar/toolbar.module) · Licensed GPL-2.0-or-later (see LICENSE)._
