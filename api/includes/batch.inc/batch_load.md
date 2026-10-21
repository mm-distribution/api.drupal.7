# batch_load()

- **Type:** Function
- **File:** [`includes/batch.inc`](_file.md), lines 27–36 · [local source](../../../source/includes/batch.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/batch.inc#L27-L36)

## Signature

```php
function batch_load($id)
```

## Documentation

```text
Loads a batch from the database.

@param $id
  The ID of the batch to load. When a progressive batch is being processed,
  the relevant ID is found in $_REQUEST['id'].

@return
  An array representing the batch, or FALSE if no batch was found.
```

## Code

```php
function batch_load($id) {
  $batch = db_query("SELECT batch FROM {batch} WHERE bid = :bid AND token = :token", array(
    ':bid' => $id,
    ':token' => drupal_get_token($id),
  ))->fetchField();
  if ($batch) {
    return unserialize($batch);
  }
  return FALSE;
}
```

---
_Drupal 7.103 · [includes/batch.inc](https://github.com/drupal/drupal/blob/7.103/includes/batch.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
