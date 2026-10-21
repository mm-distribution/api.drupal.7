# locale_translation_filters()

- **Type:** Function
- **File:** [`modules/locale/locale.admin.inc`](_file.md), lines 806–836 · [local source](../../../../source/modules/locale/locale.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.admin.inc#L806-L836)
- **Module/theme:** locale
- **Topics:** [locale-translate-administration-screens](../../../topics/locale-translate-administration-screens.md)

## Signature

```php
function locale_translation_filters()
```

## Documentation

```text
List locale translation filters that can be applied.
```

## Code

```php
function locale_translation_filters() {
  $filters = array();

  // Get all languages, except English
  drupal_static_reset('language_list');
  $languages = locale_language_list('name');
  unset($languages['en']);

  $filters['string'] = array(
    'title' => t('String contains'),
    'description' => t('Leave blank to show all strings. The search is case sensitive.'),
  );

  $filters['language'] = array(
    'title' => t('Language'),
    'options' => array_merge(array('all' => t('All languages'), 'en' => t('English (provided by Drupal)')), $languages),
  );

  $filters['translation'] = array(
    'title' => t('Search in'),
    'options' => array('all' => t('Both translated and untranslated strings'), 'translated' => t('Only translated strings'), 'untranslated' => t('Only untranslated strings')),
  );

  $groups = module_invoke_all('locale', 'groups');
  $filters['group'] = array(
    'title' => t('Limit search to'),
    'options' => array_merge(array('all' => t('All text groups')), $groups),
  );

  return $filters;
}
```

---
_Drupal 7.103 · [modules/locale/locale.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
