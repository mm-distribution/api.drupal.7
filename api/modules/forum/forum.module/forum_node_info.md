# forum_node_info()

- **Type:** Function
- **File:** [`modules/forum/forum.module`](_file.md), lines 450–459 · [local source](../../../../source/modules/forum/forum.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/forum/forum.module#L450-L459)
- **Module/theme:** forum
- **Implements:** [hook_node_info()](../../node/node.api.php/hook_node_info.md)

## Signature

```php
function forum_node_info()
```

## Documentation

```text
Implements hook_node_info().
```

## Code

```php
function forum_node_info() {
  return array(
    'forum' => array(
      'name' => t('Forum topic'),
      'base' => 'forum',
      'description' => t('A <em>forum topic</em> starts a new discussion thread within a forum.'),
      'title_label' => t('Subject'),
    )
  );
}
```

---
_Drupal 7.103 · [modules/forum/forum.module](https://github.com/drupal/drupal/blob/7.103/modules/forum/forum.module) · Licensed GPL-2.0-or-later (see LICENSE)._
