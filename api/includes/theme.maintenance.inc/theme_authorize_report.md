# theme_authorize_report()

- **Type:** Function
- **File:** [`includes/theme.maintenance.inc`](_file.md), lines 171–189 · [local source](../../../source/includes/theme.maintenance.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/theme.maintenance.inc#L171-L189)
- **Topics:** [themeable](../../topics/themeable.md)

## Signature

```php
function theme_authorize_report($variables)
```

## Documentation

```text
Returns HTML for a results report of an operation run by authorize.php.

@param $variables
  An associative array containing:
  - messages: An array of result messages.

@ingroup themeable
```

## Code

```php
function theme_authorize_report($variables) {
  $messages = $variables['messages'];
  $output = '';
  if (!empty($messages)) {
    $output .= '<div id="authorize-results">';
    foreach ($messages as $heading => $logs) {
      $items = array();
      foreach ($logs as $number => $log_message) {
        if ($number === '#abort') {
          continue;
        }
        $items[] = theme('authorize_message', array('message' => $log_message['message'], 'success' => $log_message['success']));
      }
      $output .= theme('item_list',  array('items' => $items, 'title' => $heading));
    }
    $output .= '</div>';
  }
  return $output;
}
```

---
_Drupal 7.103 · [includes/theme.maintenance.inc](https://github.com/drupal/drupal/blob/7.103/includes/theme.maintenance.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
