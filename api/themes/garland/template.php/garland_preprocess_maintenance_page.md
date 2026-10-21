# garland_preprocess_maintenance_page()

- **Type:** Function
- **File:** [`themes/garland/template.php`](_file.md), lines 22–29 · [local source](../../../../source/themes/garland/template.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/themes/garland/template.php#L22-L29)
- **Module/theme:** garland

## Signature

```php
function garland_preprocess_maintenance_page(&$variables)
```

## Documentation

```text
Override or insert variables into the maintenance page template.
```

## Code

```php
function garland_preprocess_maintenance_page(&$variables) {
  // While markup for normal pages is split into page.tpl.php and html.tpl.php,
  // the markup for the maintenance page is all in the single
  // maintenance-page.tpl.php template. So, to have what's done in
  // garland_preprocess_html() also happen on the maintenance page, it has to be
  // called here.
  garland_preprocess_html($variables);
}
```

---
_Drupal 7.103 · [themes/garland/template.php](https://github.com/drupal/drupal/blob/7.103/themes/garland/template.php) · Licensed GPL-2.0-or-later (see LICENSE)._
