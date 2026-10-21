# node_type_delete_confirm()

- **Type:** Function
- **File:** [`modules/node/content_types.inc`](_file.md), lines 415–432 · [local source](../../../../source/modules/node/content_types.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/content_types.inc#L415-L432)
- **Module/theme:** node
- **Topics:** [forms](../../../topics/forms.md)

## Signature

```php
function node_type_delete_confirm($form, &$form_state, $type)
```

## Documentation

```text
Menu callback; delete a single content type.

@ingroup forms
```

## Code

```php
function node_type_delete_confirm($form, &$form_state, $type) {
  $form['type'] = array('#type' => 'value', '#value' => $type->type);
  $form['name'] = array('#type' => 'value', '#value' => $type->name);

  $message = t('Are you sure you want to delete the content type %type?', array('%type' => $type->name));

  $num_nodes = db_query("SELECT COUNT(*) FROM {node} WHERE type = :type", array(':type' => $type->type))->fetchField();
  if ($num_nodes) {
    drupal_set_title($message, PASS_THROUGH);
    $caption = '<p>' . format_plural($num_nodes, '%type is used by 1 piece of content on your site. You cannot remove this content type until you have removed all of the %type content.', '%type is used by @count pieces of content on your site. You cannot remove this content type until you have removed all of the %type content.', array('%type' => $type->name)) . '</p>';
    $form['description'] = array('#markup' => $caption);
    return $form;
  }

  $caption = '<p>' . t('This action cannot be undone.') . '</p>';

  return confirm_form($form, $message, 'admin/structure/types', $caption, t('Delete'));
}
```

---
_Drupal 7.103 · [modules/node/content_types.inc](https://github.com/drupal/drupal/blob/7.103/modules/node/content_types.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
