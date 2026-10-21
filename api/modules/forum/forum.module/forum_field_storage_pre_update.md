# forum_field_storage_pre_update()

- **Type:** Function
- **File:** [`modules/forum/forum.module`](_file.md), lines 550–591 · [local source](../../../../source/modules/forum/forum.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/forum/forum.module#L550-L591)
- **Module/theme:** forum
- **Implements:** [hook_field_storage_pre_update()](../../field/field.api.php/hook_field_storage_pre_update.md)

## Signature

```php
function forum_field_storage_pre_update($entity_type, $entity, &$skip_fields)
```

## Documentation

```text
Implements hook_field_storage_pre_update().
```

## Code

```php
function forum_field_storage_pre_update($entity_type, $entity, &$skip_fields) {
  $first_call = &drupal_static(__FUNCTION__, array());

  if ($entity_type == 'node' && _forum_node_check_node_type($entity)) {

    // If the node is published, update the forum index.
    if ($entity->status) {

      // We don't maintain data for old revisions, so clear all previous values
      // from the table. Since this hook runs once per field, per object, make
      // sure we only wipe values once.
      if (!isset($first_call[$entity->nid])) {
        $first_call[$entity->nid] = FALSE;
        db_delete('forum_index')->condition('nid', $entity->nid)->execute();
      }
      $query = db_insert('forum_index')->fields(array('nid', 'title', 'tid', 'sticky', 'created', 'comment_count', 'last_comment_timestamp'));
      foreach ($entity->taxonomy_forums as $language) {
        foreach ($language as $item) {
          $query->values(array(
            'nid' => $entity->nid,
            'title' => $entity->title,
            'tid' => $item['tid'],
            'sticky' => $entity->sticky,
            'created' => $entity->created,
            'comment_count' => 0,
            'last_comment_timestamp' => $entity->created,
          ));
        }
      }
      $query->execute();
      // The logic for determining last_comment_count is fairly complex, so
      // call _forum_update_forum_index() too.
      _forum_update_forum_index($entity->nid);
    }

    // When a forum node is unpublished, remove it from the forum_index table.
    else {
      db_delete('forum_index')->condition('nid', $entity->nid)->execute();
    }

  }
}
```

---
_Drupal 7.103 · [modules/forum/forum.module](https://github.com/drupal/drupal/blob/7.103/modules/forum/forum.module) · Licensed GPL-2.0-or-later (see LICENSE)._
