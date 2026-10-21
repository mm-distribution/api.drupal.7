# comment_form_node_form_alter()

- **Type:** Function
- **File:** [`modules/comment/comment.module`](_file.md), lines 1215–1262 · [local source](../../../../source/modules/comment/comment.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.module#L1215-L1262)
- **Module/theme:** comment
- **Implements:** [hook_form_BASE_FORM_ID_alter()](../../system/system.api.php/hook_form_BASE_FORM_ID_alter.md)

## Signature

```php
function comment_form_node_form_alter(&$form, $form_state)
```

## Documentation

```text
Implements hook_form_BASE_FORM_ID_alter().
```

## Code

```php
function comment_form_node_form_alter(&$form, $form_state) {
  $node = $form['#node'];
  $form['comment_settings'] = array(
    '#type' => 'fieldset',
    '#access' => user_access('administer comments'),
    '#title' => t('Comment settings'),
    '#collapsible' => TRUE,
    '#collapsed' => TRUE,
    '#group' => 'additional_settings',
    '#attributes' => array(
      'class' => array('comment-node-settings-form'),
    ),
    '#attached' => array(
      'js' => array(drupal_get_path('module', 'comment') . '/comment-node-form.js'),
     ),
    '#weight' => 30,
  );
  $comment_count = isset($node->nid) ? db_query('SELECT comment_count FROM {node_comment_statistics} WHERE nid = :nid', array(':nid' => $node->nid))->fetchField() : 0;
  $comment_settings = ($node->comment == COMMENT_NODE_HIDDEN && empty($comment_count)) ? COMMENT_NODE_CLOSED : $node->comment;
  $form['comment_settings']['comment'] = array(
    '#type' => 'radios',
    '#title' => t('Comments'),
    '#title_display' => 'invisible',
    '#parents' => array('comment'),
    '#default_value' => $comment_settings,
    '#options' => array(
      COMMENT_NODE_OPEN => t('Open'),
      COMMENT_NODE_CLOSED => t('Closed'),
      COMMENT_NODE_HIDDEN => t('Hidden'),
    ),
    COMMENT_NODE_OPEN => array(
      '#description' => t('Users with the "Post comments" permission can post comments.'),
    ),
    COMMENT_NODE_CLOSED => array(
      '#description' => t('Users cannot post comments, but existing comments will be displayed.'),
    ),
    COMMENT_NODE_HIDDEN => array(
      '#description' => t('Comments are hidden from view.'),
    ),
  );
  // If the node doesn't have any comments, the "hidden" option makes no
  // sense, so don't even bother presenting it to the user.
  if (empty($comment_count)) {
    $form['comment_settings']['comment'][COMMENT_NODE_HIDDEN]['#access'] = FALSE;
    // Also adjust the description of the "closed" option.
    $form['comment_settings']['comment'][COMMENT_NODE_CLOSED]['#description'] = t('Users cannot post comments.');
  }
}
```

---
_Drupal 7.103 · [modules/comment/comment.module](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.module) · Licensed GPL-2.0-or-later (see LICENSE)._
