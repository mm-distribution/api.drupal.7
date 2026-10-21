# node_add_body_field()

- **Type:** Function
- **File:** [`modules/node/node.module`](_file.md), lines 587–621 · [local source](../../../../source/modules/node/node.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/node.module#L587-L621)
- **Module/theme:** node

## Signature

```php
function node_add_body_field($type, $label = 'Body')
```

## Documentation

```text
Adds default body field to a node type.

@param $type
  A node type object.
@param $label
  The label for the body instance.

@return
  Body field instance.
```

## Code

```php
function node_add_body_field($type, $label = 'Body') {
   // Add or remove the body field, as needed.
  $field = field_info_field('body');
  $instance = field_info_instance('node', 'body', $type->type);
  if (empty($field)) {
    $field = array(
      'field_name' => 'body',
      'type' => 'text_with_summary',
      'entity_types' => array('node'),
    );
    $field = field_create_field($field);
  }
  if (empty($instance)) {
    $instance = array(
      'field_name' => 'body',
      'entity_type' => 'node',
      'bundle' => $type->type,
      'label' => $label,
      'widget' => array('type' => 'text_textarea_with_summary'),
      'settings' => array('display_summary' => TRUE),
      'display' => array(
        'default' => array(
          'label' => 'hidden',
          'type' => 'text_default',
        ),
        'teaser' => array(
          'label' => 'hidden',
          'type' => 'text_summary_or_trimmed',
        ),
      ),
    );
    $instance = field_create_instance($instance);
  }
  return $instance;
}
```

---
_Drupal 7.103 · [modules/node/node.module](https://github.com/drupal/drupal/blob/7.103/modules/node/node.module) · Licensed GPL-2.0-or-later (see LICENSE)._
