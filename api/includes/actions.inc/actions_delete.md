# actions_delete()

- **Type:** Function
- **File:** [`includes/actions.inc`](_file.md), lines 383–388 · [local source](../../../source/includes/actions.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/actions.inc#L383-L388)

## Signature

```php
function actions_delete($aid)
```

## Documentation

```text
Deletes a single action from the database.

@param $aid
  The ID of the action to delete.
```

## Code

```php
function actions_delete($aid) {
  db_delete('actions')
    ->condition('aid', $aid)
    ->execute();
  module_invoke_all('actions_delete', $aid);
}
```

---
_Drupal 7.103 · [includes/actions.inc](https://github.com/drupal/drupal/blob/7.103/includes/actions.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
