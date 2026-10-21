# system_configure_date_formats_form()

- **Type:** Function
- **File:** [`modules/system/system.admin.inc`](_file.md), lines 2917–2964 · [local source](../../../../source/modules/system/system.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.admin.inc#L2917-L2964)
- **Module/theme:** system

## Signature

```php
function system_configure_date_formats_form($form, &$form_state, $dfid = 0)
```

## Documentation

```text
Allow users to add additional date formats.
```

## Code

```php
function system_configure_date_formats_form($form, &$form_state, $dfid = 0) {
  $ajax_path = 'admin/config/regional/date-time/formats/lookup';
  $js_settings = array(
    'type' => 'setting',
    'data' => array(
      'dateTime' => array(
        'date-format' => array(
          'text' => t('Displayed as'),
          'lookup' => url($ajax_path, array('query' => array('token' => drupal_get_token($ajax_path)))),
        ),
      ),
    ),
  );

  if ($dfid) {
    $form['dfid'] = array(
      '#type' => 'value',
      '#value' => $dfid,
    );
    $format = system_get_date_format($dfid);
  }

  $now = ($dfid ? t('Displayed as %date', array('%date' => format_date(REQUEST_TIME, 'custom', $format->format))) : '');

  $form['date_format'] = array(
    '#type' => 'textfield',
    '#title' => t('Format string'),
    '#maxlength' => 100,
    '#description' => t('A user-defined date format. See the <a href="@url">PHP manual</a> for available options.', array('@url' => 'http://php.net/manual/function.date.php')),
    '#default_value' => ($dfid ? $format->format : ''),
    '#field_suffix' => ' <small id="edit-date-format-suffix">' . $now . '</small>',
    '#attached' => array(
      'js' => array(drupal_get_path('module', 'system') . '/system.js', $js_settings),
    ),
    '#required' => TRUE,
  );

  $form['actions'] = array('#type' => 'actions');
  $form['actions']['update'] = array(
    '#type' => 'submit',
    '#value' => ($dfid ? t('Save format') : t('Add format')),
  );

  $form['#validate'][] = 'system_add_date_formats_form_validate';
  $form['#submit'][] = 'system_add_date_formats_form_submit';

  return $form;
}
```

---
_Drupal 7.103 · [modules/system/system.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/system/system.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
