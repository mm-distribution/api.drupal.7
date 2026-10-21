# theme_update_page()

- **Type:** Function
- **File:** [`includes/theme.maintenance.inc`](_file.md), lines 157–160 · [local source](../../../source/includes/theme.maintenance.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/theme.maintenance.inc#L157-L160)

## Signature

```php
function theme_update_page($variables)
```

## Documentation

```text
Returns HTML for the update page.

Note: this function is not themeable.

@param $variables
  An associative array containing:
  - content: The page content to show.
  - show_messages: Whether to output status and error messages.
    FALSE can be useful to postpone the messages to a subsequent page.
```

## Code

```php
function theme_update_page($variables) {
  drupal_add_http_header('Content-Type', 'text/html; charset=utf-8');
  return theme('maintenance_page', $variables);
}
```

---
_Drupal 7.103 · [includes/theme.maintenance.inc](https://github.com/drupal/drupal/blob/7.103/includes/theme.maintenance.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
