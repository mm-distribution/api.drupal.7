# drupal_session_id()

- **Type:** Function
- **File:** [`includes/session.inc`](_file.md), lines 617–622 · [local source](../../../source/includes/session.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/session.inc#L617-L622)

## Signature

```php
function drupal_session_id($id)
```

## Documentation

```text
Session ids are hashed by default before being stored in the database.

This should only be done if any existing sessions have been updated, as
reflected by the hash_session_ids variable.

@param $id
  A session id.

@return
  The session id which may have been hashed.
```

## Code

```php
function drupal_session_id($id) {
  if (variable_get('hashed_session_ids_supported', FALSE) && !variable_get('do_not_hash_session_ids', FALSE)) {
    $id = drupal_hash_base64($id);
  }
  return $id;
}
```

---
_Drupal 7.103 · [includes/session.inc](https://github.com/drupal/drupal/blob/7.103/includes/session.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
