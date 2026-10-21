# comment_update_dependencies()

- **Type:** Function
- **File:** [`modules/comment/comment.install`](_file.md), lines 82–98 · [local source](../../../../source/modules/comment/comment.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.install#L82-L98)
- **Module/theme:** comment
- **Implements:** [hook_update_dependencies()](../../system/system.api.php/hook_update_dependencies.md)

## Signature

```php
function comment_update_dependencies()
```

## Documentation

```text
Implements hook_update_dependencies().
```

## Code

```php
function comment_update_dependencies() {
  // comment_update_7005() creates the comment body field and therefore must
  // run after all Field modules have been enabled, which happens in
  // system_update_7027().
  $dependencies['comment'][7005] = array(
    'system' => 7027,
  );

  // comment_update_7006() needs to query the {filter_format} table to get a
  // list of existing text formats, so it must run after filter_update_7000(),
  // which creates that table.
  $dependencies['comment'][7006] = array(
    'filter' => 7000,
  );

  return $dependencies;
}
```

---
_Drupal 7.103 · [modules/comment/comment.install](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.install) · Licensed GPL-2.0-or-later (see LICENSE)._
