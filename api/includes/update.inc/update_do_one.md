# update_do_one()

- **Type:** Function
- **File:** [`includes/update.inc`](_file.md), lines 961–1013 · [local source](../../../source/includes/update.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/update.inc#L961-L1013)

## Signature

```php
function update_do_one($module, $number, $dependency_map, &$context)
```

## Documentation

```text
Implements callback_batch_operation().

Performs one update and stores the results for display on the results page.

If an update function completes successfully, it should return a message
as a string indicating success, for example:
@code
return t('New index added successfully.');
@endcode

Alternatively, it may return nothing. In that case, no message
will be displayed at all.

If it fails for whatever reason, it should throw an instance of
DrupalUpdateException with an appropriate error message, for example:
@code
throw new DrupalUpdateException(t('Description of what went wrong'));
@endcode

If an exception is thrown, the current update and all updates that depend on
it will be aborted. The schema version will not be updated in this case, and
all the aborted updates will continue to appear on update.php as updates
that have not yet been run.

If an update function needs to be re-run as part of a batch process, it
should accept the $sandbox array by reference as its first parameter
and set the #finished property to the percentage completed that it is, as a
fraction of 1.

@param $module
  The module whose update will be run.
@param $number
  The update number to run.
@param $dependency_map
  An array whose keys are the names of all update functions that will be
  performed during this batch process, and whose values are arrays of other
  update functions that each one depends on.
@param $context
  The batch context array.

@see update_resolve_dependencies()
```

## Code

```php
function update_do_one($module, $number, $dependency_map, &$context) {
  $function = $module . '_update_' . $number;

  // If this update was aborted in a previous step, or has a dependency that
  // was aborted in a previous step, go no further.
  if (!empty($context['results']['#abort']) && array_intersect($context['results']['#abort'], array_merge($dependency_map, array($function)))) {
    return;
  }

  $ret = array();
  if (function_exists($function)) {
    try {
      $ret['results']['query'] = $function($context['sandbox']);
      $ret['results']['success'] = TRUE;
    }
    // @TODO We may want to do different error handling for different
    // exception types, but for now we'll just log the exception and
    // return the message for printing.
    catch (Exception $e) {
      watchdog_exception('update', $e);

      require_once DRUPAL_ROOT . '/includes/errors.inc';
      $variables = _drupal_decode_exception($e);
      // The exception message is run through check_plain() by _drupal_decode_exception().
      $ret['#abort'] = array('success' => FALSE, 'query' => t('%type: !message in %function (line %line of %file).', $variables));
    }
  }

  if (isset($context['sandbox']['#finished'])) {
    $context['finished'] = $context['sandbox']['#finished'];
    unset($context['sandbox']['#finished']);
  }

  if (!isset($context['results'][$module])) {
    $context['results'][$module] = array();
  }
  if (!isset($context['results'][$module][$number])) {
    $context['results'][$module][$number] = array();
  }
  $context['results'][$module][$number] = array_merge($context['results'][$module][$number], $ret);

  if (!empty($ret['#abort'])) {
    // Record this function in the list of updates that were aborted.
    $context['results']['#abort'][] = $function;
  }

  // Record the schema update if it was completed successfully.
  if ($context['finished'] == 1 && empty($ret['#abort'])) {
    drupal_set_installed_schema_version($module, $number);
  }

  $context['message'] = 'Updating ' . check_plain($module) . ' module';
}
```

---
_Drupal 7.103 · [includes/update.inc](https://github.com/drupal/drupal/blob/7.103/includes/update.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
