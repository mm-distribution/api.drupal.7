# actions_load()

- **Type:** Function
- **File:** [`includes/actions.inc`](_file.md), lines 373–375 · [local source](../../../source/includes/actions.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/actions.inc#L373-L375)

## Signature

```php
function actions_load($aid)
```

## Documentation

```text
Retrieves a single action from the database.

@param $aid
  The ID of the action to retrieve.

@return
  The appropriate action row from the database as an object.
```

## Code

```php
function actions_load($aid) {
  return db_query("SELECT aid, type, callback, parameters, label FROM {actions} WHERE aid = :aid", array(':aid' => $aid))->fetchObject();
}
```

---
_Drupal 7.103 · [includes/actions.inc](https://github.com/drupal/drupal/blob/7.103/includes/actions.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
