# comment_field_extra_fields()

- **Type:** Function
- **File:** [`modules/comment/comment.module`](_file.md), lines 167–190 · [local source](../../../../source/modules/comment/comment.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.module#L167-L190)
- **Module/theme:** comment
- **Implements:** [hook_field_extra_fields()](../../field/field.api.php/hook_field_extra_fields.md)

## Signature

```php
function comment_field_extra_fields()
```

## Documentation

```text
Implements hook_field_extra_fields().
```

## Code

```php
function comment_field_extra_fields() {
  $return = array();

  foreach (node_type_get_types() as $type) {
    if (variable_get('comment_subject_field_' . $type->type, 1) == 1) {
      $return['comment']['comment_node_' . $type->type] = array(
        'form' => array(
          'author' => array(
            'label' => t('Author'),
            'description' => t('Author textfield'),
            'weight' => -2,
          ),
          'subject' => array(
            'label' => t('Subject'),
            'description' => t('Subject textfield'),
            'weight' => -1,
          ),
        ),
      );
    }
  }

  return $return;
}
```

---
_Drupal 7.103 · [modules/comment/comment.module](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.module) · Licensed GPL-2.0-or-later (see LICENSE)._
