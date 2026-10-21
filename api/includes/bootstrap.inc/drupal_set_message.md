# drupal_set_message()

- **Type:** Function
- **File:** [`includes/bootstrap.inc`](_file.md), lines 2122–2138 · [local source](../../../source/includes/bootstrap.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/bootstrap.inc#L2122-L2138)

## Signature

```php
function drupal_set_message($message = NULL, $type = 'status', $repeat = TRUE)
```

## Documentation

```text
Sets a message to display to the user.

Messages are stored in a session variable and displayed in page.tpl.php via
the $messages theme variable.

Example usage:
@code
drupal_set_message(t('An error occurred and processing did not complete.'), 'error');
@endcode

@param string $message
  (optional) The translated message to be displayed to the user. For
  consistency with other messages, it should begin with a capital letter and
  end with a period.
@param string $type
  (optional) The message's type. Defaults to 'status'. These values are
  supported:
  - 'status'
  - 'warning'
  - 'error'
@param bool $repeat
  (optional) If this is FALSE and the message is already set, then the
  message won't be repeated. Defaults to TRUE.

@return array|null
  A multidimensional array with keys corresponding to the set message types.
  The indexed array values of each contain the set messages for that type.
  Or, if there are no messages set, the function returns NULL.

@see drupal_get_messages()
@see theme_status_messages()
```

## Code

```php
function drupal_set_message($message = NULL, $type = 'status', $repeat = TRUE) {
  if ($message || $message === '0' || $message === 0) {
    if (!isset($_SESSION['messages'][$type])) {
      $_SESSION['messages'][$type] = array();
    }

    if ($repeat || !in_array($message, $_SESSION['messages'][$type])) {
      $_SESSION['messages'][$type][] = $message;
    }

    // Mark this page as being uncacheable.
    drupal_page_is_cacheable(FALSE);
  }

  // Messages not set when DB connection fails.
  return isset($_SESSION['messages']) ? $_SESSION['messages'] : NULL;
}
```

---
_Drupal 7.103 · [includes/bootstrap.inc](https://github.com/drupal/drupal/blob/7.103/includes/bootstrap.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
