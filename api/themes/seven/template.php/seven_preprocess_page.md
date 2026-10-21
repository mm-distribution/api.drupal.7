# seven_preprocess_page()

- **Type:** Function
- **File:** [`themes/seven/template.php`](_file.md), lines 30–37 · [local source](../../../../source/themes/seven/template.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/themes/seven/template.php#L30-L37)
- **Module/theme:** seven

## Signature

```php
function seven_preprocess_page(&$vars)
```

## Documentation

```text
Override or insert variables into the page template.
```

## Code

```php
function seven_preprocess_page(&$vars) {
  $vars['primary_local_tasks'] = $vars['tabs'];
  unset($vars['primary_local_tasks']['#secondary']);
  $vars['secondary_local_tasks'] = array(
    '#theme' => 'menu_local_tasks',
    '#secondary' => $vars['tabs']['#secondary'],
  );
}
```

---
_Drupal 7.103 · [themes/seven/template.php](https://github.com/drupal/drupal/blob/7.103/themes/seven/template.php) · Licensed GPL-2.0-or-later (see LICENSE)._
