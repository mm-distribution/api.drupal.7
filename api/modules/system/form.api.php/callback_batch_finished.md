# callback_batch_finished()

- **Type:** Function
- **File:** [`modules/system/form.api.php`](_file.md), lines 107–126 · [local source](../../../../source/modules/system/form.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/form.api.php#L107-L126)
- **Module/theme:** system
- **Topics:** [callbacks](../../../topics/callbacks.md)

## Signature

```php
function callback_batch_finished($success, $results, $operations)
```

## Documentation

```text
Complete a batch process.

Callback for batch_set().

This callback may be specified in a batch to perform clean-up operations, or
to analyze the results of the batch operations.

@param $success
  A boolean indicating whether the batch has completed successfully.
@param $results
  The value set in $context['results'] by callback_batch_operation().
@param $operations
  If $success is FALSE, contains the operations that remained unprocessed.
```

## Code

```php
function callback_batch_finished($success, $results, $operations) {
  if ($success) {
    // Here we do something meaningful with the results.
    $message = t("!count items were processed.", array(
      '!count' => count($results),
      ));
    $message .= theme('item_list', array('items' => $results));
    drupal_set_message($message);
  }
  else {
    // An error occurred.
    // $operations contains the operations that remained unprocessed.
    $error_operation = reset($operations);
    $message = t('An error occurred while processing %error_operation with arguments: @arguments', array(
      '%error_operation' => $error_operation[0],
      '@arguments' => print_r($error_operation[1], TRUE)
    ));
    drupal_set_message($message, 'error');
  }
}
```

---
_Drupal 7.103 · [modules/system/form.api.php](https://github.com/drupal/drupal/blob/7.103/modules/system/form.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
