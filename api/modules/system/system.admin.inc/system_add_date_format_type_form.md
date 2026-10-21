# system_add_date_format_type_form()

- **Type:** Function
- **File:** [`modules/system/system.admin.inc`](_file.md), lines 2133–2181 · [local source](../../../../source/modules/system/system.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.admin.inc#L2133-L2181)
- **Module/theme:** system
- **Topics:** [forms](../../../topics/forms.md), system_add_date_format_type_form_validate(), system_add_date_format_type_form_submit()

## Signature

```php
function system_add_date_format_type_form($form, &$form_state)
```

## Documentation

```text
Add new date type.

@ingroup forms
@ingroup system_add_date_format_type_form_validate()
@ingroup system_add_date_format_type_form_submit()
```

## Code

```php
function system_add_date_format_type_form($form, &$form_state) {
  $form['date_type'] = array(
    '#title' => t('Date type'),
    '#type' => 'textfield',
    '#required' => TRUE,
  );
  $form['machine_name'] = array(
    '#type' => 'machine_name',
    '#machine_name' => array(
      'exists' => 'system_get_date_types',
      'source' => array('date_type'),
    ),
  );

  // Get list of all available date formats.
  $formats = array();
  drupal_static_reset('system_get_date_formats');
  $date_formats = system_get_date_formats(); // Call this to rebuild the list, and to have default list.
  foreach ($date_formats as $type => $format_info) {
    $formats = array_merge($formats, $format_info);
  }
  $custom_formats = system_get_date_formats('custom');
  if (!empty($custom_formats)) {
    $formats = array_merge($formats, $custom_formats);
  }
  $choices = array();
  foreach ($formats as $f => $format) {
    $choices[$f] = format_date(REQUEST_TIME, 'custom', $f);
  }
  // Show date format select list.
  $form['date_format'] = array(
    '#type' => 'select',
    '#title' => t('Date format'),
    '#attributes' => array('class' => array('date-format')),
    '#options' => $choices,
    '#required' => TRUE,
  );

  $form['actions'] = array('#type' => 'actions');
  $form['actions']['submit'] = array(
    '#type' => 'submit',
    '#value' => t('Add date type'),
  );

  $form['#validate'][] = 'system_add_date_format_type_form_validate';
  $form['#submit'][] = 'system_add_date_format_type_form_submit';

  return $form;
}
```

---
_Drupal 7.103 · [modules/system/system.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/system/system.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
