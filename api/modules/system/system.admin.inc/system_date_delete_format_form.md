# system_date_delete_format_form()

- **Type:** Function
- **File:** [`modules/system/system.admin.inc`](_file.md), lines 2821–2837 · [local source](../../../../source/modules/system/system.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.admin.inc#L2821-L2837)
- **Module/theme:** system

## Signature

```php
function system_date_delete_format_form($form, &$form_state, $dfid)
```

## Documentation

```text
Menu callback; present a form for deleting a date format.
```

## Code

```php
function system_date_delete_format_form($form, &$form_state, $dfid) {
  $form['dfid'] = array(
    '#type' => 'value',
    '#value' => $dfid,
  );
  $format = system_get_date_format($dfid);

  $output = confirm_form($form,
    t('Are you sure you want to remove the format %format?', array('%format' => format_date(REQUEST_TIME, 'custom', $format->format))),
    'admin/config/regional/date-time/formats',
    t('This action cannot be undone.'),
    t('Remove'), t('Cancel'),
    'confirm'
  );

  return $output;
}
```

---
_Drupal 7.103 · [modules/system/system.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/system/system.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
