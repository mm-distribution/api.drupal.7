# PollCreateTestCase::getInfo()

- **Type:** Method
- **File:** [`modules/poll/poll.test`](../_file.md), lines 185–191 · [local source](../../../../../source/modules/poll/poll.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/poll/poll.test#L185-L191)
- **Class:** [PollCreateTestCase](../PollCreateTestCase.md)
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
      'name' => 'Poll create',
      'description' => 'Adds "more choices", previews and creates a poll.',
      'group' => 'Poll'
    );
  }
```

---
_Drupal 7.103 · [modules/poll/poll.test](https://github.com/drupal/drupal/blob/7.103/modules/poll/poll.test) · Licensed GPL-2.0-or-later (see LICENSE)._
