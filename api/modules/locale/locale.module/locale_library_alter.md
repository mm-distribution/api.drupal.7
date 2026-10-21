# locale_library_alter()

- **Type:** Function
- **File:** [`modules/locale/locale.module`](_file.md), lines 991–1013 · [local source](../../../../source/modules/locale/locale.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.module#L991-L1013)
- **Module/theme:** locale
- **Implements:** [hook_library_alter()](../../system/system.api.php/hook_library_alter.md)

## Signature

```php
function locale_library_alter(&$libraries, $module)
```

## Documentation

```text
Implement hook_library_alter().

Provides the language support for the jQuery UI Date Picker.
```

## Code

```php
function locale_library_alter(&$libraries, $module) {
  if ($module == 'system' && isset($libraries['ui.datepicker'])) {
    global $language;
    // locale.datepicker.js should be added in the JS_LIBRARY group, so that
    // this attach behavior will execute early. JS_LIBRARY is the default for
    // hook_library_info_alter(), thus does not have to be specified explicitly.
    $datepicker = drupal_get_path('module', 'locale') . '/locale.datepicker.js';
    $libraries['ui.datepicker']['js'][$datepicker] = array();
    $libraries['ui.datepicker']['js'][] = array(
      'data' => array(
        'jquery' => array(
          'ui' => array(
            'datepicker' => array(
              'isRTL' => $language->direction == LANGUAGE_RTL,
              'firstDay' => variable_get('date_first_day', 0),
            ),
          ),
        ),
      ),
      'type' => 'setting',
    );
  }
}
```

---
_Drupal 7.103 · [modules/locale/locale.module](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.module) · Licensed GPL-2.0-or-later (see LICENSE)._
