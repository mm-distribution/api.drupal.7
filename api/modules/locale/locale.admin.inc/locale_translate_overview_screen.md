# locale_translate_overview_screen()

- **Type:** Function
- **File:** [`modules/locale/locale.admin.inc`](_file.md), lines 756–788 · [local source](../../../../source/modules/locale/locale.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.admin.inc#L756-L788)
- **Module/theme:** locale
- **Topics:** [locale-translate-administration-screens](../../../topics/locale-translate-administration-screens.md)

## Signature

```php
function locale_translate_overview_screen()
```

## Documentation

```text
Overview screen for translations.
```

## Code

```php
function locale_translate_overview_screen() {
  drupal_static_reset('language_list');
  $languages = language_list('language');
  $groups = module_invoke_all('locale', 'groups');

  // Build headers with all groups in order.
  $headers = array_merge(array(t('Language')), array_values($groups));

  // Collect summaries of all source strings in all groups.
  $sums = db_query("SELECT COUNT(*) AS strings, textgroup FROM {locales_source} GROUP BY textgroup");
  $groupsums = array();
  foreach ($sums as $group) {
    $groupsums[$group->textgroup] = $group->strings;
  }

  // Set up overview table with default values, ensuring common order for values.
  $rows = array();
  foreach ($languages as $langcode => $language) {
    $rows[$langcode] = array('name' => ($langcode == 'en' ? t('English (built-in)') : t($language->name)));
    foreach ($groups as $group => $name) {
      $rows[$langcode][$group] = ($langcode == 'en' ? t('n/a') : '0/' . (isset($groupsums[$group]) ? $groupsums[$group] : 0) . ' (0%)');
    }
  }

  // Languages with at least one record in the locale table.
  $translations = db_query("SELECT COUNT(*) AS translation, t.language, s.textgroup FROM {locales_source} s INNER JOIN {locales_target} t ON s.lid = t.lid GROUP BY textgroup, language");
  foreach ($translations as $data) {
    $ratio = (!empty($groupsums[$data->textgroup]) && $data->translation > 0) ? round(($data->translation/$groupsums[$data->textgroup]) * 100.0, 2) : 0;
    $rows[$data->language][$data->textgroup] = $data->translation . '/' . $groupsums[$data->textgroup] . " ($ratio%)";
  }

  return theme('table', array('header' => $headers, 'rows' => $rows));
}
```

---
_Drupal 7.103 · [modules/locale/locale.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
