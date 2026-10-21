# forum_form()

- **Type:** Function
- **File:** [`modules/forum/forum.module`](_file.md), lines 731–749 · [local source](../../../../source/modules/forum/forum.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/forum/forum.module#L731-L749)
- **Module/theme:** forum
- **Implements:** [hook_form()](../../node/node.api.php/hook_form.md)

## Signature

```php
function forum_form($node, $form_state)
```

## Documentation

```text
Implements hook_form().
```

## Code

```php
function forum_form($node, $form_state) {
  $type = node_type_get_type($node);
  $form['title'] = array(
    '#type' => 'textfield',
    '#title' => check_plain($type->title_label),
    '#default_value' => !empty($node->title) ? $node->title : '',
    '#required' => TRUE, '#weight' => -5
  );

  if (!empty($node->nid)) {
    $forum_terms = $node->taxonomy_forums;
    // If editing, give option to leave shadows.
    $shadow = (count($forum_terms) > 1);
    $form['shadow'] = array('#type' => 'checkbox', '#title' => t('Leave shadow copy'), '#default_value' => $shadow, '#description' => t('If you move this topic, you can leave a link in the old forum to the new forum.'));
    $form['forum_tid'] = array('#type' => 'value', '#value' => $node->forum_tid);
  }

  return $form;
}
```

---
_Drupal 7.103 · [modules/forum/forum.module](https://github.com/drupal/drupal/blob/7.103/modules/forum/forum.module) · Licensed GPL-2.0-or-later (see LICENSE)._
