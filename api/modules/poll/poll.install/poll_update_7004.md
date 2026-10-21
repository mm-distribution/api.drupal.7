# poll_update_7004()

- **Type:** Function
- **File:** [`modules/poll/poll.install`](_file.md), lines 208–211 · [local source](../../../../source/modules/poll/poll.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/poll/poll.install#L208-L211)
- **Module/theme:** poll
- **Topics:** [updates-7.x-extra](../../../topics/updates-7.x-extra.md)

## Signature

```php
function poll_update_7004()
```

## Documentation

```text
Update the database to match the schema.
```

## Code

```php
function poll_update_7004() {
  // Remove field default.
  db_change_field('poll_vote', 'chid', 'chid', array('type' => 'int', 'unsigned' => TRUE, 'not null' => TRUE));
}
```

---
_Drupal 7.103 · [modules/poll/poll.install](https://github.com/drupal/drupal/blob/7.103/modules/poll/poll.install) · Licensed GPL-2.0-or-later (see LICENSE)._
