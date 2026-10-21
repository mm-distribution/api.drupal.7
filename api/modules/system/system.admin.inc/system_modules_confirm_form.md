# system_modules_confirm_form()

- **Type:** Function
- **File:** [`modules/system/system.admin.inc`](_file.md), lines 1077–1112 · [local source](../../../../source/modules/system/system.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.admin.inc#L1077-L1112)
- **Module/theme:** system
- **Topics:** [forms](../../../topics/forms.md)

## Signature

```php
function system_modules_confirm_form($modules, $storage)
```

## Documentation

```text
Display confirmation form for required modules.

@param $modules
  Array of module file objects as returned from system_rebuild_module_data().
@param $storage
  The contents of $form_state['storage']; an array with two
  elements: the list of required modules and the list of status
  form field values from the previous screen.
@ingroup forms
```

## Code

```php
function system_modules_confirm_form($modules, $storage) {
  $items = array();

  $form['validation_modules'] = array('#type' => 'value', '#value' => $modules);
  $form['status']['#tree'] = TRUE;

  foreach ($storage['more_required'] as $info) {
    $t_argument = array(
      '@module' => $info['name'],
      '@required' => implode(', ', $info['requires']),
    );
    $items[] = format_plural(count($info['requires']), 'You must enable the @required module to install @module.', 'You must enable the @required modules to install @module.', $t_argument);
  }

  foreach ($storage['missing_modules'] as $name => $info) {
    $t_argument = array(
      '@module' => $name,
      '@depends' => implode(', ', $info['depends']),
    );
    $items[] = format_plural(count($info['depends']), 'The @module module is missing, so the following module will be disabled: @depends.', 'The @module module is missing, so the following modules will be disabled: @depends.', $t_argument);
  }

  $form['text'] = array('#markup' => theme('item_list', array('items' => $items)));

  if ($form) {
    // Set some default form values
    $form = confirm_form(
      $form,
      t('Some required modules must be enabled'),
      'admin/modules',
      t('Would you like to continue with the above?'),
      t('Continue'),
      t('Cancel'));
    return $form;
  }
}
```

---
_Drupal 7.103 · [modules/system/system.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/system/system.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
