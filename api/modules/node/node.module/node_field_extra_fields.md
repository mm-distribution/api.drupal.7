# node_field_extra_fields()

- **Type:** Function
- **File:** [`modules/node/node.module`](_file.md), lines 626–644 · [local source](../../../../source/modules/node/node.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/node.module#L626-L644)
- **Module/theme:** node
- **Implements:** [hook_field_extra_fields()](../../field/field.api.php/hook_field_extra_fields.md)

## Signature

```php
function node_field_extra_fields()
```

## Documentation

```text
Implements hook_field_extra_fields().
```

## Code

```php
function node_field_extra_fields() {
  $extra = array();

  foreach (node_type_get_types() as $type) {
    if ($type->has_title) {
      $extra['node'][$type->type] = array(
        'form' => array(
          'title' => array(
            'label' => $type->title_label,
            'description' => t('Node module element'),
            'weight' => -5,
          ),
        ),
      );
    }
  }

  return $extra;
}
```

---
_Drupal 7.103 · [modules/node/node.module](https://github.com/drupal/drupal/blob/7.103/modules/node/node.module) · Licensed GPL-2.0-or-later (see LICENSE)._
