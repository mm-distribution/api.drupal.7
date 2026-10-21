# DatabaseConnection::nextId()

- **Type:** Method
- **File:** [`includes/database/database.inc`](../_file.md), lines 1385–1385 · [local source](../../../../../source/includes/database/database.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/database.inc#L1385)
- **Class:** [DatabaseConnection](../DatabaseConnection.md)
- **Topics:** [database](../../../../topics/database.md)

## Signature

```php
abstract public function nextId($existing_id = 0);
```

## Documentation

```text
Retrieves an unique id from a given sequence.

Use this function if for some reason you can't use a serial field. For
example, MySQL has no ways of reading of the current value of a sequence
and PostgreSQL can not advance the sequence to be larger than a given
value. Or sometimes you just need a unique integer.

@param $existing_id
  After a database import, it might be that the sequences table is behind,
  so by passing in the maximum existing id, it can be assured that we
  never issue the same id.

@return
  An integer number larger than any number returned by earlier calls and
  also larger than the $existing_id if one was passed in.
```

## Code

```php
  abstract public function nextId($existing_id = 0);
```

---
_Drupal 7.103 · [includes/database/database.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/database.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
