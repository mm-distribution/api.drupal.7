# system_date_time_formats()

- **Type:** Function
- **File:** [`modules/system/system.admin.inc`](_file.md), lines 2888–2912 · [local source](../../../../source/modules/system/system.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.admin.inc#L2888-L2912)
- **Module/theme:** system

## Signature

```php
function system_date_time_formats()
```

## Documentation

```text
Displays the date format strings overview page.
```

## Code

```php
function system_date_time_formats() {
  $header = array(t('Format'), array('data' => t('Operations'), 'colspan' => '2'));
  $rows = array();

  drupal_static_reset('system_get_date_formats');
  $formats = system_get_date_formats('custom');
  if (!empty($formats)) {
    foreach ($formats as $format) {
      $row = array();
      $row[] = array('data' => format_date(REQUEST_TIME, 'custom', $format['format']));
      $row[] = array('data' => l(t('edit'), 'admin/config/regional/date-time/formats/' . $format['dfid'] . '/edit'));
      $row[] = array('data' => l(t('delete'), 'admin/config/regional/date-time/formats/' . $format['dfid'] . '/delete'));
      $rows[] = $row;
    }
  }

  $build['date_formats_table'] = array(
    '#theme' => 'table',
    '#header' => $header,
    '#rows' => $rows,
    '#empty' => t('No custom date formats available. <a href="@link">Add date format</a>.', array('@link' => url('admin/config/regional/date-time/formats/add'))),
  );

  return $build;
}
```

---
_Drupal 7.103 · [modules/system/system.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/system/system.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
