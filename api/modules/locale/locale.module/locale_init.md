# locale_init()

- **Type:** Function
- **File:** [`modules/locale/locale.module`](_file.md), lines 226–244 · [local source](../../../../source/modules/locale/locale.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.module#L226-L244)
- **Module/theme:** locale
- **Implements:** [hook_init()](../../system/system.api.php/hook_init.md)

## Signature

```php
function locale_init()
```

## Documentation

```text
Implements hook_init().

Initialize date formats according to the user's current locale.
```

## Code

```php
function locale_init() {
  global $conf, $language;
  include_once DRUPAL_ROOT . '/includes/locale.inc';

  // For each date type (e.g. long, short), get the localized date format
  // for the user's current language and override the default setting for it
  // in $conf. This should happen on all pages except the date and time formats
  // settings page, where we want to display the site default and not the
  // localized version.
  if (strpos($_GET['q'], 'admin/config/regional/date-time/formats') !== 0) {
    $languages = array($language->language);

    // Setup appropriate date formats for this locale.
    $formats = locale_get_localized_date_format($languages);
    foreach ($formats as $format_type => $format) {
      $conf[$format_type] = $format;
    }
  }
}
```

---
_Drupal 7.103 · [modules/locale/locale.module](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.module) · Licensed GPL-2.0-or-later (see LICENSE)._
