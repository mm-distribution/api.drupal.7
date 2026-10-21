# system_update_7053()

- **Type:** Function
- **File:** [`modules/system/system.install`](_file.md), lines 2569–2603 · [local source](../../../../source/modules/system/system.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.install#L2569-L2603)
- **Module/theme:** system
- **Topics:** [updates-6.x-to-7.x](../../../topics/updates-6.x-to-7.x.md)

## Signature

```php
function system_update_7053()
```

## Documentation

```text
Upgrade standard blocks and menus.
```

## Code

```php
function system_update_7053() {
  if (db_table_exists('menu_custom')) {
    // Create the same menus as in menu_install().
    db_insert('menu_custom')
      ->fields(array('menu_name' => 'user-menu', 'title' => 'User Menu', 'description' => "The <em>User</em> menu contains links related to the user's account, as well as the 'Log out' link."))
      ->execute();

    db_insert('menu_custom')
      ->fields(array('menu_name' => 'management', 'title' => 'Management', 'description' => "The <em>Management</em> menu contains links for administrative tasks."))
      ->execute();
  }

  block_flush_caches();

  // Show the new menu blocks along the navigation block.
  $blocks = db_query("SELECT theme, status, region, weight, visibility, pages FROM {block} WHERE module = 'system' AND delta = 'navigation'");
  $deltas = db_or()
    ->condition('delta', 'user-menu')
    ->condition('delta', 'management');

  foreach ($blocks as $block) {
    db_update('block')
      ->fields(array(
        'status' => $block->status,
        'region' => $block->region,
        'weight' => $block->weight,
        'visibility' => $block->visibility,
        'pages' => $block->pages,
      ))
      ->condition('theme', $block->theme)
      ->condition('module', 'system')
      ->condition($deltas)
      ->execute();
  }
}
```

---
_Drupal 7.103 · [modules/system/system.install](https://github.com/drupal/drupal/blob/7.103/modules/system/system.install) · Licensed GPL-2.0-or-later (see LICENSE)._
