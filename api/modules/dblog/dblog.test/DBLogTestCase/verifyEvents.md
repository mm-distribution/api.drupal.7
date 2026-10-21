# DBLogTestCase::verifyEvents()

- **Type:** Method
- **File:** [`modules/dblog/dblog.test`](../_file.md), lines 244–255 · [local source](../../../../../source/modules/dblog/dblog.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/dblog/dblog.test#L244-L255)
- **Class:** [DBLogTestCase](../DBLogTestCase.md)
- **Module/theme:** dblog

## Signature

```php
private function verifyEvents()
```

## Documentation

```text
Generates and then verifies various types of events.
```

## Code

```php
  private function verifyEvents() {
    // Invoke events.
    $this->doUser();
    $this->doNode('article');
    $this->doNode('blog');
    $this->doNode('page');
    $this->doNode('poll');

    // When a user account is canceled, any content they created remains but the
    // uid = 0. Their blog entry shows as "'s blog" on the home page. Records
    // in the watchdog table related to that user have the uid set to zero.
  }
```

---
_Drupal 7.103 · [modules/dblog/dblog.test](https://github.com/drupal/drupal/blob/7.103/modules/dblog/dblog.test) · Licensed GPL-2.0-or-later (see LICENSE)._
