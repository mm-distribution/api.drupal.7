# locale_menu()

- **Type:** Function
- **File:** [`modules/locale/locale.module`](_file.md), lines 73–219 · [local source](../../../../source/modules/locale/locale.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.module#L73-L219)
- **Module/theme:** locale
- **Implements:** [hook_menu()](../../system/system.api.php/hook_menu.md)

## Signature

```php
function locale_menu()
```

## Documentation

```text
Implements hook_menu().
```

## Code

```php
function locale_menu() {
  // Manage languages
  $items['admin/config/regional/language'] = array(
    'title' => 'Languages',
    'description' => 'Configure languages for content and the user interface.',
    'page callback' => 'drupal_get_form',
    'page arguments' => array('locale_languages_overview_form'),
    'access arguments' => array('administer languages'),
    'file' => 'locale.admin.inc',
    'weight' => -10,
  );
  $items['admin/config/regional/language/overview'] = array(
    'title' => 'List',
    'weight' => 0,
    'type' => MENU_DEFAULT_LOCAL_TASK,
  );
  $items['admin/config/regional/language/add'] = array(
    'title' => 'Add language',
    'page callback' => 'locale_languages_add_screen', // two forms concatenated
    'access arguments' => array('administer languages'),
    'weight' => 5,
    'type' => MENU_LOCAL_ACTION,
    'file' => 'locale.admin.inc',
  );
  $items['admin/config/regional/language/configure'] = array(
    'title' => 'Detection and selection',
    'page callback' => 'drupal_get_form',
    'page arguments' => array('locale_languages_configure_form'),
    'access arguments' => array('administer languages'),
    'weight' => 10,
    'file' => 'locale.admin.inc',
    'type' => MENU_LOCAL_TASK,
  );
  $items['admin/config/regional/language/configure/url'] = array(
    'title' => 'URL language detection configuration',
    'page callback' => 'drupal_get_form',
    'page arguments' => array('locale_language_providers_url_form'),
    'access arguments' => array('administer languages'),
    'file' => 'locale.admin.inc',
    'type' => MENU_VISIBLE_IN_BREADCRUMB,
  );
  $items['admin/config/regional/language/configure/session'] = array(
    'title' => 'Session language detection configuration',
    'page callback' => 'drupal_get_form',
    'page arguments' => array('locale_language_providers_session_form'),
    'access arguments' => array('administer languages'),
    'file' => 'locale.admin.inc',
    'type' => MENU_VISIBLE_IN_BREADCRUMB,
  );
  $items['admin/config/regional/language/edit/%'] = array(
    'title' => 'Edit language',
    'page callback' => 'drupal_get_form',
    'page arguments' => array('locale_languages_edit_form', 5),
    'access arguments' => array('administer languages'),
    'file' => 'locale.admin.inc',
  );
  $items['admin/config/regional/language/delete/%'] = array(
    'title' => 'Confirm',
    'page callback' => 'drupal_get_form',
    'page arguments' => array('locale_languages_delete_form', 5),
    'access arguments' => array('administer languages'),
    'file' => 'locale.admin.inc',
  );

  // Translation functionality
  $items['admin/config/regional/translate'] = array(
    'title' => 'Translate interface',
    'description' => 'Translate the built in interface and optionally other text.',
    'page callback' => 'locale_translate_overview_screen',
    'access arguments' => array('translate interface'),
    'file' => 'locale.admin.inc',
    'weight' => -5,
  );
  $items['admin/config/regional/translate/overview'] = array(
    'title' => 'Overview',
    'weight' => 0,
    'type' => MENU_DEFAULT_LOCAL_TASK,
  );
  $items['admin/config/regional/translate/translate'] = array(
    'title' => 'Translate',
    'weight' => 10,
    'type' => MENU_LOCAL_TASK,
    'page callback' => 'locale_translate_seek_screen', // search results and form concatenated
    'access arguments' => array('translate interface'),
    'file' => 'locale.admin.inc',
  );
  $items['admin/config/regional/translate/import'] = array(
    'title' => 'Import',
    'page callback' => 'drupal_get_form',
    'page arguments' => array('locale_translate_import_form'),
    'access arguments' => array('translate interface'),
    'weight' => 20,
    'type' => MENU_LOCAL_TASK,
    'file' => 'locale.admin.inc',
  );
  $items['admin/config/regional/translate/export'] = array(
    'title' => 'Export',
    'page callback' => 'locale_translate_export_screen',  // possibly multiple forms concatenated
    'access arguments' => array('translate interface'),
    'weight' => 30,
    'type' => MENU_LOCAL_TASK,
    'file' => 'locale.admin.inc',
  );
  $items['admin/config/regional/translate/edit/%'] = array(
    'title' => 'Edit string',
    'page callback' => 'drupal_get_form',
    'page arguments' => array('locale_translate_edit_form', 5),
    'access arguments' => array('translate interface'),
    'file' => 'locale.admin.inc',
  );
  $items['admin/config/regional/translate/delete/%'] = array(
    'title' => 'Delete string',
    'page callback' => 'locale_translate_delete_page',
    'page arguments' => array(5),
    'access arguments' => array('translate interface'),
    'file' => 'locale.admin.inc',
  );

  // Localize date formats.
  $items['admin/config/regional/date-time/locale'] = array(
    'title' => 'Localize',
    'description' => 'Configure date formats for each locale',
    'page callback' => 'locale_date_format_language_overview_page',
    'access arguments' => array('administer site configuration'),
    'type' => MENU_LOCAL_TASK,
    'weight' => -8,
    'file' => 'locale.admin.inc',
  );
  $items['admin/config/regional/date-time/locale/%/edit'] = array(
    'title' => 'Localize date formats',
    'description' => 'Configure date formats for each locale',
    'page callback' => 'drupal_get_form',
    'page arguments' => array('locale_date_format_form', 5),
    'access arguments' => array('administer site configuration'),
    'file' => 'locale.admin.inc',
  );
  $items['admin/config/regional/date-time/locale/%/reset'] = array(
    'title' => 'Reset date formats',
    'description' => 'Reset localized date formats to global defaults',
    'page callback' => 'drupal_get_form',
    'page arguments' => array('locale_date_format_reset_form', 5),
    'access arguments' => array('administer site configuration'),
    'file' => 'locale.admin.inc',
  );

  return $items;
}
```

---
_Drupal 7.103 · [modules/locale/locale.module](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.module) · Licensed GPL-2.0-or-later (see LICENSE)._
