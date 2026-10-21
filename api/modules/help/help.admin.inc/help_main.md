# help_main()

- **Type:** Function
- **File:** [`modules/help/help.admin.inc`](_file.md), lines 11–16 · [local source](../../../../source/modules/help/help.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/help/help.admin.inc#L11-L16)
- **Module/theme:** help

## Signature

```php
function help_main()
```

## Documentation

```text
Menu callback; prints a page listing a glossary of Drupal terminology.
```

## Code

```php
function help_main() {
  // Add CSS
  drupal_add_css(drupal_get_path('module', 'help') . '/help.css');
  $output = '<h2>' . t('Help topics') . '</h2><p>' . t('Help is available on the following items:') . '</p>' . help_links_as_list();
  return $output;
}
```

---
_Drupal 7.103 · [modules/help/help.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/help/help.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
