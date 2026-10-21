# theme_authorize_message()

- **Type:** Function
- **File:** [`includes/theme.maintenance.inc`](_file.md), lines 201–211 · [local source](../../../source/includes/theme.maintenance.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/theme.maintenance.inc#L201-L211)
- **Topics:** [themeable](../../topics/themeable.md)

## Signature

```php
function theme_authorize_message($variables)
```

## Documentation

```text
Returns HTML for a single log message from the authorize.php batch operation.

@param $variables
  An associative array containing:
  - message: The log message.
  - success: A boolean indicating failure or success.

@ingroup themeable
```

## Code

```php
function theme_authorize_message($variables) {
  $message = $variables['message'];
  $success = $variables['success'];
  if ($success) {
    $item = array('data' => $message, 'class' => array('success'));
  }
  else {
    $item = array('data' => '<strong>' . $message . '</strong>', 'class' => array('failure'));
  }
  return $item;
}
```

---
_Drupal 7.103 · [includes/theme.maintenance.inc](https://github.com/drupal/drupal/blob/7.103/includes/theme.maintenance.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
