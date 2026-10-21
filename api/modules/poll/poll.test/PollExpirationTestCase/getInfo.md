# PollExpirationTestCase::getInfo()

- **Type:** Method
- **File:** [`modules/poll/poll.test`](../_file.md), lines 714–720 · [local source](../../../../../source/modules/poll/poll.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/poll/poll.test#L714-L720)
- **Class:** [PollExpirationTestCase](../PollExpirationTestCase.md)
- **Module/theme:** poll

## Signature

```php
public static function getInfo()
```

## Documentation

_No docblock in source._

## Code

```php
  public static function getInfo() {
    return array(
      'name' => 'Poll expiration',
      'description' => 'Test the poll auto-expiration logic.',
      'group' => 'Poll',
    );
  }
```

---
_Drupal 7.103 · [modules/poll/poll.test](https://github.com/drupal/drupal/blob/7.103/modules/poll/poll.test) · Licensed GPL-2.0-or-later (see LICENSE)._
