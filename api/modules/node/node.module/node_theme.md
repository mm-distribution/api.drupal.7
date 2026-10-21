# node_theme()

- **Type:** Function
- **File:** [`modules/node/node.module`](_file.md), lines 125–153 · [local source](../../../../source/modules/node/node.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/node.module#L125-L153)
- **Module/theme:** node
- **Implements:** [hook_theme()](../../system/system.api.php/hook_theme.md)

## Signature

```php
function node_theme()
```

## Documentation

```text
Implements hook_theme().
```

## Code

```php
function node_theme() {
  return array(
    'node' => array(
      'render element' => 'elements',
      'template' => 'node',
    ),
    'node_search_admin' => array(
      'render element' => 'form',
    ),
    'node_add_list' => array(
      'variables' => array('content' => NULL),
      'file' => 'node.pages.inc',
    ),
    'node_preview' => array(
      'variables' => array('node' => NULL),
      'file' => 'node.pages.inc',
    ),
    'node_admin_overview' => array(
      'variables' => array('name' => NULL, 'type' => NULL),
      'file' => 'content_types.inc',
    ),
    'node_recent_block' => array(
      'variables' => array('nodes' => NULL),
    ),
    'node_recent_content' => array(
      'variables' => array('node' => NULL),
    ),
  );
}
```

---
_Drupal 7.103 · [modules/node/node.module](https://github.com/drupal/drupal/blob/7.103/modules/node/node.module) · Licensed GPL-2.0-or-later (see LICENSE)._
