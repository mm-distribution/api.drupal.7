# menu_update_7002()

- **Type:** Function
- **File:** [`modules/menu/menu.install`](_file.md), lines 168–184 · [local source](../../../../source/modules/menu/menu.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/menu/menu.install#L168-L184)
- **Module/theme:** menu
- **Topics:** [updates-7.x-extra](../../../topics/updates-7.x-extra.md)

## Signature

```php
function menu_update_7002(&$sandbox)
```

## Documentation

```text
Rename the primary/secondary menu blocks to match previously renamed menus.
```

## Code

```php
function menu_update_7002(&$sandbox) {
  // Check for the presence of old or new table names.
  if (db_table_exists('blocks') || db_table_exists('block')) {
    $renamed_deltas = array(
      'menu' => array(
        'primary-links' => 'main-menu',
        'secondary-links' => 'secondary-menu',
      ),
    );

    $moved_deltas = array(
      'menu' => array('main-menu' => 'system'),
    );

    update_fix_d7_block_deltas($sandbox, $renamed_deltas, $moved_deltas);
  }
}
```

---
_Drupal 7.103 · [modules/menu/menu.install](https://github.com/drupal/drupal/blob/7.103/modules/menu/menu.install) · Licensed GPL-2.0-or-later (see LICENSE)._
