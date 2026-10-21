# comment_file_download_access()

- **Type:** Function
- **File:** [`modules/comment/comment.module`](_file.md), lines 2752–2760 · [local source](../../../../source/modules/comment/comment.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.module#L2752-L2760)
- **Module/theme:** comment
- **Implements:** [hook_file_download_access()](../../file/file.api.php/hook_file_download_access.md)

## Signature

```php
function comment_file_download_access($field, $entity_type, $entity)
```

## Documentation

```text
Implements hook_file_download_access().
```

## Code

```php
function comment_file_download_access($field, $entity_type, $entity) {
  if ($entity_type == 'comment') {
    if (user_access('access comments') && $entity->status == COMMENT_PUBLISHED || user_access('administer comments')) {
      $node = node_load($entity->nid);
      return node_access('view', $node);
    }
    return FALSE;
  }
}
```

---
_Drupal 7.103 · [modules/comment/comment.module](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.module) · Licensed GPL-2.0-or-later (see LICENSE)._
