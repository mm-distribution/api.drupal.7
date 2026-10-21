# poll_update_7002()

- **Type:** Function
- **File:** [`modules/poll/poll.install`](_file.md), lines 179–186 · [local source](../../../../source/modules/poll/poll.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/poll/poll.install#L179-L186)
- **Module/theme:** poll

## Signature

```php
function poll_update_7002()
```

## Documentation

```text
Add timestamp field to {poll_vote}.
```

## Code

```php
function poll_update_7002() {
  $field = array(
    'type' => 'int',
    'not null' => TRUE,
    'default' => 0,
  );
  db_add_field('poll_vote', 'timestamp', $field);
}
```

---
_Drupal 7.103 · [modules/poll/poll.install](https://github.com/drupal/drupal/blob/7.103/modules/poll/poll.install) · Licensed GPL-2.0-or-later (see LICENSE)._
