# locale_date_format_language_overview_page()

- **Type:** Function
- **File:** [`modules/locale/locale.admin.inc`](_file.md), lines 1310–1328 · [local source](../../../../source/modules/locale/locale.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.admin.inc#L1310-L1328)
- **Module/theme:** locale

## Signature

```php
function locale_date_format_language_overview_page()
```

## Documentation

```text
Display edit date format links for each language.
```

## Code

```php
function locale_date_format_language_overview_page() {
  $header = array(
    t('Language'),
    array('data' => t('Operations'), 'colspan' => '2'),
  );

  // Get list of languages.
  $languages = locale_language_list('native');

  foreach ($languages as $langcode => $info) {
    $row = array();
    $row[] = $languages[$langcode];
    $row[] = l(t('edit'), 'admin/config/regional/date-time/locale/' . $langcode . '/edit');
    $row[] = l(t('reset'), 'admin/config/regional/date-time/locale/' . $langcode . '/reset');
    $rows[] = $row;
  }

  return theme('table', array('header' => $header, 'rows' => $rows));
}
```

---
_Drupal 7.103 · [modules/locale/locale.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
