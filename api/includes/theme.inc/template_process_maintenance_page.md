# template_process_maintenance_page()

- **Type:** Function
- **File:** [`includes/theme.inc`](_file.md), lines 2952–2957 · [local source](../../../source/includes/theme.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/theme.inc#L2952-L2957)

## Signature

```php
function template_process_maintenance_page(&$variables)
```

## Documentation

```text
Theme process function for theme_maintenance_field().

The variables array generated here is a mirror of template_process_html().
This processor will run its course when theme_maintenance_page() is invoked.

@see maintenance-page.tpl.php
@see template_process_html()
```

## Code

```php
function template_process_maintenance_page(&$variables) {
  $variables['head']    = drupal_get_html_head();
  $variables['css']     = drupal_add_css();
  $variables['styles']  = drupal_get_css();
  $variables['scripts'] = drupal_get_js();
}
```

---
_Drupal 7.103 · [includes/theme.inc](https://github.com/drupal/drupal/blob/7.103/includes/theme.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
