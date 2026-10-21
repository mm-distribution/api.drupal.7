# bartik_preprocess_maintenance_page()

- **Type:** Function
- **File:** [`themes/bartik/template.php`](_file.md), lines 79–88 · [local source](../../../../source/themes/bartik/template.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/themes/bartik/template.php#L79-L88)
- **Module/theme:** bartik

## Signature

```php
function bartik_preprocess_maintenance_page(&$variables)
```

## Documentation

```text
Implements hook_preprocess_maintenance_page().
```

## Code

```php
function bartik_preprocess_maintenance_page(&$variables) {
  // By default, site_name is set to Drupal if no db connection is available
  // or during site installation. Setting site_name to an empty string makes
  // the site and update pages look cleaner.
  // @see template_preprocess_maintenance_page
  if (!$variables['db_is_active']) {
    $variables['site_name'] = '';
  }
  drupal_add_css(drupal_get_path('theme', 'bartik') . '/css/maintenance-page.css');
}
```

---
_Drupal 7.103 · [themes/bartik/template.php](https://github.com/drupal/drupal/blob/7.103/themes/bartik/template.php) · Licensed GPL-2.0-or-later (see LICENSE)._
