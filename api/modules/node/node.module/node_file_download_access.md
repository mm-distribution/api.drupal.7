# node_file_download_access()

- **Type:** Function
- **File:** [`modules/node/node.module`](_file.md), lines 4197–4201 · [local source](../../../../source/modules/node/node.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/node.module#L4197-L4201)
- **Module/theme:** node
- **Implements:** [hook_file_download_access()](../../file/file.api.php/hook_file_download_access.md)

## Signature

```php
function node_file_download_access($field, $entity_type, $entity)
```

## Documentation

```text
Implements hook_file_download_access().
```

## Code

```php
function node_file_download_access($field, $entity_type, $entity) {
  if ($entity_type == 'node') {
    return node_access('view', $entity);
  }
}
```

---
_Drupal 7.103 · [modules/node/node.module](https://github.com/drupal/drupal/blob/7.103/modules/node/node.module) · Licensed GPL-2.0-or-later (see LICENSE)._
