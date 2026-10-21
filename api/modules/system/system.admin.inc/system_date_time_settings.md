# system_date_time_settings()

- **Type:** Function
- **File:** [`modules/system/system.admin.inc`](_file.md), lines 2023–2090 · [local source](../../../../source/modules/system/system.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.admin.inc#L2023-L2090)
- **Module/theme:** system
- **Topics:** [forms](../../../topics/forms.md)

## Signature

```php
function system_date_time_settings()
```

## Documentation

```text
Form builder; Configure the site date and time settings.

@ingroup forms
@see system_settings_form()
```

## Code

```php
function system_date_time_settings() {
  // Get list of all available date types.
  drupal_static_reset('system_get_date_types');
  $format_types = system_get_date_types();

  // Get list of all available date formats.
  $all_formats = array();
  drupal_static_reset('system_get_date_formats');
  $date_formats = system_get_date_formats(); // Call this to rebuild the list, and to have default list.
  foreach ($date_formats as $type => $format_info) {
    $all_formats = array_merge($all_formats, $format_info);
  }
  $custom_formats = system_get_date_formats('custom');
  if (!empty($format_types)) {
    foreach ($format_types as $type => $type_info) {
      // If a system type, only show the available formats for that type and
      // custom ones.
      if ($type_info['locked'] == 1) {
        $formats = system_get_date_formats($type);
        if (empty($formats)) {
          $formats = $all_formats;
        }
        elseif (!empty($custom_formats)) {
          $formats = array_merge($formats, $custom_formats);
        }
      }
      // If a user configured type, show all available date formats.
      else {
        $formats = $all_formats;
      }

      $choices = array();
      foreach ($formats as $f => $format) {
        $choices[$f] = format_date(REQUEST_TIME, 'custom', $f);
      }
      reset($formats);
      $default = variable_get('date_format_' . $type, key($formats));

      // Get date type info for this date type.
      $type_info = system_get_date_types($type);
      $form['formats']['#theme'] = 'system_date_time_settings';

      // Show date format select list.
      $form['formats']['format']['date_format_' . $type] = array(
        '#type' => 'select',
        '#title' => check_plain($type_info['title']),
        '#attributes' => array('class' => array('date-format')),
        '#default_value' => (isset($choices[$default]) ? $default : 'custom'),
        '#options' => $choices,
      );

      // If this isn't a system provided type, allow the user to remove it from
      // the system.
      if ($type_info['locked'] == 0) {
        $form['formats']['delete']['date_format_' . $type . '_delete'] = array(
          '#type' => 'link',
          '#title' => t('delete'),
          '#href' => 'admin/config/regional/date-time/types/' . $type . '/delete',
        );
      }
    }
  }

  // Display a message if no date types configured.
  $form['#empty_text'] = t('No date types available. <a href="@link">Add date type</a>.', array('@link' => url('admin/config/regional/date-time/types/add')));

  return system_settings_form($form);
}
```

---
_Drupal 7.103 · [modules/system/system.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/system/system.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
