# system_modules_uninstall_confirm_form()

- **Type:** Function
- **File:** [`modules/system/system.admin.inc`](_file.md), lines 1333–1362 · [local source](../../../../source/modules/system/system.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.admin.inc#L1333-L1362)
- **Module/theme:** system
- **Topics:** [forms](../../../topics/forms.md)

## Signature

```php
function system_modules_uninstall_confirm_form($storage)
```

## Documentation

```text
Confirm uninstall of selected modules.

@ingroup forms
@param $storage
  An associative array of modules selected to be uninstalled.
@return
  A form array representing modules to confirm.
```

## Code

```php
function system_modules_uninstall_confirm_form($storage) {
  // Nothing to build.
  if (empty($storage)) {
    return;
  }

  // Construct the hidden form elements and list items.
  foreach (array_filter($storage['uninstall']) as $module => $value) {
    $info = drupal_parse_info_file(drupal_get_path('module', $module) . '/' . $module . '.info');
    $uninstall[] = $info['name'];
    $form['uninstall'][$module] = array('#type' => 'hidden',
      '#value' => 1,
    );
  }

  // Display a confirm form if modules have been selected.
  if (isset($uninstall)) {
    $form['#confirmed'] = TRUE;
    $form['uninstall']['#tree'] = TRUE;
    $form['modules'] = array('#markup' => '<p>' . t('The following modules will be completely uninstalled from your site, and <em>all data from these modules will be lost</em>!') . '</p>' . theme('item_list', array('items' => $uninstall)));
    $form = confirm_form(
      $form,
      t('Confirm uninstall'),
      'admin/modules/uninstall',
      t('Would you like to continue with uninstalling the above?'),
      t('Uninstall'),
      t('Cancel'));
    return $form;
  }
}
```

---
_Drupal 7.103 · [modules/system/system.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/system/system.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
