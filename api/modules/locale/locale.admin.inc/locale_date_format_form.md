# locale_date_format_form()

- **Type:** Function
- **File:** [`modules/locale/locale.admin.inc`](_file.md), lines 1333–1390 · [local source](../../../../source/modules/locale/locale.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.admin.inc#L1333-L1390)
- **Module/theme:** locale

## Signature

```php
function locale_date_format_form($form, &$form_state, $langcode)
```

## Documentation

```text
Provide date localization configuration options to users.
```

## Code

```php
function locale_date_format_form($form, &$form_state, $langcode) {
  $languages = locale_language_list('native');
  $language_name = $languages[$langcode];

  // Display the current language name.
  $form['language'] = array(
    '#type' => 'item',
    '#title' => t('Language'),
    '#markup' => check_plain($language_name),
    '#weight' => -10,
  );
  $form['langcode'] = array(
    '#type' => 'value',
    '#value' => $langcode,
  );

  // Get list of date format types.
  $types = system_get_date_types();

  // Get list of available formats.
  $formats = system_get_date_formats();
  $choices = array();
  foreach ($formats as $type => $list) {
    foreach ($list as $f => $format) {
      $choices[$f] = format_date(REQUEST_TIME, 'custom', $f);
    }
  }
  reset($formats);

  // Get configured formats for each language.
  $locale_formats = system_date_format_locale($langcode);
  // Display a form field for each format type.
  foreach ($types as $type => $type_info) {
    if (!empty($locale_formats) && in_array($type, array_keys($locale_formats))) {
      $default = $locale_formats[$type];
    }
    else {
      $default = variable_get('date_format_' . $type, key($formats));
    }

    // Show date format select list.
    $form['date_formats']['date_format_' . $type] = array(
      '#type' => 'select',
      '#title' => check_plain($type_info['title']),
      '#attributes' => array('class' => array('date-format')),
      '#default_value' => (isset($choices[$default]) ? $default : 'custom'),
      '#options' => $choices,
    );
  }

  $form['actions'] = array('#type' => 'actions');
  $form['actions']['submit'] = array(
    '#type' => 'submit',
    '#value' => t('Save configuration'),
  );

  return $form;
}
```

---
_Drupal 7.103 · [modules/locale/locale.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
