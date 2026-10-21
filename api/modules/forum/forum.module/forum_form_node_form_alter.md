# forum_form_node_form_alter()

- **Type:** Function
- **File:** [`modules/forum/forum.module`](_file.md), lines 626–640 · [local source](../../../../source/modules/forum/forum.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/forum/forum.module#L626-L640)
- **Module/theme:** forum
- **Implements:** [hook_form_BASE_FORM_ID_alter()](../../system/system.api.php/hook_form_BASE_FORM_ID_alter.md)

## Signature

```php
function forum_form_node_form_alter(&$form, &$form_state, $form_id)
```

## Documentation

```text
Implements hook_form_BASE_FORM_ID_alter() for node_form().
```

## Code

```php
function forum_form_node_form_alter(&$form, &$form_state, $form_id) {
  if (isset($form['taxonomy_forums'])) {
    $langcode = $form['taxonomy_forums']['#language'];
    // Make the vocabulary required for 'real' forum-nodes.
    $form['taxonomy_forums'][$langcode]['#required'] = TRUE;
    $form['taxonomy_forums'][$langcode]['#multiple'] = FALSE;
    if (empty($form['taxonomy_forums'][$langcode]['#default_value'])) {
      // If there is no default forum already selected, try to get the forum
      // ID from the URL (e.g., if we are on a page like node/add/forum/2, we
      // expect "2" to be the ID of the forum that was requested).
      $requested_forum_id = arg(3);
      $form['taxonomy_forums'][$langcode]['#default_value'] = is_numeric($requested_forum_id) ? $requested_forum_id : '';
    }
  }
}
```

---
_Drupal 7.103 · [modules/forum/forum.module](https://github.com/drupal/drupal/blob/7.103/modules/forum/forum.module) · Licensed GPL-2.0-or-later (see LICENSE)._
