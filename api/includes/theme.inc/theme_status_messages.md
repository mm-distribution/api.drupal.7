# theme_status_messages()

- **Type:** Function
- **File:** [`includes/theme.inc`](_file.md), lines 1673–1700 · [local source](../../../source/includes/theme.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/theme.inc#L1673-L1700)
- **Topics:** [themeable](../../topics/themeable.md)

## Signature

```php
function theme_status_messages($variables)
```

## Documentation

```text
Returns HTML for status and/or error messages, grouped by type.

An invisible heading identifies the messages for assistive technology.
Sighted users see a colored box. See http://www.w3.org/TR/WCAG-TECHS/H69.html
for info.

@param $variables
  An associative array containing:
  - display: (optional) Set to 'status' or 'error' to display only messages
    of that type.
```

## Code

```php
function theme_status_messages($variables) {
  $display = $variables['display'];
  $output = '';

  $status_heading = array(
    'status' => t('Status message'),
    'error' => t('Error message'),
    'warning' => t('Warning message'),
  );
  foreach (drupal_get_messages($display) as $type => $messages) {
    $output .= "<div class=\"messages $type\">\n";
    if (!empty($status_heading[$type])) {
      $output .= '<h2 class="element-invisible">' . $status_heading[$type] . "</h2>\n";
    }
    if (count($messages) > 1) {
      $output .= " <ul>\n";
      foreach ($messages as $message) {
        $output .= '  <li>' . $message . "</li>\n";
      }
      $output .= " </ul>\n";
    }
    else {
      $output .= reset($messages);
    }
    $output .= "</div>\n";
  }
  return $output;
}
```

---
_Drupal 7.103 · [includes/theme.inc](https://github.com/drupal/drupal/blob/7.103/includes/theme.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
