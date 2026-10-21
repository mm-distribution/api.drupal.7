# drupal_get_messages()

- **Type:** Function
- **File:** [`includes/bootstrap.inc`](_file.md), lines 2165–2183 · [local source](../../../source/includes/bootstrap.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/bootstrap.inc#L2165-L2183)

## Signature

```php
function drupal_get_messages($type = NULL, $clear_queue = TRUE)
```

## Documentation

```text
Returns all messages that have been set with drupal_set_message().

@param string $type
  (optional) Limit the messages returned by type. Defaults to NULL, meaning
  all types. These values are supported:
  - NULL
  - 'status'
  - 'warning'
  - 'error'
@param bool $clear_queue
  (optional) If this is TRUE, the queue will be cleared of messages of the
  type specified in the $type parameter. Otherwise the queue will be left
  intact. Defaults to TRUE.

@return array
  A multidimensional array with keys corresponding to the set message types.
  The indexed array values of each contain the set messages for that type.
  The messages returned are limited to the type specified in the $type
  parameter. If there are no messages of the specified type, an empty array
  is returned.

@see drupal_set_message()
@see theme_status_messages()
```

## Code

```php
function drupal_get_messages($type = NULL, $clear_queue = TRUE) {
  if ($messages = drupal_set_message()) {
    if ($type) {
      if ($clear_queue) {
        unset($_SESSION['messages'][$type]);
      }
      if (isset($messages[$type])) {
        return array($type => $messages[$type]);
      }
    }
    else {
      if ($clear_queue) {
        unset($_SESSION['messages']);
      }
      return $messages;
    }
  }
  return array();
}
```

---
_Drupal 7.103 · [includes/bootstrap.inc](https://github.com/drupal/drupal/blob/7.103/includes/bootstrap.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
