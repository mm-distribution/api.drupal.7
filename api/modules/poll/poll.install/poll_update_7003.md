# poll_update_7003()

- **Type:** Function
- **File:** [`modules/poll/poll.install`](_file.md), lines 191–198 · [local source](../../../../source/modules/poll/poll.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/poll/poll.install#L191-L198)
- **Module/theme:** poll

## Signature

```php
function poll_update_7003()
```

## Documentation

```text
Change the weight column to normal int.
```

## Code

```php
function poll_update_7003() {
  db_change_field('poll_choice', 'weight', 'weight', array(
    'type' => 'int',
    'not null' => TRUE,
    'default' => 0,
    'description' => 'The sort order of this choice among all choices for the same node.',
  ));
}
```

---
_Drupal 7.103 · [modules/poll/poll.install](https://github.com/drupal/drupal/blob/7.103/modules/poll/poll.install) · Licensed GPL-2.0-or-later (see LICENSE)._
