# _node_mass_update_batch_finished()

- **Type:** Function
- **File:** [`modules/node/node.admin.inc`](_file.md), lines 379–389 · [local source](../../../../source/modules/node/node.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/node.admin.inc#L379-L389)
- **Module/theme:** node

## Signature

```php
function _node_mass_update_batch_finished($success, $results, $operations)
```

## Documentation

```text
Implements callback_batch_finished().

Reports the status of batch operation for node_mass_update().

@param bool $success
  A boolean indicating whether the batch mass update operation successfully
  concluded.
@param int $results
  The number of nodes updated via the batch mode process.
@param array $operations
  An array of function calls (not used in this function).
```

## Code

```php
function _node_mass_update_batch_finished($success, $results, $operations) {
  if ($success) {
    drupal_set_message(t('The update has been performed.'));
  }
  else {
    drupal_set_message(t('An error occurred and processing did not complete.'), 'error');
    $message = format_plural(count($results), '1 item successfully processed:', '@count items successfully processed:');
    $message .= theme('item_list', array('items' => $results));
    drupal_set_message($message);
  }
}
```

---
_Drupal 7.103 · [modules/node/node.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/node/node.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
