# PollVoteCheckHostname::getInfo()

- **Type:** Method
- **File:** [`modules/poll/poll.test`](../_file.md), lines 485–491 · [local source](../../../../../source/modules/poll/poll.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/poll/poll.test#L485-L491)
- **Class:** [PollVoteCheckHostname](../PollVoteCheckHostname.md)
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
      'name' => 'User poll vote capability.',
      'description' => 'Check that users and anonymous users from specified ip-address can only vote once.',
      'group' => 'Poll'
    );
  }
```

---
_Drupal 7.103 · [modules/poll/poll.test](https://github.com/drupal/drupal/blob/7.103/modules/poll/poll.test) · Licensed GPL-2.0-or-later (see LICENSE)._
