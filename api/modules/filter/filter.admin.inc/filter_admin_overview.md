# filter_admin_overview()

- **Type:** Function
- **File:** [`modules/filter/filter.admin.inc`](_file.md), lines 15–47 · [local source](../../../../source/modules/filter/filter.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/filter/filter.admin.inc#L15-L47)
- **Module/theme:** filter
- **Topics:** [forms](../../../topics/forms.md)

## Signature

```php
function filter_admin_overview($form)
```

## Documentation

```text
Page callback: Form constructor for a form to list and reorder text formats.

@ingroup forms
@see filter_menu()
@see filter_admin_overview_submit()
```

## Code

```php
function filter_admin_overview($form) {
  // Overview of all formats.
  $formats = filter_formats();
  $fallback_format = filter_fallback_format();

  $form['#tree'] = TRUE;
  foreach ($formats as $id => $format) {
    // Check whether this is the fallback text format. This format is available
    // to all roles and cannot be disabled via the admin interface.
    $form['formats'][$id]['#is_fallback'] = ($id == $fallback_format);
    if ($form['formats'][$id]['#is_fallback']) {
      $form['formats'][$id]['name'] = array('#markup' => drupal_placeholder($format->name));
      $roles_markup = drupal_placeholder(t('All roles may use this format'));
    }
    else {
      $form['formats'][$id]['name'] = array('#markup' => check_plain($format->name));
      $roles = array_map('check_plain', filter_get_roles_by_format($format));
      $roles_markup = $roles ? implode(', ', $roles) : t('No roles may use this format');
    }
    $form['formats'][$id]['roles'] = array('#markup' => $roles_markup);
    $form['formats'][$id]['configure'] = array('#type' => 'link', '#title' => t('configure'), '#href' => 'admin/config/content/formats/' . $id);
    $form['formats'][$id]['disable'] = array('#type' => 'link', '#title' => t('disable'), '#href' => 'admin/config/content/formats/' . $id . '/disable', '#access' => !$form['formats'][$id]['#is_fallback']);
    $form['formats'][$id]['weight'] = array(
      '#type' => 'weight',
      '#title' => t('Weight for @title', array('@title' => $format->name)),
      '#title_display' => 'invisible',
      '#default_value' => $format->weight,
    );
  }
  $form['actions'] = array('#type' => 'actions');
  $form['actions']['submit'] = array('#type' => 'submit', '#value' => t('Save changes'));
  return $form;
}
```

---
_Drupal 7.103 · [modules/filter/filter.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/filter/filter.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
