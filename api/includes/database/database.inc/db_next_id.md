# db_next_id()

- **Type:** Function
- **File:** [`includes/database/database.inc`](_file.md), lines 2773–2775 · [local source](../../../../source/includes/database/database.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/database.inc#L2773-L2775)
- **Topics:** [database](../../../topics/database.md)

## Signature

```php
function db_next_id($existing_id = 0)
```

## Documentation

```text
Retrieves a unique id.

Use this function if for some reason you can't use a serial field. Using a
serial field is preferred, and InsertQuery::execute() returns the value of
the last ID inserted.

@param $existing_id
  After a database import, it might be that the sequences table is behind, so
  by passing in a minimum ID, it can be assured that we never issue the same
  ID.

@return
  An integer number larger than any number returned before for this sequence.
```

## Code

```php
function db_next_id($existing_id = 0) {
  return Database::getConnection()->nextId($existing_id);
}
```

---
_Drupal 7.103 · [includes/database/database.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/database.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
