# forum_install()

- **Type:** Function
- **File:** [`modules/forum/forum.install`](_file.md), lines 11–20 · [local source](../../../../source/modules/forum/forum.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/forum/forum.install#L11-L20)
- **Module/theme:** forum
- **Implements:** [hook_install()](../../system/system.api.php/hook_install.md)

## Signature

```php
function forum_install()
```

## Documentation

```text
Implements hook_install().
```

## Code

```php
function forum_install() {
  // Set the weight of the forum.module to 1 so it is loaded after the taxonomy.module.
  db_update('system')
    ->fields(array('weight' => 1))
    ->condition('name', 'forum')
    ->execute();
  // Forum topics are published by default, but do not have any other default
  // options set (for example, they are not promoted to the front page).
  variable_set('node_options_forum', array('status'));
}
```

---
_Drupal 7.103 · [modules/forum/forum.install](https://github.com/drupal/drupal/blob/7.103/modules/forum/forum.install) · Licensed GPL-2.0-or-later (see LICENSE)._
