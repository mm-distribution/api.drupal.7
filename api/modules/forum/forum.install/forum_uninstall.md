# forum_uninstall()

- **Type:** Function
- **File:** [`modules/forum/forum.install`](_file.md), lines 105–121 · [local source](../../../../source/modules/forum/forum.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/forum/forum.install#L105-L121)
- **Module/theme:** forum
- **Implements:** [hook_uninstall()](../../system/system.api.php/hook_uninstall.md)

## Signature

```php
function forum_uninstall()
```

## Documentation

```text
Implements hook_uninstall().
```

## Code

```php
function forum_uninstall() {
  // Load the dependent Taxonomy module, in case it has been disabled.
  drupal_load('module', 'taxonomy');

  variable_del('forum_containers');
  variable_del('forum_hot_topic');
  variable_del('forum_per_page');
  variable_del('forum_order');
  variable_del('forum_block_num_active');
  variable_del('forum_block_num_new');
  variable_del('node_options_forum');

  field_delete_field('taxonomy_forums');
  // Purge field data now to allow taxonomy module to be uninstalled
  // if this is the only field remaining.
  field_purge_batch(10);
}
```

---
_Drupal 7.103 · [modules/forum/forum.install](https://github.com/drupal/drupal/blob/7.103/modules/forum/forum.install) · Licensed GPL-2.0-or-later (see LICENSE)._
