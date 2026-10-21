# comment_update_7006()

- **Type:** Function
- **File:** [`modules/comment/comment.install`](_file.md), lines 289–342 · [local source](../../../../source/modules/comment/comment.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.install#L289-L342)
- **Module/theme:** comment
- **Topics:** [updates-6.x-to-7.x](../../../topics/updates-6.x-to-7.x.md)

## Signature

```php
function comment_update_7006(&$sandbox)
```

## Documentation

```text
Migrate data from the comment field to field storage.
```

## Code

```php
function comment_update_7006(&$sandbox) {
  // This is a multipass update. First set up some comment variables.
  if (empty($sandbox['total'])) {
    $comments = (bool) db_query_range('SELECT 1 FROM {comment}', 0, 1)->fetchField();
    $sandbox['types'] = array();
    if ($comments) {
      $sandbox['types'] = array_keys(_update_7000_node_get_types());
    }
    $sandbox['total'] = count($sandbox['types']);
  }

  if (!empty($sandbox['types'])) {
    $type = array_shift($sandbox['types']);

    $query = db_select('comment', 'c');
    $query->innerJoin('node', 'n', 'c.nid = n.nid AND n.type = :type', array(':type' => $type));
    $query->addField('c', 'cid', 'entity_id');
    $query->addExpression("'comment_node_$type'", 'bundle');
    $query->addExpression("'comment'", 'entity_type');
    $query->addExpression('0', 'deleted');
    $query->addExpression("'" . LANGUAGE_NONE . "'", 'language');
    $query->addExpression('0', 'delta');
    $query->addField('c', 'comment', 'comment_body_value');
    $query->addField('c', 'format', 'comment_body_format');

    db_insert('field_data_comment_body')
      ->from($query)
      ->execute();

    $sandbox['#finished'] = 1 - count($sandbox['types']) / $sandbox['total'];
  }

  // On the last pass of the update, $sandbox['types'] will be empty.
  if (empty($sandbox['types'])) {
    // Update the comment body text formats. For an explanation of these
    // updates, see the code comments in user_update_7010().
    db_update('field_data_comment_body')
      ->fields(array('comment_body_format' => NULL))
      ->condition('comment_body_value', '')
      ->condition('comment_body_format', 0)
      ->execute();
    $existing_formats = db_query("SELECT format FROM {filter_format}")->fetchCol();
    $default_format = variable_get('filter_default_format', 1);
    db_update('field_data_comment_body')
      ->fields(array('comment_body_format' => $default_format))
      ->isNotNull('comment_body_format')
      ->condition('comment_body_format', $existing_formats, 'NOT IN')
      ->execute();

    // Finally, remove the old comment data.
    db_drop_field('comment', 'comment');
    db_drop_field('comment', 'format');
  }
}
```

---
_Drupal 7.103 · [modules/comment/comment.install](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.install) · Licensed GPL-2.0-or-later (see LICENSE)._
