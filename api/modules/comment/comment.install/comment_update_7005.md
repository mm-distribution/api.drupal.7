# comment_update_7005()

- **Type:** Function
- **File:** [`modules/comment/comment.install`](_file.md), lines 236–284 · [local source](../../../../source/modules/comment/comment.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.install#L236-L284)
- **Module/theme:** comment
- **Topics:** [updates-6.x-to-7.x](../../../topics/updates-6.x-to-7.x.md)

## Signature

```php
function comment_update_7005()
```

## Documentation

```text
Create the comment_body field.
```

## Code

```php
function comment_update_7005() {
  // Create comment body field.
  $field = array(
    'field_name' => 'comment_body',
    'type' => 'text_long',
    'module' => 'text',
    'entity_types' => array(
      'comment',
    ),
    'settings' => array(),
    'cardinality' => 1,
  );
  _update_7000_field_create_field($field);

  // Add the field to comments for all existing bundles.
  $generic_instance = array(
    'entity_type' => 'comment',
    'label' => t('Comment'),
    'settings' => array(
      'text_processing' => 1,
    ),
    'required' => TRUE,
    'display' => array(
      'default' => array(
        'label' => 'hidden',
        'type' => 'text_default',
        'weight' => 0,
        'settings' => array(),
        'module' => 'text',
      ),
    ),
    'widget' => array(
      'type' => 'text_textarea',
      'settings' => array(
        'rows' => 5,
      ),
      'weight' => 0,
      'module' => 'text',
    ),
    'description' => '',
  );

  $types = _update_7000_node_get_types();
  foreach ($types as $type => $type_object) {
    $instance = $generic_instance;
    $instance['bundle'] = 'comment_node_' . $type;
    _update_7000_field_create_instance($field, $instance);
  }
}
```

---
_Drupal 7.103 · [modules/comment/comment.install](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.install) · Licensed GPL-2.0-or-later (see LICENSE)._
