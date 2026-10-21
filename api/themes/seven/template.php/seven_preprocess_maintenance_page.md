# seven_preprocess_maintenance_page()

- **Type:** Function
- **File:** [`themes/seven/template.php`](_file.md), lines 6–13 · [local source](../../../../source/themes/seven/template.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/themes/seven/template.php#L6-L13)
- **Module/theme:** seven

## Signature

```php
function seven_preprocess_maintenance_page(&$vars)
```

## Documentation

```text
Override or insert variables into the maintenance page template.
```

## Code

```php
function seven_preprocess_maintenance_page(&$vars) {
  // While markup for normal pages is split into page.tpl.php and html.tpl.php,
  // the markup for the maintenance page is all in the single
  // maintenance-page.tpl.php template. So, to have what's done in
  // seven_preprocess_html() also happen on the maintenance page, it has to be
  // called here.
  seven_preprocess_html($vars);
}
```

---
_Drupal 7.103 · [themes/seven/template.php](https://github.com/drupal/drupal/blob/7.103/themes/seven/template.php) · Licensed GPL-2.0-or-later (see LICENSE)._
