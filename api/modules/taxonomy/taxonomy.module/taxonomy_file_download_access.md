# taxonomy_file_download_access()

- **Type:** Function
- **File:** [`modules/taxonomy/taxonomy.module`](_file.md), lines 2068–2072 · [local source](../../../../source/modules/taxonomy/taxonomy.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.module#L2068-L2072)
- **Module/theme:** taxonomy
- **Implements:** [hook_file_download_access()](../../file/file.api.php/hook_file_download_access.md)

## Signature

```php
function taxonomy_file_download_access($field, $entity_type, $entity)
```

## Documentation

```text
Implements hook_file_download_access().
```

## Code

```php
function taxonomy_file_download_access($field, $entity_type, $entity) {
  if ($entity_type == 'taxonomy_term') {
    return user_access('access content');
  }
}
```

---
_Drupal 7.103 · [modules/taxonomy/taxonomy.module](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.module) · Licensed GPL-2.0-or-later (see LICENSE)._
