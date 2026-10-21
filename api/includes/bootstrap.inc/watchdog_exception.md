# watchdog_exception()

- **Type:** Function
- **File:** [`includes/bootstrap.inc`](_file.md), lines 1999–2014 · [local source](../../../source/includes/bootstrap.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/bootstrap.inc#L1999-L2014)

## Signature

```php
function watchdog_exception($type, Exception $exception, $message = NULL, $variables = array(), $severity = WATCHDOG_ERROR, $link = NULL)
```

## Documentation

```text
Logs an exception.

This is a wrapper function for watchdog() which automatically decodes an
exception.

@param $type
  The category to which this message belongs.
@param $exception
  The exception that is going to be logged.
@param $message
  The message to store in the log. If empty, a text that contains all useful
  information about the passed-in exception is used.
@param $variables
  Array of variables to replace in the message on display. Defaults to the
  return value of _drupal_decode_exception().
@param $severity
  The severity of the message, as per RFC 3164.
@param $link
  A link to associate with the message.

@see watchdog()
@see _drupal_decode_exception()
```

## Code

```php
function watchdog_exception($type, Exception $exception, $message = NULL, $variables = array(), $severity = WATCHDOG_ERROR, $link = NULL) {

   // Use a default value if $message is not set.
   if (empty($message)) {
     // The exception message is run through check_plain() by _drupal_decode_exception().
     $message = '%type: !message in %function (line %line of %file).';
   }
   // $variables must be an array so that we can add the exception information.
   if (!is_array($variables)) {
     $variables = array();
   }

   require_once DRUPAL_ROOT . '/includes/errors.inc';
   $variables += _drupal_decode_exception($exception);
   watchdog($type, $message, $variables, $severity, $link);
}
```

---
_Drupal 7.103 · [includes/bootstrap.inc](https://github.com/drupal/drupal/blob/7.103/includes/bootstrap.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
