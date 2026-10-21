# language_list()

- **Type:** Function
- **File:** [`includes/bootstrap.inc`](_file.md), lines 3130–3164 · [local source](../../../source/includes/bootstrap.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/bootstrap.inc#L3130-L3164)

## Signature

```php
function language_list($field = 'language')
```

## Documentation

```text
Returns a list of installed languages, indexed by the specified key.

@param $field
  (optional) The field to index the list with.

@return
  An associative array, keyed on the values of $field.
  - If $field is 'weight' or 'enabled', the array is nested, with the outer
    array's values each being associative arrays with language codes as
    keys and language objects as values.
  - For all other values of $field, the array is only one level deep, and
    the array's values are language objects.
```

## Code

```php
function language_list($field = 'language') {
  $languages = &drupal_static(__FUNCTION__);
  // Init language list
  if (!isset($languages)) {
    if (drupal_multilingual() || module_exists('locale')) {
      $languages['language'] = db_query('SELECT * FROM {languages} ORDER BY weight ASC, name ASC')->fetchAllAssoc('language');
      // Users cannot uninstall the native English language. However, we allow
      // it to be hidden from the installed languages. Therefore, at least one
      // other language must be enabled then.
      if (!$languages['language']['en']->enabled && !variable_get('language_native_enabled', TRUE)) {
        unset($languages['language']['en']);
      }
    }
    else {
      // No locale module, so use the default language only.
      $default = language_default();
      $languages['language'][$default->language] = $default;
    }
  }

  // Return the array indexed by the right field
  if (!isset($languages[$field])) {
    $languages[$field] = array();
    foreach ($languages['language'] as $lang) {
      // Some values should be collected into an array
      if (in_array($field, array('enabled', 'weight'))) {
        $languages[$field][$lang->$field][$lang->language] = $lang;
      }
      else {
        $languages[$field][$lang->$field] = $lang;
      }
    }
  }
  return $languages[$field];
}
```

---
_Drupal 7.103 · [includes/bootstrap.inc](https://github.com/drupal/drupal/blob/7.103/includes/bootstrap.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
