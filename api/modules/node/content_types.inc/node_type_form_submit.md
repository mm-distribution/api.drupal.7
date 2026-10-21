# node_type_form_submit()

- **Type:** Function
- **File:** [`modules/node/content_types.inc`](_file.md), lines 286–362 · [local source](../../../../source/modules/node/content_types.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/content_types.inc#L286-L362)
- **Module/theme:** node

## Signature

```php
function node_type_form_submit($form, &$form_state)
```

## Documentation

```text
Form submission handler for node_type_form().

@see node_type_form_validate()
```

## Code

```php
function node_type_form_submit($form, &$form_state) {
  $op = isset($form_state['values']['op']) ? $form_state['values']['op'] : '';

  $type = node_type_set_defaults();

  $type->type = $form_state['values']['type'];
  $type->name = trim($form_state['values']['name']);
  $type->orig_type = trim($form_state['values']['orig_type']);
  $type->old_type = isset($form_state['values']['old_type']) ? $form_state['values']['old_type'] : $type->type;

  $type->description = $form_state['values']['description'];
  $type->help = $form_state['values']['help'];
  $type->title_label = $form_state['values']['title_label'];
  // title_label is required in core; has_title will always be true, unless a
  // module alters the title field.
  $type->has_title = ($type->title_label != '');

  $type->base = !empty($form_state['values']['base']) ? $form_state['values']['base'] : 'node_content';
  $type->custom = $form_state['values']['custom'];
  $type->modified = TRUE;
  $type->locked = $form_state['values']['locked'];
  if (isset($form['#node_type']->module)) {
    $type->module = $form['#node_type']->module;
  }

  if ($op == t('Delete content type')) {
    $form_state['redirect'] = 'admin/structure/types/manage/' . str_replace('_', '-', $type->old_type) . '/delete';
    return;
  }

  $variables = $form_state['values'];

  // Remove everything that's been saved already - whatever's left is assumed
  // to be a persistent variable.
  foreach ($variables as $key => $value) {
    if (isset($type->$key)) {
      unset($variables[$key]);
    }
  }

  unset($variables['form_token'], $variables['op'], $variables['submit'], $variables['delete'], $variables['reset'], $variables['form_id'], $variables['form_build_id']);

  // Save or reset persistent variable values.
  foreach ($variables as $key => $value) {
    $variable_new = $key . '_' . $type->type;
    $variable_old = $key . '_' . $type->old_type;

    if (is_array($value)) {
      $value = array_keys(array_filter($value));
    }
    variable_set($variable_new, $value);

    if ($variable_new != $variable_old) {
      variable_del($variable_old);
    }
  }

  // Saving the content type after saving the variables allows modules to act
  // on those variables via hook_node_type_insert().
  $status = node_type_save($type);

  node_types_rebuild();
  menu_rebuild();
  $t_args = array('%name' => $type->name);

  if ($status == SAVED_UPDATED) {
    drupal_set_message(t('The content type %name has been updated.', $t_args));
  }
  elseif ($status == SAVED_NEW) {
    node_add_body_field($type);
    drupal_set_message(t('The content type %name has been added.', $t_args));
    watchdog('node', 'Added content type %name.', $t_args, WATCHDOG_NOTICE, l(t('view'), 'admin/structure/types'));
  }

  $form_state['redirect'] = 'admin/structure/types';
  return;
}
```

---
_Drupal 7.103 · [modules/node/content_types.inc](https://github.com/drupal/drupal/blob/7.103/modules/node/content_types.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
