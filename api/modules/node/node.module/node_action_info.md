# node_action_info()

- **Type:** Function
- **File:** [`modules/node/node.module`](_file.md), lines 3794–3858 · [local source](../../../../source/modules/node/node.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/node.module#L3794-L3858)
- **Module/theme:** node
- **Implements:** [hook_action_info()](../../system/system.api.php/hook_action_info.md)

## Signature

```php
function node_action_info()
```

## Documentation

```text
Implements hook_action_info().
```

## Code

```php
function node_action_info() {
  return array(
    'node_publish_action' => array(
      'type' => 'node',
      'label' => t('Publish content'),
      'configurable' => FALSE,
      'behavior' => array('changes_property'),
      'triggers' => array('node_presave', 'comment_insert', 'comment_update', 'comment_delete'),
    ),
    'node_unpublish_action' => array(
      'type' => 'node',
      'label' => t('Unpublish content'),
      'configurable' => FALSE,
      'behavior' => array('changes_property'),
      'triggers' => array('node_presave', 'comment_insert', 'comment_update', 'comment_delete'),
    ),
    'node_make_sticky_action' => array(
      'type' => 'node',
      'label' => t('Make content sticky'),
      'configurable' => FALSE,
      'behavior' => array('changes_property'),
      'triggers' => array('node_presave', 'comment_insert', 'comment_update', 'comment_delete'),
    ),
    'node_make_unsticky_action' => array(
      'type' => 'node',
      'label' => t('Make content unsticky'),
      'configurable' => FALSE,
      'behavior' => array('changes_property'),
      'triggers' => array('node_presave', 'comment_insert', 'comment_update', 'comment_delete'),
    ),
    'node_promote_action' => array(
      'type' => 'node',
      'label' => t('Promote content to front page'),
      'configurable' => FALSE,
      'behavior' => array('changes_property'),
      'triggers' => array('node_presave', 'comment_insert', 'comment_update', 'comment_delete'),
    ),
    'node_unpromote_action' => array(
      'type' => 'node',
      'label' => t('Remove content from front page'),
      'configurable' => FALSE,
      'behavior' => array('changes_property'),
      'triggers' => array('node_presave', 'comment_insert', 'comment_update', 'comment_delete'),
    ),
    'node_assign_owner_action' => array(
      'type' => 'node',
      'label' => t('Change the author of content'),
      'configurable' => TRUE,
      'behavior' => array('changes_property'),
      'triggers' => array('node_presave', 'comment_insert', 'comment_update', 'comment_delete'),
    ),
    'node_save_action' => array(
      'type' => 'node',
      'label' => t('Save content'),
      'configurable' => FALSE,
      'triggers' => array('comment_insert', 'comment_update', 'comment_delete'),
    ),
    'node_unpublish_by_keyword_action' => array(
      'type' => 'node',
      'label' => t('Unpublish content containing keyword(s)'),
      'configurable' => TRUE,
      'triggers' => array('node_presave', 'node_insert', 'node_update'),
    ),
  );
}
```

---
_Drupal 7.103 · [modules/node/node.module](https://github.com/drupal/drupal/blob/7.103/modules/node/node.module) · Licensed GPL-2.0-or-later (see LICENSE)._
