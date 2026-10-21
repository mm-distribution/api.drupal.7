# forum_field_storage_pre_insert()

- **Type:** Function
- **File:** [`modules/forum/forum.module`](_file.md), lines 527–545 · [local source](../../../../source/modules/forum/forum.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/forum/forum.module#L527-L545)
- **Module/theme:** forum
- **Implements:** [hook_field_storage_pre_insert()](../../field/field.api.php/hook_field_storage_pre_insert.md)

## Signature

```php
function forum_field_storage_pre_insert($entity_type, $entity, &$skip_fields)
```

## Documentation

```text
Implements hook_field_storage_pre_insert().
```

## Code

```php
function forum_field_storage_pre_insert($entity_type, $entity, &$skip_fields) {
  if ($entity_type == 'node' && $entity->status && _forum_node_check_node_type($entity)) {
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
  }
}
```

---
_Drupal 7.103 · [modules/forum/forum.module](https://github.com/drupal/drupal/blob/7.103/modules/forum/forum.module) · Licensed GPL-2.0-or-later (see LICENSE)._
