# _drupal_log_error()

- **Type:** Function
- **File:** [`includes/errors.inc`](_file.md), lines 169–256 · [local source](../../../source/includes/errors.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/errors.inc#L169-L256)

## Signature

```php
function _drupal_log_error($error, $fatal = FALSE)
```

## Documentation

```text
Logs a PHP error or exception and displays an error page in fatal cases.

@param $error
  An array with the following keys: %type, !message, %function, %file, %line
  and severity_level. All the parameters are plain-text, with the exception
  of !message, which needs to be a safe HTML string.
@param $fatal
  TRUE if the error is fatal.
```

## Code

```php
function _drupal_log_error($error, $fatal = FALSE) {
  // Initialize a maintenance theme if the bootstrap was not complete.
  // Do it early because drupal_set_message() triggers a drupal_theme_initialize().
  if ($fatal && (drupal_get_bootstrap_phase() != DRUPAL_BOOTSTRAP_FULL)) {
    unset($GLOBALS['theme']);
    if (!defined('MAINTENANCE_MODE')) {
      define('MAINTENANCE_MODE', 'error');
    }
    drupal_maintenance_theme();
  }

  // When running inside the testing framework, we relay the errors
  // to the tested site by the way of HTTP headers.
  $test_info = &$GLOBALS['drupal_test_info'];
  if (!empty($test_info['in_child_site']) && !headers_sent() && (!defined('SIMPLETEST_COLLECT_ERRORS') || SIMPLETEST_COLLECT_ERRORS)) {
    // $number does not use drupal_static as it should not be reset
    // as it uniquely identifies each PHP error.
    static $number = 0;
    $assertion = array(
      $error['!message'],
      $error['%type'],
      array(
        'function' => $error['%function'],
        'file' => $error['%file'],
        'line' => $error['%line'],
      ),
    );
    header('X-Drupal-Assertion-' . $number . ': ' . rawurlencode(serialize($assertion)));
    $number++;
  }

  // Log the error immediately, unless this is a non-fatal error which has been
  // triggered via drupal_trigger_error_with_delayed_logging(); in that case
  // trigger it in a shutdown function. Fatal errors are always triggered
  // immediately since for a fatal error the page request will end here anyway.
  if (!$fatal && drupal_static('_drupal_trigger_error_with_delayed_logging')) {
    drupal_register_shutdown_function('watchdog', 'php', '%type: !message in %function (line %line of %file).', $error, $error['severity_level']);
  }
  else {
    watchdog('php', '%type: !message in %function (line %line of %file).', $error, $error['severity_level']);
  }

  if ($fatal) {
    drupal_add_http_header('Status', '500 Service unavailable (with message)');
  }

  if (drupal_is_cli()) {
    if ($fatal) {
      // When called from CLI, simply output a plain text message.
      print html_entity_decode(strip_tags(t('%type: !message in %function (line %line of %file).', $error))). "\n";
      exit(1);
    }
  }

  if (isset($_SERVER['HTTP_X_REQUESTED_WITH']) && $_SERVER['HTTP_X_REQUESTED_WITH'] == 'XMLHttpRequest') {
    if ($fatal) {
      if (error_displayable($error)) {
        // When called from JavaScript, simply output the error message.
        print t('%type: !message in %function (line %line of %file).', _drupal_strip_error_file_path($error));
      }
      exit;
    }
  }
  else {
    // Display the message if the current error reporting level allows this type
    // of message to be displayed, and unconditionally in update.php.
    if (error_displayable($error)) {
      $class = 'error';

      // If error type is 'User notice' then treat it as debug information
      // instead of an error message, see dd().
      if ($error['%type'] == 'User notice') {
        $error['%type'] = 'Debug';
        $class = 'status';
      }

      drupal_set_message(t('%type: !message in %function (line %line of %file).', _drupal_strip_error_file_path($error)), $class);
    }

    if ($fatal) {
      drupal_set_title(t('Error'));
      // We fallback to a maintenance page at this point, because the page generation
      // itself can generate errors.
      print theme('maintenance_page', array('content' => t('The website encountered an unexpected error. Please try again later.')));
      exit;
    }
  }
}
```

---
_Drupal 7.103 · [includes/errors.inc](https://github.com/drupal/drupal/blob/7.103/includes/errors.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
