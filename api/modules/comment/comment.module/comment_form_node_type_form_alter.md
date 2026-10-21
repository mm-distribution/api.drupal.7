# comment_form_node_type_form_alter()

- **Type:** Function
- **File:** [`modules/comment/comment.module`](_file.md), lines 1138–1210 · [local source](../../../../source/modules/comment/comment.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.module#L1138-L1210)
- **Module/theme:** comment
- **Implements:** [hook_form_FORM_ID_alter()](../../system/system.api.php/hook_form_FORM_ID_alter.md)

## Signature

```php
function comment_form_node_type_form_alter(&$form, $form_state)
```

## Documentation

```text
Implements hook_form_FORM_ID_alter().
```

## Code

```php
function comment_form_node_type_form_alter(&$form, $form_state) {
  if (isset($form['type'])) {
    $form['comment'] = array(
      '#type' => 'fieldset',
      '#title' => t('Comment settings'),
      '#collapsible' => TRUE,
      '#collapsed' => TRUE,
      '#group' => 'additional_settings',
      '#attributes' => array(
        'class' => array('comment-node-type-settings-form'),
      ),
      '#attached' => array(
        'js' => array(drupal_get_path('module', 'comment') . '/comment-node-form.js'),
      ),
    );
    // Unlike coment_form_node_form_alter(), all of these settings are applied
    // as defaults to all new nodes. Therefore, it would be wrong to use #states
    // to hide the other settings based on the primary comment setting.
    $form['comment']['comment'] = array(
      '#type' => 'select',
      '#title' => t('Default comment setting for new content'),
      '#default_value' => variable_get('comment_' . $form['#node_type']->type, COMMENT_NODE_OPEN),
      '#options' => array(
        COMMENT_NODE_OPEN => t('Open'),
        COMMENT_NODE_CLOSED => t('Closed'),
        COMMENT_NODE_HIDDEN => t('Hidden'),
      ),
    );
    $form['comment']['comment_default_mode'] = array(
      '#type' => 'checkbox',
      '#title' => t('Threading'),
      '#default_value' => variable_get('comment_default_mode_' . $form['#node_type']->type, COMMENT_MODE_THREADED),
      '#description' => t('Show comment replies in a threaded list.'),
    );
    $form['comment']['comment_default_per_page'] = array(
      '#type' => 'select',
      '#title' => t('Comments per page'),
      '#default_value' => variable_get('comment_default_per_page_' . $form['#node_type']->type, 50),
      '#options' => _comment_per_page(),
    );
    $form['comment']['comment_anonymous'] = array(
      '#type' => 'select',
      '#title' => t('Anonymous commenting'),
      '#default_value' => variable_get('comment_anonymous_' . $form['#node_type']->type, COMMENT_ANONYMOUS_MAYNOT_CONTACT),
      '#options' => array(
        COMMENT_ANONYMOUS_MAYNOT_CONTACT => t('Anonymous posters may not enter their contact information'),
        COMMENT_ANONYMOUS_MAY_CONTACT => t('Anonymous posters may leave their contact information'),
        COMMENT_ANONYMOUS_MUST_CONTACT => t('Anonymous posters must leave their contact information'),
      ),
      '#access' => user_access('post comments', drupal_anonymous_user()),
    );
    $form['comment']['comment_subject_field'] = array(
      '#type' => 'checkbox',
      '#title' => t('Allow comment title'),
      '#default_value' => variable_get('comment_subject_field_' . $form['#node_type']->type, 1),
    );
    $form['comment']['comment_form_location'] = array(
      '#type' => 'checkbox',
      '#title' => t('Show reply form on the same page as comments'),
      '#default_value' => variable_get('comment_form_location_' . $form['#node_type']->type, COMMENT_FORM_BELOW),
    );
    $form['comment']['comment_preview'] = array(
      '#type' => 'radios',
      '#title' => t('Preview comment'),
      '#default_value' => variable_get('comment_preview_' . $form['#node_type']->type, DRUPAL_OPTIONAL),
      '#options' => array(
        DRUPAL_DISABLED => t('Disabled'),
        DRUPAL_OPTIONAL => t('Optional'),
        DRUPAL_REQUIRED => t('Required'),
      ),
    );
  }
}
```

---
_Drupal 7.103 · [modules/comment/comment.module](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.module) · Licensed GPL-2.0-or-later (see LICENSE)._
