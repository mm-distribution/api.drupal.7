# locale_language_list()

- **Type:** Function
- **File:** [`modules/locale/locale.module`](_file.md), lines 846–859 · [local source](../../../../source/modules/locale/locale.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.module#L846-L859)
- **Module/theme:** locale

## Signature

```php
function locale_language_list($field = 'name', $all = FALSE)
```

## Documentation

```text
Returns array of language names

@param $field
  'name' => names in current language, localized
  'native' => native names
@param $all
  Boolean to return all languages or only enabled ones
```

## Code

```php
function locale_language_list($field = 'name', $all = FALSE) {
  if ($all) {
    $languages = language_list();
  }
  else {
    $languages = language_list('enabled');
    $languages = $languages[1];
  }
  $list = array();
  foreach ($languages as $language) {
    $list[$language->language] = ($field == 'name') ? t($language->name) : $language->$field;
  }
  return $list;
}
```

---
_Drupal 7.103 · [modules/locale/locale.module](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.module) · Licensed GPL-2.0-or-later (see LICENSE)._
