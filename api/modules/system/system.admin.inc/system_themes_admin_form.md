# system_themes_admin_form()

- **Type:** Function
- **File:** [`modules/system/system.admin.inc`](_file.md), lines 258–282 · [local source](../../../../source/modules/system/system.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.admin.inc#L258-L282)
- **Module/theme:** system
- **Topics:** [forms](../../../topics/forms.md)

## Signature

```php
function system_themes_admin_form($form, &$form_state, $theme_options)
```

## Documentation

```text
Form to select the administration theme.

@ingroup forms
@see system_themes_admin_form_submit()
```

## Code

```php
function system_themes_admin_form($form, &$form_state, $theme_options) {
  // Administration theme settings.
  $form['admin_theme'] = array(
    '#type' => 'fieldset',
    '#title' => t('Administration theme'),
  );
  $form['admin_theme']['admin_theme'] = array(
    '#type' => 'select',
    '#options' => array(0 => t('Default theme')) + $theme_options,
    '#title' => t('Administration theme'),
    '#description' => t('Choose "Default theme" to always use the same theme as the rest of the site.'),
    '#default_value' => variable_get('admin_theme', 0),
  );
  $form['admin_theme']['node_admin_theme'] = array(
    '#type' => 'checkbox',
    '#title' => t('Use the administration theme when editing or creating content'),
    '#default_value' => variable_get('node_admin_theme', '0'),
  );
  $form['admin_theme']['actions'] = array('#type' => 'actions');
  $form['admin_theme']['actions']['submit'] = array(
    '#type' => 'submit',
    '#value' => t('Save configuration'),
  );
  return $form;
}
```

---
_Drupal 7.103 · [modules/system/system.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/system/system.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
