# comment_forms()

- **Type:** Function
- **File:** [`modules/comment/comment.module`](_file.md), lines 1840–1846 · [local source](../../../../source/modules/comment/comment.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.module#L1840-L1846)
- **Module/theme:** comment
- **Implements:** [hook_forms()](../../system/system.api.php/hook_forms.md)

## Signature

```php
function comment_forms()
```

## Documentation

```text
Implements hook_forms().
```

## Code

```php
function comment_forms() {
  $forms = array();
  foreach (node_type_get_types() as $type) {
    $forms["comment_node_{$type->type}_form"]['callback'] = 'comment_form';
  }
  return $forms;
}
```

---
_Drupal 7.103 · [modules/comment/comment.module](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.module) · Licensed GPL-2.0-or-later (see LICENSE)._
