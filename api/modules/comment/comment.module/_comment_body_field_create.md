# _comment_body_field_create()

- **Type:** Function
- **File:** [`modules/comment/comment.module`](_file.md), lines 362–393 · [local source](../../../../source/modules/comment/comment.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.module#L362-L393)
- **Module/theme:** comment

## Signature

```php
function _comment_body_field_create($info)
```

## Documentation

```text
Creates a comment_body field instance for a given node type.
```

## Code

```php
function _comment_body_field_create($info) {
  // Create the field if needed.
  if (!field_read_field('comment_body', array('include_inactive' => TRUE))) {
    $field = array(
      'field_name' => 'comment_body',
      'type' => 'text_long',
      'entity_types' => array('comment'),
    );
    field_create_field($field);
  }
  // Create the instance if needed.
  if (!field_read_instance('comment', 'comment_body', 'comment_node_' . $info->type, array('include_inactive' => TRUE))) {
    field_attach_create_bundle('comment', 'comment_node_' . $info->type);
    // Attaches the body field by default.
    $instance = array(
      'field_name' => 'comment_body',
      'label' => 'Comment',
      'entity_type' => 'comment',
      'bundle' => 'comment_node_' . $info->type,
      'settings' => array('text_processing' => 1),
      'required' => TRUE,
      'display' => array(
        'default' => array(
          'label' => 'hidden',
          'type' => 'text_default',
          'weight' => 0,
        ),
      ),
    );
    field_create_instance($instance);
  }
}
```

---
_Drupal 7.103 · [modules/comment/comment.module](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.module) · Licensed GPL-2.0-or-later (see LICENSE)._
