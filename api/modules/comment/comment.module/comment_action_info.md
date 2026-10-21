# comment_action_info()

- **Type:** Function
- **File:** [`modules/comment/comment.module`](_file.md), lines 2535–2565 · [local source](../../../../source/modules/comment/comment.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.module#L2535-L2565)
- **Module/theme:** comment
- **Implements:** [hook_action_info()](../../system/system.api.php/hook_action_info.md)

## Signature

```php
function comment_action_info()
```

## Documentation

```text
Implements hook_action_info().
```

## Code

```php
function comment_action_info() {
  return array(
    'comment_publish_action' => array(
      'label' => t('Publish comment'),
      'type' => 'comment',
      'configurable' => FALSE,
      'behavior' => array('changes_property'),
      'triggers' => array('comment_presave', 'comment_insert', 'comment_update'),
    ),
    'comment_unpublish_action' => array(
      'label' => t('Unpublish comment'),
      'type' => 'comment',
      'configurable' => FALSE,
      'behavior' => array('changes_property'),
      'triggers' => array('comment_presave', 'comment_insert', 'comment_update'),
    ),
    'comment_unpublish_by_keyword_action' => array(
      'label' => t('Unpublish comment containing keyword(s)'),
      'type' => 'comment',
      'configurable' => TRUE,
      'behavior' => array('changes_property'),
      'triggers' => array('comment_presave', 'comment_insert', 'comment_update'),
    ),
    'comment_save_action' => array(
      'label' => t('Save comment'),
      'type' => 'comment',
      'configurable' => FALSE,
      'triggers' => array('comment_insert', 'comment_update'),
    ),
  );
}
```

---
_Drupal 7.103 · [modules/comment/comment.module](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.module) · Licensed GPL-2.0-or-later (see LICENSE)._
