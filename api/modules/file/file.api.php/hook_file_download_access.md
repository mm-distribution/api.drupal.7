# hook_file_download_access()

- **Type:** Hook (documentation function)
- **File:** [`modules/file/file.api.php`](_file.md), lines 29–33 · [local source](../../../../source/modules/file/file.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/file/file.api.php#L29-L33)
- **Module/theme:** file

## Signature

```php
function hook_file_download_access($file_item, $entity_type, $entity)
```

## Documentation

```text
Control download access to files.

The hook is typically implemented to limit access based on the entity the
file is referenced, e.g., only users with access to a node should be allowed
to download files attached to that node.

@param array $file_item
  The array of information about the file to check access for.
@param $entity_type
  The type of $entity; for example, 'node' or 'user'.
@param $entity
  The $entity to which $file is referenced.

@return
  TRUE is access should be allowed by this entity or FALSE if denied. Note
  that denial may be overridden by another entity controller, making this
  grant permissive rather than restrictive.

@see hook_field_access().
```

## Code

```php
function hook_file_download_access($file_item, $entity_type, $entity) {
  if ($entity_type == 'node') {
    return node_access('view', $entity);
  }
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_file_download_access()".

- [comment_file_download_access()](../../comment/comment.module/comment_file_download_access.md) — `modules/comment/comment.module`
- [node_file_download_access()](../../node/node.module/node_file_download_access.md) — `modules/node/node.module`
- [taxonomy_file_download_access()](../../taxonomy/taxonomy.module/taxonomy_file_download_access.md) — `modules/taxonomy/taxonomy.module`
- [user_file_download_access()](../../user/user.module/user_file_download_access.md) — `modules/user/user.module`

---
_Drupal 7.103 · [modules/file/file.api.php](https://github.com/drupal/drupal/blob/7.103/modules/file/file.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
