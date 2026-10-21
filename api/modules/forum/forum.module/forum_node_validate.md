# forum_node_validate()

- **Type:** Function
- **File:** [`modules/forum/forum.module`](_file.md), lines 291–320 · [local source](../../../../source/modules/forum/forum.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/forum/forum.module#L291-L320)
- **Module/theme:** forum
- **Implements:** [hook_node_validate()](../../node/node.api.php/hook_node_validate.md)

## Signature

```php
function forum_node_validate($node, $form)
```

## Documentation

```text
Implements hook_node_validate().

Checks in particular that the node is assigned only a "leaf" term in the
forum taxonomy.
```

## Code

```php
function forum_node_validate($node, $form) {
  if (_forum_node_check_node_type($node)) {
    $langcode = $form['taxonomy_forums']['#language'];
    // vocabulary is selected, not a "container" term.
    if (!empty($node->taxonomy_forums[$langcode])) {
      // Extract the node's proper topic ID.
      $containers = variable_get('forum_containers', array());
      foreach ($node->taxonomy_forums[$langcode] as $delta => $item) {
        // If no term was selected (e.g. when no terms exist yet), remove the
        // item.
        if (empty($item['tid'])) {
          unset($node->taxonomy_forums[$langcode][$delta]);
          continue;
        }
        $term = taxonomy_term_load($item['tid']);
        if (!$term) {
          form_set_error('taxonomy_forums', t('Select a forum.'));
          continue;
        }
        $used = db_query_range('SELECT 1 FROM {taxonomy_term_data} WHERE tid = :tid AND vid = :vid',0 , 1, array(
          ':tid' => $term->tid,
          ':vid' => $term->vid,
        ))->fetchField();
        if ($used && in_array($term->tid, $containers)) {
          form_set_error('taxonomy_forums', t('The item %forum is a forum container, not a forum. Select one of the forums below instead.', array('%forum' => $term->name)));
        }
      }
    }
  }
}
```

---
_Drupal 7.103 · [modules/forum/forum.module](https://github.com/drupal/drupal/blob/7.103/modules/forum/forum.module) · Licensed GPL-2.0-or-later (see LICENSE)._
