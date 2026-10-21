# PollTranslateTestCase::setUp()

- **Type:** Method
- **File:** [`modules/poll/poll.test`](../_file.md), lines 824–826 · [local source](../../../../../source/modules/poll/poll.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/poll/poll.test#L824-L826)
- **Class:** [PollTranslateTestCase](../PollTranslateTestCase.md)
- **Module/theme:** poll

## Signature

```php
function setUp()
```

## Documentation

_No docblock in source._

## Code

```php
  function setUp() {
    parent::setUp('poll', 'translation');
  }
```

---
_Drupal 7.103 · [modules/poll/poll.test](https://github.com/drupal/drupal/blob/7.103/modules/poll/poll.test) · Licensed GPL-2.0-or-later (see LICENSE)._
